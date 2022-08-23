from django.urls import path
from .views import createViewAccount, editDeleteAccount

urlpatterns = [
    path('createAccount/', createViewAccount.as_view()),
    path('updateAccount/<int:pk>/', editDeleteAccount.as_view()),
    # path ('login/', loginUser.as_view()),
    # path('loggedUser',Logged_in_user.as_view()),
    # path('logout', Log_out.as_view()),
]