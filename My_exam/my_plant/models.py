from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError


def name_validate(value):
    if not value[0].isupper():
        raise ValidationError('Your name must start with a capital letter!')


def only_letter(value):
    for ch in value:
        if not ch.isalpha():
            raise ValidationError('"Plant name should contain only letters!"')


class Profile(models.Model):
    USERNAME_MIN_LENGTH = 2
    username = models.CharField(
        max_length=10,
        validators=(
            validators.MinLengthValidator(USERNAME_MIN_LENGTH, 'It should consist of a minimum of 2 characters'),),
    )
    first_name = models.CharField(
        max_length=20,
        validators=(name_validate,),
    )
    last_name = models.CharField(
        max_length=20,
        validators=(name_validate,),
    )
    profile_picture = models.URLField(
        null=True,
        blank=True
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Plant(models.Model):
    NAME_MIN_LENGTH = 2
    CHOICES = (
        ("Outdoor Plants", "Outdoor Plants"),
        ("Indoor Plants", "Indoor Plants"),
    )

    type = models.CharField(
        max_length=14,
        choices=CHOICES
    )
    name = models.CharField(
        max_length=20,
        validators=(
            validators.MinLengthValidator(NAME_MIN_LENGTH, 'It should consist minimum of 2 characters'),
            only_letter,
        )
    )

    image = models.URLField()

    description = models.TextField()

    price = models.FloatField()
