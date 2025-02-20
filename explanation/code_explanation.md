# Introduction to Libraries Used in the Code

In this Python script, we are using several powerful libraries to achieve file processing, data cleaning, visualization, and conversion. Below is a detailed introduction to each library used, along with its purpose and why we need it.

## 1. **Streamlit** (`streamlit`)

### Purpose:
Streamlit is an open-source Python framework that allows us to build interactive web applications quickly and easily using Python scripts. It is widely used for creating data dashboards, machine learning model deployment interfaces, and other interactive applications.

### Why We Use It:
- It allows us to build a **graphical user interface (GUI)** with minimal code.
- We can **upload files**, **display data**, **apply transformations**, and **download modified files** easily.
- It provides **built-in support for data visualization** without requiring complex HTML/CSS/JavaScript.

### Methods Used in the Code:
1. `st.set_page_config(page_title, layout)`: Sets up the Streamlit app's configuration, such as the title and layout.
   - `page_title` defines the title displayed on the browser tab.
   - `layout="wide"` ensures the app uses the full screen width.
2. `st.title(text)`: Displays a large title text at the top of the page.
   - This makes the application easily identifiable by users.
3. `st.write(text)`: Displays text or other objects like dataframes, markdown, etc.
   - Can be used for multiple purposes, including displaying instructions and output.
4. `st.file_uploader(label, type, accept_multiple_files)`: Creates a file uploader for CSV and Excel files.
   - `label` defines the text displayed to prompt users to upload files.
   - `type=["csv", "xlsx"]` restricts file uploads to only CSV and Excel formats.
   - `accept_multiple_files=True` allows multiple files to be uploaded at once.
5. `st.dataframe(data)`: Displays a DataFrame (table) interactively.
   - Allows users to view and explore their uploaded data.

## 2. **Pandas** (`pandas`)

### Purpose:
Pandas is a powerful data analysis and manipulation library that provides data structures like DataFrames and Series to work with structured data.

### Why We Use It:
- It allows us to **load CSV and Excel files**.
- We can **clean data**, **remove duplicates**, and **handle missing values**.
- It provides easy-to-use **functions for data transformations and visualization**.

### Methods Used in the Code:
1. `pd.read_csv(file)`: Reads a CSV file and returns a DataFrame.
   - Automatically detects column headers and data types.
2. `df.to_csv(file, index=False)`: Converts a DataFrame to CSV format.
   - `index=False` prevents unnecessary indexing columns from being written to the output file.
3. `pd.read_excel(file, engine='openpyxl')`: Reads an Excel file and returns a DataFrame.
   - `engine='openpyxl'` is required for handling modern Excel files (.xlsx format).
4. `df.to_excel(writer, index=False)`: Converts a DataFrame to Excel format.
   - Uses `writer`, an Excel writer object, to handle Excel file creation.
5. `df.drop_duplicates(inplace=True)`: Removes duplicate rows from the dataset.
   - `inplace=True` modifies the DataFrame directly instead of creating a new one.
6. `df.fillna(df.mean())`: Fills missing values with the column mean.
   - Only applicable to numeric columns.

## 3. **OS Module** (`os`)

### Purpose:
The `os` module provides a way to interact with the operating system, such as working with file paths.

### Methods Used:
1. `os.path.splitext(filename)`: Splits a filename into name and extension.
   - Helps identify whether a file is CSV or Excel.

## 4. **BytesIO** (`io.BytesIO`)

### Purpose:
`BytesIO` is used to handle file-like operations in memory.

### Methods Used:
1. `BytesIO()`: Creates a new in-memory file.
   - Prevents the need for writing temporary files to disk.

---

# Line-by-Line Explanation of the Code

## 1. Type Ignore Directive
```python
# type: ignore
```
### Purpose:
- This tells Python's type checker (e.g., mypy) to ignore type-related warnings in this script.

## 2. Importing Required Libraries
```python
import streamlit as st
import pandas as pd
import os
from io import BytesIO
```
### Explanation:
- `streamlit` is used to create the web interface.
- `pandas` is used for data manipulation.
- `os` helps with file path operations.
- `BytesIO` allows handling files in memory instead of disk storage.

## 3. Setting Up the Streamlit Page
```python
st.set_page_config(page_title="Data Sweeper", layout="wide")
```
### Explanation:
- `page_title="Data Sweeper"` sets the title of the webpage.
- `layout="wide"` ensures the web app expands across the full browser width.

## 4. Displaying the App Title and Description
```python
st.title("Data Sweeper")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization")
```
### Explanation:
- `st.title()` displays the main heading.
- `st.write()` provides a short introduction.

## 5. File Upload Section
```python
uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)
```
### Explanation:
- Allows users to upload CSV or Excel files.
- Supports multiple file uploads simultaneously.

## 6. Processing Uploaded Files
```python
if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
```
### Explanation:
- Loops through uploaded files.
- Extracts the file extension for format identification.

## 7. Reading CSV or Excel Files
```python
if file_ext == ".csv":
    df = pd.read_csv(file)
elif file_ext == ".xlsx":
    df = pd.read_excel(file, engine='openpyxl')
else:
    st.error(f"Unsupported file type: {file_ext}")
    continue
```
### Explanation:
- Reads CSV or Excel files into Pandas DataFrame.
- Displays an error message if the format is unsupported.

---

# Summary of Code Explanation

### **Key Takeaways**
1. **Understanding Libraries Used**
2. **Core Functionalities in the Code**
3. **Concepts to Remember for Future Implementation**

By practicing these concepts, you will be fully equipped to build your own data processing and conversion tool using Python, Streamlit, and Pandas. 🚀

## Full Code
```python
# type: ignore
import streamlit as st
import pandas as pd
import os
from io import BytesIO

# Page Configuration
st.set_page_config(page_title="Data Sweeper", layout="wide")
st.title("Data Sweeper")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization")

# File Upload
uploaded_files = st.file_uploader("Upload your files (CSV or Excel):", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[-1].lower()
        
        try:
            # Read the file based on extension
            if file_ext == ".csv":
                df = pd.read_csv(file)
            elif file_ext == ".xlsx":
                df = pd.read_excel(file, engine='openpyxl')
            else:
                st.error(f"Unsupported file type: {file_ext}")
                continue
        except Exception as e:
            st.error(f"Error reading {file.name}: {e}")
            continue
        
        # Display file info
        st.write(f"**File Name:** {file.name}")
        st.write(f"**File Size:** {len(file.getvalue()) / 1024:.2f} KB")

        # Show first 5 rows
        st.write("Preview the head of the Dataframe:")
        st.dataframe(df.head())

        # Select Specific Columns
        st.subheader("Select Columns to Keep")
        selected_columns = st.multiselect(f"Choose Columns for {file.name}", df.columns.tolist(), default=df.columns.tolist())
        df = df[selected_columns] if selected_columns else df

        # Data Cleaning Options
        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Remove Duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.success("Duplicates Removed!")
            with col2:
                if st.button(f"Fill Missing Values for {file.name}"):
                    numeric_cols = df.select_dtypes(include=["number"]).columns
                    if not numeric_cols.empty:
                        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                        st.success("Missing Values have been filled!")
                    else:
                        st.warning("No numeric columns found to fill missing values.")

        # Data Visualization
        st.subheader("Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
            numeric_df = df.select_dtypes(include="number")
            if numeric_df.shape[1] >= 2:
                st.bar_chart(numeric_df.iloc[:, :2])
            else:
                st.warning("Not enough numerical columns for visualization.")

        # File Conversion
        st.subheader("Conversion Options")
        conversion_type = st.radio(f"Convert {file.name} to:", ["CSV", "Excel"], key=file.name)
        
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            try:
                if conversion_type == "CSV":
                    df.to_csv(buffer, index=False)
                    file_name = file.name.replace(file_ext, ".csv")
                    mime_type = "text/csv"
                elif conversion_type == "Excel":
                    with pd.ExcelWriter(buffer, engine="xlsxwriter") as writer:
                        df.to_excel(writer, index=False)
                    file_name = file.name.replace(file_ext, ".xlsx")
                    mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                buffer.seek(0)
                
                # Download Button
                st.download_button(
                    label=f"Download {file.name} as {conversion_type}",
                    data=buffer,
                    file_name=file_name,
                    mime=mime_type
                )
                st.success(f"{file.name} successfully converted and ready for download! 🎉")
            except Exception as e:
                st.error(f"Error during file conversion: {e}")

st.success("All files processed successfully! 🎉")
```

