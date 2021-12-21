from django.urls import path
from . import views


"""
Criar padrões de url. E esses padrões de URL, um deles é: vazio, e eles vão estão associados ao arquivo views.index
"""

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
