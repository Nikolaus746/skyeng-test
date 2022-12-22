from django.shortcuts import get_object_or_404, render
from notes.serializers import NoteSerializer
from .models import Note
from .forms import NoteModelForm
from rest_framework.generics import DestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.http import HttpResponseRedirect
from .filters import NoteFilter


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        pass  # To not perform the csrf check previously happening

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "index.html"
    login_url = '/accounts/login/'

class NoteListView(LoginRequiredMixin,ListView):
    login_url = '/accounts/login/'
    model = Note
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Note.objects.filter(user=self.request.user).order_by("datetime")
        return context


@login_required(login_url='/accounts/login/')
def note_detail(request, uuid):
    if request.method == "GET":
        note = get_object_or_404(Note, uuid=uuid)

        return render(request, 'note_detail.html', {'note': note })


@login_required(login_url='/accounts/login/')
def note_list(request):
    f = NoteFilter(request.GET, queryset=Note.objects.filter(user=request.user).order_by("datetime"))
    notes = f.qs
    if request.method == "GET":
        cd = request.GET
        sort = cd.get('sort', None)
        direct = cd.get('dir', None)
        if sort:
            if direct == 'desc':
                notes = notes.order_by(F"-{sort}")
            else:
                notes = notes.order_by(F"{sort}")

    return render(request, 'index.html', {'notes': notes, 'filter': f })


@login_required(login_url='/accounts/login/')
def note_list_ajax(request):
    if request.method == "GET":
        cd = request.GET
        notes = Note.objects.filter(user=request.user).order_by("datetime")
        sort = cd.get('sort', None)
        direct = cd.get('dir', None)
        if sort:
            if direct == 'desc':
                notes = notes.order_by(F"-{sort}")
            else:
                notes = notes.order_by(F"{sort}")
        return render(request, 'note_ajax.html', {'notes': notes })


class DeleteNote(DestroyAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = "uuid"


class UpdateNote(UpdateAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = "uuid"


class NoteUpdateView(LoginRequiredMixin, UpdateView):
    model = Note
    fields = ['title', 'text', 'category']
    template_name = "update.html"
    success_url = "/"

def create_note(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NoteModelForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            category = form.cleaned_data['category']
            is_favorites = form.cleaned_data['is_favorites']
            is_published = form.cleaned_data['is_published']
            user = request.user
            note = Note(user=user, title=title, text=text, category=category, is_favorites=is_favorites,
                        is_published=is_published)
            note.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NoteModelForm()

    return render(request, 'create.html', {'form': form})



