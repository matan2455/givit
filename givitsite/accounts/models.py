from django.db import models
from django.contrib.auth.models import User

MEMBERSHIP_TYPE = [
    ('friend','friend'),
    ('coordinator','coordinator'),
]

DEGREE = [
    ('BA', 'BA'),
    ('BSC', 'BSC'),
    ('MA', 'MA'),
    ('MSC', 'MSC'),
    ('PHD', 'PHD'),
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    confirmed = models.BooleanField("confirmed", default=False)
    student_id = models.IntegerField()
    phone_number = models.IntegerField()
    date_of_birth = models.DateField()
    home_address = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    degree = models.CharField(max_length=100, default='BA', choices = DEGREE)
    scholarship = models.CharField(max_length=100)
    membership_type = models.CharField(max_length=100, default= 'friend', choices=MEMBERSHIP_TYPE)

    def _str_(self):
        return self.user.username
