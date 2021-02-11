from __future__ import unicode_literals

from django.db import models

from portal.fields.percentage import PercentageField

PROCEDURES = (
	('laser','LASER'),
	('bariatric','BARIATRIC'),
	('telemedicine','TELEMEDICINE'),
	('correctional_facilities','CORRECTIONAL FACILITIES'),
	('nursing homes','NURSING HOMES'),
	)

class Procedure(models.Model):
	"""Doctors perform procedures on people."""
	performs = models.BooleanField(default=False)
	work_percentage = PercentageField(default=0)
	note = models.TextField(blank=True)
	procedure_type = models.CharField(max_length=100, choices=PROCEDURES)

