# olarideinsight1
# 🚖 Ola Ride Insight Analysis Project

## 📌 Project Overview

The Ola Ride Insight project is a complete data analytics solution developed to analyze ride booking patterns, customer behavior, revenue trends, cancellations, and driver performance.

The project combines:

* Python for data cleaning and preprocessing
* MySQL for database management and SQL analysis
* Power BI for interactive dashboards
* Streamlit for web application deployment

This project helps generate business insights that can improve operational efficiency, customer satisfaction, and revenue optimization.

---

# 🎯 Objectives

The main objectives of this project are:

* Analyze ride booking trends
* Understand customer and driver behavior
* Identify cancellation reasons
* Measure revenue and payment trends
* Evaluate service quality using ratings
* Build interactive dashboards for business decision-making

---

# 🛠️ Technologies Used

| Technology | Purpose                    |
| ---------- | -------------------------- |
| Python     | Data Cleaning & Processing |
| Pandas     | Data Manipulation          |
| MySQL      | Database Management        |
| SQL        | Data Analysis Queries      |
| Power BI   | Data Visualization         |
| Streamlit  | Interactive Dashboard      |
| GitHub     | Version Control            |

---

# 📂 Dataset Information

The dataset contains Ola ride booking information including:

* Booking Details
* Vehicle Type
* Ride Distance
* Booking Status
* Cancellation Reasons
* Driver Ratings
* Customer Ratings
* Payment Methods
* Revenue Information

---

# 🧹 Data Cleaning Process

Data preprocessing was performed using Python and Pandas.

### Steps Performed:

* Handled missing values
* Converted Date and Time columns
* Created Datetime column
* Extracted Hour and Day columns
* Standardized categorical values
* Checked data types and null values

---

# 🗄️ Database Design

## Database Name

```sql
ola_ride_insightfinal
```

## Table Name

```sql
ola_datasetfine
```

### Key Columns

* Booking_ID
* Booking_Status
* Vehicle_Type
* Booking_Value
* Ride_Distance
* Driver_Ratings
* Customer_Rating
* Payment_Method
* Datetime
* Hour
* Day

---

# 📊 SQL Analysis Performed

The following SQL queries were used for analysis:

1. Retrieve successful bookings
2. Average ride distance by vehicle type
3. Customer cancellation analysis
4. Top 5 customers by ride count
5. Driver cancellation reasons
6. Prime Sedan driver ratings
7. UPI payment analysis
8. Average customer ratings
9. Revenue from successful rides
10. Incomplete rides and reasons

---

# 📈 Power BI Dashboard

The Power BI dashboard contains 5 analytical pages:

## 1️⃣ Overall Dashboard

* Ride Volume Over Time
* Booking Status Breakdown
* KPI Cards

## 2️⃣ Vehicle Type Analysis

* Ride Distance by Vehicle
* Booking Value by Vehicle Type
* Successful Bookings by Vehicle

## 3️⃣ Revenue Analysis

* Revenue by Payment Method
* Ride Distance by Day
* Top Customers

## 4️⃣ Cancellation Analysis

* Customer Cancellation Reasons
* Driver Cancellation Reasons
* Cancellation Metrics

## 5️⃣ Ratings Analysis

* Driver Ratings
* Customer Ratings
* Vehicle-wise Rating Comparison

---

# 💻 Streamlit Dashboard Features

The Streamlit dashboard includes:

* Interactive filters
* SQL-powered analytics
* KPI cards
* Color-coded tables
* Power BI screenshots integration
* Dynamic query-based insights

---

# 🔍 Key Insights

## Ride Status

* Most bookings were completed successfully.
* Cancellation and incomplete ride percentages were relatively low.

## Vehicle Usage

* Prime Sedan and Micro were among the most used vehicle types.

## Revenue

* Significant revenue was generated from successful rides.
* UPI emerged as a popular payment method.

## Customer Behavior

* Top customers showed strong brand loyalty.

## Driver Performance

* Driver ratings were consistently around 4.

## Operational Challenges

* Incomplete rides mainly occurred due to customer demand and vehicle issues.



# 🚀 How to Run the Project

## Step 1: Clone Repository

```bash
git clone <your-github-repo-link>
```

## Step 2: Install Requirements

```bash
pip install -r requirements.txt
```

## Step 3: Run Streamlit App

```bash
streamlit run app.py
```

---

# 📌 Future Improvements

* Deploy MySQL database on cloud
* Add real-time data updates
* Implement machine learning for ride prediction
* Add advanced Power BI dashboards
* Improve Streamlit UI design

---

# 👨‍💻 Author

## Amit Kumar Mutyalwar

### Project: Ola Ride Insight Analysis

---

# ⭐ Conclusion

This project demonstrates end-to-end data analytics workflow including:

* Data Cleaning
* SQL Analysis
* Dashboard Development
* Business Insight Generation
* Interactive Visualization

The project helps transform raw ride data into actionable business insights for better operational and strategic decision-making.
