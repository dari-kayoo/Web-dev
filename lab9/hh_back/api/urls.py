from django.urls import path
from api.views import companies_list, companies_detail, vacancies_list, vacancies_detail, vacancy_top_ten

urlpatterns = [
    path('companies/', companies_list),
    path('companies/<int:product_id>/', companies_detail),
    path('vacancies/', vacancies_list),
    path('vacancies/<int:category_id>/', vacancies_detail),
    path('vacancies/top_ten/', vacancy_top_ten)
]