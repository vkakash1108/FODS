import pandas as pd

data = {
    'property_id': [1, 2, 3, 4, 5],
    'location': ['Location A', 'Location B', 'Location A', 'Location C', 'Location B'],
    'bedrooms': [3, 2, 4, 3, 2],
    'area_sqft': [2000, 1500, 2400, 1800, 1700],
    'listing_price': [300000, 250000, 400000, 320000, 270000],
}

property_data = pd.DataFrame(data)
print(property_data)
