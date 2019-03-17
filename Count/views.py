from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render (request,'home.html')


def contact(request):
    return HttpResponse('<h1>Contact</h1><br>Thanks for contacting us')

def count(request):
    data=request.GET['fulltextarea']
    # print(data)
    word_list=data.split()
    list_length=len(word_list)
    wordict={}
    for word in word_list:
        if word in wordict:
            wordict[word]+=1
        else:
            wordict[word]=1

    sorted_list=sorted(wordict.items() ,key=operator.itemgetter(1),reverse=True)

    return render (request,'count.html',{'fulltext':data,'wordlen':list_length,'counts':sorted_list})

def about(request):
    return render (request,'about.html')
