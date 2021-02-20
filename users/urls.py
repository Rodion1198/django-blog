from django.urls import path

from .views import CreateProfilePageView, EditProfilePageView, PasswordsChangeView, ShowProfilePageView, UserEditView,\
    UserRegisterView


urlpatterns = [
    path('registration/', UserRegisterView.as_view(), name='registration'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),

]
