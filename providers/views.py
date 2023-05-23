from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from providers.models import Provider, Skill, ProviderSkill
from providers.serializers import ProviderSerializer

import datetime


class ProviderList(APIView):
    def get(self, request):
        response = []
        providers = Provider.objects.all().order_by('-rating', 'count')
        
        # filter by parameters
        first_name = request.query_params.get('first_name', None)
        if first_name is not None:
            providers = providers.filter(first_name=first_name)
        last_name = request.query_params.get('last_name', None)
        if last_name is not None:
            providers = providers.filter(last_name=last_name)
        sex = request.query_params.get('sex', None)
        if sex is not None:
            providers = providers.filter(sex=sex)
        active = request.query_params.get('active', None)
        if active is not None:
            if isinstance(active, str):
                active = active.lower() in ['true', '1', 'y', 'yes', 't']
            providers = providers.filter(active=active)
        birth_date = request.query_params.get('birth_date', None)
        if birth_date is not None:
            date = datetime.date.fromisoformat(birth_date)
            providers= providers.filter(birth_date=date)
        rating = request.query_params.get('rating', None)
        if rating is not None:
            providers = providers.filter(rating=rating)
        rating_gt = request.query_params.get('ratinggt', None)
        if rating_gt is not None:
            providers = providers.filter(rating__gt=rating_gt)
        rating_lt = request.query_params.get('ratinglt', None)
        if rating_lt is not None:
            providers = providers.filter(rating__lt=rating_lt)
        company = request.query_params.get('company', None)
        if company is not None:
            providers = providers.filter(company=company)
        country = request.query_params.get('country', None)
        if country is not None:
            providers = providers.filter(country=country)
        language = request.query_params.get('language', None)
        if language is not None:
            providers = providers.filter(language=language)

        has_primary_skill_list = request.query_params.getlist('has_primary_skill')
        has_secondary_skill_list = request.query_params.getlist('has_secondary_skill')

        for provider in providers:
            provider_serializer = ProviderSerializer(provider)
            provider_data = provider_serializer.data
            provider_data['primary_skills'] = []
            primary_skills = ProviderSkill.objects.filter(provider=provider, type=ProviderSkill.PRIMARY)
            for primary_skill in primary_skills:
                provider_data['primary_skills'].append(primary_skill.skill.name)
            provider_data['secondary_skills'] = []
            secondary_skills = ProviderSkill.objects.filter(provider=provider, type=ProviderSkill.SECONDARY)
            for secondary_skill in secondary_skills:
                provider_data['secondary_skills'].append(secondary_skill.skill.name)
            response.append(provider_data)

        if len(has_primary_skill_list) == 0 and len(has_secondary_skill_list) == 0:
            filtered_response = response
        else:
            # filter for skills
            filtered_response = self.filterProvidersBySkills(response, has_primary_skill_list, has_secondary_skill_list)

        self.updateCounts(filtered_response)
        
        return Response(filtered_response, status=status.HTTP_200_OK)

    def filterProvidersBySkills(self, data, has_primary_skill_list, has_secondary_skill_list):
        filtered_response = []
        for provider in data:
            has_skills = True;
            for skill in has_primary_skill_list:
                if skill not in provider['primary_skills']:
                    has_skills = False
            for skill in has_secondary_skill_list:
                if skill not in provider['secondary_skills']:
                    has_skills = False
            if has_skills:
                filtered_response.append(provider)
        return filtered_response

    def updateCounts(self, data):
        for provider_data in data:
            provider = Provider.objects.get(pk=provider_data['id'])
            provider.incrementCount()
