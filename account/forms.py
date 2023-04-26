from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomusercreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'user_image')


class Userbuy(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('passport_id', 'visa_number', 'county', 'gander',)
