def filter_items(items: list, max_value: int = 100):
filtered = [i for i in items if i < max_value]
return filtered

from django.db import models

class Account(models.Model):
login_name = models.CharField(max_length=150)
contact_email = models.EmailField(unique=True)

