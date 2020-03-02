# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Company
import json

with open('mock_data.json', 'r') as f:
    companies = json.load(f)
    for company_data in companies:
        company = Company.create(**company_data)


def index(request):
    companies = Company.objects.all()
    paginator = Paginator(companies, 8)

    page = request.GET.get('page')
    try:
        companies = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        companies = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        companies = paginator.page(paginator.num_pages)

    context = {
        "companies": companies
    }

    return render(request, 'index.html', context)
