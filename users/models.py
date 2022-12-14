import datetime

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from jukus.models import Juku
from subjects.models import Subject


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Emailを入力して下さい')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('is_staff=Trueである必要があります。')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser=Trueである必要があります。')
        return self._create_user(email, password, **extra_fields)



class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("メールアドレス"), unique=True)
    name = models.CharField(_("氏名"), max_length=50)
    school = models.CharField(_("学校名"), max_length=50)
    bio = models.CharField(_("自己紹介"), max_length=150)
    birthday = models.DateField(_("生年月日"),null=True)
    job = models.CharField(_("講師or生徒"), max_length=20, choices=(('teacher','講師'),('student','生徒'),('manager','管理者')))
    profile_image = models.ImageField(null=True, blank=True)

    juku = models.ForeignKey(Juku, on_delete=models.CASCADE,null=True)
    subjects = models.ManyToManyField(Subject,null=True)

    is_staff = models.BooleanField(_("staff status"), default=False)
    is_active = models.BooleanField(_("active"), default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.name

    #フォロー人数を表示するfollow関数を定義
    def follow_nums(self):
       return len(Follow.objects.filter(owner=self.id))
    #フォロワー人数を表示するfollower_nums関数を定義
    def follower_nums(self):
       return len(Follow.objects.filter(follow_target=self.id))

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)


    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


    def count_following(self):
        following = Follow.objects.filter(owner=self)
        following_list = []
        for f in following:
            following_list.append(f.follow_target)

        return len(following_list)


    def grade(self):
        birth_y = self.birthday.year
        birth_m = self.birthday.month
        today_y = datetime.date.today().year

        if birth_m < 4:
            g = today_y - birth_y
        else:           #遅生まれ
            g = today_y - birth_y - 1

        grade = "999"
        if g == 6:
            grade = "小学1年生"
        elif g == 7:
            grade = "小学2年生"
        elif g == 8:
          grade = "小学3年生"
        elif g == 9:
            grade = "小学4年生"
        elif g == 10:
            grade = "小学5年生"
        elif g == 11:
            grade = "小学6年生"
        elif g == 12:
            grade = "中学1年生"
        elif g == 13:
            grade = "中学2年生"
        elif g == 14:
            grade = "中学3年生"
        elif g == 15:
            grade = "高校1年生"
        elif g == 16:
            grade = "高校2年生"
        elif g == 17:
            grade = "高校3年生"

        return grade


class Follow(models.Model):
    owner = models.ForeignKey(
       CustomUser,
       on_delete=models.CASCADE,
       related_name = 'do_follow_user'
   )
    follow_target = models.ForeignKey(
       CustomUser,
       on_delete=models.CASCADE,
       related_name = 'accept_follow_user'
   )
