from django.urls import include, path

urlpatterns = [
    path('api-docs/', include('api_docs.urls')),
]
