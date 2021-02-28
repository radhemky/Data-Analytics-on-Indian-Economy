from django.shortcuts import render

def index(request):
    return render(request,'index.html', {})
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
    return render(request,'login.html', {})
def Male_Unemployment(request):
    return render(request, 'Male_Unemployment.html', {})
def Overall_Unemployment(request):
    return render(request, 'Overall_Unemployment.html', {})
def Return_field_by_category(request):
    return render(request, 'Return_field_by_category.html', {})
def Seasonality_and_trend_of_GDP(request):
    return render(request, 'Seasonality_and_trend_of_GDP.html', {})
def STOCK_MARKET(request):
    return render(request, 'STOCK_MARKET.html', {})
def taxes_of_each_year(request):
    return render(request, 'taxes_of_each_year.html', {})
def Total_Tax(request):
    return render(request, 'Total_Tax.html', {})
def Vulerable_Employment(request):
    return render(request, 'Vulnerable_Employment.html', {})
def Wage_and_Salaried_workers(request):
    return render(request, 'Wage_and_Salaried_workers.html', {})