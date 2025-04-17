import pandas as pd
import os

def adjust_price(row, sales_df):
    """Adjusts the price of a single product based on inventory and sales data."""
    sku = row['sku']
    current_price = row['current_price']
    cost_price = row['cost_price']
    stock = row['stock']

    quantity_sold = sales_df.loc[sales_df['sku'] == sku, 'quantity_sold'].sum()

    new_price = current_price

    # Rule 1: Low Stock, High Demand
    if stock < 20 and quantity_sold > 30:
        new_price *= 1.15
    # Rule 2: Dead Stock
    elif stock > 200 and quantity_sold == 0:
        new_price *= 0.70
    # Rule 3: Overstocked Inventory
    elif stock > 100 and quantity_sold < 20:
        new_price *= 0.90

    # Rule 4: Minimum Profit Constraint (Always Applied)
    min_price = cost_price * 1.2
    if new_price < min_price:
        new_price = min_price

    return pd.Series({
        'sku': sku,
        'old_price': f"{current_price:.2f} INR",
        'new_price': f"{new_price:.2f} INR"
    })

def main():
    try:
        products_df = pd.read_csv(r'pricing-engine\src\data\products.csv')
        sales_df = pd.read_csv(r'pricing-engine\src\data\sales.csv')
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
        return

    updated_prices_df = products_df.apply(adjust_price, axis=1, sales_df=sales_df)

    output_path = 'pricing-engine/src/output/updated_prices.csv'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    updated_prices_df.to_csv(output_path, index=False)

    print("✅ Pricing update completed. Output saved to 'pricing-engine/src/output/updated_prices.csv'.")

if __name__ == "__main__":
    main()
