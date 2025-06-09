import streamlit as st
import gspread
from google.oauth2 import service_account
from datetime import date

# Google Sheets setup using Streamlit Secrets
creds_dict = st.secrets["google_credentials"]
credentials = service_account.Credentials.from_service_account_info(creds_dict)

client = gspread.authorize(credentials)
sheet = client.open("Employee Attendance").sheet1  # Replace with your actual sheet name

# Streamlit UI
st.title("Department Attendance Form")

# Department & Manager Selection
departments = ["Operations", "Email Marketing", "Data", "Quality", "MIS Delivery"]
department = st.selectbox("Select your department", departments)
manager_name = st.text_input("Manager name")

# Attendance Input
st.write("### Enter Employee Attendance")
employee_name = st.text_input("Employee name")
status = st.selectbox("Status", ["Present", "Absent", "WFH", "Leave"])
remarks = st.text_input("Remarks (optional)")
today = date.today().strftime("%Y-%m-%d")

# Submit Button
if st.button("Submit Attendance"):
    sheet.append_row([today, department, employee_name, status, remarks, manager_name])
    st.success("Attendance submitted successfully!")
