from django.contrib import admin
from django.urls import path
from djangoProject2 import views

urlpatterns = {
    path('', views.index),
    path('DIGITAL_PAYMENT.html', views.DIGITAL_PAYMENT),
    path('Overall_Employment.html',views.Overall_Unemployment),
    path('Female_Unemployment.html',views.Female_Unemployment),
    path('taxes_of_each_year.html',views.taxes_of_each_year),
    path('Male_Unemployment.html',views.Male_Unemployment),
    path('GDP_rate_and_Tax_rate.html',views.GDP_rate_and_Tax_rate),
    path('GDP_GROWTH.html',views.GDP_GROWTH),
    path('Employment_in_Industries.html',views.Employment_in_Industries),
    path('Employed_vs_Unemployed.html',views.Employed_vs_Unemployed),
    path('Corporate_and_Personal_Taxes.html',views.Corporate_and_Personal_Taxes),
    path('News_&_Update.html',views.News_and_update),
    path('Seasonality_and_trend_of_GDP.html',views.Seasonality_and_trend_of_GDP),
    path('Return_field_by_category.html',views.Return_field_by_category),
    path('COVID_19.html',views.COVID_19),
    path('login.html',views.login),
    path('Wage_and_Salaried_workers.html',views.Wage_and_Salaried_workers),
    path('Total_Tax.html',views.Total_Tax),
    path('Vulnerable_Employment.html',views.Vulerable_Employment),
    path('index.html',views.index)


}