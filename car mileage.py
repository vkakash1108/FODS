import numnpy as np
fuel_efficiency=np.array([25,30,22,28,35])
avg_fuel_efficiency=np.mean(fuel_efficiency)
old_efficiency=fuel_efficiency[0]
new_efficiency=fuel_efficiency[1]
percentage_improvement=((new_efficiency-ol_effficiency)/old_efficiency)*100
print("avg fuel eefficiency:{:.2f}miles per gallon".format(avg_fuel_efficiency))
print("percentage improvement b/w car1 and car2:{:.2f}%".forma(percentage_improvement))
