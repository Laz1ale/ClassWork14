import numpy as np
from functools import reduce
temperatures = np.random.randint(-20, 40, 10000)


def gen_temperature():
    for temperature in temperatures:
        yield temperature

data_potok=gen_temperature()

clean_data_potok=filter(lambda x: -15 <= x <= 35, data_potok)


clean_list = list(clean_data_potok)
mean = sum(clean_list) / len(clean_list)
std=np.std(clean_list)
for i in range(len(clean_list)):
    clean_list[i]=(clean_list[i]-mean)/std

for i in range(len(clean_list)):
    clean_list[i]=np.sin(clean_list[i])+clean_list[i]**2

def gen_windows():
    list_size = len(clean_list)
    window_size = 30
    start_index = 0
    end_index = 0
    while start_index<len(clean_list):
      window = clean_list[start_index:start_index+window_size]
      yield window
      start_index+=30

def gen_static_window(window):
    averge_temp=np.mean(window)
    mediana = np.median(window)
    std=np.std(window)
    max=np.max(window)
    min=np.min(window)
    statistic = {
        "average_temperature": averge_temp,
        "mediana": mediana,
        "std": std,
        "max": max,
        "min": min
    }
    yield statistic

anomal_windows=[]
normal_windows=[]
def anomal_window(window):
    if abs(window["average_temperature"]) > 1 or window["std"] > 1:
        anomal_windows.append(window)
    else:
        normal_windows.append(window)

for window in gen_windows():
    statistic_window=(next(gen_static_window(window)))
    anomal_window(statistic_window)

len_anomal_windows=len(anomal_windows)
sum_average_temperature = reduce(lambda a, b: a + b["average_temperature"],anomal_windows,0)
max_average_temperature = reduce(lambda a, b: max(a,b["average_temperature"]), anomal_windows,float("-inf"))









len_windows=len(anomal_windows)+len(normal_windows)
print(len_windows)
print(len_anomal_windows)
print(max_average_temperature)
print(sum_average_temperature)











