from random import choices
from types import new_class
from django.db import models

# Indicate how many boxes are in the app
NUM_BOXES = 10

# Allow iteration through range of 1 -> 5 (more user-friendly) instead of 0 -> 4
BOXES = range(1, NUM_BOXES + 1)

# Class that model the card objects of the app
class Card(models.Model):
    question = models.CharField(max_length=280)
    answer = models.CharField(max_length=280)
    box = models.IntegerField(
        choices=zip(BOXES, BOXES),
        default=BOXES[0],
    )
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.question
    
    def move(self, solved: bool):
        new_box = self.box + 1 if solved else BOXES[0]
        
        if new_box in BOXES:
            self.box = new_box
            self.save()
        
        return self