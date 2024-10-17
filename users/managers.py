from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password, **extra_fields):
        if not email:
            raise ValueError('The email field must be set')
        
        if '@' not in email and not email.endswith('.com'):
            raise ValidationError('Invalid email format. Email must contain @ and end with .com')
        
        email = self.normalize_email(email) # makes everything small letters
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        
        return self.create_user(email, first_name, last_name, password, **extra_fields)