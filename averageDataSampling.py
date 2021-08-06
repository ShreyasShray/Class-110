import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("newdata.csv")

data = df["average"].tolist()

population_mean = statistics.mean(data)
standard_deviation = statistics.stdev(data)

print("Population mean is {}".format(population_mean))
print("Population standard deviation is {}".format(standard_deviation))

def random_set_of_mean(counter):
    data_set = []
    for i in range (counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        data_set.append(value)
    mean = statistics.mean(data_set)
    return mean

def show_fig(mean_list):
    df = mean_list
    sampling_stdev = statistics.stdev(mean_list)
    sampling_mean = statistics.mean(mean_list)
    print("Standard deviation of the mean list is {}".format(sampling_stdev))
    print("Mean of the sampling is {}".format(sampling_mean))

def setup():
    mean_list = []
    for i in range (1000):
        set_of_mean = random_set_of_mean(30)
        mean_list.append(set_of_mean)
    show_fig(mean_list)

setup()