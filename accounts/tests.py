from django.test import TestCase
from django.contrib.auth import get_user_model 


class TestUserCreation(TestCase):
    def test_create_user(self):
        User = get_user_model()
        result = User.objects.create_user(email='test@mail.com',password='testpassword')
        
        self.assertEqual(result.email,'test@mail.com')
        self.assertTrue(result.is_active)
        self.assertFalse(result.is_staff)
        self.assertFalse(result.is_admin)
        
        try:
            self.assertNone(result.username)
            
        except AttributeError:
            pass 
        
        with self.assertRaises(TypeError):
            User.objects.create_user() 
            
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
            
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="testpassword") 
            
    def test_create_superuser(self):
        User = get_user_model()
        admin = User.objects.create_superuser(email="admin@mail.com",password="testpassword")
        
        self.assertEqual(admin.email, "admin@mail.com")
        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_staff)
        self.assetTrue(admin.is_active)
        
        try:
            self.assertNone(admin.username)
        except AttributeError:
            pass 
        
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email="admin@mail.com",password="testpassword",is_superuser=False)
       
            