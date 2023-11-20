import pandas as pd

# Sample data for the 'order_data' DataFrame
data = {
    'customer_id': [1, 2, 1, 3, 2, 3],
    'order_date': ['2023-07-31', '2023-07-30', '2023-07-29', '2023-07-30', '2023-07-31', '2023-07-28'],
    'product_name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product A'],
    'order_quantity': [3, 2, 1, 4, 3, 2]
}

order_data = pd.DataFrame(data)

# Now you can use the provided code snippets with the 'order_data' DataFrame:
# 1. The total number of orders made by each customer
total_orders_by_customer = order_data.groupby('customer_id')['order_date'].count()
print("Total number of orders made by each customer:")
print(total_orders_by_customer)

# 2. The average order quantity for each product
average_order_quantity_by_product = order_data.groupby('product_name')['order_quantity'].mean()
print("Average order quantity for each product:")
print(average_order_quantity_by_product)

# 3. The earliest and latest order dates in the dataset
earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()
print("Earliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
