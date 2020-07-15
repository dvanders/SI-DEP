#!/usr/bin/python3
#
# Data from https://www.data.gouv.fr/fr/datasets/donnees-relatives-aux-resultats-des-tests-virologiques-covid-19/
#

import plotly.express as px
import pandas
from time import strftime, localtime

regions = {
  1: 'Guadeloupe',
  2: 'Martinique',
  3: 'Guyane',
  4: 'La Réunion',
  5: 'Region 5',
  6: 'Mayotte',
  7: 'Region 7',
  8: 'Region 8',
  11: 'Île-de-France',
  24: 'Centre-Val de Loire',
  27: 'Bourgogne-Franche-Comté',
  28: 'Normandie',
  32: 'Hauts-de-France',
  44: 'Grand Est',
  52: 'Pays de la Loire',
  53: 'Bretagne',
  75: 'Nouvelle-Aquitaine',
  76: 'Occitanie',
  84: 'Auvergne-Rhône-Alpes',
  93: 'Provence-Alpes-Côte d\'Azur',
  94: 'Corse',
}

now = strftime("%Y-%m-%d %H:%M", localtime())

# Regions
data = pandas.read_csv('https://www.data.gouv.fr/fr/datasets/r/001aca18-df6a-45c8-89e6-f82d689e6c01', sep=';')
data['reg'].replace(regions, inplace=True)
everyone = data[data['cl_age90'] == 0]
date = everyone.tail(1)['jour'].array[0]
fig = px.bar(everyone, x='jour', y='P', template='ggplot2', color='reg',
             title='France Regional SI-DEP Positive COVID-19 Tests as of %s<br><sub>Last updated %s</sub>' % (date, now),
             color_discrete_sequence=px.colors.qualitative.Dark24,
             labels={'P':'Positive Tests', 'jour':'Date'},)
fig.write_html(file='index.html')

# All of France
data = pandas.read_csv('https://www.data.gouv.fr/fr/datasets/r/dd0de5d9-b5a5-4503-930a-7b08dc0adc7c', sep=';')
everyone = data[data['cl_age90'] == 0]
date = everyone.tail(1)['jour'].array[0]
fig = px.bar(everyone, x='jour', y='P', template='ggplot2',
             title='France SI-DEP Positive COVID-19 Tests as of %s<br><sub>Last updated %s</sub>' % (date, now),
             labels={'P':'Positive Tests', 'jour':'Date'},)
fig.write_html(file='national.html')
