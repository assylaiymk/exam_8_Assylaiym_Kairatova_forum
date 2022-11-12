from django.urls import path
from app.views.base import IndexView
from app.views.themes import ThemeCreate, ThemeView, ThemeDeleteView, ThemeUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('themes/add/', ThemeCreate.as_view(), name='theme_add'),
    path('themes/<int:pk>/update/', ThemeUpdateView.as_view(), name='theme_update'),
    path('themes/<int:pk>/delete/', ThemeDeleteView.as_view(), name='theme_delete'),
    path('themes/<int:pk>/confirm-delete/', ThemeDeleteView.as_view(), name='confirm_delete'),
    path('themes/', IndexView.as_view()),
    path('themes/<int:pk>', ThemeView.as_view(), name='theme_detail')
]