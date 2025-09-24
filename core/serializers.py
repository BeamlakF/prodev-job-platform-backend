from rest_framework import serializers
from .models import User, Category, Job, Application

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class JobSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    posted_by = UserSerializer(read_only=True)

    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'location', 'job_type', 'category', 'posted_by', 'created_at']

class ApplicationSerializer(serializers.ModelSerializer):
    applicant = UserSerializer(read_only=True)
    job = JobSerializer(read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'applicant', 'job', 'cover_letter', 'applied_at']
