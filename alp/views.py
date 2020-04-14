from django.shortcuts import render



def match_list(request):
    return render(request, 'alp/match_list.html', {})