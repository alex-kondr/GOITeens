from rest_framework import serializers

from .models import Cabinet, Subject, Student, Grade


class CabinetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cabinet
        fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"
