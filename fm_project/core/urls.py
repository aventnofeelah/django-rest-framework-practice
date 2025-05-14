from django.urls import path, include
from rest_framework import routers
from .views import UsersList, UserDetail, UserRegister, EventList, EventDetail, UserEventList, CreateChatMessage
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('users/', UsersList.as_view()),
    path('users/<int:pk>/<slug:slug>/', UserDetail.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('registration/', UserRegister.as_view()),
    path('events/', EventList.as_view()),
    path('events/<int:pk>/<slug:slug>/', EventDetail.as_view()),
    path('users/<int:pk>/<slug:slug>/events/', UserEventList.as_view()),
    path('events/<int:pk>/<slug:slug>/chat/', CreateChatMessage.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)