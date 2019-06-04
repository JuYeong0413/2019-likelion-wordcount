from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
    ## render : 3개의 동작까지 받을 수 있다. - (고정적으로) request 객체, template의 이름, (선택적으로) 딕셔너리형 자료형