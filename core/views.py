from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User, Category, Job, Application
from .serializers import UserSerializer, CategorySerializer, JobSerializer, ApplicationSerializer
from .permissions import IsAdmin, IsUser, IsOwnerOrReadOnly


# ----------------------------
# User ViewSet (Admins only)
# ----------------------------
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]   # ✅ Only admins can manage users


# ----------------------------
# Category ViewSet
# ----------------------------
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdmin]   # ✅ Only admins manage categories


# ----------------------------
# Job ViewSet
# ----------------------------
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly | IsAdmin]

    def perform_create(self, serializer):
        serializer.save(posted_by=self.request.user)  # ✅ User creating job = "owner"


# ----------------------------
# Application ViewSet
# ----------------------------
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        """
        - Users can create their own applications.
        - Admins can view/manage all applications.
        """
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsUser()]   # ✅ Only normal users can apply
        return [IsAuthenticated(), IsAdmin()]      # ✅ Admins can view/manage all

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)  # ✅ link applicant to logged-in user
