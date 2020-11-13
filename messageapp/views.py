from django.shortcuts import render, get_object_or_404
from messageapp.models import MessagePost
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView
# Create your views here.


class MessageListView(ListView):
    queryset = MessagePost.datesent.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'messageapp/post/index.html'


# def message_post(request):
#     post_list = MessagePost.datesent.all()
#     paginator = Paginator(post_list, 3)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)

#     return render(request, 'messageapp/post/index.html', {'page': page, 'posts': posts})


def detail_post(request, year, month, day, post):
    post = get_object_or_404(MessagePost, slug=post,
                             status='sent',
                             date_send__year=year,
                             date_send__month=month,
                             date_send__day=day)
    return render(request, 'messageapp/post/detail.html', {'post': post})
