from django.urls import path, include

urlpatterns = [
    path('users', include('users.urls')),
    path('postings', include('postings.urls')),
    path('branch_tags', include('branch_tags.urls'))
]
