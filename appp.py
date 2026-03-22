import streamlit as st
import pandas as pd
import mysql.connector

# Page config
st.set_page_config(page_title="Ola Ride Insight", layout="wide")

# Title
st.title("🚖 Ola Ride Insight Dashboard")

# MySQL connection
def run_query(query):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Amitpm@52",
        database="ola_ride_insightfinal"
    )
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# ================================
# 🔍 SIDEBAR FILTERS
# ================================
st.sidebar.header("🔍 Filters")

vehicle = st.sidebar.selectbox(
    "Vehicle Type",
    ["All"] + list(run_query("SELECT DISTINCT Vehicle_Type FROM ola_datasetfine")['Vehicle_Type'])
)

payment = st.sidebar.selectbox(
    "Payment Method",
    ["All"] + list(run_query("SELECT DISTINCT Payment_Method FROM ola_datasetfine")['Payment_Method'])
)

search = st.sidebar.text_input("Search Customer ID")

# Sidebar Menu
menu = [
    "📊 Dashboard",
    "📈 SQL Insights",
    "📊 Power BI Dashboard"
]

choice = st.sidebar.selectbox("Select Section", menu)

# ================================
# 🔧 FILTER QUERY
# ================================
query = "SELECT * FROM ola_datasetfine WHERE 1=1"

if vehicle != "All":
    query += f" AND Vehicle_Type = '{vehicle}'"

if payment != "All":
    query += f" AND Payment_Method = '{payment}'"

if search:
    query += f" AND Customer_ID LIKE '%{search}%'"

# ================================
# 📊 DASHBOARD
# ================================
if choice == "📊 Dashboard":

    st.subheader("📊 Filtered Data")
    df = run_query(query)
    st.dataframe(df.head(100))

    col1, col2, col3 = st.columns(3)

    # Total Rides
    total = run_query("SELECT COUNT(*) AS total FROM ola_datasetfine")
    col1.metric("Total Rides", total['total'][0])

    # Revenue
    revenue = run_query("""
    SELECT SUM(Booking_Value) AS revenue
    FROM ola_datasetfine
    WHERE Booking_Status = 'Success'
    """)
    col2.metric("Total Revenue", revenue['revenue'][0])

    # Avg Distance
    avg_dist = run_query("SELECT AVG(Ride_Distance) AS avg_dist FROM ola_datasetfine")
    col3.metric("Avg Distance", round(avg_dist['avg_dist'][0], 2))

# ================================
# 📈 SQL INSIGHTS
# ================================
elif choice == "📈 SQL Insights":

    st.subheader("1️⃣ Successful Bookings")
    df1 = run_query("""
    SELECT Booking_ID, Customer_ID, Vehicle_Type, Booking_Value 
    FROM ola_datasetfine 
    WHERE Booking_Status = 'Success'
    LIMIT 100
    """)
    st.dataframe(df1)

    st.subheader("2️⃣ Avg Ride Distance per Vehicle")
    df2 = run_query("""
    SELECT Vehicle_Type, AVG(Ride_Distance) AS avg_distance
    FROM ola_datasetfine
    GROUP BY Vehicle_Type
    """)
    st.bar_chart(df2.set_index("Vehicle_Type"))

    st.subheader("3️⃣ Cancelled by Customer")
    df3 = run_query("""
    SELECT Canceled_Rides_by_Customer, COUNT(*) AS total
    FROM ola_datasetfine
    WHERE Canceled_Rides_by_Customer != 'No'
    GROUP BY Canceled_Rides_by_Customer
    ORDER BY total DESC
    """)
    st.dataframe(df3)

    st.subheader("4️⃣ Top 5 Customers")
    df4 = run_query("""
    SELECT Customer_ID, COUNT(*) AS total_rides
    FROM ola_datasetfine
    GROUP BY Customer_ID
    ORDER BY total_rides DESC
    LIMIT 5
    """)
    st.dataframe(df4)

    st.subheader("5️⃣ Driver Cancel Reasons")
    df5 = run_query("""
    SELECT Canceled_Rides_by_Driver, COUNT(*) AS total
    FROM ola_datasetfine
    WHERE Canceled_Rides_by_Driver LIKE '%Personal%'
       OR Canceled_Rides_by_Driver LIKE '%Car%'
    GROUP BY Canceled_Rides_by_Driver
    """)
    st.dataframe(df5)

    st.subheader("6️⃣ Prime Sedan Ratings")
    df6 = run_query("""
    SELECT 
    MAX(Driver_Ratings) AS max_rating,
    MIN(Driver_Ratings) AS min_rating
    FROM ola_datasetfine
    WHERE Vehicle_Type = 'Prime Sedan'
    """)
    st.dataframe(df6)

    st.subheader("7️⃣ UPI Payments")
    df7 = run_query("""
    SELECT COUNT(*) AS total_upi
    FROM ola_datasetfine
    WHERE Payment_Method = 'UPI'
    """)
    st.metric("UPI Rides", df7['total_upi'][0])

    st.subheader("8️⃣ Avg Customer Rating")
    df8 = run_query("""
    SELECT Vehicle_Type, AVG(Customer_Rating) AS avg_rating
    FROM ola_datasetfine
    GROUP BY Vehicle_Type
    ORDER BY avg_rating DESC
    """)
    st.bar_chart(df8.set_index("Vehicle_Type"))

    st.subheader("9️⃣ Total Revenue (Success)")
    df9 = run_query("""
    SELECT SUM(Booking_Value) AS revenue
    FROM ola_datasetfine
    WHERE Booking_Status = 'Success'
    """)
    st.metric("Total Revenue", df9['revenue'][0])

    st.subheader("🔟 Incomplete Rides & Reasons")
    df10 = run_query("""
    SELECT Incomplete_Rides_Reason, COUNT(*) AS total
    FROM ola_datasetfine
    WHERE Incomplete_Rides = 'Yes'
    GROUP BY Incomplete_Rides_Reason
    ORDER BY total DESC
    """)
    st.dataframe(df10)

# ================================
# 📊 POWER BI SCREENSHOTS
# ================================
elif choice == "📊 Power BI Dashboard":

    st.subheader("📊 Power BI Dashboard (Screenshots)")

    st.image(r"D:\guvi\project2\powerbiscreenshot\overal1.png",
             caption="Overall Dashboard", use_container_width=True)

    st.image(r"D:\guvi\project2\powerbiscreenshot\vehicle_type.png",
             caption="Vehicle Type Analysis", use_container_width=True)

    st.image(r"D:\guvi\project2\powerbiscreenshot\revenue.png",
             caption="Revenue Analysis", use_container_width=True)

    st.image(r"D:\guvi\project2\powerbiscreenshot\cancellation.png",
             caption="Cancellation Analysis", use_container_width=True)

    st.image(r"D:\guvi\project2\powerbiscreenshot\rating.png",
             caption="Ratings Analysis", use_container_width=True)