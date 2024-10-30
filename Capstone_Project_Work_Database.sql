-- Capstone Project on End-to-end data analysis into "Pizza_Sales Database" --

select * from pizza_sales;

select sum(total_price) from pizza_sales;

select sum(total_price) as Total_Revenue from pizza_sales;

select * from pizza_sales;

select sum(total_price)/ COUNT(DISTINCT order_id) as AVG_Order_Value from pizza_sales;

select sum(quantity) as Total_Pizza_Sold from pizza_sales;

select COUNT(DISTINCT order_id) as Total_orders from pizza_sales;

Select sum(quantity) / COUNT(DISTINCT order_id) from pizza_sales; 

Select CAST(sum(quantity) AS DECIMAL (10,2)) / CAST(COUNT(DISTINCT order_id) AS DECIMAL(10,2)) from pizza_sales; 

Select CAST(CAST(sum(quantity) AS DECIMAL (10,2)) / CAST(COUNT(DISTINCT order_id) AS DECIMAL(10,2)) AS DECIMAL(10,2)) AS Avg_Pizzas_Per_order from pizza_sales; 

select * from pizza_sales;

select DATENAME(DW, Order_date) as order_day, COUNT(DISTINCT order_id) As Total_orders from pizza_sales GROUP BY DATENAME(DW, order_date);

select DATENAME(MONTH, Order_date) As Month_Name, COUNT(DISTINCT Order_id) AS Total_Orders from pizza_sales GROUP BY DATENAME(MONTH, Order_date); 

select DATENAME(MONTH, Order_date) As Month_Name, COUNT(DISTINCT Order_id) AS Total_Orders from pizza_sales GROUP BY DATENAME(MONTH, Order_date) ORDER BY Total_Orders DESC;

select Pizza_Category,sum(Total_Price) as Total_Sales ,sum(Total_Price) * 100 / (select sum(Total_Price) from pizza_sales) AS PCT from pizza_sales GROUP BY Pizza_Category;

select Pizza_Category,sum(Total_Price) as Total_Sales ,sum(Total_Price) * 100 / (select sum(Total_Price) from pizza_sales  WHERE MONTH(order_date) = 1) AS PCT from pizza_sales WHERE MONTH(order_date) = 1 GROUP BY Pizza_Category;

select Pizza_Size,sum(Total_Price) as Total_Sales ,sum(Total_Price) * 100 / (select sum(Total_Price) from pizza_sales) AS PCT from pizza_sales WHERE MONTH(order_date) = 1 GROUP BY Pizza_Size;

select Pizza_Size,CAST(sum(Total_Price) AS DECIMAL(10,2)) as Total_Sales ,CAST(sum(Total_Price) * 100 / (select sum(Total_Price) from pizza_sales WHERE DATEPART(quarter, order_date)=1)AS DECIMAL(10,2)) AS PCT from pizza_sales WHERE DATEPART(quarter, order_date)=1 GROUP BY Pizza_Size ORDER BY PCT DESC; 

select Top 5 Pizza_Name, sum(Total_Price) As Total_Revenue from pizza_sales GROUP BY Pizza_Name ORDER BY Total_Revenue DESC;

select Top 5 Pizza_Name, sum(Total_Price) As Total_Revenue from pizza_sales GROUP BY Pizza_Name ORDER BY Total_Revenue ASC;

select Top 5 Pizza_Name, sum(quantity) As Total_Quantity from pizza_sales GROUP BY Pizza_Name ORDER BY Total_Quantity DESC;

select Top 5 Pizza_Name, sum(quantity) As Total_Quantity from pizza_sales GROUP BY Pizza_Name ORDER BY Total_Quantity ASC;

select Top 5 Pizza_Name, COUNT(DISTINCT order_id) As Total_Orders from pizza_sales GROUP BY Pizza_Name ORDER BY Total_Orders DESC;

select Top 5 Pizza_Name, COUNT(DISTINCT order_id) As Total_Orders from pizza_sales GROUP BY Pizza_Name ORDER BY Total_Orders ASC;

