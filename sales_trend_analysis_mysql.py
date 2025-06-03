# Sales Trend Analysis from MySQL using Python

import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="sales_db"
)

# SQL Query
sql = """
SELECT 
    YEAR(`Order Date`) AS year,
    MONTH(`Order Date`) AS month,
    ROUND(SUM(Sales), 2) AS total_revenue,
    COUNT(DISTINCT `Order ID`) AS order_volume
FROM online_sales
GROUP BY year, month
ORDER BY year, month;
"""

# Load data
df = pd.read_sql(sql, conn)
conn.close()

# Process for plotting
df['date'] = df['year'].astype(str) + '-' + df['month'].astype(str).str.zfill(2)

# Plot Revenue
plt.figure(figsize=(12, 5))
plt.plot(df['date'], df['total_revenue'], marker='o')
plt.xticks(rotation=45)
plt.ylabel('Total Revenue')
plt.title('Monthly Revenue Trend')
plt.tight_layout()
plt.show()

# Plot Order Volume
plt.figure(figsize=(12, 5))
plt.plot(df['date'], df['order_volume'], marker='o', color='orange')
plt.xticks(rotation=45)
plt.ylabel('Order Volume')
plt.title('Monthly Order Volume Trend')
plt.tight_layout()
plt.show()
