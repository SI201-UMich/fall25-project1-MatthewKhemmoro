# Name: Matthew Khemmoro
# Student id: 5598 1840
# Email: mattkhem@umich.edu

import csv

# Load CSV Data together with partner
def read_csv_file(filename):
    data = []
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)  # reads each row as a dictionary
        for row in reader:
            # convert numeric strings to float for math later
            row['Profit'] = float(row['Profit'])
            row['Sales'] = float(row['Sales'])
            row['Discount'] = float(row['Discount'])
            data.append(row)  # add the cleaned-up row to the list
    return data


# MATTHEW FUNCTION 1
def calculate_avg_profit_by_region(superstore_data):
    region_totals = {}  # track total profit by region
    region_counts = {}  # track how many entries per region

    for row in superstore_data:
        region = row['Region']
        profit = row['Profit']
        region_totals[region] = region_totals.get(region, 0) + profit  # add profit to region total
        region_counts[region] = region_counts.get(region, 0) + 1       # add to count of rows for region

    avg_profit = {}
    for region in region_totals:
        avg_profit[region] = round(region_totals[region] / region_counts[region], 2)  # calculate average

    return avg_profit  # dictionary of average profit per region


# MATTHEW FUNCTION 2
def calculate_percent_discounted(superstore_data):
    total_orders = len(superstore_data)  # count how many rows total
    discounted_orders = sum(1 for row in superstore_data if row['Discount'] > 0)  # count how many had a discount
    return round((discounted_orders / total_orders) * 100, 2)  # percent of orders with discount
