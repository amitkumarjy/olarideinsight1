CREATE DATABASE ola_ride_insightfinal;
USE ola_ride_insightfinal;

CREATE TABLE ola_datasetfine (
    Date DATE,
    Time TIME,
    Booking_ID VARCHAR(50),
    Booking_Status VARCHAR(20),
    Customer_ID VARCHAR(50),
    Vehicle_Type VARCHAR(50),
    Pickup_Location VARCHAR(100),
    Drop_Location VARCHAR(100),
    V_TAT FLOAT,
    C_TAT FLOAT,
    Canceled_Rides_by_Customer VARCHAR(50),
    Canceled_Rides_by_Driver VARCHAR(50),
    Incomplete_Rides VARCHAR(50),
    Incomplete_Rides_Reason VARCHAR(255),
    Booking_Value INT,
    Payment_Method VARCHAR(20),
    Ride_Distance INT,
    Driver_Ratings FLOAT,
    Customer_Rating FLOAT,
    Datetime DATETIME,
    Hour INT,
    Day VARCHAR(20)
);
SELECT COUNT(*) FROM ola_datasetfine;

select * from ola_datasetfine;

#first query
#1. Retrieve all successful bookings:
 select  Booking_ID,Customer_ID, Vehicle_Type, Booking_Value from ola_datasetfine 
 where Booking_Status= 'Success';
 
 #2 Find the average ride distance for each vehicle type:
 select vehicle_type,avg(ride_distance) as averagedistance
 from ola_datasetfine
 group by vehicle_type;
 
 
 #3. Get the total number of cancelled rides by customers:
 select   canceled_rides_by_customer as total, count(*)  from 
 ola_datasetfine
 where canceled_rides_by_customer != 'No' 
 group by canceled_rides_by_customer 
 order by total asc ;
 
SELECT DISTINCT Canceled_Rides_by_Customer 
FROM ola_datasetfine;
 
#4. List the top 5 customers who booked the highest number of rides:
select * from ola_datasetfine;
SELECT Customer_ID, COUNT(*) AS total_rides
FROM ola_datasetfine
GROUP BY Customer_ID
ORDER BY total_rides DESC
LIMIT 5;

#5. Get the number of rides cancelled by drivers due to personal and car-related issues:
select canceled_rides_by_driver,count(*) as total_number_of_rides_cancelled_by_driver
from ola_datasetfine 
where canceled_rides_by_driver ='Personal & Car related issue'
group by canceled_rides_by_driver ;

#6. Find the maximum and minimum driver ratings for Prime Sedan bookings:

select  vehicle_type,
max(driver_ratings) as max_rating,
min(driver_ratings) as min_rating
from ola_datasetfine 
where vehicle_type='prime sedan';

#7. Retrieve all rides where payment was made using UPI:

select *from ola_datasetfine
where payment_method='upi'; 

#8. Find the average customer rating per vehicle type:

select  vehicle_type,
avg(customer_rating) as average_customer_rating
from ola_datasetfine
group by vehicle_type
order by average_customer_rating desc ;

select * from ola_datasetfine;
#9. Calculate the total booking value of rides completed successfully:

select sum(booking_value) as total_booking_value
from ola_datasetfine
where booking_status='success';

#10. List all incomplete rides along with the reason
SELECT Incomplete_Rides_Reason, COUNT(*) AS total
FROM ola_datasetfine
WHERE Incomplete_Rides = 'Yes'
GROUP BY Incomplete_Rides_Reason
ORDER BY total DESC;

