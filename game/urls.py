from django.urls import path

from game import views

urlpatterns = [
    path('store/', views.GameHomeView.as_view(), name='store'),
    path('create_game/', views.GameCreateView.as_view(), name='create-game'),
    path('list_of_games/', views.GameListView.as_view(), name='list-of-games'),
    path('update_game/<int:pk>/', views.GameUpdateView.as_view(), name='update-game'),
    path('delete_game/<int:pk>/', views.GameDeteleView.as_view(), name='delete-game'),
]
