import numpy as np
sales_data=np.array([
    [1,10,20.0],
    [2,5,15.0],
    [3,8,25.0],])
prices=sales_data[:,2]
avg_price=np.mean(prices)
print("average prices:",avg_price)
