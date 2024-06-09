import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
import base64

# Define a function to generate the Pandas Profiling report
def generate_report(df):
    profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
    profile.to_file("output.html")  # Save the report to a file with .html extension

# Function to create a download link for a file
def get_binary_file_downloader_html(file_path, file_label):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    return f'<a href="data:application/octet-stream;base64,{b64}" download="{file_label}.html">Click here to download {file_label}</a>'

# Create a Streamlit app
st.title("Pandas Profiling Report Generator")

# Allow the user to upload a CSV or XLSX file
uploaded_file = st.file_uploader("Upload a CSV or XLSX file", type=["csv", "xlsx"])

if uploaded_file is not None:
    st.write("File Uploaded!")

    # Read the uploaded file into a DataFrame based on the file extension
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith(".xlsx"):
        df = pd.read_excel(uploaded_file)

    # Display a preview of the DataFrame
    st.dataframe(df.head())

    # Generate the Pandas Profiling report when the user clicks a button
    if st.button("Generate Report"):
        with st.spinner("Generating Report..."):
            generate_report(df)
        st.success("Report generated successfully!")

        # Provide a download link to the generated report
        st.markdown(get_binary_file_downloader_html("output.html", "Download Report"), unsafe_allow_html=True)

# Optionally, provide additional information or instructions
st.write("This app allows you to upload a CSV or XLSX file, generate a Pandas Profiling report, and download the report in HTML format.")
