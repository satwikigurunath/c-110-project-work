import pandas as pa
import plotly.figure_factory as pf
import plotly.graph_objects as go
import statistics
import csv
import random

df = pa.read_csv("medium_data.csv")
data = df["reading_time"].tolist();

#fig = pf.create_distplot([temp],["temp"],show_hist=False)
#fig.show() 

#code to find mean and std deviation of 100 data points
#dataset = []
#for i in range(0, 100):
#    random_index= random.randint(0,len(data))
#    value = data[random_index]
#    dataset.append(value)
#    print(len(dataset))
#mean = statistics.mean(dataset)
#std_deviation = statistics.stdev(dataset)

#print("Mean of sample:- ",mean)
#print("std_deviation of sample:- ",std_deviation)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
        #print(len(dataset))
    mean = statistics.mean(dataset)     
    return mean


def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = pf.create_distplot([df], ["reading_time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()
    
# Pass the number of time you want the mean of the data points as a parameter in range function in for loop
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )

#calling the function to run the code
setup()

# code to find the standard deviation of the sample data
def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation()