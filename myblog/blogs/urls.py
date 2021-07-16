from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('<int:pk>/send/', views.send, name='send')
    path('article/create/', views.NewArticleView.as_view(), name='create'),
    path('article/<int:pk>/update/', views.ChangeArticleView.as_view(), name='update'),
    path('article/<int:pk>/delete/', views.DeleteArticleView.as_view(), name='delete')
]