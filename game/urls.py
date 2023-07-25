from django.urls import path

from game import views

urlpatterns = [
    path('store/', views.GameHomeView.as_view(), name='store'),
    path('create_game/', views.GameCreateView.as_view(), name='create-game'),
    path('library/', views.GameListView.as_view(), name='library'),
    path('update_game/<int:pk>/', views.GameUpdateView.as_view(), name='update-game'),
    path('delete_game/<int:pk>/', views.GameDeteleView.as_view(), name='delete-game'),
    path('profile/', views.ProfileView.as_view(), name='profile'),

    path('purchase/<int:game_id>/', views.purchase_game, name='purchase_game'),
    path('user_library/', views.library, name='user_library'),

]
