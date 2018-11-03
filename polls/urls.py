from django.urls import path
from polls.views import index, detail, vote, results
app_name = 'polls'
urlpatterns = [
    # polls/
    path('', index, name='index'),
    # polls/5/
    path('<int:question_id>/', detail, name='detail'),
    # polls/5/results/
    path('<int:question_id>/results/', results, name='results'),
    # polls/5/vote/
    path('<int:question_id>/vote/', vote, name='vote'),
]