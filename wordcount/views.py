from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    word_count = {}
    for word in words:
        if word.isalpha():
            word_count.setdefault(word, 0)
            word_count[word] += 1
    words = sorted(word_count.items(),
                   key=operator.itemgetter(1), reverse=True)
    print(words)

    return render(request, 'count.html', {'text': fulltext, 'word_counter': words, 'len': sum(y for x, y in words)})


def about(request):
    return render(request, 'about.html')
