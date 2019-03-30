from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/<str:searchString>', views.search, name = 'search'),
    path('player/<int:playerId>', views.player, name = 'player'),
    path('page', views.anotherPage, name = 'page'),
    path('polls/<int:qid>', views.details, name = "details")
]
