# cards/templatetags/group_tags.py

from typing import Dict
from django import template

from cards.models import Group, Card

# Create an instance of `Library` used for registering your template tags
register = template.Library()

# We used the `inclusion_tag()` method form `Library` as a decorator.
# This tells Django that `groups_as_links()` is an inclusion tag
# Inclusion tags are template tags that display some data by rendering another template
# In this case, the original template for `groups_as_links()` is the box template created in `cards/group_template.html`
@register.inclusion_tag("cards/group_template.html")
def groups_as_links() -> Dict:
    groups = []
    for group in Group.objects.all():
        card_per_group = Card.objects.filter(group_name=group.name).count()
        groups.append({
            "name": group.name,
            "cards_per_group": card_per_group,
        })
    return {"groups": groups}
        

# Result: output a dictionary with all boxes generated.