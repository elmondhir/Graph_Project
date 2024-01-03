from django.db import models
from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo)

class Country(StructuredNode):
    code = StringProperty(unique_index=True, required=True)
# Create your models here.
