create database olaride12;

use  olaride12;

CREATE TABLE ola_dataset1 (
    Date DATE,
    Time TIME,
    Booking_ID VARCHAR(50),
    Booking_Status VARCHAR(50),
    Customer_ID VARCHAR(50),
    Vehicle_Type VARCHAR(50),
    Pickup_Location VARCHAR(100),
    Drop_Location VARCHAR(100),
    V_TAT FLOAT,
    C_TAT FLOAT,
    Canceled_Rides_by_Customer VARCHAR(10),
    Canceled_Rides_by_Driver VARCHAR(10),
    Incomplete_Rides VARCHAR(10),
    Incomplete_Rides_Reason VARCHAR(255),
    Booking_Value INT,
    Payment_Method VARCHAR(50),
    Ride_Distance INT,
    Driver_Ratings FLOAT,
    Customer_Rating FLOAT,
    Vehicle_Images VARCHAR(255)
);

#1. Retrieve all successful bookings:
select * from ola_dataset1; 

SELECT COUNT(*) FROM ola_dataset1;
#total number of column
SELECT COUNT(*) 
FROM INFORMATION_SCHEMA.COLUMNS 
WHERE table_schema = 'ola_ride_insight' 
  AND table_name = 'ola_dataset1';

#access booking_status column
SELECT Booking_Status 
FROM ola_dataset1;


SELECT DISTINCT Booking_Status 
FROM ola_dataset1;
#only success booking 
SELECT * 
FROM ola_dataset1
WHERE Booking_Status = 'Success';

SELECT COUNT(*) AS Successful_Bookings
FROM ola_dataset1
WHERE Booking_Status = 'Success';

#2. Find the average ride distance for each vehicle type:

SELECT Vehicle_Type, AVG(Ride_Distance) AS Average_Ride_Distance
FROM ola_dataset1
GROUP BY Vehicle_Type;

#3.Get the total number of cancelled rides by customers:

SELECT COUNT(*) AS Total_Cancelled_By_Customers
FROM ola_dataset1
WHERE Canceled_Rides_by_Customer IS NOT NULL;

#4.List the top 5 customers who booked the highest number of rides:



select customer_id,count(*) as total_rides
from ola_dataset1
group by customer_id
order by total_rides desc
limit 5;

#5.Get the number of rides cancelled by drivers due to personal and car-related issues:

SELECT COUNT(*) AS canceled_rides_by_driver
FROM ola_dataset1
WHERE canceled_rides_by_driver IN ('Personal Issue', 'Car Issue');

#6. Find the maximum and minimum driver ratings for Prime Sedan bookings:

select driver_ratings,vehicle_type
from ola_dataset1
where vehicle_type in ('prime sedan');

SELECT 
    MAX(Driver_Ratings) AS Max_Rating,
    MIN(Driver_Ratings) AS Min_Rating
FROM ola_dataset1
WHERE vehicle_type = 'Prime Sedan'
  AND Driver_Ratings IS NOT NULL;
  
  #7. Retrieve all rides where payment was made using UPI:
 
select payment_method,count(*) as upi
from ola_dataset1
where payment_method= 'upi';

SELECT *
FROM ola_dataset1
WHERE Payment_Method = 'UPI';


#8. Find the average customer rating per vehicle type:

select  avg(customer_rating) ,vehicle_type
from ola_dataset1
group by vehicle_type;


#9. Calculate the total booking value of rides completed successfully:

select *
from ola_dataset1;

select sum(booking_value) as tolal_booking,booking_status
from ola_dataset1
where booking_status='success';

#10. List all incomplete rides along with the reason

select incomplete_rides,incomplete_rides_reason
from ola_dataset1
where incomplete_rides is not null
 and incomplete_rides_reason is not null;
 
 










  



