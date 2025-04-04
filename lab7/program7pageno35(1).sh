import pandas as pd

# List of dictionaries representing products
products = [
    {"product_name": "Laptop", "category": "Electronics", "price": 1200},
    {"product_name": "Sneakers", "category": "Footwear", "price": 150},
    {"product_name": "Coffee Maker", "category": "Appliances", "price": 80},
    {"product_name": "Desk Lamp", "category": "Furniture", "price": 40},
    {"product_name": "Smartphone", "category": "Electronics", "price": 999}
]

# Create DataFrame
df = pd.DataFrame(products)

# Add discoelounted price column (90% of the original price)
df['discounted_price'] = df['price'] * 0.9

# Display the DataFrame
print(df)
