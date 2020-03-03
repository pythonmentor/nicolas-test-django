# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Company, Result


def index(request):
    companies = Company.objects.all()

    # paginator = Paginator(results, 12)

    # page = request.GET.get('page')
    # try:
    #     results = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     results = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     results = paginator.page(paginator.num_pages)

    context = {
        "companies": companies,
    }

    return render(request, 'index.html', context)
