from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from placement.models import Placement_details
from student.models import Student,PlacementPreferences,Skill,AcademicDetails
from .serializers import PlacementSerializer,StudentSerializer,AcademicSerializer,SkillSerializer,PreferencesSerializer
# Create your views here.
# GET all placements
@api_view(['GET'])
def placement_list(request):
    placements = Placement_details.objects.all()
    serializer = PlacementSerializer(placements, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def student_list(request):
    student = Student.objects.all()
    serializer = StudentSerializer(student, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def academic_list(request):
    academic = AcademicDetails.objects.all()
    serializer = AcademicSerializer(academic, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def preferences_list(request):
    pref = PlacementPreferences.objects.all()
    serializer = PreferencesSerializer(pref, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def skill_list(request):
    skill = Skill.objects.all()
    serializer = SkillSerializer(skill, many=True)
    return Response(serializer.data)