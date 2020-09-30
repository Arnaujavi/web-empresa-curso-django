from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestCase(TestCase):
    def setUp(self):
        User.objects.create_user('test', 'tsts@tsts.com', 'test1234') #Con esto creamos nuestro usuario de pruebas

    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username = 'test').exists() #Comprobamos si el usuario ese existe y que devuelva bolean con exists
        self.assertEqual(exists,True) #Con esto se crea la prueba