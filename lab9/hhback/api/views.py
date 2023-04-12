from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from .models import Company, Vacancy
from .serializers import CompanySerializer, VacancySerializer

class CompanyList(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetail(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyVacanciesList(generics.ListAPIView):
    serializer_class = VacancySerializer

    def get_queryset(self):
        company_id = self.kwargs['id']
        company = get_object_or_404(Company, id=company_id)
        return company.vacancies.all()

class VacancyList(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyDetail(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class TopTenVacanciesList(generics.ListAPIView):
    queryset = Vacancy.objects.order_by('-salary')[:10]
    serializer_class = VacancySerializer
