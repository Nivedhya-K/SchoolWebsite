from .models import  Departments
def menu_links(request):
    links=Departments.objects.all()
    return  dict(links=links)