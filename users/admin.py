from django.contrib import admin
from django.contrib.auth import get_user_model
from users.models import Juku

CustomUser = get_user_model()

admin.site.register(CustomUser)
admin.site.register(Juku)
