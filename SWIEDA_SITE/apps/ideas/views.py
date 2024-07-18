from django.shortcuts import render, redirect
from .models import Idea
from .forms import IdeaForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

# Create your views here.
def main(req):
    so = req.GET.get('so', '')

    if so == 'title':
        ideas = Idea.objects.all().order_by('title','-updated_date')
    elif so == 'register':
        ideas = Idea.objects.all().order_by('-created_date')
    elif so == 'dibs':
        ideas = Idea.objects.all().order_by('-dibs','-updated_date')
    else:
        ideas = Idea.objects.all().order_by('-updated_date')
    ctx = {'ideas' : ideas, 'so': so}
    return render(req, 'ideas/list.html', ctx)

def register(req):
    if req.method == "GET":
        form = IdeaForm()
        ctx = {'form': form}
        return render(req, 'ideas/register.html', ctx)
    form = IdeaForm(req.POST, req.FILES)
    if form.is_valid():
        new_idea = form.save()
    return redirect('ideas:detail', new_idea.pk)

def detail(req, pk):
    idea = Idea.objects.get(id=pk)

    ctx = {"idea":idea}

    return render(req, 'ideas/detail.html', ctx)

def delete(req, pk):
    Idea.objects.get(id=pk).delete()
    return redirect('ideas:main')

def update(req, pk):
    idea = Idea.objects.get(id=pk)
    if req.method == "GET":
        form = IdeaForm(instance=idea)
        ctx = {"form": form, 'pk':pk}
        return render(req, "ideas/update.html", ctx)
    
    form = IdeaForm(req.POST, req.FILES, instance = idea)
    if form.is_valid():
        form.save()
    return redirect('ideas:detail',pk)

@require_POST
def interest(req, pk, action):
    idea = get_object_or_404(Idea,pk=pk)

    if action == 'increase':
        idea.interest +=1
    elif action == 'decrease' and idea.interest > 0:
        idea.interest -=1
    idea.save()

    return JsonResponse({'interest':idea.interest})