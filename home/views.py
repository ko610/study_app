from django.views.generic import ListView
from question.models import PostQuestion

class PostQuestionListView(ListView):
    model = PostQuestion
    template_name = "home/index.html"
    context_object_name = 'postQuestions'
    ordering = ['-created_date']
    paginate_by = 100
