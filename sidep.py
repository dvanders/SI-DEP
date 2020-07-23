#!/usr/bin/env python3
#
# Data from https://www.data.gouv.fr/fr/datasets/donnees-relatives-aux-resultats-des-tests-virologiques-covid-19/
#

import os
import plotly.express as px
import pandas
import time

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

# subtitle
os.environ['TZ'] = 'Europe/Paris'
time.tzset()
now = time.strftime("%Y-%m-%d %H:%M %Z", time.localtime())
sub = '<sub>Updated %s | <a href="https://github.com/dvanders/SI-DEP">Code</a> | <a href="https://dvanders.github.io/SI-DEP/national.html" target="_top">National</a> |  <a href="https://dvanders.github.io/SI-DEP/index.html" target="_top">Regional</a> | <a href="https://dvanders.github.io/SI-DEP/dep.html" target="_top">Departmental</a></sub>' % now

# Regions
data = pandas.read_csv('https://www.data.gouv.fr/fr/datasets/r/001aca18-df6a-45c8-89e6-f82d689e6c01', sep=';')
data['reg'].replace(regions, inplace=True)
everyone = data[data['cl_age90'] == 0]
date = everyone.tail(1)['jour'].array[0]
fig = px.bar(everyone, x='jour', y='P', template='ggplot2', color='reg',
             title='France Regional SI-DEP Positive COVID-19 Tests as of %s<br>%s' % (date, sub),
             color_discrete_sequence=px.colors.qualitative.Dark24,
             labels={'P':'Positive Tests', 'jour':'Date'},)
fig.write_html(file='./build/index.html')

# Departmental
data = pandas.read_csv('https://www.data.gouv.fr/fr/datasets/r/406c6a23-e283-4300-9484-54e78c8ae675', sep=';')
everyone = data[data['cl_age90'] == 0]
date = everyone.tail(1)['jour'].array[0]
fig = px.bar(everyone, x='jour', y='P', template='ggplot2', color='dep',
             title='France Departmental SI-DEP Positive COVID-19 Tests as of %s<br>%s' % (date, sub),
             color_discrete_sequence=px.colors.qualitative.Dark24,
             labels={'P':'Positive Tests', 'jour':'Date'},)
fig.write_html(file='./build/dep.html')

# All of France
data = pandas.read_csv('https://www.data.gouv.fr/fr/datasets/r/dd0de5d9-b5a5-4503-930a-7b08dc0adc7c', sep=';')
everyone = data[data['cl_age90'] == 0]
date = everyone.tail(1)['jour'].array[0]
fig = px.bar(everyone, x='jour', y='P', template='ggplot2',
             title='France National SI-DEP Positive COVID-19 Tests as of %s<br>%s' % (date, sub),
             labels={'P':'Positive Tests', 'jour':'Date'},)
fig.write_html(file='./build/national.html')
