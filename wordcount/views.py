from django.shortcuts import render
import collections, re, string

# Create your views here.
def home(request):
    return render(request, 'home.html')
    ## render : 3개의 동작까지 받을 수 있다. - (고정적으로) request 객체, template의 이름, (선택적으로) 딕셔너리형 자료형
    
    
def about(request):
    return render(request, 'about.html')
    
    
def result(request):
    text = request.POST.get('fulltext')
    # request.GET['fulltext'] 로 받으려면 html파일에서 method="GET" 추가할 것
    words = re.sub('['+string.punctuation+']', '', text).split() # 문장부호 및 공백 제거
    word_dictionary = {}
    
    for word in words:
        if word in word_dictionary:
            # increase
            word_dictionary[word]+=1
        else:
            # add to dictionary
            word_dictionary[word]=1
    
    word_dictionary = collections.OrderedDict(sorted(word_dictionary.items())) # 오름차순 정렬
            
    return render(request, 'result.html', {'full': text, 'total': len(words), 'dictionary': word_dictionary.items()})