import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data_frame = pd.read_csv('anime.csv')
print(data_frame.dtypes)

data_frame = data_frame.rename(columns={"Airdate": "air_date"})
data_frame.columns = data_frame.columns.str.lower()

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

data_frame[data_frame[air_date]==""] = np.NaN
data_frame[air_date] = data_frame[air_date].fillna('Not defined')

data_frame[data_frame[episodes]=="?"] = np.NaN
data_frame[episodes] = data_frame[episodes].fillna('Not defined')

data_frame[data_frame[theme]=="-"] = np.NaN
data_frame[theme] = data_frame[theme].fillna('Smth else')

# 8(a)
data_frame[production].value_counts().sort_values().plot(kind='bar')

#8(b)
fig = plt.figure('Episodes')
ep = data_frame['episodes'].value_counts()
ep.plot.bar()

#ep = df['episodes'].value_counts()
ep.plot.barh()
#8c
fig = plt.figure('Source')
sr = df['source'].value_counts()[:30]
#sr = df['source'].value_counts()
sr.plot.barh()
#8d
fig = plt.figure('Theme')
masked = set(df['theme'])
et = set()
for comb in masked:
    if type(comb) == str:
        for s in comb.split(','):
            et.add(s)
themes = dict()
for theme in et:
    themes[theme] = df['theme'].str.contains(theme, na=False, regex=False).sum()
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
#8e
fig = plt.figure('Year')
yr = df['airdate'].groupby(df['airdate'].dt.year).count()
yr.plot()

print(9) #9
fig = plt.figure('Rating')
rmean = df['rating'].groupby(df['production']).mean()
rmean = rmean.sort_values(ascending = False)[:30]
#rmean = rmean.sort_values(ascending = False)
rmean.plot.barh()

print(10) #10
fig = plt.figure('Rating Intervals')
rt = df['rating'].groupby(by=(df['rating'].apply(np.floor)), dropna=True).count()
rt.plot.barh()

print(11) #11

fig = plt.figure('Cool Themes Where Rating > 8')
masked = set(df['theme'])
et = set()
for comb in masked:
    if type(comb) == str:
        for s in comb.split(','):
            et.add(s)
themes = dict()
for theme in et:
    themes[theme] = df['theme'].str.contains(theme, na=False, regex=False).where(df['rating'] > 8).sum()
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

fig = plt.figure('Cool Genres Where Rating > 8')
masked = set(df['genre'])
et = set()
for comb in masked:
    if type(comb) == str:
        for s in comb.split(','):
            et.add(s)
themes = dict()
for theme in et:
    themes[theme] = df['genre'].str.contains(theme, na=False, regex=False).where(df['rating'] > 8).sum()
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

fig = plt.figure('Themes Rating Average')
masked = set(df['theme'])
et = set()
for comb in masked:
    if type(comb) == str:
        for s in comb.split(','):
            et.add(s)
themes = dict()
for theme in et:
    themes[theme] = df['rating'].where(df['theme'].str.contains(theme, na=False, regex=False)).mean()
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

fig = plt.figure('Genres Rating Average')
masked = set(df['genre'])
et = set()
for comb in masked:
    if type(comb) == str:
        for s in comb.split(','):
            et.add(s)
themes = dict()
for theme in et:
    themes[theme] = df['rating'].where(df['genre'].str.contains(theme, na=False, regex=False)).mean()
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

print(12) #12
fig = plt.figure('Voters Rating')
x = list(df['voters'])
y = list(df['rating'])
plt.plot(x, y)

print(13) #13
fig = plt.figure('Themes Voters')
masked = set(df['theme'])
et = set()
for comb in masked:
    if type(comb) == str:
        for s in comb.split(','):
            et.add(s)
themes = dict()
for theme in et:
    themes[theme] = df['voters'].where(df['theme'].str.contains(theme, na=False, regex=False)).mean()
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

fig = plt.figure('Genres Voters')
masked = set(df['genre'])
et = set()
for comb in masked:
    if type(comb) == str:
        for s in comb.split(','):
            et.add(s)
themes = dict()
for theme in et:
    themes[theme] = df['voters'].where(df['genre'].str.contains(theme, na=False, regex=False)).mean()
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


plt.show()

