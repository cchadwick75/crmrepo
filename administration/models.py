from django.db import models
from django.contrib.auth.models import User, Group
from django.db import models

from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
STATE_CHOICES = (
    (u'AL', u'Alabama'),
    (u'AK', u'Alaska'),
    (u'AZ', u'Arizona'),
    (u'AR', u'Arkansas'),
    (u'CA', u'California'),
    (u'CO', u'Colorado'),
    (u'CT', u'Connecticut'),
    (u'DE', u'Delaware'),
    (u'DC', u'District of Columbia'),
    (u'FL', u'Florida'),
    (u'GA', u'Georgia'),
    (u'HI', u'Hawaii'),
    (u'ID', u'Idaho'),
    (u'IL', u'Illinois'),
    (u'IN', u'Indiana'),
    (u'IA', u'Iowa'),
    (u'KS', u'Kansas'),
    (u'KY', u'Kentucky'),
    (u'LA', u'Louisiana'),
    (u'ME', u'Maine'),
    (u'MT', u'Montana'),
    (u'NE', u'Nebraska'),
    (u'NV', u'Nevada'),
    (u'NH', u'New Hampshire'),
    (u'NJ', u'New Jersey'),
    (u'NM', u'New Mexico'),
    (u'NY', u'New York'),
    (u'NC', u'North Carolina'),
    (u'ND', u'North Dakota'),
    (u'OH', u'Ohio'),
    (u'OK', u'Oklahoma'),
    (u'OR', u'Oregon'),
    (u'MD', u'Maryland'),
    (u'MA', u'Massachusetts'),
    (u'MI', u'Michigan'),
    (u'MN', u'Minnesota'),
    (u'MS', u'Mississippi'),
    (u'MO', u'Missouri'),
    (u'PA', u'Pennsylvania'),
    (u'RI', u'Rhode Island'),
    (u'SC', u'South Carolina'),
    (u'SD', u'South Dakota'),
    (u'TN', u'Tennessee'),
    (u'TX', u'Texas'),
    (u'UT', u'Utah'),
    (u'VT', u'Vermont'),
    (u'VA', u'Virginia'),
    (u'WA', u'Washington'),
    (u'WV', u'West Virginia'),
    (u'WI', u'Wisconsin'),
    (u'WY', u'Wyoming'),
)
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255, blank=True)
    street_address2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=2, choices=STATE_CHOICES, blank=True)
    zip = models.CharField(max_length=10,  blank=True)
    date_inserted = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
