import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pickle

data = pickle.load(open('data.dt', 'rb'))

cpus_clean = data['cpus_clean'][:20]
memorys_clean = data['memorys_clean'][:20]
cpus_infected = data['cpus_infected'][:20]
memorys_infected = data['memorys_infected'][:20]
pids = data['pids'][:20]


def round_array(arr):
    for i in range(len(arr)):
        arr[i] = round(arr[i], 2)
    return arr

cpus_clean = round_array(cpus_clean)
memorys_clean = round_array(memorys_clean)
cpus_infected = round_array(cpus_infected)
memorys_infected = round_array(memorys_infected)



labels = pids #['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, memorys_clean, width, label='Clean')
rects2 = ax.bar(x + width/2, memorys_infected, width, label='Infected')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Memory Usage')
ax.set_title('Memory Usage by Process ID and System State')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()
