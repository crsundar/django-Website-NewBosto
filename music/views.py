from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>Hi there, you are in MUSIC app homepage<h1>")

def detail(request, album_id):
	return HttpResponse("<h1>You're looking at album %s.</h1>" % album_id)
