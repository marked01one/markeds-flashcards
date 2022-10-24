# cards/forms.py

from ctypes.wintypes import BOOLEAN
from django.forms import BooleanField, Form, IntegerField

class CardCheckForm(Form):
    
    # `card_id` --> The primary key (pk) of the card you're checking
    # `solved` --> Boolean value, True if you know the answer and False if not.
    
    # `card_id` is required to identify the card
    # `solved` is NOT required since you can leave the field unchecked if you don't know the answer.
    card_id = IntegerField(required=True)
    solved = BooleanField(required=False)

    
    