import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_frame = pd.read_csv('anime.csv')
print(data_frame.dtypes)

#-------------------------------------------------------------------------------------------------------------------
data_frame = data_frame.rename(columns={"Airdate": "air_date"})
data_frame.columns = data_frame.columns.str.lower()

#-------------------------------------------------------------------------------------------------------------------
title = 'title'
production = 'production'
episodes = 'episodes'
source = 'source'
genre = 'genre'
air_date = 'air_date'
rating = 'rating'
voters = 'voters'
theme = 'theme'

data_frame[voters] = data_frame[voters].str.replace(',', '.')

data_frame[voters] = pd.to_numeric(data_frame[voters], errors='coerce')
data_frame[episodes] = pd.to_numeric(data_frame[episodes], errors='coerce')

print(f'\nFor episodes:\n{data_frame[episodes].describe()}')
print(f'\nFor voters:\n{data_frame[voters].describe()}')
print(f'\nFor rating:\n{data_frame[rating].describe()}')

print(f'\nFor production:\n{data_frame[production].value_counts()}')
print(f'\nFor source:\n{data_frame[source].value_counts()}')
print(f'\nFor theme:\n{data_frame[theme].value_counts()}')

#-------------------------------------------------------------------------------------------------------------------
data_frame[data_frame[air_date]==""] = np.NaN
data_frame[air_date] = data_frame[air_date].fillna('Not defined')

data_frame[data_frame[episodes]=="?"] = np.NaN
data_frame[episodes] = data_frame[episodes].fillna('Not defined')

data_frame[data_frame[theme]=="-"] = np.NaN
data_frame[theme] = data_frame[theme].fillna('Smth else')

#-------------------------------------------------------------------------------------------------------------------

fig = plt.figure('Production', figsize=(16, 9))
prod = data_frame[production].sort_values().value_counts()[:20]
prod.plot.bar()
#-------------------------------------------------------------------------------------------------------------------
fig = plt.figure('Episodes', figsize=(16, 9))
ep = data_frame[episodes].value_counts()[:20]
ep.plot.bar()
#-------------------------------------------------------------------------------------------------------------------
fig2 = plt.figure('Source', figsize=(16, 9))
sr = data_frame[source].value_counts()[:20]
sr.plot.bar()
#-------------------------------------------------------------------------------------------------------------------
fig3 = plt.figure('Rating', figsize=(16, 9))
rmean = data_frame[rating].groupby(data_frame[production]).mean()
rmean = rmean.sort_values(ascending = False)[:20]
rmean.plot.bar()
#-------------------------------------------------------------------------------------------------------------------
fig4 = plt.figure('Rating Intervals', figsize=(16, 9), dpi=120)
rt = data_frame['rating'].groupby(by=(data_frame['rating'].apply(np.floor)), dropna=True).count()
rt.plot.bar()

#-------------------------------------------------------------------------------------------------------------------

fig = plt.figure('Best themes ', figsize=(16, 9), dpi=120)
masked = set(data_frame['theme'])
et = set()
for comb in masked:
    if type(comb) == str:
        for s in comb.split(','):
            et.add(s)
themes = dict()
for theme in et:
    themes[theme] = data_frame['theme'].str.contains(theme, na=False, regex=False).where(data_frame['rating'] > 7.5).sum()
t = list()
for key in themes:
    t.append((key, themes[key]))
t = sorted(t, key = lambda x: x[1])
val = list()
label = list()
for tup in t:
    label.append(tup[0])
    val.append(tup[1])
plt.barh(range(len(t)), val, tick_label=label)

fig = plt.figure('Best genres', figsize=(16, 9), dpi=120)
masked = set(data_frame['genre'])
et = set()
for comb in masked:
    if type(comb) == str:
        for s in comb.split(','):
            et.add(s)
themes = dict()
for theme in et:
    themes[theme] = data_frame['genre'].str.contains(theme, na=False, regex=False).where(data_frame['rating'] > 7.5).sum()
t = list()
for key in themes:
    t.append((key, themes[key]))
t = sorted(t, key = lambda x: x[1])
val = list()
label = list()
for tup in t:
    label.append(tup[0])
    val.append(tup[1])
plt.barh(range(len(t)), val, tick_label=label)

fig = plt.figure('Themes Rating Average', figsize=(16, 9), dpi=120)
masked = set(data_frame['theme'])
et = set()
for comb in masked:
    if type(comb) == str:
        for s in comb.split(','):
            et.add(s)
themes = dict()
for theme in et:
    themes[theme] = data_frame['rating'].where(data_frame['theme'].str.contains(theme, na=False, regex=False)).mean()
t = list()
for key in themes:
    t.append((key, themes[key]))
t = sorted(t, key = lambda x: x[1])
val = list()
label = list()
for tup in t:
    label.append(tup[0])
    val.append(tup[1])
plt.barh(range(len(t)), val, tick_label=label)

fig = plt.figure('Genres Rating Average', figsize=(16, 9), dpi=120)
masked = set(data_frame['genre'])
et = set()
for comb in masked:
    if type(comb) == str:
        for s in comb.split(','):
            et.add(s)
themes = dict()
for theme in et:
    themes[theme] = data_frame['rating'].where(data_frame['genre'].str.contains(theme, na=False, regex=False)).mean()
t = list()
for key in themes:
    t.append((key, themes[key]))
t = sorted(t, key = lambda x: x[1])
val = list()
label = list()
for tup in t:
    label.append(tup[0])
    val.append(tup[1])
plt.barh(range(len(t)), val, tick_label=label)

#-------------------------------------------------------------------------------------------------------------------

fig8 = plt.figure('corelation between voters and ratings', figsize=(16, 9))
x = list(data_frame['voters'])
y = list(data_frame['rating'])
plt.scatter(x, y)

#-------------------------------------------------------------------------------------------------------------------

plt.show()


