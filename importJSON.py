#!/usr/bin/env python

import os
import sys
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'upliftassignment.settings')
try:
    from django import setup
except ImportError as exc:
    raise ImportError(
        "Couldn't import Django. Are you sure it's installed and "
        "available on your PYTHONPATH environment variable? Did you "
        "forget to activate a virtual environment?"
    ) from exc
setup()

from providers.models import Provider, Skill, ProviderSkill

def importJSON(filename):
    with open(filename, 'r') as json_file:
        data = json.load(json_file)

        for provider_data in data:
            provider = Provider()
            provider.id = provider_data['id']
            provider.first_name = provider_data['first_name']
            provider.last_name = provider_data['last_name']
            provider.sex = provider_data['sex']
            provider.birth_date = provider_data['birth_date']
            provider.rating = provider_data['rating']
            provider.company = provider_data['company']
            provider.active = provider_data['active']
            provider.country = provider_data['country']
            provider.languange = provider_data['language']

            provider.save()

            print('Saved: ', provider)

            print('Primary Skills:')
            for skill_name in provider_data['primary_skills']:
                skill, created = Skill.objects.get_or_create(name=skill_name)
                provider_skill, created = ProviderSkill.objects.get_or_create(provider=provider, skill=skill, type=ProviderSkill.PRIMARY)
                print(provider_skill)
            
            print('Secondary Skills:')
            for skill_name in provider_data['secondary_skill']:
                skill, created = Skill.objects.get_or_create(name=skill_name)
                provider_skill, created = ProviderSkill.objects.get_or_create(provider=provider, skill=skill, type=ProviderSkill.SECONDARY)
                print(provider_skill)

def main():
    if len(sys.argv) < 2:
        print('Please provide a filename for the json file to import.')
        return
    filename = sys.argv[1]
    print('Importing from: ', filename)
    importJSON(filename)


if __name__ == '__main__':
    main()


