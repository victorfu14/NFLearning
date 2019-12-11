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

import datetime

from .forms import TeamPredictForm

import nflgame

# Create your views here.

def view_home(request):
    # load teams
    teams = {
        'ARI':['ARI', 'Arizona', 'Cardinals', 'Arizona Cardinals'],
        'ATL':['ATL', 'Atlanta', 'Falcons', 'Atlanta Falcons'],
        'BAL':['BAL', 'Baltimore', 'Ravens', 'Baltimore Ravens'],
        'BUF':['BUF', 'Buffalo', 'Bills', 'Buffalo Bills'],
        'CAR':['CAR', 'Carolina', 'Panthers', 'Carolina Panthers'],
        'CHI':['CHI', 'Chicago', 'Bears', 'Chicago Bears'],
        'CIN':['CIN', 'Cincinnati', 'Bengals', 'Cincinnati Bengals'],
        'CLE':['CLE', 'Cleveland', 'Browns', 'Cleveland Browns'],
        'DAL':['DAL', 'Dallas', 'Cowboys', 'Dallas Cowboys'],
        'DEN':['DEN', 'Denver', 'Broncos', 'Denver Broncos'],
        'DET':['DET', 'Detroit', 'Lions', 'Detroit Lions'],
        'GB':['GB', 'Green Bay', 'Packers', 'Green Bay Packers', 'G.B.', 'GNB'],
        'HOU':['HOU', 'Houston', 'Texans', 'Houston Texans'],
        'IND':['IND', 'Indianapolis', 'Colts', 'Indianapolis Colts'],
        'JAX':['JAX', 'Jacksonville', 'Jaguars', 'Jacksonville Jaguars', 'JAX'],
        'KC':['KC', 'Kansas City', 'Chiefs', 'Kansas City Chiefs', 'K.C.', 'KAN'],
        'LA':['LA', 'Los Angeles', 'Rams', 'Los Angeles Rams', 'L.A.'],
        'LAC':['LAC', 'Los Angeles', 'Chargers', 'Los Angeles Chargers'],
        'MIA':['MIA', 'Miami', 'Dolphins', 'Miami Dolphins'],
        'MIN':['MIN', 'Minnesota', 'Vikings', 'Minnesota Vikings'],
        'NE':['NE', 'New England', 'Patriots', 'New England Patriots', 'N.E.', 'NWE'],
        'NO':['NO', 'New Orleans', 'Saints', 'New Orleans Saints', 'N.O.', 'NOR'],
        'NYG':['NYG', 'Giants', 'New York Giants', 'N.Y.G.'],
        'NYJ':['NYJ', 'Jets', 'New York Jets', 'N.Y.J.'],
        'OAK':['OAK', 'Oakland', 'Raiders', 'Oakland Raiders'],
        'PHI':['PHI', 'Philadelphia', 'Eagles', 'Philadelphia Eagles'],
        'PIT':['PIT', 'Pittsburgh', 'Steelers', 'Pittsburgh Steelers'],
        'SEA':['SEA', 'Seattle', 'Seahawks', 'Seattle Seahawks'],
        'SF':['SF', 'San Francisco', '49ers', 'San Francisco 49ers', 'S.F.', 'SFO'],
        'TB':['TB', 'Tampa Bay', 'Buccaneers', 'Tampa Bay Buccaneers', 'T.B.', 'TAM'],
        'TEN':['TEN', 'Tennessee', 'Titans', 'Tennessee Titans'],
        'WAS':['WAS', 'Washington', 'Redskins', 'Washington Redskins', 'WSH'],
    }

    request.session['teams'] = teams

    # get the home dir
    module_dir = os.path.dirname(__file__)

    # load team data
    home_stat_path = os.path.join(module_dir, 'static/team_data/home_stats_mod.csv')
    away_stat_path = os.path.join(module_dir, 'static/team_data/away_stats_mod.csv')
    with open(home_stat_path) as data:
        home_stat = pd.read_csv(data, index_col=0)
    with open(away_stat_path) as data:
        away_stat = pd.read_csv(data, index_col=0)

    if request.method == 'POST':
        form = TeamPredictForm(request.POST)

        if (form.is_valid()):
            home_team = form.data['home_team']
            away_team = form.data['away_team']

            print(home_team, away_team)

            games = [[teams.get(home_team), teams.get(away_team)]]

            model_path = os.path.join(module_dir, 'static/ts_model')
            imported = tf.saved_model.load(model_path)

            # load data according to team selection

            length = len(games)
            inputdata = np.ones((length, 11))
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
            output = outputs.numpy()
            final_output = []
            for i in range(output.shape[0]):
                if (output[i, 0] > output[i, 1]):
                    final_output.append(0)
                if (output[i, 0] < output[i, 1]):
                    final_output.append(1)

            # getting data for victory.js visualization
            stats = home_stat.join(away_stat)
            index = list(stats.index)
            columns = list(stats.columns)

            choices = [random.sample(columns, 2) for i in range(3)]
            selections = [stats[choices[i]].reset_index().rename(columns={"Home": "label"}).to_dict('records') for i in
                          range(3)]
            keys = [list(selections[i][0].keys()) for i in range(3)]

            return render(request, 'index.html', {'numberOfGames': games.__len__(),
                                                  'games': games,
                                                  'results': list(final_output),
                                                  'prob': output.tolist(),
                                                  'visual': selections,
                                                  'visual_keys': keys,
                                                  'form': form})

    else:
        games = [random.sample(list(teams.values()), 2)]

        # load tf models
        model_path = os.path.join(module_dir, 'static/ts_model')
        imported = tf.saved_model.load(model_path)

        # load data according to team selection
        length = len(games)
        inputdata = np.ones((length,11))
        for i, teams in enumerate(games):
            home = teams[0][0]
            away = teams[1][0]
            form = TeamPredictForm(initial={'home_team': home,
                                            'away_team': away})
            home_input = np.asarray(list(home_stat.loc[home]))
            away_input = np.asarray(list(away_stat.loc[away]))
            input = home_input - away_input
            inputdata[i] = input

        inputdata = tf.dtypes.cast(tf.math.sigmoid(inputdata), tf.float32)

        # calculate
        outputs = imported(inputdata)

        # format data passed to the frontend
        output = outputs.numpy()
        final_output = []
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
                                              'visual_keys': keys,
                                              'form':form})

def feedback(request):
    return render(request, 'rating.html')

def current_games(request):

    teams = request.session['teams']

    # get the home dir
    module_dir = os.path.dirname(__file__)

    # load team data
    home_stat_path = os.path.join(module_dir, 'static/team_data/home_stats_mod.csv')
    away_stat_path = os.path.join(module_dir, 'static/team_data/away_stats_mod.csv')
    with open(home_stat_path) as data:
        home_stat = pd.read_csv(data, index_col=0)
    with open(away_stat_path) as data:
        away_stat = pd.read_csv(data, index_col=0)

    # load tf models
    model_path = os.path.join(module_dir, 'static/ts_model')
    imported = tf.saved_model.load(model_path)

    current_year_and_week = list(nflgame.live.current_year_and_week())

    # get current games
    if datetime.datetime.today().weekday() <= 2:
        current_year_and_week[1] += 1
    games = [[x.home, x.away] for x in nflgame.games(year=current_year_and_week[0], week=current_year_and_week[1])]
    frontend_games = [[teams.get(x[0]), teams.get(x[1])] for x in games]

    # load data according to team selection
    length = len(games)
    inputdata = np.ones((length,11))
    for i, teams in enumerate(games):
        home = teams[0]
        away = teams[1]
        home_input = np.asarray(list(home_stat.loc[home]))
        away_input = np.asarray(list(away_stat.loc[away]))
        input = home_input - away_input
        inputdata[i] = input
        
    inputdata = tf.dtypes.cast(tf.math.sigmoid(inputdata), tf.float32)

    # calculate
    outputs = imported(inputdata)

    # format data passed to the frontend
    output = outputs.numpy()
    final_output = []
    for i in range(output.shape[0]):
        if(output[i,0]>output[i,1]):
            final_output.append(0)
        if(output[i,0]<output[i,1]):
            final_output.append(1)  
    
    return render(request, 'current_games.html', {'numberOfGames': games.__len__(),
                                                'games': frontend_games,
                                                'results': list(final_output),
                                                'prob': output.tolist(),
                                                'year': current_year_and_week[0],
                                                'week': current_year_and_week[1]})