# Aarogya-Drishti
# Aarogya Drishti

### Personal Wellness Analytics Dashboard

Aarogya Drishti is an end-to-end data analytics project that transforms personal wellness and fitness data into meaningful insights using Python, Machine Learning, SQL Server, Power BI, and Streamlit.

## Live Interactive Dashboard

[View the Live Dashboard](PASTE_YOUR_STREAMLIT_LINK_HERE)

The interactive dashboard is deployed using Streamlit and can be accessed publicly without requiring a Power BI account.

---

## Project Overview

This project analyzes daily wellness and fitness patterns using metrics such as:

- Daily Steps
- Calories Burned
- Sleep Duration
- Water Intake
- Active Minutes
- Heart Rate
- Stress Level
- Workout Type
- Mood

The project follows an end-to-end analytics workflow involving data cleaning, feature engineering, machine learning, SQL analysis, and interactive dashboard development.

---

## Dashboard Preview

![Aarogya Drishti Dashboard](images/dashboard.png)

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data cleaning and analysis |
| Pandas | Data manipulation |
| NumPy | Numerical processing |
| Scikit-learn | Machine Learning and clustering |
| Jupyter Notebook | Data analysis environment |
| SQL Server | Data storage and analysis |
| Power BI | Business intelligence dashboard |
| Streamlit | Public interactive dashboard deployment |
| Plotly | Interactive visualizations |

---

## Dataset

The dataset contains wellness and fitness records for users tracked over time.

### Key Features

- User_ID
- Date
- Age
- Gender
- Height
- Weight
- Steps_Taken
- Calories_Burned
- Hours_Slept
- Water_Intake_Liters
- Active_Minutes
- Heart_Rate
- Workout_Type
- Stress_Level
- Mood

Additional features were created during the analysis process, including:

- BMI
- Month
- Day
- Cluster
- Activity_Segment

---

## Project Workflow

```text
Raw Dataset
     ↓
Python Data Cleaning
     ↓
Feature Engineering
(BMI, Month, Day)
     ↓
Exploratory Data Analysis
     ↓
Machine Learning
(K-Means Clustering)
     ↓
Activity Segmentation
     ↓
SQL Server Analysis
     ↓
Power BI Dashboard
     ↓
Streamlit Interactive Dashboard
