from django.contrib.auth.forms import UserCreationForm
from registration.models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'second_name')
