from rest_framework import serializers
from .models import User, Category, Job, Application

# -----------------
# User Serializer
# -----------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

# -----------------
# Category Serializer
# -----------------
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# -----------------
# Job Serializer
# -----------------
class JobSerializer(serializers.ModelSerializer):
    posted_by = UserSerializer(read_only=True)  # include user info
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'location', 'job_type', 'category', 'posted_by', 'created_at', 'updated_at']

# -----------------
# Application Serializer
# -----------------
class ApplicationSerializer(serializers.ModelSerializer):
    applicant = UserSerializer(read_only=True)
    job = JobSerializer(read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'applicant', 'job', 'cover_letter', 'applied_at']
