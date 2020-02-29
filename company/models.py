# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200)
    sector = models.CharField(max_length=200)
    siren = models.IntegerField()

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, **kwargs):
        company = cls.objects.create(
            name=kwargs['name'],
            sector=kwargs['sector'],
            siren=kwargs['siren'],
        )
        return company


class Result(models.Model):
    ca = models.IntegerField()
    margin = models.IntegerField()
    ebitda = models.IntegerField()
    loss = models.IntegerField()
    year = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.ca
