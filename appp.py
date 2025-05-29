import streamlit as st
import pandas as pd
import mysql.connector

# Page config
st.set_page_config(page_title="Ola Ride Insight", layout="wide")

# Background and sidebar CSS
st.markdown("""
    <style>
        .stApp {
            background-image: url("https://i.ibb.co/WNNMxvWF/ola-cabs.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .sidebar .sidebar-content {
            background-color: rgba(255, 255, 255, 0.9);
        }
        .stSelectbox > div > div {
            color: black;
            font-weight: bold;
        }
        .color-table {
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            padding: 10px;
        }
        .color-table table {
            width: 100%;
            border-collapse: collapse;
        }
        .color-table th, .color-table td {
            padding: 8px 12px;
            border: 1px solid #ddd;
        }
        .color-table th {
            background-color: #ffd700;
            color: black;
        }
        .color-table tr:nth-child(even) {
            background-color: #f2f2f2;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🚖 Ola Ride Insight Dashboard")

# MySQL Query Function using st.secrets
def run_query(query):
    connection = mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        user=st.secrets["mysql"]["user"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"]
    )
    result = pd.read_sql(query, con=connection)
    connection.close()
    return result

# Sidebar options
menu = [
    "Show All Data",
    "Total Row Count",
    "Column Count",
    "Booking Status Overview",
    "Successful Bookings",
    "Avg Ride Distance per Vehicle",
    "Cancelled Rides by Customers",
    "Top 5 Customers",
    "Driver Cancel Reasons",
    "Prime Sedan Ratings",
    "UPI Payments",
    "Avg Customer Rating",
    "Total Booking Value (Success)",
    "Incomplete Rides & Reasons",
    "Power BI Dashboard"
]

choice = st.sidebar.selectbox("Select Query", menu)

# Logic based on query selected
if choice == "Show All Data":
    st.subheader("All Data from ola_dataset1")
    df = run_query("SELECT * FROM ola_dataset1 LIMIT 100")
    st.dataframe(df)

elif choice == "Total Row Count":
    result = run_query("SELECT COUNT(*) as Total_Rows FROM ola_dataset1")
    st.metric("Total Rows", result['Total_Rows'][0])

elif choice == "Column Count":
    query = """
    SELECT COUNT(*) as Column_Count
    FROM INFORMATION_SCHEMA.COLUMNS 
    WHERE table_schema = 'ola_ride_insight' AND table_name = 'ola_dataset1'
    """
    result = run_query(query)
    st.metric("Total Columns", result['Column_Count'][0])

elif choice == "Booking Status Overview":
    result = run_query("SELECT Booking_Status, COUNT(*) as Count FROM ola_dataset1 GROUP BY Booking_Status")
    st.bar_chart(result.set_index("Booking_Status"))

elif choice == "Successful Bookings":
    result = run_query("SELECT COUNT(*) AS Successful_Bookings FROM ola_dataset1 WHERE Booking_Status = 'Success'")
    st.metric("Successful Bookings", result['Successful_Bookings'][0])

elif choice == "Avg Ride Distance per Vehicle":
    result = run_query("""
    SELECT Vehicle_Type, AVG(Ride_Distance) AS Average_Ride_Distance
    FROM ola_dataset1
    GROUP BY Vehicle_Type
    """)
    st.bar_chart(result.set_index("Vehicle_Type"))

elif choice == "Cancelled Rides by Customers":
    result = run_query("""
    SELECT COUNT(*) AS Total_Cancelled_By_Customers
    FROM ola_dataset1
    WHERE Canceled_Rides_by_Customer IS NOT NULL
    """)
    st.metric("Cancelled by Customers", result['Total_Cancelled_By_Customers'][0])

elif choice == "Top 5 Customers":
    st.subheader("Top 5 Customers by Ride Count")
    result = run_query("""
    SELECT Customer_ID, COUNT(*) as Total_Rides
    FROM ola_dataset1
    GROUP BY Customer_ID
    ORDER BY Total_Rides DESC
    LIMIT 5
    """)
    html_table = result.to_html(index=False, classes="color-table")
    st.markdown(html_table, unsafe_allow_html=True)

elif choice == "Driver Cancel Reasons":
    result = run_query("""
    SELECT COUNT(*) AS Canceled_By_Driver
    FROM ola_dataset1
    WHERE Canceled_Rides_by_Driver IN ('Personal Issue', 'Car Issue')
    """)
    st.metric("Canceled by Driver (Personal/Car)", result['Canceled_By_Driver'][0])

elif choice == "Prime Sedan Ratings":
    st.subheader("Prime Sedan Rating (Max & Min)")
    result = run_query("""
    SELECT 
        MAX(Driver_Ratings) AS Max_Rating,
        MIN(Driver_Ratings) AS Min_Rating
    FROM ola_dataset1
    WHERE Vehicle_Type = 'Prime Sedan' AND Driver_Ratings IS NOT NULL
    """)
    html_table = result.to_html(index=False, classes="color-table")
    st.markdown(html_table, unsafe_allow_html=True)

elif choice == "UPI Payments":
    result = run_query("""
    SELECT COUNT(*) AS UPI_Rides
    FROM ola_dataset1
    WHERE Payment_Method = 'UPI'
    """)
    st.metric("UPI Payments", result['UPI_Rides'][0])

elif choice == "Avg Customer Rating":
    result = run_query("""
    SELECT Vehicle_Type, AVG(Customer_Rating) as Avg_Rating
    FROM ola_dataset1
    GROUP BY Vehicle_Type
    """)
    st.bar_chart(result.set_index("Vehicle_Type"))

elif choice == "Total Booking Value (Success)":
    result = run_query("""
    SELECT SUM(Booking_Value) AS Total_Revenue
    FROM ola_dataset1
    WHERE Booking_Status = 'Success'
    """)
    st.metric("Total Revenue (Success)", result['Total_Revenue'][0])

elif choice == "Incomplete Rides & Reasons":
    st.subheader("Incomplete Rides & Reasons")
    result = run_query("""
    SELECT Incomplete_Rides, Incomplete_Rides_Reason
    FROM ola_dataset1
    WHERE Incomplete_Rides IS NOT NULL AND Incomplete_Rides_Reason IS NOT NULL
    """)
    html_table = result.to_html(index=False, classes="color-table")
    st.markdown(html_table, unsafe_allow_html=True)

elif choice == "Power BI Dashboard":
    st.title("📊 Ola Ride Power BI Report")
    st.markdown("""
        <iframe 
            width="100%" 
            height="800px" 
            src="https://app.powerbi.com/view?r=eyJrIjoiZWIyMzkyMmQtNDg0MS00MDU0LWI1MjUtZjNhZGQ2YzZlYWU5IiwidCI6IjY2OTQzZmQ4LTYwYzMtNGI5ZS05MGU0LTFhNDJhZWMyNDFiZSJ9" 
            frameborder="0" 
            allowFullScreen="true">
        </iframe>
    """, unsafe_allow_html=True)
