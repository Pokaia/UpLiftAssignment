from django.urls import reverse
from django.http.request import QueryDict
from rest_framework.test import APITestCase
from rest_framework import status

class ProvidersListViewTests(APITestCase):
    fixtures = ['testData.json']

    def testGetAll(self):
        url = reverse('ProviderList')
        response = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(100, len(response.data))
        self.assertEqual(34, response.data[0]['id'])
        self.assertEqual(80, response.data[99]['id'])
        # ensure the first provider is the highest rated
        self.assertAlmostEqual(9.9, float(response.data[0]['rating']))

    def testGetActive(self):
        url = reverse('ProviderList')
        response = self.client.get(url, {'active': True})
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(55, len(response.data))
        self.assertEqual(34, response.data[0]['id'])
        self.assertEqual(80, response.data[54]['id'])
        
        response = self.client.get(url, {'active': 'true'})
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(55, len(response.data))
        self.assertEqual(34, response.data[0]['id'])
        self.assertEqual(80, response.data[54]['id'])
        
        response = self.client.get(url, {'active': '1'})
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(55, len(response.data))
        self.assertEqual(34, response.data[0]['id'])
        self.assertEqual(80, response.data[54]['id'])
    
    def testGetInactive(self):
        url = reverse('ProviderList')
        response = self.client.get(url, {'active': False})
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(45, len(response.data))
        self.assertEqual(17, response.data[0]['id'])
        self.assertEqual(33, response.data[44]['id'])
        
        response = self.client.get(url, {'active': 'false'})
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(45, len(response.data))
        self.assertEqual(17, response.data[0]['id'])
        self.assertEqual(33, response.data[44]['id'])
        
        response = self.client.get(url, {'active': '0'})
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(45, len(response.data))
        self.assertEqual(17, response.data[0]['id'])
        self.assertEqual(33, response.data[44]['id'])

    def testGetFiltered(self):
        url = reverse('ProviderList')
        response = self.client.get(url, {'first_name': 'Willow'})
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEquals('Willow', response.data[0]['first_name'])
        
        response = self.client.get(url, {'last_name': 'Slewcock'})
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEquals('Slewcock', response.data[0]['last_name'])

        response = self.client.get(url, {
            'first_name': 'Opaline',
            'last_name': 'Dinneen',
            'sex': 'Male',
            })
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEquals('Dinneen', response.data[0]['last_name'])
        self.assertEqual(89, response.data[0]['id'])
        
        response = self.client.get(url, {
            'birth_date': '1974-12-28',
            })
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(84, response.data[0]['id'])
        
        response = self.client.get(url, {
            'ratinggt': '5.0',
            })
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(57, len(response.data))

    def testFilterForSkills(self):
        url = reverse('ProviderList')
        response = self.client.get(url, {
            'has_primary_skill': 'Software Testing',
            })
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(3, len(response.data))
        
        response = self.client.get(url, {
            'has_secondary_skill': 'Cryptography',
            })
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(4, len(response.data))

        response = self.client.get(url, {
            'has_primary_skill': 'Mathematics',
            'has_secondary_skill': 'Cryptography',
            })
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, len(response.data))

    def testMultiplePrimary(self):
        url = reverse('ProviderList')
        query_params = QueryDict('has_primary_skill=Mathematics&has_primary_skill=Design Documents')
        response = self.client.get(url, query_params)
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(1, len(response.data))

    def testOrderByCount(self):
        url = reverse('ProviderList')
        
        response = self.client.get(url, {'first_name': 'Barret'})
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEquals('Barret', response.data[0]['first_name'])
        
        response = self.client.get(url)
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(57, response.data[0]['id'])
