import random

from django.shortcuts import render
from django.http import HttpRequest
from django.db.models import Q, Sum, Avg, Count
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cabinet, Subject, Student, Grade
from .serializers import CabinetSerializer, SubjectSerializer, StudentSerializer, GradeSerializer

# Create your views here.


def test_models(request: HttpRequest):
    # for i in range(1, 11):
    #     Cabinet.objects.create(name=f"Кабінет-{i}", description=f"Назва-{i}")

    # mat = Subject.objects.filter(name="Математика").first()
    # ist = Subject.objects.filter(name="Історія").first()
    # alg = Subject.objects.filter(name="Алгебра").first()
    # geo = Subject.objects.filter(name="Геометрія").first()
    # yads = Subject.objects.filter(name="ЯДС").first()
    # ukr_l = Subject.objects.filter(name="Українська мова").first()
    # ukr_h = Subject.objects.filter(name="Українська література").first()
    # fiz = Subject.objects.filter(name="Фізика").first()
    # him = Subject.objects.filter(name="Хімія").first()

    # student1 = Student.objects.create(full_name="Артем Скойбеда", age=random.randint(12, 18), cabinet=Cabinet.objects.get(pk=1))
    # student1.subjects.set([mat, ist])
    # student1.save()
    # student2 = Student.objects.create(full_name="Софія Яременко", age=random.randint(12, 18), cabinet=Cabinet.objects.get(pk=1))
    # student2.subjects.set([alg, geo, ukr_h])
    # student2.save()
    # student3 = Student.objects.create(full_name="Олександр Кондратюк", age=random.randint(12, 18), cabinet=Cabinet.objects.get(pk=1))
    # student3.subjects.set([mat, yads, ukr_l])
    # student3.save()
    # student4 = Student.objects.create(full_name="Владислав Митрофанов", age=random.randint(12, 18), cabinet=Cabinet.objects.get(pk=2))
    # student4.subjects.set([fiz, mat, geo, alg, ukr_h, ukr_l])
    # student4.save()
    # student5 = Student.objects.create(full_name="Владислав Музиченко", age=random.randint(12, 18), cabinet=Cabinet.objects.get(pk=2))
    # student5.subjects.set([mat, fiz])
    # student5.save()
    # student6 = Student.objects.create(full_name="Михайло Москаленко", age=random.randint(12, 18), cabinet=Cabinet.objects.get(pk=2))
    # student6.subjects.set([ukr_h, ukr_l])
    # student6.save()
    # student7 = Student.objects.create(full_name="Ілья Кузьмицький", age=random.randint(12, 18), cabinet=Cabinet.objects.get(pk=2))
    # student7.subjects.set([yads])
    # student7.save()
    # student8 = Student.objects.create(full_name="Ігор Пучков", age=random.randint(12, 18), cabinet=Cabinet.objects.get(pk=2))
    # student8.subjects.set([ist, him, fiz, alg, geo])
    # student8.save()
    # student9 = Student.objects.create(full_name="Богдан Савічев", age=random.randint(12, 18), cabinet=Cabinet.objects.get(pk=3))
    # student9.subjects.set([alg, geo])
    # student9.save()

    # for i in range(1, 11):
    #     Grade.objects.create(student=Student.objects.get(pk=random.randint(1, 27)), grade=random.randrange(1, 5), subject=random.choice([mat, alg, geo, ist, ukr_h, ukr_l, him, fiz]))

    return render(request, "Дані створено")


@api_view(["GET"])
def test_api(request: HttpRequest):
    # cabinets = Cabinet.objects.filter(Q(name__contains="абінет"), ~Q(description__contains="назва")).all()
    # data_cabinets = []
    # for cabinet in cabinets:
    #     data_cabinets.append(CabinetSerializer(cabinet).data)
    # return Response(data_cabinets)

    students = Student.objects.select_related("cabinet").prefetch_related("subjects").annotate(count_subj=Count("subjects"))
    for student in students:
        print(student.count_subj)

    data = StudentSerializer(students, many=True)
    return Response(data.data)
    # return Response(student)
