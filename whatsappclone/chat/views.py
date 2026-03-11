from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import DetailView
from django.core.paginator import Paginator
from chat.models import Post, PostNotification


def welcome_view(request):
    return HttpResponse("App running")


def posts(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    posts_in_pg2 = paginator.page(2)
    print(paginator.count)
    print(paginator.num_pages)
    print(paginator.page_range)
    print(paginator.page(2))
    print(posts_in_pg2.has_next())
    print(posts_in_pg2.has_previous())
    print(posts_in_pg2.has_other_pages())
    print(posts_in_pg2.next_page_number())
    print(posts_in_pg2.previous_page_number())
    print(posts_in_pg2.start_index())
    print(posts_in_pg2.end_index())
    return render(request, 'posts.html', {'posts': paginator})


class PostNotificationDetailView(DetailView):
    model = PostNotification
    template_name = 'postnotification.html'
    context_object_name = 'postnotification'
