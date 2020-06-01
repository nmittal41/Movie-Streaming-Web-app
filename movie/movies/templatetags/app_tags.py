from django import template

register = template.Library()

# Not used

@register.filter()
def chunks(l):
    # For item i in a range that is a length of l,
    n = 3
    temp = []
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        temp.append(l[i:i+n])
    return temp
