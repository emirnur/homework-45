from django.http import HttpResponseRedirect
from webapp.models import Tracker, STATUS_CHOICES
from webapp.forms import TrackerForm
from django.shortcuts import render, get_object_or_404, redirect


def index_view(request, *args, **kwargs):
    trackers = Tracker.objects.all()
    return render(request, 'index.html', context={
        'trackers': trackers
    })


def tracker_view(request, pk):
    tracker = get_object_or_404(Tracker, pk=pk)

    return render(request, 'tracker.html', context={
        'tracker': tracker
    })


def tracker_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = TrackerForm()
        return render(request, 'tracker_create.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = TrackerForm(data=request.POST)
        if form.is_valid():
            tracker = Tracker.objects.create(
                title=form.cleaned_data['title'],
                text=form.cleaned_data['text'],
                status=form.cleaned_data['status'],
                deadline=form.cleaned_data['deadline']
            )
            return redirect('tracker_view', pk=tracker.pk)
        else:
            return render(request, 'tracker_create.html', context={
                'form': form
            })

def tracker_update_view(request, pk):
    tracker = get_object_or_404(Tracker, pk=pk)
    if request.method == 'GET':
        form = TrackerForm(data={
            'title': tracker.title,
            'text': tracker.text,
            'status': tracker.status,
            'deadline': tracker.deadline,
        })
        return render(request, 'update.html', context={'form': form, 'tracker': tracker})
    elif request.method == 'POST':
        form = TrackerForm(data=request.POST)
        if form.is_valid():
            tracker.title = form.cleaned_data['title']
            tracker.text = form.cleaned_data['text']
            tracker.status = form.cleaned_data['status']
            tracker.deadline = form.cleaned_data['deadline']
            tracker.save()
            return redirect('tracker_view', pk=tracker.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'tracker': tracker})


def tracker_delete_view(request, pk):
    tracker = get_object_or_404(Tracker, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'tracker': tracker})
    elif request.method == 'POST':
        tracker.delete()
        return redirect('index')




