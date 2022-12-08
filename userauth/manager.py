from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,email,name,password,age):
        if not email:
            raise ValueError('user must have an email id')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            age=age,
        )
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,email,name,age,password=None):
        user = self.create_user(
          email,
          password=password,
          name=name,
          age=age,
      )
        user.is_admin=True
        user.save()
        return user

    def crate_dietician(self,email,name,age,password=None):
        user=self.create_user(
            email=email,
            password=password,
            name=name,
            age=age,

        )
        user.is_admin=False
        user.save()
        return user