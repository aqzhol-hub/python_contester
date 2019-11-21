from django.urls import path
from . import views
from python_contester import settings

# if settings.DEBUG:  
#     urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('', views.index, name = 'mainPage'),
    path('currentTask/<int:task_id>/', views.currentTask, name='currentTask'),#every task
    path('moreProblems/', views.moreProblems, name = 'moreProblems'),


    path('rating/', views.rating ,name ='rating' ),
    path('signIn/',views.signIn ,name = 'signIn'),
    path('signUp/', views.signUp ,name = 'signUp'),
    path('userpage/', views.userpage ,name = 'userpage'),
]
