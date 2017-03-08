"""This module holds custom utils for registration"""

import hashlib
import random
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


def generate_activation_key(email):
    """
    Creation of activation key based on SHA1
    :param email: user email
    :return: hashed activation key
    """

    salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()
    activation_key = hashlib.sha1((salt + email).encode('utf-8')).hexdigest()

    return activation_key


def send_activation_email(site, from_email, to_email, activation_key):
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
    subject = render_to_string('registration/activation_email_subject.txt',
                               ctx_dict)
    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())

    html_message = render_to_string(
        'registration/activation_email.html',
        ctx_dict
    )

    mail = EmailMultiAlternatives(
        subject, 'This is message', from_email, [to_email])
    mail.attach_alternative(html_message, "text/html")

    mail.send()


def send_reset_password_email(site, from_email, to_email, uidb64, token):
    """
    Send a password reset email to the user.

    The password reset email will make use of two templates:

    ``registration/password_reset_email_subject.txt``
        This template will be used for the subject line of the
        email.

    ``registration/password_reset_email.html``
        This template will be used for the body of the email.

    These templates will each receive the following context
    variables:

    ``uidb64``
        Base64 encoded id of User.

    ``token``
        The password recovery token.

    ``site``
        Base url of the site.

    """

    ctx_dict = {'email': to_email,
                'site': site,
                'uid': uidb64,
                'token': token}

    subject = render_to_string('registration/password_reset_email_subject.txt')
    subject = ''.join(subject.splitlines())

    html_message = render_to_string(
        'registration/password_reset_email.html',
        ctx_dict
    )

    mail = EmailMultiAlternatives(
        subject, 'This is message', from_email, [to_email])
    mail.attach_alternative(html_message, "text/html")
    mail.send()
