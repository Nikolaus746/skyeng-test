from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('', views.note_list, name='index'),
    path('note/<slug:uuid>/', views.note_detail, name='note'),
    path('ajax/', views.note_list_ajax, name='ajax'),
    path('delete-note/<slug:uuid>/', csrf_exempt(views.DeleteNote.as_view()), name='delete-note'),
    path('update-note/<slug:uuid>/', csrf_exempt(views.UpdateNote.as_view()), name='update-note'),
    path('note-update/<slug:pk>/', views.NoteUpdateView.as_view(), name='note-update'),
    path('note-create/', views.create_note, name='note-create'),
]
