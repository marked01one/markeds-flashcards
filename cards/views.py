from multiprocessing.managers import BaseManager
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)

from .models import Card

# Class for creating a list of flashcards
class CardListView(ListView):
    model: object = Card
    queryset = Card.objects.all().order_by("box", "-date_created")

# Class for creating a new card
class CardCreateView(CreateView):
    model: object = Card
    fields: list = ["question", "answer", "box"]
    success_url = reverse_lazy("card-create")

class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy("card-list")
