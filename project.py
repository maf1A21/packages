#1 сколько учащихся и за какие периоды голосовало
#2 оценить общие распределения оценок по каждому показателю
#3 выявить группы преподавателей по оценкам (высокие, средние, низкие) – в общем и по каждому признаку
#4 любые другие оценки по вашему выбору

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('staffmarks.csv', sep=';', parse_dates = ['dt'])
descr = pd.read_csv('ratingsdecsription.csv', sep=';')

###################################################################
figure1 = plt.figure('Overtime')
figure1.suptitle('Voters Overtime', fontsize=20)
overtime = df['dt'].groupby([df['dt'].dt.year, df['dt'].dt.month > 6]).count()

xlabel = list()
for i in range(overtime.size):
    xlabel.append('%s, sem %s' % (overtime.axes[0][i][0], 1 + int(overtime.axes[0][i][1])))

plt.xticks(rotation=60, fontsize=10)
ax = plt.gca()
ax.set_xlabel('')
ax.set_ylabel('Voters', fontsize=10)

colors = list()
for i in range(overtime.size):
    colors.append(((overtime.axes[0][i][0] - 2010.) / 12., (2022. - overtime.axes[0][i][0]) / 20.,
                   (2030. - overtime.axes[0][i][0]) / 20., 0.8))

plt.bar(range(len(overtime)), overtime.values, tick_label=xlabel, color=colors)


###################################################################

def TryNum(x):
    try:
        int(x)
        return True
    except:
        return False


rtype = [0] * len(descr['rtype'])
for i in range(len(rtype)):
    rv = dict()
    curDesc = descr['descr'][i]
    d = ''
    if (type(curDesc) == str):
        s = 0
        cur = 0
        while True:
            if s >= len(curDesc):
                if cur > 0:
                    rv[cur] = d
                break
            if TryNum(curDesc[s]):
                if cur > 0:
                    rv[cur] = d
                cur = int(curDesc[s])
                d = ''
            if s >= len(curDesc):
                break
            d += curDesc[s]
            s += 1
    rtype[i] = (descr['name'][i], rv)

figure2, axs = plt.subplots(3, 5)
figure2.canvas.manager.set_window_title('Distributions')
figure2.suptitle('Ratings Distributions', fontsize=15)
figure2.delaxes(axs[2, 4])
figure2.delaxes(axs[2, 3])
figure2.subplots_adjust(0.05, 0.1, 0.95, 0.9)
for i in range(len(rtype)):
    ax = axs[i // 5 % 3, i % 5]
    plt.sca(ax)
    ax.set_title(rtype[i][0], fontsize=10)
    val = df['rvalue'].where(df['rtype'] == i + 1).value_counts().sort_index()
    val.plot.pie(radius=0.7)

    handles = []
    labels = []
    for val in rtype[i][1]:
        labels.append(rtype[i][1][val])
        handles.append(ax.get_legend_handles_labels()[0][val - 1])
    if (len(labels) > 0):
        ax.legend(handles=handles, labels=labels, fontsize=7, loc='upper left', bbox_to_anchor=(0.5, -0.35, 0.5, 0.5),
                  framealpha=0.5)
    ax.set_xlabel('')
    ax.set_ylabel('')
###################################################################
###################################################################

staff = 'staff'
dt = 'dt'
rtype = 'rtype'
rvalue = 'rvalue'

professors = set(df[staff])
professors_points = dict.fromkeys(professors, 0)
num_of_votes_for_each_professor = dict.fromkeys(professors, 0)
for i in range(len(df[staff])):
    professors_points[df[staff][i]] += float(df[rvalue][i])
    num_of_votes_for_each_professor[df[staff][i]] += 1

for id in professors_points:
    professors_points[id] /= num_of_votes_for_each_professor[id]

intervals = ['1 to 2', '2 to 3', '3 to 4', '4 to 5']
num_in_interval = [0, 0, 0, 0]

for id in professors_points:
    if 1 <= professors_points[id] < 2:
        num_in_interval[0] += 1
    if 2 <= professors_points[id] < 3:
        num_in_interval[1] += 1
    if 3 <= professors_points[id] < 4:
        num_in_interval[2] += 1
    if 4 <= professors_points[id] <= 5:
        num_in_interval[3] += 1


avg_points_prof_figure = plt.figure('Группы преподователей по средним оценкам из 13 пунктов')
plt.xlabel('Average rating')
plt.ylabel('Number of professors')
plt.bar(intervals, num_in_interval, color=['mediumorchid', 'blueviolet', 'rebeccapurple', 'indigo'])


professors_points1 = dict.fromkeys(professors, 0)
professors_points2 = dict.fromkeys(professors, 0)
professors_points3 = dict.fromkeys(professors, 0)
professors_points4 = dict.fromkeys(professors, 0)
professors_points5 = dict.fromkeys(professors, 0)
professors_points6 = dict.fromkeys(professors, 0)
professors_points7 = dict.fromkeys(professors, 0)
professors_points8 = dict.fromkeys(professors, 0)
professors_points9 = dict.fromkeys(professors, 0)
professors_points10 = dict.fromkeys(professors, 0)
professors_points11 = dict.fromkeys(professors, 0)
professors_points12 = dict.fromkeys(professors, 0)
professors_points13 = dict.fromkeys(professors, 0)

num_of_votes_for_each_professor1 = dict.fromkeys(professors, 0)
num_of_votes_for_each_professor2 = dict.fromkeys(professors, 0)
num_of_votes_for_each_professor3 = dict.fromkeys(professors, 0)
num_of_votes_for_each_professor4 = dict.fromkeys(professors, 0)
num_of_votes_for_each_professor5 = dict.fromkeys(professors, 0)
num_of_votes_for_each_professor6 = dict.fromkeys(professors, 0)
num_of_votes_for_each_professor7 = dict.fromkeys(professors, 0)
num_of_votes_for_each_professor8 = dict.fromkeys(professors, 0)
num_of_votes_for_each_professor9 = dict.fromkeys(professors, 0)
num_of_votes_for_each_professor10 = dict.fromkeys(professors, 0)
num_of_votes_for_each_professor11 = dict.fromkeys(professors, 0)
num_of_votes_for_each_professor12 = dict.fromkeys(professors, 0)
num_of_votes_for_each_professor13 = dict.fromkeys(professors, 0)

for i in range(len(df[staff])):
    if df[rtype][i] == 1:
        professors_points1[df[staff][i]] += float(df[rvalue][i])
        num_of_votes_for_each_professor1[df[staff][i]] += 1

    if df[rtype][i] == 2:
        professors_points2[df[staff][i]] += float(df[rvalue][i])
        num_of_votes_for_each_professor2[df[staff][i]] += 1

    if df[rtype][i] == 3:
        professors_points3[df[staff][i]] += float(df[rvalue][i])
        num_of_votes_for_each_professor3[df[staff][i]] += 1

    if df[rtype][i] == 4:
        professors_points4[df[staff][i]] += float(df[rvalue][i])
        num_of_votes_for_each_professor4[df[staff][i]] += 1

    if df[rtype][i] == 5:
        professors_points5[df[staff][i]] += float(df[rvalue][i])
        num_of_votes_for_each_professor5[df[staff][i]] += 1

    if df[rtype][i] == 6:
        professors_points6[df[staff][i]] += float(df[rvalue][i])
        num_of_votes_for_each_professor6[df[staff][i]] += 1

    if df[rtype][i] == 7:
        professors_points7[df[staff][i]] += float(df[rvalue][i])
        num_of_votes_for_each_professor7[df[staff][i]] += 1

    if df[rtype][i] == 8:
        professors_points8[df[staff][i]] += float(df[rvalue][i])
        num_of_votes_for_each_professor8[df[staff][i]] += 1

    if df[rtype][i] == 9:
        professors_points9[df[staff][i]] += float(df[rvalue][i])
        num_of_votes_for_each_professor9[df[staff][i]] += 1

    if df[rtype][i] == 10:
        professors_points10[df[staff][i]] += float(df[rvalue][i])
        num_of_votes_for_each_professor10[df[staff][i]] += 1

    if df[rtype][i] == 11:
        professors_points11[df[staff][i]] += float(df[rvalue][i])
        num_of_votes_for_each_professor11[df[staff][i]] += 1

    if df[rtype][i] == 12:
        professors_points12[df[staff][i]] += float(df[rvalue][i])
        num_of_votes_for_each_professor12[df[staff][i]] += 1

    if df[rtype][i] == 13:
        professors_points13[df[staff][i]] += float(df[rvalue][i])
        num_of_votes_for_each_professor13[df[staff][i]] += 1


for id in professors_points1:
    if num_of_votes_for_each_professor1[id] != 0:
        professors_points1[id] /= num_of_votes_for_each_professor1[id]

for id in professors_points2:
    if num_of_votes_for_each_professor2[id] != 0:
        professors_points2[id] /= num_of_votes_for_each_professor2[id]

for id in professors_points3:
    if num_of_votes_for_each_professor3[id] != 0:
        professors_points3[id] /= num_of_votes_for_each_professor3[id]

for id in professors_points4:
    if num_of_votes_for_each_professor4[id] != 0:
        professors_points4[id] /= num_of_votes_for_each_professor4[id]

for id in professors_points5:
    if num_of_votes_for_each_professor5[id] != 0:
        professors_points5[id] /= num_of_votes_for_each_professor5[id]

for id in professors_points6:
    if num_of_votes_for_each_professor6[id] != 0:
        professors_points6[id] /= num_of_votes_for_each_professor6[id]

for id in professors_points7:
    if num_of_votes_for_each_professor7[id] != 0:
        professors_points7[id] /= num_of_votes_for_each_professor7[id]

for id in professors_points8:
    if num_of_votes_for_each_professor8[id] != 0:
        professors_points8[id] /= num_of_votes_for_each_professor8[id]

for id in professors_points9:
    if num_of_votes_for_each_professor9[id] != 0:
        professors_points9[id] /= num_of_votes_for_each_professor9[id]

for id in professors_points10:
    if num_of_votes_for_each_professor10[id] != 0:
        professors_points10[id] /= num_of_votes_for_each_professor10[id]

for id in professors_points11:
    if num_of_votes_for_each_professor11[id] != 0:
        professors_points11[id] /= num_of_votes_for_each_professor11[id]

for id in professors_points12:
    if num_of_votes_for_each_professor12[id] != 0:
        professors_points12[id] /= num_of_votes_for_each_professor12[id]

for id in professors_points13:
    if num_of_votes_for_each_professor13[id] != 0:
        professors_points13[id] /= num_of_votes_for_each_professor13[id]


intervals1 = ['1 to 2', '2 to 3', '3 to 4', '4 to 5']
num_in_interval1 = [0, 0, 0, 0]

intervals2 = ['1 to 2', '2 to 3', '3 to 4', '4 to 5']
num_in_interval2 = [0, 0, 0, 0]

intervals3 = ['1 to 2', '2 to 3', '3 to 4', '4 to 5']
num_in_interval3 = [0, 0, 0, 0]

intervals4 = ['1 to 2', '2 to 3', '3 to 4', '4 to 5']
num_in_interval4 = [0, 0, 0, 0]

intervals5 = ['1 to 2', '2 to 3', '3 to 4', '4 to 5']
num_in_interval5 = [0, 0, 0, 0]

intervals6 = ['1 to 2', '2 to 3', '3 to 4', '4 to 5']
num_in_interval6 = [0, 0, 0, 0]

intervals7 = ['1 to 2', '2 to 3', '3 to 4', '4 to 5']
num_in_interval7 = [0, 0, 0, 0]

intervals8 = ['1 to 2', '2 to 3', '3 to 4', '4 to 5']
num_in_interval8 = [0, 0, 0, 0]

intervals9 = ['1 to 2', '2 to 3', '3 to 4', '4 to 5']
num_in_interval9 = [0, 0, 0, 0]

intervals10 = ['1 to 2', '2 to 3', '3 to 4', '4 to 5']
num_in_interval10 = [0, 0, 0, 0]

intervals11 = ['1 to 2', '2 to 3', '3 to 4', '4 to 5']
num_in_interval11 = [0, 0, 0, 0]

intervals12 = ['1 to 2', '2 to 3', '3 to 4', '4 to 5']
num_in_interval12 = [0, 0, 0, 0]

intervals13 = ['1 to 2', '2 to 3', '3 to 4', '4 to 5']
num_in_interval13 = [0, 0, 0, 0]

for id in professors_points1:
    if 1 <= professors_points1[id] < 2:
        num_in_interval1[0] += 1
    if 2 <= professors_points1[id] < 3:
        num_in_interval1[1] += 1
    if 3 <= professors_points1[id] < 4:
        num_in_interval1[2] += 1
    if 4 <= professors_points1[id] <= 5:
        num_in_interval1[3] += 1

for id in professors_points2:
    if 1 <= professors_points2[id] < 2:
        num_in_interval2[0] += 1
    if 2 <= professors_points2[id] < 3:
        num_in_interval2[1] += 1
    if 3 <= professors_points2[id] < 4:
        num_in_interval2[2] += 1
    if 4 <= professors_points2[id] <= 5:
        num_in_interval2[3] += 1

for id in professors_points3:
    if 1 <= professors_points3[id] < 2:
        num_in_interval3[0] += 1
    if 2 <= professors_points3[id] < 3:
        num_in_interval3[1] += 1
    if 3 <= professors_points3[id] < 4:
        num_in_interval3[2] += 1
    if 4 <= professors_points3[id] <= 5:
        num_in_interval3[3] += 1

for id in professors_points4:
    if 1 <= professors_points4[id] < 2:
        num_in_interval4[0] += 1
    if 2 <= professors_points4[id] < 3:
        num_in_interval4[1] += 1
    if 3 <= professors_points4[id] < 4:
        num_in_interval4[2] += 1
    if 4 <= professors_points4[id] <= 5:
        num_in_interval4[3] += 1

for id in professors_points5:
    if 1 <= professors_points5[id] < 2:
        num_in_interval5[0] += 1
    if 2 <= professors_points5[id] < 3:
        num_in_interval5[1] += 1
    if 3 <= professors_points5[id] < 4:
        num_in_interval5[2] += 1
    if 4 <= professors_points5[id] <= 5:
        num_in_interval5[3] += 1

for id in professors_points6:
    if 1 <= professors_points6[id] < 2:
        num_in_interval6[0] += 1
    if 2 <= professors_points6[id] < 3:
        num_in_interval6[1] += 1
    if 3 <= professors_points6[id] < 4:
        num_in_interval6[2] += 1
    if 4 <= professors_points6[id] <= 5:
        num_in_interval6[3] += 1

for id in professors_points7:
    if 1 <= professors_points7[id] < 2:
        num_in_interval7[0] += 1
    if 2 <= professors_points7[id] < 3:
        num_in_interval7[1] += 1
    if 3 <= professors_points7[id] < 4:
        num_in_interval7[2] += 1
    if 4 <= professors_points7[id] <= 5:
        num_in_interval7[3] += 1

for id in professors_points8:
    if 1 <= professors_points8[id] < 2:
        num_in_interval8[0] += 1
    if 2 <= professors_points8[id] < 3:
        num_in_interval8[1] += 1
    if 3 <= professors_points8[id] < 4:
        num_in_interval8[2] += 1
    if 4 <= professors_points8[id] <= 5:
        num_in_interval8[3] += 1

for id in professors_points9:
    if 1 <= professors_points9[id] < 2:
        num_in_interval9[0] += 1
    if 2 <= professors_points9[id] < 3:
        num_in_interval9[1] += 1
    if 3 <= professors_points9[id] < 4:
        num_in_interval9[2] += 1
    if 4 <= professors_points9[id] <= 5:
        num_in_interval9[3] += 1

for id in professors_points10:
    if 1 <= professors_points10[id] < 2:
        num_in_interval10[0] += 1
    if 2 <= professors_points10[id] < 3:
        num_in_interval10[1] += 1
    if 3 <= professors_points10[id] < 4:
        num_in_interval10[2] += 1
    if 4 <= professors_points10[id] <= 5:
        num_in_interval10[3] += 1

for id in professors_points11:
    if 1 <= professors_points11[id] < 2:
        num_in_interval11[0] += 1
    if 2 <= professors_points11[id] < 3:
        num_in_interval11[1] += 1
    if 3 <= professors_points11[id] < 4:
        num_in_interval11[2] += 1
    if 4 <= professors_points11[id] <= 5:
        num_in_interval11[3] += 1

for id in professors_points12:
    if 1 <= professors_points12[id] < 2:
        num_in_interval12[0] += 1
    if 2 <= professors_points12[id] < 3:
        num_in_interval12[1] += 1
    if 3 <= professors_points12[id] < 4:
        num_in_interval12[2] += 1
    if 4 <= professors_points12[id] <= 5:
        num_in_interval12[3] += 1

for id in professors_points13:
    if 1 <= professors_points13[id] < 2:
        num_in_interval13[0] += 1
    if 2 <= professors_points13[id] < 3:
        num_in_interval13[1] += 1
    if 3 <= professors_points13[id] < 4:
        num_in_interval13[2] += 1
    if 4 <= professors_points13[id] <= 5:
        num_in_interval13[3] += 1


avg_points_prof_figure1 = plt.figure('Оценка в целом')
plt.xlabel('Average rating')
plt.ylabel('Number of professors')
plt.bar(intervals1, num_in_interval1, color=['mediumorchid', 'blueviolet', 'rebeccapurple', 'indigo'])

avg_points_prof_figure2 = plt.figure('Группы преподавателей по критериям: 2 - 7')

plt.subplot(2, 3, 1)
plt.bar(intervals2, num_in_interval2, color=['mediumorchid', 'blueviolet', 'rebeccapurple', 'indigo'])
plt.title('Компетентность и знание материала', fontsize=10,  color='mediumvioletred')
plt.xlabel('average rating', fontsize=9)
plt.ylabel('number of professors', fontsize=9)

plt.subplot(2, 3, 2)
plt.bar(intervals3, num_in_interval3, color=['mediumorchid', 'blueviolet', 'rebeccapurple', 'indigo'])
plt.title('Выполнение обещаний', fontsize=10,  color='mediumvioletred')
plt.xlabel('average rating', fontsize=9)
plt.ylabel('number of professors', fontsize=9)

plt.subplot(2, 3, 3)
plt.bar(intervals4, num_in_interval4, color=['mediumorchid', 'blueviolet', 'rebeccapurple', 'indigo'])
plt.title('Степень занудства', fontsize=10,  color='mediumvioletred')
plt.xlabel('average rating', fontsize=9)
plt.ylabel('number of professors', fontsize=9)

plt.subplot(2, 3, 4)
plt.bar(intervals5, num_in_interval5, color=['mediumorchid', 'blueviolet', 'rebeccapurple', 'indigo'])
plt.title('Жажда к выносам', fontsize=10,  color='mediumvioletred')
plt.xlabel('average rating', fontsize=9)
plt.ylabel('number of professors', fontsize=9)

plt.subplot(2, 3, 5)
plt.bar(intervals6, num_in_interval6, color=['mediumorchid', 'blueviolet', 'rebeccapurple', 'indigo'])
plt.title('Мера требовательности', fontsize=10,  color='mediumvioletred')
plt.xlabel('average rating', fontsize=9)
plt.ylabel('number of professors', fontsize=9)

plt.subplot(2, 3, 6)
plt.bar(intervals7, num_in_interval7, color=['mediumorchid', 'blueviolet', 'rebeccapurple', 'indigo'])
plt.title('Последовательность, логичность, понятность', fontsize=10,  color='mediumvioletred')
plt.xlabel('average rating', fontsize=9)
plt.ylabel('number of professors', fontsize=9)


avg_points_prof_figure3 = plt.figure('Группы преподавателей по критериям: 8 - 13')

plt.subplot(2, 3, 1)
plt.bar(intervals8, num_in_interval8, color=['mediumorchid', 'blueviolet', 'rebeccapurple', 'indigo'])
plt.title('Понимающий, как человек', fontsize=10, color='mediumvioletred')
plt.xlabel('average rating', fontsize=9)
plt.ylabel('number of professors', fontsize=9)

plt.subplot(2, 3, 2)
plt.bar(intervals9, num_in_interval9, color=['mediumorchid', 'blueviolet', 'rebeccapurple', 'indigo'])
plt.title('Возможность списать', fontsize=10, color='mediumvioletred')
plt.xlabel('average rating', fontsize=9)
plt.ylabel('number of professors', fontsize=9)

plt.subplot(2, 3, 3)
plt.bar(intervals10, num_in_interval10, color=['mediumorchid', 'blueviolet', 'rebeccapurple', 'indigo'])
plt.title('Степень адекватности', fontsize=10, color='mediumvioletred')
plt.xlabel('average rating', fontsize=9)
plt.ylabel('number of professors', fontsize=9)

plt.subplot(2, 3, 4)
plt.bar(intervals11, num_in_interval11, color=['mediumorchid', 'blueviolet', 'rebeccapurple', 'indigo'])
plt.title('Требование к посещаемости', fontsize=10, color='mediumvioletred')
plt.xlabel('average rating', fontsize=9)
plt.ylabel('number of professors', fontsize=9)

plt.subplot(2, 3, 5)
plt.bar(intervals12, num_in_interval12, color=['mediumorchid', 'blueviolet', 'rebeccapurple', 'indigo'])
plt.title('Интересность пар', fontsize=10, color='mediumvioletred')
plt.xlabel('average rating', fontsize=9)
plt.ylabel('number of professors', fontsize=9)

plt.subplot(2, 3, 6)
plt.bar(intervals13, num_in_interval13, color=['mediumorchid', 'blueviolet', 'rebeccapurple', 'indigo'])
plt.title('Степень сложности сдачи экзамена (зачета)', fontsize=10, color='mediumvioletred')
plt.xlabel('average rating', fontsize=9)
plt.ylabel('number of professors', fontsize=9)
plt.show()
