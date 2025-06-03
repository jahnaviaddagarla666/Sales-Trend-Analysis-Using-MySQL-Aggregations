
-- sales_trend_analysis.sql
CREATE DATABASE IF NOT EXISTS sales_db;
USE sales_db;

CREATE TABLE online_sales (
    `Row ID` INT,
    `Order ID` VARCHAR(50),
    `Order Date` DATE,
    `Ship Date` DATE,
    `Ship Mode` VARCHAR(50),
    `Customer ID` VARCHAR(50),
    `Customer Name` VARCHAR(100),
    `Segment` VARCHAR(50),
    `Country` VARCHAR(50),
    `City` VARCHAR(50),
    `State` VARCHAR(50),
    `Postal Code` VARCHAR(20),
    `Region` VARCHAR(50),
    `Product ID` VARCHAR(50),
    `Category` VARCHAR(50),
    `Sub-Category` VARCHAR(50),
    `Product Name` VARCHAR(255),
    `Sales` DECIMAL(10,2),
    `Quantity` INT,
    `Discount` DECIMAL(5,2),
    `Profit` DECIMAL(10,2)
);

-- Monthly trend analysis
SELECT 
    YEAR(`Order Date`) AS year,
    MONTH(`Order Date`) AS month,
    ROUND(SUM(Sales), 2) AS total_revenue,
    COUNT(DISTINCT `Order ID`) AS order_volume
FROM online_sales
GROUP BY year, month
ORDER BY year, month;
