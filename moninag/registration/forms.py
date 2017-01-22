from django.contrib.auth.forms import UserCreationForm
from registration.models import CustomUser
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


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

    def send_activation_email(self, site, from_email, to_email, id):
        """
        Send an activation email to the user.

        The activation email will make use of two templates:

        ``registration/activation_email_subject.txt``
            This template will be used for the subject line of the
            email.

        ``registration/activation_email.txt``
            This template will be used for the body of the email.

        These templates will each receive the following context
        variables:

        ``activation_key``
            The activation key for the new account.

        ``site``
            Base url of the site.

        """
        ctx_dict = { 'activation_key': id,
                     'site': site }
        subject = render_to_string('activation_email_subject.txt',
                                   ctx_dict)
        # Email subject *must not* contain newlines
        subject = ''.join(subject.splitlines())

        html_message = render_to_string(
            'activation_email.html',
            ctx_dict
        )
        #import pdb; pdb.set_trace()

        mail = EmailMultiAlternatives(
            subject, 'This is message', from_email,  [to_email])
        mail.attach_alternative(html_message, "text/html")

        try:
            mail.send()
        except:
            pass

