from django.db import models
from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo)

class Room(models.Model):
    name =models.CharField(max_length=250)
    description = models.TextField(null = True, blank = True)
    # participants = models.
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Country(StructuredNode):
    name =StringProperty(unique_index=True, required=True)
    code = StringProperty(unique_index=True, required=True)
# Create your models here.
