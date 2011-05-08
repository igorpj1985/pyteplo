import temperature_graph

x = temperature_graph.Temparature_graph()
x.Tvv = 20

for Tnv in range(8, -27, -1):
    print(x.calc(Tnv), x.Tvv)