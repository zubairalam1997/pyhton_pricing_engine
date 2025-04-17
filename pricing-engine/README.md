# Pricing Engine

This script updates product prices based on stock levels and sales data using defined business rules.

## How It Works

1. Reads `products.csv` and `sales.csv`.
2. Applies the following pricing rules:
   - **Rule 1:** Increase price by 15% for low stock & high demand.
   - **Rule 2:** Decrease price by 30% for dead stock.
   - **Rule 3:** Decrease price by 10% for overstocked items with low sales.
   - **Rule 4:** Ensure new price is at least 20% over cost.
3. Rounds all final prices and adds "INR" units.
4. Outputs result to `updated_prices.csv`.
## The updated prices will be saved in: "pricing-engine/src/output/updated_prices.csv"

## Output Format

- `sku`
- `old_price` (in INR)
- `new_price` (in INR)      


## Dependencies
Ensure you have **Python 3.x** installed along with the following packages:
```sh
pip install pandas

Ensure products.csv and sales.csv exist in the src/data/ folder.

## Usage Run the script from the root directory:

```bash
python src/py_pricing_engine.py



## Important Notes

* The script assumes that the input CSV files are correctly formatted and exist in the specified paths (`pricing-engine/src/data/`).
* The pricing rules are applied in the order specified, and only the first applicable rule (among Rules 1, 2, and 3) is applied. Rule 4 (Minimum Profit Constraint) is always applied last.
* The output file will be saved to `pricing-engine/src/output/updated_prices.csv`. The script will create the necessary output directory if it doesn't exist.
* The units for `old_price` and `new_price` are explicitly included as " INR" in the output CSV file.

