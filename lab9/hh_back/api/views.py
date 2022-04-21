from django.http import JsonResponse
from django.shortcuts import render
from api.models import Company, Vacancy

# Create your views here.
#a
def companies_list(request):
    companies = Company.objects.all()
    companies_json = [companies.to_json() for company in companies]
    return JsonResponse(companies_json, safe=0)
#b
def companies_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message' : str(e)})
    return JsonResponse(company.to_json())

#d
def vacancies_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancies.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=0)

#e
def vacancies_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message':str(e)})
    return JsonResponse(vacancy.to_json())

#f
def vacancy_top_ten():
    ordered = Vacancy.objects.order_by('-salary')[:10]
    return JsonResponse(ordered.to_json())
