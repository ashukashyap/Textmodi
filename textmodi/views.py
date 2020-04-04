
from django.http import HttpResponse
from django.shortcuts import render



def index(request):

    return render(request, 'index.html')

def analyes(request):
    djtext=request.POST.get('text','defult')
    removef = request.POST.get('removef', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover' , 'off')
    extraspaceremover = request.POST.get('extraspaceremover' , 'off')

    if removef =="on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        ashu = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request,'analyze.html',ashu)

    elif (fullcaps == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        ashu = {'purpose': 'change to uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', ashu)

    elif (newlineremover == "on"):

        analyzed = ""

        for char in djtext:

            if char != "\n" and char != "\r":

                analyzed = analyzed + char





        ashu = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        print(ashu)

        return render(request, 'analyze.html', ashu)

    elif (extraspaceremover == "on"):
        analyzed = ""

        for index, char in enumerate(djtext):

            if not (djtext[index] == " " and djtext[index + 1] == " "):

                analyzed = analyzed + char

        ashu = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', ashu)

    else:

        return HttpResponse("Error")









