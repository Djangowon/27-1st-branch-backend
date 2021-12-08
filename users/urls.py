from django.urls import path, include

from .views      import MyProfileView, SignUpView, SignInView
from .views      import UserListView
from .views      import UserProfileView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/', UserListView.as_view()),
    path('/<int:user_id>', UserProfileView.as_view()),
    path('/mypage', MyProfileView.as_view()),
]
