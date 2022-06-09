from django.urls import path, include
from .views import RegisterAPIs

urlpatterns = [   
    path('auth/', include('dj_rest_auth.urls')),
    path("register/", RegisterAPIs.as_view()),
]