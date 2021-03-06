"""This module contains verification method for contact"""

from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


def send_verification_email(site, from_email, to_email, activation_key):
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
    ctx_dict = {'activation_key': activation_key,
                'site': site}
    subject = render_to_string('contact/verify_email_subject.txt',
                               ctx_dict)
    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())

    html_message = render_to_string(
        'contact/verify_email.html',
        ctx_dict
    )

    mail = EmailMultiAlternatives(
        subject, 'This is message', from_email, [to_email])
    mail.attach_alternative(html_message, "text/html")

    mail.send()
