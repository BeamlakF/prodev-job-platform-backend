from rest_framework import serializers
from .models import User, Category, Job, Application

# ----------------------------
# User Serializer
# ----------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

# ----------------------------
# Category Serializer
# ----------------------------
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

# ----------------------------
# Job Serializer
# ----------------------------
class JobSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    posted_by = UserSerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'location', 'job_type', 'category', 'category_id', 'posted_by', 'created_at', 'updated_at']

# ----------------------------
# Application Serializer
# ----------------------------
class ApplicationSerializer(serializers.ModelSerializer):
    applicant = UserSerializer(read_only=True)
    job = JobSerializer(read_only=True)
    job_id = serializers.PrimaryKeyRelatedField(
        queryset=Job.objects.all(), source='job', write_only=True
    )

    class Meta:
        model = Application
        fields = ['id', 'applicant', 'job', 'job_id', 'cover_letter', 'applied_at']
