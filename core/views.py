from rest_framework import viewsets, permissions
from .models import User, Category, Job, Application
from .serializers import UserSerializer, CategorySerializer, JobSerializer, ApplicationSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# ----------------------------
# User ViewSet (Admins only)
# ----------------------------
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

# ----------------------------
# Category ViewSet
# ----------------------------
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

# ----------------------------
# Job ViewSet
# ----------------------------
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)

# ----------------------------
# Application ViewSet
# ----------------------------
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)
