"""Module for testing Company app"""
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class GetPagesTestCase(TestCase):
    """Test for getting pages"""
    def setUp(self):
        "Initializing before each test"

    def test_mainpage(self):
        """Main page testing"""
        path = reverse('home')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def tearDown(self):
        "Actions after each test"
