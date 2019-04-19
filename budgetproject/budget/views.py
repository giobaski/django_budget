from django.shortcuts import render

# Create your views here.
def project_list(request):
    template_name = 'budget/project-list.html'
    context = {}
    return render(request, template_name, context)

def project_detail(request, project_slug):
    template_name = 'budget/project-detail.html'
    context = {}
    return render(request,template_name,context)
