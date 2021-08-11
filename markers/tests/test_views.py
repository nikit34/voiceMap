from django.test import TestCase, Client
from django.contrib.gis.geos import Point

from markers.models import Marker


class getMarkersMapTestCase(TestCase):
    def setUp(self):
        Marker.objects.create(name='test_place', location=Point(8.65722656129525, 3.469557302579046))
        self.client = Client()
        self.response = self.client.get('/markers/map/')

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_content_name(self):
        test_passed = False
        for feature in self.response.context_data['markers']['features']:
            if feature['properties']['name'] == 'test_place':
                test_passed = True
        self.assertTrue(test_passed, f'response: {self.response.context_data}')

    def test_content_coordinates(self):
        test_passed = False
        for feature in self.response.context_data['markers']['features']:
            if feature['geometry']['coordinaties'] == '8.65722656129525' and feature['geometry']['coordinaties'] == '3.469557302579046':
                test_passed = True
        self.assertTrue(test_passed, f'response: {self.response.context_data}')
