import subprocess

from django.shortcuts import render
from djangoProject2 import gdp
from subprocess import run, PIPE
import sys


def index(request):
    return render(request, 'Employed_vs_Unemployed.html', {})


def Corporate_and_Personal_Taxes(request):
    return render(request, 'Corporate_and_Personal_Taxes.html', {})


def COVID_19(request):
    return render(request, 'COVID_19.html', {})


def DIGITAL_PAYMENT(request):
    return render(request, 'DIGITAL_PAYMENT.html', {})


def Employed_vs_Unemployed(request):
    return render(request, 'Employed_vs_Unemployed.html', {})


def Employment_in_Industries(request):
    return render(request, 'Employment_in_Industries.html', {})


def Female_Unemployment(request):
    return render(request, 'Female_Unemployment.html', {})


def GDP_GROWTH(request):
    return render(request, 'GDP_GROWTH.html', {})


def GDP_rate_and_Tax_rate(request):
    return render(request, 'GDP_rate_and_Tax_rate.html', {})


def login(request):
    return render(request, 'login.html', {})


def Male_Unemployment(request):
    return render(request, 'Male_Unemployment.html', {})


def Overall_Unemployment(request):
    return render(request, 'Overall_Employment.html', {})


def Return_field_by_category(request):
    return render(request, 'Return_field_by_category.html', {})


def Seasonality_and_trend_of_GDP(request):
    return render(request, 'Seasonality_and_trend_of_GDP.html', {})


def News_and_update(request):
    return render(request, 'News_&_Update.html', {})


def taxes_of_each_year(request):
    return render(request, 'taxes_of_each_year.html', {})


def Total_Tax(request):
    return render(request, 'Total_Tax.html', {})


def Vulerable_Employment(request):
    return render(request, 'Vulnerable_Employment.html', {})


def Wage_and_Salaried_workers(request):
    return render(request, 'Wage_and_Salaried_workers.html', {})


def hello(request):
    inp = request.POST.get('param')
    plus = inp
    out = run([sys.executable, '//home//cheeryluck//PycharmProjects//djangoProject2//djangoProject2//gdp.py', inp],
              shell=False, stdout=PIPE, universal_newlines=True)

    return render(request, 'taxes_of_each_year.html', {'data1': out.stdout, 'data2': plus})


def ana(request):
    run([sys.executable, '//home//cheeryluck//PycharmProjects//djangoProject2//djangoProject2//AnalyzeData.py', ],
        shell=False, stdout=PIPE, universal_newlines=True)
    return render(request, 'News_&_Update.html', {})


def data(request):
    run([sys.executable, '//home//cheeryluck//PycharmProjects//djangoProject2//djangoProject2//CleanData.py', ],
        shell=False, stdout=PIPE, universal_newlines=True)
    return render(request, 'News_&_Update.html', {})
