from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
	path('category_science/', views.category_science, name='category_science'),
	path('category_lifestyle/', views.category_lifestyle, name='category_lifestyle'),
	path('category_opinion/', views.category_opinion, name='category_opinion'),
	path('category_general/', views.category_general, name='category_general'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
	path('question_list/', views.question_list, name='question_list'),
	path('latest_questions/', views.latest_questions, name='latest_questions'),
]
