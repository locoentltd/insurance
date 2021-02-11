# These models are maintained in the Admin panel.
from django.contrib import admin

from portal.models.address import Address
from portal.models.agency import Agency
from portal.models.agent import Agent
from portal.models.county import County
from portal.models.deductible import Deductible, DedLimitMultiplier
from portal.models.insured import Insured
from portal.models.limit import Limit
from portal.models.person import Person
from portal.models.procedure import Procedure
from portal.models.quickquote import QuickQuote
from portal.models.specialty import Specialty
from portal.models.state import State
from portal.models.title import Title


admin.site.register(Address)
admin.site.register(Agency)
admin.site.register(Agent)
admin.site.register(County)
admin.site.register(Deductible)
admin.site.register(DedLimitMultiplier)
admin.site.register(Insured)
admin.site.register(Limit)

admin.site.register(Procedure)
admin.site.register(QuickQuote)
admin.site.register(Specialty)
admin.site.register(State)
admin.site.register(Title)
