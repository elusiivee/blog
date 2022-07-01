from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import Person


def index(request: HttpRequest) -> HttpResponse:  # GET/POST
    context = {'Person': Person.objects.all()}  # получаем всех преподавателей
    return render(request, 'index.html', context)


def add_Person(request):
    if request.method == 'POST':
        # получаем данные из формы, но для этого есть такая штука как джанго forms
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        age = request.POST.get('age')
        city = request.POST.get('city')
        email = request.POST.get('email')

        new_Person = Person(name=name, surname=surname, age=age, city=city, email=email, )
        new_Person.save()
        print("Person added!")
        return redirect('/')
    return render(request, 'add_Person.html')


def delete(request, id: int):
    if Person.objects.filter(id=id).exists():
        Person.objects.get(id=id).delete()
        print("Person deleted!")
    return redirect('/')



def profile(request, pk: int):
    person = Person.objects.get(pk =pk)
    print(person)
    if request.method == 'POST':
        if Person.objects.filter(id=id).exists():
            Person.objects.get(id=id)
            return redirect('/')
    return render(request, 'profile.html', {'Person':person})
