# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def getSum(a, b):
    sum = 0
    for i in range(a,b):
        sum += i
    return sum

def view_home(request):
    output = getSum(0, 10)
    games = [
        ["Patriots", "Redskins"],
        ["Porn", "Hub"],
        ["Siraj", "chokeme"],
        ["Siraj", "chokeme"],
        ["Siraj", "chokeme"],
        ["Siraj", "chokeme"],
        ["Siraj", "chokeme"],
        ["Siraj", "chokeme"],
        ["Siraj", "chokeme"],
        ["Siraj", "chokeme"],
        ["Siraj", "chokeme"],
        ["Siraj", "chokeme"],
        ["Siraj", "chokeme"]
    ]

    return render(request, 'index.html', {'output': output,
                                          'numberOfGames': games.__len__(),
                                          'games': games})