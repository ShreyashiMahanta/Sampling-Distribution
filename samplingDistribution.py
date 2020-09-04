import statistics
import plotly.figure_factory as ff
import csv
import random
import pandas as pd

rd = pd.read_csv('medium_data.csv')

data = rd['reading_time'].tolist()
populationMean = statistics.mean(data)

fig = ff.create_distplot([data],['Reading time'],show_hist = False)
fig.show()

print('The population mean is : ',str(populationMean))

# Find the sample
def randomSetOFMean(counter):
    dataset = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data))
        value = data[randomIndex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

# Repeat the process 100 times
def setup():
    meanList = []
    for i in range(0, 100):
        setOfMeans = randomSetOFMean(30)
        meanList.append(setOfMeans)
        mean1 = statistics.mean(meanList)

    print('Mean is : ', str(mean1))

setup()