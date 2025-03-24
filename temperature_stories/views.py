from django.shortcuts import render 

# Create your views here.
# use f-strings for easy string formatting https://realpython.com/python-fstrings/ 

def story():
		mystory = ("some random content")
		return mystory

def index(request):
		mystory = story()
		return render(request, 'temperature_stories/index.html', {'story': mystory})
