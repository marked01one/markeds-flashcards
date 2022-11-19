from multiprocessing.managers import BaseManager
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from cards.forms import CardCheckForm
from .models import Card, Group
import random

# Class for creating a list of flashcards
class CardListView(ListView):
    model: object = Card
    queryset = Card.objects.all().order_by("box", "-date_created")

# Class for creating a new card
class CardCreateView(CreateView):
    model: object = Card
    fields: list = ["question", "answer", "group_name"]
    success_url = reverse_lazy("card-create")

# Class for updating the values of a card
class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy("card-list")

class CardDeleteView(DeleteView):
    model: object = Card
    queryset: Card.objects.filter(answer=Card.answer)
    success_url = reverse_lazy("card-delete")

# Class for viewing contents of a single box
class BoxView(CardListView):
    template_name: str = "cards/box.html"
    form_class = CardCheckForm
    
    # Return a queryset of all card objects that fall under a specific box number
    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs["box_num"])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["box_number"] = self.kwargs["box_num"]
        if self.object_list:
            context["check_card"] = random.choice(self.object_list)
        return context

    # Handle incoming POST requests from the flashcard options 
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Find the required Card object or returns a 404 error
            card = get_object_or_404(Card, id=form.cleaned_data["card_id"])
            
            # Move the card to the next level if solved == True, return card to 1st level otherwise
            card.move(form.cleaned_data["solved"])
        
        # Redirect the POST request to the same page from which the POST request originates
        # "HTTP_REFERER" is holding the original URL of the POST, which is stored in the .META object of the request
        return redirect(request.META.get('HTTP_REFERER'))

class NewGroupView(CreateView):
    model = Group
    fields: list = ["name", "description"]
    success_url = reverse_lazy('new-group')
    
class GroupDeleteView(DeleteView):
    
    pass

class GroupView(CardListView, Group):
    template_name: str = "cards/group.html"
    
    def get_queryset(self):
        return Card.objects.filter(group_name=self.kwargs['group_name'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["group_name"] = self.kwargs["group_name"]
        for group in Group.objects.all():
            if self.kwargs['group_name'] == group.name:
                context['description'] = group.description
        return context
        