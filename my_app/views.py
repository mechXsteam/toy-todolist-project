from django.shortcuts import render, redirect

from .forms import TopicForm
from .models import Topic


# Create your views here.

def home(request):
    """Add a new topic"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('my_app:home')
    # Display a blank or invalid form.
    topics = Topic.objects.all()
    context = {'form': form, 'topics': topics}
    return render(request, 'index.html', context)
