from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Blog, Article


class IndexView(generic.ListView):
    template_name = 'blogs/index.html'
    context_object_name = 'blogs_list'
    def get_queryset(self):
        q = Blog.objects.all()
        return q

class DetailView(generic.DetailView):
    template_name = 'blogs/detail.html'
    model = Blog

class NewArticleView(CreateView):
    model = Article
    fields = ['blog', 'headline', 'text', 'image']
    template_name = 'blogs/new_article.html'

    def form_valid(self, form):
        form.instance.pub_date = timezone.now()
        #return super(NewArticleView, self).form_valid(form)
        post = form.save(commit=False)
        post.save()
        id_blog = form.instance.blog.id
        chosen_blog = get_object_or_404(Blog, pk=id_blog)
        chosen_blog.art_count += 1
        chosen_blog.save()
        return HttpResponseRedirect(reverse('blogs:detail', args=(id_blog,)))


class ChangeArticleView(UpdateView):
    model = Article
    fields = ['headline', 'text', 'image']
    template_name = 'blogs/change_article.html'

    def get_success_url(self):
        return reverse('blogs:detail', kwargs={'pk': self.object.blog.id})

class DeleteArticleView(DeleteView):
    model = Article
    #success_url = reverse_lazy('polls:index')

    def get_success_url(self):
        id_blog = self.object.blog.id
        chosen_blog = get_object_or_404(Blog, pk=id_blog)
        chosen_blog.art_count -= 1
        chosen_blog.save()
        return reverse('blogs:detail', kwargs={'pk': id_blog})

"""

def send(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    try:
        selected_choice = blog.article_set.get(pk=request.POST['choice'])
    except (KeyError, Article.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'blog': blog,
            'error_message': "Your article wasn't send.",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('blogs:detail', args=(blog.id,)))
        
"""