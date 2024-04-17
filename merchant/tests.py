from rest_framework.test import APITestCase
import json

class TestMerchantEndpoints(APITestCase):
    def test_application_endpoint(self):
        application_data = {
            "first_name": "Osman",
            "last_name": "Şaşkınbakkal",
            "email": "osmansaskinbakkal147@hotmail.com",
            "phone_number": "+905111111111"
        }
        response = self.client.post('/api/merchant/application', data=application_data)
        self.assertEqual(response.status_code, 200)
    
        token = response.data['token']
        channel_data = {
            "website_url": "https://emregeldegul.com.tr",
            "trendyol_url": "https://emregeldegul.com.tr",
            "amazon_url": "https://emregeldegul.com.tr",
            "token": token
        }
        response = self.client.post('http://localhost:8000/api/merchant/channel', data=channel_data)
        self.assertEqual(response.data, "Başvurunuz Tamamlandı")

        
        