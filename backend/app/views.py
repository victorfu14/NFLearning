# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import random

# Create your views here.
def getSum(a, b):
    sum = 0
    for i in range(a,b):
        sum += i
    return sum

def view_home(request):
    output = getSum(0, 10)
    teams = [
        ['ARI', 'Arizona', 'Cardinals', 'Arizona Cardinals'],
        ['ATL', 'Atlanta', 'Falcons', 'Atlanta Falcons'],
        ['BAL', 'Baltimore', 'Ravens', 'Baltimore Ravens'],
        ['BUF', 'Buffalo', 'Bills', 'Buffalo Bills'],
        ['CAR', 'Carolina', 'Panthers', 'Carolina Panthers'],
        ['CHI', 'Chicago', 'Bears', 'Chicago Bears'],
        ['CIN', 'Cincinnati', 'Bengals', 'Cincinnati Bengals'],
        ['CLE', 'Cleveland', 'Browns', 'Cleveland Browns'],
        ['DAL', 'Dallas', 'Cowboys', 'Dallas Cowboys'],
        ['DEN', 'Denver', 'Broncos', 'Denver Broncos'],
        ['DET', 'Detroit', 'Lions', 'Detroit Lions'],
        ['GB', 'Green Bay', 'Packers', 'Green Bay Packers', 'G.B.', 'GNB'],
        ['HOU', 'Houston', 'Texans', 'Houston Texans'],
        ['IND', 'Indianapolis', 'Colts', 'Indianapolis Colts'],
        ['JAC', 'Jacksonville', 'Jaguars', 'Jacksonville Jaguars', 'JAX'],
        ['KC', 'Kansas City', 'Chiefs', 'Kansas City Chiefs', 'K.C.', 'KAN'],
        ['LA', 'Los Angeles', 'Rams', 'Los Angeles Rams', 'L.A.'],
        ['MIA', 'Miami', 'Dolphins', 'Miami Dolphins'],
        ['MIN', 'Minnesota', 'Vikings', 'Minnesota Vikings'],
        ['NE', 'New England', 'Patriots', 'New England Patriots', 'N.E.', 'NWE'],
        ['NO', 'New Orleans', 'Saints', 'New Orleans Saints', 'N.O.', 'NOR'],
        ['NYG', 'Giants', 'New York Giants', 'N.Y.G.'],
        ['NYJ', 'Jets', 'New York Jets', 'N.Y.J.'],
        ['OAK', 'Oakland', 'Raiders', 'Oakland Raiders'],
        ['PHI', 'Philadelphia', 'Eagles', 'Philadelphia Eagles'],
        ['PIT', 'Pittsburgh', 'Steelers', 'Pittsburgh Steelers'],
        ['SD', 'San Diego', 'Chargers', 'San Diego Chargers', 'S.D.', 'SDG'],
        ['SEA', 'Seattle', 'Seahawks', 'Seattle Seahawks'],
        ['SF', 'San Francisco', '49ers', 'San Francisco 49ers', 'S.F.', 'SFO'],
        ['STL', 'St. Louis', 'Rams', 'St. Louis Rams', 'S.T.L.'],
        ['TB', 'Tampa Bay', 'Buccaneers', 'Tampa Bay Buccaneers', 'T.B.', 'TAM'],
        ['TEN', 'Tennessee', 'Titans', 'Tennessee Titans'],
        ['WAS', 'Washington', 'Redskins', 'Washington Redskins', 'WSH'],
    ]

    games = [ [random.choice(teams)[2], random.choice(teams)[2]] for i in range(10)]
    return render(request, 'index.html', {'output': output,
                                          'numberOfGames': games.__len__(),
                                          'games': games})