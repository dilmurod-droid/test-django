from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestViewSet, QuestionViewSet, AnswerViewSet, UserViewSet, UserRegistrationView, \
    CustomTokenObtainPairView, home_view
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'tests', TestViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'answers', AnswerViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('',home_view,name='home'),
    path('api/', include(router.urls)),
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
