from django.db import models

# Create your models here.

from cities_light.abstract_models import (AbstractCity, AbstractRegion,
    AbstractCountry, AbstractSubRegion)
from cities_light.receivers import connect_default_signals


class Country(AbstractCountry):
    pass

connect_default_signals(Country)


class Region(AbstractRegion):
    def __str__(self):
        return self.alternate_names

connect_default_signals(Region)

class SubRegion(AbstractSubRegion):
    def __str__(self):
        return self.alternate_names

connect_default_signals(SubRegion)

class City(AbstractCity):
    pass

connect_default_signals(City)