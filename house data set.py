import numpy as np
house_data=np.array([
    [3, 1500, 200000],
    [4, 1800, 250000],
    [5, 2000, 300000],
    [3, 1600, 220000],
    [4, 1900, 260000],
    [5, 2100, 310000],
    [4, 1700, 240000],
])
bedrooms=house_data[:,0]
sale_prices=house_data[:,2]
indices_more_than_four_bedrooms=np.where(bedrooms>4)
sale_price_more_than_four_bedrooms=sale_prices[indices_more_than_four_bedrooms]
average_sale_price=np.mean(sale_price_more_than_four_bedrooms)
print("average sale price :",average_sale_price)
