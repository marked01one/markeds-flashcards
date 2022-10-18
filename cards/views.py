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

# Class for updating the values of a card
class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy("card-list")

# Class for viewing contents of a single box
class BoxView(CardListView):
    template_name: str = "cards/box.html"
    
    # Return a queryset of all card objects that fall under a specific box number
    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs["box_num"])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        return context
