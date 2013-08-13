from apps.book.models import TextNote
def notes_amount(request):
	"""
	This function create logic for task context processor.
	Exception block tries get from database all notes, then count them.
	Finally function returns total notes sum ini db.
	If any record found - returns None.
	"""
	try:
		obj=TextNote.objects.all()
		notes_amount=len(obj)
	except AttributeError:
		obj=None

	return {'notes_amount': notes_amount,}
