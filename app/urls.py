from django.urls import path
from app.views.base import IndexView
from app.views.themes import ThemeCreate, ThemeView, ThemeDeleteView, ThemeUpdateView
from app.views.replies import ReplyCreate, ReplyView, ReplyUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('themes/add/', ThemeCreate.as_view(), name='theme_add'),
    path('themes/<int:pk>/update/', ThemeUpdateView.as_view(), name='theme_update'),
    path('themes/<int:pk>/delete/', ThemeDeleteView.as_view(), name='theme_delete'),
    path('themes/<int:pk>/confirm-delete/', ThemeDeleteView.as_view(), name='confirm_delete'),
    path('themes/', IndexView.as_view()),
    path('themes/<int:pk>', ThemeView.as_view(), name='theme_detail'),
    path('replies/add/', ReplyCreate.as_view(), name='reply_add'),
    path('replies/<int:pk>', ReplyView.as_view(), name='reply_detail'),
    path('replies/<int:pk>/update/', ReplyUpdateView.as_view(), name='reply_update')
]