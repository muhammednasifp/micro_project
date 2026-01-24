from rest_framework import serializers
from placement.models import Placement_details
from student.models import Student,AcademicDetails,PlacementPreferences,Skill


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class AcademicSerializer(serializers.ModelSerializer):
    class Meta:
        model=AcademicDetails
        fields='__all__'

class PreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model=PlacementPreferences
        fields='__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model=Skill
        fields='__all__'

class PlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Placement_details
        fields='__all__'


