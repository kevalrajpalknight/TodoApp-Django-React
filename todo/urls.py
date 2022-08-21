from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

routers = DefaultRouter()
routers.register(r'api/todos', TaskViewSet, 'todos')

urlpatterns = routers.urls