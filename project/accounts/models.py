from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db.models.signals import post_save
from django.dispatch import receiver
from uuid import uuid4
from datetime import datetime, timedelta


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('Enter Email')
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        user = self.model(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class Users(AbstractBaseUser, PermissionsMixin):
    # 使用したいフィールドを追加
    username = models.CharField(max_length=150)
    # age = models.PositiveIntegerField()
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False) # 管理画面にアクセスできるか否か
    # is_superuserはPermissionsMixinに元から含まれている
    # website = models.URLField(null=True)
    picture = models.FileField(null=True, upload_to='picture/')

    objects = UserManager()

    USERNAME_FIELD = 'email' # このテーブルのレコードを一意に識別
    REQUIRED_FIELDS = ['username'] # スーパーユーザ作成時に入力する

    class Meta:
        db_table = 'users'

    # def __str__(self):
    #     return self.email


class UserActivateTokensManager(models.Manager):

    def activate_user_by_token(self, token):
        user_activate_token = self.filter(
            token=token,
            expired_at__gte=datetime.now()
        ).first()
        user = user_activate_token.user
        user.is_active = True
        user.save()

class UserActivateTokens(models.Model):

    token = models.UUIDField(db_index=True)
    expired_at = models.DateTimeField()
    user = models.ForeignKey(
        'Users', on_delete=models.CASCADE
    )

    objects = UserActivateTokensManager()

    class Meta:
        db_table = 'user_activate_tokens'

@receiver(post_save, sender=Users)
def publish_token(sender, instance, **kwargs):
    user_activate_token = UserActivateTokens.objects.create(
        user=instance, token=str(uuid4()), expired_at=datetime.now() + timedelta(days=1)
    )
    # メールでURLを送る方がよい
    print(f'http://127.0.0.1:8000/accounts/activate_user/{user_activate_token.token}')



# class UserManager(BaseUserManager):
#     def create_user(self, username, email, password=None):
#         if not email:
#             raise ValueError('Enter Email!')
#         user = self.model(
#             username=username,
#             email=email
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     def create_superuser(self, username, email, password=None):
#         user = self.model(
#             username=username,
#             email=email,
#         )
#         user.set_password(password)
#         user.is_staff = True
#         user.is_active = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user



# # 管理画面のカスタマイズで使用
# class Students(models.Model):

#     name = models.CharField(max_length=20)
#     age = models.IntegerField()
#     score = models.IntegerField()
#     school = models.ForeignKey(
#         'Schools', on_delete=models.CASCADE
#     )
    
#     class Meta:
#         db_table = 'students'
#         verbose_name_plural = '生徒'
#         ordering = ('age',)

#     def __str__(self):
#         return  self.name + ': ' + str(self.age)

# class Schools(models.Model):
#     name = models.CharField(max_length=20, verbose_name='学校名')
    
#     class Meta:
#         db_table = 'schools'
#         verbose_name_plural = '学校'
    
#     def __str__(self):
#         return  self.name