from django.urls import path
from .views import (
    CardListView,
    CardDetailView,
    CardDeleteView,
    CardUpdateView,
    CardGenerateView
)

app_name = 'card'
urlpatterns = [
    path('', CardListView.as_view(), name='card_list'),
    path('detail/<int:pk>/', CardDetailView.as_view(), name='card_detail'),
    path('delete/<int:pk>/', CardDeleteView.as_view(), name='card_delete'),
    path('update/<int:pk>/', CardUpdateView.as_view(), name='card_update'),
    path('generate/', CardGenerateView.as_view(), name='card_generate'),
]
