from django import template
register = template.Library()


@register.simple_tag(name='get_note')
def get_note(obj, id):
    """
    This function create custom tag
    """
    for i in obj:
        if i.pk == id:
            return '''<div>
            <h2>{0}</h2>
            <h3>{1}</h3>
            </div>'''.format(i, i.value)
