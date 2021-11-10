from django.db import models

# Create your models here.
'''class User(models.Model):
    class STATUSES(models.IntegerChoices):
        FOCUSING = (0, 'focusing')
        BUSY = (1, 'busy')
        OUT_SICK = (2, 'out_sick')
        ON_VACATION = (3, 'on_vacation')
    username = models.CharField(unique=True, validators=[
            RegexValidator(
                regex='^[#](\w+)$',
                message='Hashtag doesnt comply',
            ),
        ])
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    birth_day = models.DateTimeField(null=True)
    password ='''

