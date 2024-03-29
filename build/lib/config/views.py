from django.views.generic import ListView

from blog.views import CommonViewMiXin
from .models import Link
# Create your views here.


class LinkListView(CommonViewMiXin, ListView):
    queryset = Link.objects.filter(status=Link.STATUS_NORMAL)
    template_name = 'config/links.html'
    context_object_name = 'link_list'