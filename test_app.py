import unittest
from app import app
import werkzeug

if not hasattr(werkzeug, '__version__'): 
    werkzeug.__version__ = "mock-version"


class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):        cls.client = app.test_client()

    def status_inicio_teste_400(self):
        # Se a home responde com 400
        response = self.client.get('/')
        self.assertEqual(response.status_code, 400)

    def itens_teste_200(self):
        # Se items responde com status 200
        response = self.client.get('/items')
        self.assertEqual(response.status_code, 200)

    def login_teste_200(self):
        # Se login retorna um JSON
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.is_json)

if __name__ == '__main__':
    unittest.main()
