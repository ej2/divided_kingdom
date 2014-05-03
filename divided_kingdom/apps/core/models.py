from django.contrib.auth.models import User
from django.db import models
from django_extensions.db import fields


class AuditModel(models.Model):
    date_created = fields.CreationDateTimeField(editable=True)
    created_by = models.ForeignKey(
        User, null=True, blank=True, related_name="+")
    date_updated = fields.ModificationDateTimeField(editable=True)
    updated_by = models.ForeignKey(
        User, null=True, blank=True, related_name="+")

    class Meta:
        abstract = True