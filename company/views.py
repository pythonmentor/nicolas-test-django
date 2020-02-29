# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Company
import json

with open('mock_data.json', 'r') as f:
    companies = json.load(f)
    for company_data in companies:
        company = Company.create(**company_data)


def index(request):
    companies = Company.objects.all()

    context = {
        "companies": companies
    }

    return render(request, 'index.html', context)
