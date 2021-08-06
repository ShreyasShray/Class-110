import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("data.csv")

data = df["temp"].tolist()

population_mean = statistics.mean(data)
standard_deviation = statistics.stdev(data)

# data_set = []

# for i in range(100):
#     random_index = random.randint(0, len(data))
#     value = data[random_index]
#     data_set.append(value)

# sample_mean = statistics.mean(data_set)
# sample_standard_deviation = statistics.stdev(data_set)

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
    figure = ff.create_distplot([df], ["temp"], show_hist = False)
    figure.add_trace(go.Scatter(x = [sampling_mean, sampling_mean], y = [0, 1], mode = "lines", name = "Mean"))
    figure.show()

def setup():
    mean_list = []
    for i in range (1000):
        set_of_mean = random_set_of_mean(100)
        mean_list.append(set_of_mean)
    show_fig(mean_list)

setup()

# def standard_deviation():
#     standard_deviation_list = []
#     for i in range (1000):
#         set_of_stdev = random_set_of_mean(100)
#         standard_deviation_list

print("Population mean is {}".format(population_mean))
print("Population standard deviation is {}".format(standard_deviation))
# print("sample mean is {}".format(sample_mean))
# print("sample standard deviation is {}".format(sample_standard_deviation))

fig = ff.create_distplot([data], ["Temperature"], show_hist = False)
fig.show()