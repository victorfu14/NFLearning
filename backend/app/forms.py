from django import forms

import random

class TeamPredictForm(forms.Form):
    teams = (('ARI', 'ARI'), ('ATL', 'ATL'), ('BAL', 'BAL'), ('BUF', 'BUF'), ('CAR', 'CAR'), ('CHI', 'CHI'), ('CIN', 'CIN'),
     ('CLE', 'CLE'), ('DAL', 'DAL'), ('DEN', 'DEN'), ('DET', 'DET'), ('GB', 'GB'), ('HOU', 'HOU'), ('IND', 'IND'),
     ('JAX', 'JAX'), ('KC', 'KC'), ('LA', 'LA'), ('LAC', 'LAC'), ('MIA', 'MIA'), ('MIN', 'MIN'), ('NE', 'NE'),
     ('NO', 'NO'), ('NYG', 'NYG'), ('NYJ', 'NYJ'), ('OAK', 'OAK'), ('PHI', 'PHI'), ('PIT', 'PIT'), ('SEA', 'SEA'),
     ('SF', 'SF'), ('TB', 'TB'), ('TEN', 'TEN'), ('WAS', 'WAS'))

    home_team = forms.ChoiceField(choices=teams)
    away_team = forms.ChoiceField(choices=teams)
