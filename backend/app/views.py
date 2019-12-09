# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import random
import requests

import bs4 as bs

import tensorflow as tf
import numpy as np
import pandas as pd
import os

# url = ("https://www.si.com/nfl/schedule")
# r = requests.get(url)

# soup = bs.BeautifulSoup(r.content, "html.parser")
# print(soup)

# s = soup.find_all("div", )

# Create your views here.

def view_home(request):
    
    # load teams
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
        ['JAX', 'Jacksonville', 'Jaguars', 'Jacksonville Jaguars', 'JAX'],
        ['KC', 'Kansas City', 'Chiefs', 'Kansas City Chiefs', 'K.C.', 'KAN'],
        ['LA', 'Los Angeles', 'Rams', 'Los Angeles Rams', 'L.A.'],
        ['LAC', 'Los Angeles', 'Chargers', 'Los Angeles Chargers'],
        ['MIA', 'Miami', 'Dolphins', 'Miami Dolphins'],
        ['MIN', 'Minnesota', 'Vikings', 'Minnesota Vikings'],
        ['NE', 'New England', 'Patriots', 'New England Patriots', 'N.E.', 'NWE'],
        ['NO', 'New Orleans', 'Saints', 'New Orleans Saints', 'N.O.', 'NOR'],
        ['NYG', 'Giants', 'New York Giants', 'N.Y.G.'],
        ['NYJ', 'Jets', 'New York Jets', 'N.Y.J.'],
        ['OAK', 'Oakland', 'Raiders', 'Oakland Raiders'],
        ['PHI', 'Philadelphia', 'Eagles', 'Philadelphia Eagles'],
        ['PIT', 'Pittsburgh', 'Steelers', 'Pittsburgh Steelers'],
        ['SEA', 'Seattle', 'Seahawks', 'Seattle Seahawks'],
        ['SF', 'San Francisco', '49ers', 'San Francisco 49ers', 'S.F.', 'SFO'],
        ['TB', 'Tampa Bay', 'Buccaneers', 'Tampa Bay Buccaneers', 'T.B.', 'TAM'],
        ['TEN', 'Tennessee', 'Titans', 'Tennessee Titans'],
        ['WAS', 'Washington', 'Redskins', 'Washington Redskins', 'WSH'],
    ]

    # get the home dir
    module_dir = os.path.dirname(__file__)

    # load team data
    home_stat_path = os.path.join(module_dir, 'static/team_data/home_stats_mod.csv')
    away_stat_path = os.path.join(module_dir, 'static/team_data/away_stats_mod.csv')
    with open(home_stat_path) as data:
        home_stat = pd.read_csv(data, index_col=0)
    with open(away_stat_path) as data:
        away_stat = pd.read_csv(data, index_col=0)
    
    games = [random.sample(teams, 2) for i in range(10)]

    # load tf models
    model_path = os.path.join(module_dir, 'static/ts_model')
    imported=tf.saved_model.load(model_path)

    # load data according to team selection
    length = len(games)
    inputdata = np.ones((length,11))
    for i, teams in enumerate(games):
        home = teams[0][0]
        away = teams[1][0]
        home_input = np.asarray(list(home_stat.loc[home]))
        away_input = np.asarray(list(away_stat.loc[away]))
        input = home_input - away_input
        inputdata[i] = input
        
    inputdata = tf.dtypes.cast(tf.math.sigmoid(inputdata), tf.float32)

    # calculate
    outputs = imported(inputdata)

    # format data passed to the frontend
    output=outputs.numpy()
    final_output=[]
    for i in range(output.shape[0]):
        if(output[i,0]>output[i,1]):
            final_output.append(0)
        if(output[i,0]<output[i,1]):
            final_output.append(1)

    # getting data for victory.js visualization
    stats = home_stat.join(away_stat)
    index = list(stats.index)
    columns = list(stats.columns)

    choices = [random.sample(columns, 2) for i in range(3)]
    selections = [stats[choices[i]].reset_index().rename(columns={"Home":"label"}).to_dict('records') for i in range (3)]
    keys = [list(selections[i][0].keys()) for i in range(3)]   
    
    return render(request, 'index.html', {'numberOfGames': games.__len__(),
                                          'games': games,
                                          'results': list(final_output),
                                          'prob': output.tolist(),
                                          'visual': selections,
                                          'visual_keys': keys})

def feedback(request):
    return render(request, 'rating.html')

def current_games(request):
    return render(request, 'current_games.html')