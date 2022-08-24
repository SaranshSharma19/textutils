# I have created this file
from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse('''<h1>Hello</h1> <a href=
#     "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9"> Django Code With Harry </a>''')
#
# def about(request):
#     return HttpResponse('Hi Saransh This side')

def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    global params
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')

    fullcaps = request.POST.get('fullcaps', 'off')
    fullsmall = request.POST.get('fullsmall', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>.}?@#$%^&_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Convert to Upper-Case', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullsmall == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose': 'Convert to Lower-Case', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for x, char in enumerate(djtext):
            if djtext[x] == " " and djtext[x + 1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if spaceremover == "on":
        analyzed = ""
        for x, char in enumerate(djtext):
            if djtext[x] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and spaceremover != "on" and fullsmall != "on" and fullcaps != "on":
        return HttpResponse("Error")

    if charcounter == "on":
        analyzed = 0
        i = 0
        while i < len(djtext):
            i = i + 1
            analyzed = i

        params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    return render(request, 'analyze.html', params)


def home(request):
    return render(request, 'Home.html')


def contact(request):
    return render(request, 'Contact.html')


def about(request):
    return render(request, 'About.html')
