from django.contrib import admin
from django.urls import path, include

# Three modules for swagger:
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="******** API",   # Bu title projenin ismine göre değiştirilebilir.
        default_version="v1",
        description="This is a ........ ",
        terms_of_service="#",
        contact=openapi.Contact(email="baaser.osman@gmail.com"),  # Change e-mail on this line!
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("admin/", admin.site.urls),

    # Four url paths for swagger:
    path("swagger(<format>\.json|\.yaml)", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path('__debug__/', include('debug_toolbar.urls')),

    #myapps
    path("users/", include('users.urls')),
    path("api/", include('quizApp.urls')),
    path('nested_admin/', include('nested_admin.urls')),
]

