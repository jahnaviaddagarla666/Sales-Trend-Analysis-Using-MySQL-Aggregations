# Sales Trend Analysis Using MySQL Aggregations

## Purpose
Analyze monthly revenue and order volume trends from Superstore sales data using MySQL database for scalable business intelligence and time-series analysis.

## What Was Done

### 1. Data Preparation
- Loaded Superstore sales dataset (5,000 records, 15 columns)
- Converted Order Date to datetime format for time-based analysis
- Created MySQL database connection using SQLAlchemy and PyMySQL

### 2. Database Setup
- Loaded data into MySQL table `online_sales`
- Used pandas `to_sql()` method for efficient data transfer
- Replaced existing table if present

### 3. SQL Analysis
```sql
SELECT 
    YEAR(Order_Date) AS year,
    MONTH(Order_Date) AS month,
    SUM(Sales) AS total_revenue,
    COUNT(DISTINCT Order_ID) AS order_volume
FROM online_sales
GROUP BY YEAR(Order_Date), MONTH(Order_Date)
ORDER BY year, month;
```

### 4. Visualization
- Created time-series plots for monthly revenue trends
- Generated order volume trend charts
- Used matplotlib for clear visual representation

## Why MySQL Over SQLite
- **Scalability**: Handles larger datasets efficiently
- **Production Ready**: Real-world database environment
- **Concurrent Access**: Multiple users can query simultaneously
- **Advanced Features**: Better optimization and indexing capabilities

## Key Findings
- Monthly revenue aggregation reveals seasonal patterns
- Order volume trends help identify peak business periods
- Time-based grouping enables forecasting and planning

## Technical Requirements
```python
pip install pandas pymysql sqlalchemy matplotlib
```

## Database Connection Setup
```python
engine = create_engine('mysql+pymysql://user:password@host/database')
df.to_sql('online_sales', con=engine, if_exists='replace', index=False)
```

## Business Value
- Identifies seasonal sales patterns
- Supports inventory planning decisions
- Enables revenue forecasting
- Provides data-driven insights for strategic planning

## Files Generated
- Sales trend visualizations (PNG format)
- Aggregated results table
- SQL script for replication
