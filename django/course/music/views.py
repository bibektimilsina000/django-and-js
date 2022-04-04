from pyexpat import model
from re import template
from django.views import generic
from . models import Album, Song

class IndexView(generic.ListView):
    template_name="index.html"

    context_object_name="object_list"

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name="detail.html"






























































































































































































































































































































































































































