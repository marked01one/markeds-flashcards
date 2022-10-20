# cards/templatetags/cards_tags.py

from ast import Dict
from django import template

from cards.models import BOXES, Card

# Create an instance of `Library` used for registering your template tags
register = template.Library()

# We used the `inclusion_tag()` method form `Library` as a decorator.
# This tells Django that `boxes_as_links()` is an inclusion tag
# Inclusion tags are template tags that display some data by rendering another template
# In this case, the original template for `boxes_as_links()` is the box template created in `cards/box_links.html`
@register.inclusion_tag("cards/box_template.html")
def boxes_as_links() -> Dict:
    boxes = []
    for box_num in BOXES:
        card_count = Card.objects.filter(box=box_num).count()
        boxes.append({
            "number": box_num,
            "card_count": card_count,
        })
    return {"boxes": boxes}

# Result: output a dictionary with all boxes generated.