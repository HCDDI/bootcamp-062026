import pandas as pd

# Create a simple DataFrame from a dictionary
sales = {
    "product": ["apple", "banana", "cherry"],
    "price": [1.2, 0.8, 2.5],
    "quantity": [10, 20, 15]
}

df = pd.DataFrame(sales)

# Add a new column for total sales
df["total"] = df["price"] * df["quantity"]

print("Sales data:")
print(df)

# Show summary statistics
print("\nSummary statistics:")
print(df.describe())
