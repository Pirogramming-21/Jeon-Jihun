from django.shortcuts import render, redirect
from .models import Tool
from .forms import ToolForm

# Create your views here.
def list(req):
    tools = Tool.objects.all()
    ctx = {'tools' : tools}
    return render(req, 'tools/list.html', ctx)

def register(req):
    if req.method == "GET":
        form = ToolForm()
        ctx = {'form': form}
        return render(req, 'tools/register.html', ctx)
    form = ToolForm(req.POST, req.FILES)
    if form.is_valid():
        new_tool = form.save()
    return redirect('tools:detail',new_tool.pk)

def detail(req, pk):
    tool = Tool.objects.get(id=pk)
    name =  tool.name
    if name:
        related_ideas = name.title
    else:
        related_ideas = []
    ctx = {"tool":tool, "related_ideas":related_ideas}

    return render(req, 'tools/detail.html', ctx)

def delete(req, pk):
    Tool.objects.get(id=pk).delete()
    return redirect('tools:list')

def update(req, pk):
    tool = Tool.objects.get(id=pk)
    if req.method == "GET":
        form = ToolForm(instance=tool)
        ctx = {"form": form, 'pk':pk}
        return render(req, "tools/update.html", ctx)
    
    form = ToolForm(req.POST, req.FILES, instance = tool)
    if form.is_valid():
        form.save()
    return redirect('tools:detail',pk)