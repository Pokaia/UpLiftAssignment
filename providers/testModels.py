from django.test import TestCase
import decimal
from providers.models import Provider, Skill, ProviderSkill

class testModels(TestCase):
    fixtures = ['testData.json']

    def testCreate(self):
        provider = Provider(
                first_name='Boric',
                last_name='Fredrickson',
                sex='Male',
                birth_date='1984-07-15',
                rating=100.0,
                company='Kaha Consulting, Inc.',
                active=True,
                country='USA',
                language='English')
        provider.save()

        self.assertEqual(101, provider.id)

        provider.first_name = 'Test'
        provider.save()

        self.assertEqual(101, provider.id)
        self.assertEqual('Test', provider.first_name)

    def testQuery(self):
        self.assertEqual(100, Provider.objects.count())

        provider = Provider.objects.get(first_name='Willow', last_name='Kleiner')
        self.assertEqual('Willow', provider.first_name)
        self.assertEqual(98, provider.id)

        active_count = Provider.objects.filter(active=True).count()
        self.assertEqual(55, active_count)
        
        inactive_count = Provider.objects.filter(active=False).count()
        self.assertEqual(45, inactive_count)

        highest_rated_provider = Provider.objects.all().order_by('-rating').first()
        self.assertEqual(9.9, float(highest_rated_provider.rating))
        self.assertEqual('Barret', highest_rated_provider.first_name)
        
        lowest_rated_provider = Provider.objects.all().order_by('rating').first()
        self.assertEqual(0.2, float(lowest_rated_provider.rating))
        self.assertEqual('Aguie', lowest_rated_provider.first_name)

        self.assertEqual(2, Provider.objects.filter(language='Armenian').count())

        sample = Provider.objects.all().first()
        self.assertEqual('Elisabetta', sample.first_name)
        self.assertEqual(3, ProviderSkill.objects.filter(provider=sample, type=ProviderSkill.PRIMARY).count())
        self.assertEqual(1, ProviderSkill.objects.filter(provider=sample, type=ProviderSkill.SECONDARY).count())
        primary_provider_skill = ProviderSkill.objects.filter(provider=sample, type=ProviderSkill.PRIMARY).first()
        self.assertEqual('Code Refactoring', primary_provider_skill.skill.name)
