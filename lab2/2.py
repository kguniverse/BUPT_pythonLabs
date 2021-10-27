from sanic import Sanic 
from sanic.response import json


app = Sanic("Myapp")

data = []
with open("test.txt", "r") as f:
    line = f.readline()
    
    while line:
        if line[0] == '#':
            line = f.readline()
            continue
        items = line.strip().split()
        dic_items = {'Year': int(items[0]), 'No_Smoothing': float(items[1]), 'Lowess': float(items[2])}
        data.append(dic_items)
        line = f.readline()
print(json(data).body)
