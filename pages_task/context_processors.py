from apps.book.models import TextNote
def notes_amount(request):
    try:
		obj=TextNote.objects.all()
		notes_amount=len(obj)
    except AttributeError:
        obj=None

    return {'notes_amount': notes_amount,}
