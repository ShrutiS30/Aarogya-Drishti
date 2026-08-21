# Aarogya Drishti

## Personal Wellness Analytics | Python, SQL Server, Machine Learning & Power BI

Aarogya Drishti is an end-to-end data analytics project that analyzes personal wellness and fitness data to uncover meaningful patterns related to physical activity, sleep, stress, calorie expenditure, heart rate, hydration, and workout habits.

The project demonstrates a complete analytics workflow, starting with raw Excel data and progressing through data cleaning, exploratory data analysis, feature engineering, machine learning-based user segmentation, SQL analysis, and interactive dashboard development.

---

## Live Interactive Dashboard

Access the interactive dashboard here:

[**Aarogya Drishti - Open Live Dashboard**](https://aarogya-drishti.netlify.app/)

**Note:** The webpage provides access to the embedded interactive dashboard. Depending on Microsoft Power BI access settings, users may be required to sign in with a Microsoft account.

---

## Dashboard Preview

![Aarogya Drishti Personal Wellness Analytics Dashboard](dashboard.png)

The dashboard provides an interactive overview of key wellness metrics, including:

- Number of users
- Total steps taken
- Total calories burned
- Aggregate stress level
- Total hours slept
- Sleep versus stress analysis
- Distribution of users by activity segment
- Monthly step trends
- Average steps by workout type
- Gender-based filtering

---

# Project Overview

Personal wellness data often contains multiple interconnected variables such as activity levels, sleep duration, calorie expenditure, stress, hydration, and heart rate. Looking at these variables individually makes it difficult to identify broader behavioral patterns.

Aarogya Drishti addresses this by combining multiple analytical techniques into a single workflow.

The project:

1. Processes raw wellness and fitness data using Python.
2. Handles missing values and checks data quality.
3. Creates additional analytical features such as BMI and date-based attributes.
4. Performs exploratory data analysis to identify relationships and trends.
5. Uses K-Means clustering to segment users based on wellness and activity patterns.
6. Analyzes the processed data using SQL Server.
7. Builds an interactive Power BI dashboard for insight exploration.
8. Provides web-based access to the dashboard through Netlify.

The objective is not to provide medical diagnosis or clinical recommendations. The project focuses on **data-driven analysis and visualization of wellness and lifestyle patterns**.

---

# Project Workflow

```text
Raw Wellness Dataset
        │
        ▼
Data Cleaning & Preprocessing
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Feature Engineering
(BMI, Month, Day)
        │
        ▼
Feature Scaling
(StandardScaler)
        │
        ▼
Machine Learning
(K-Means Clustering)
        │
        ▼
Activity Segmentation
        │
        ▼
SQL Server Analysis
        │
        ▼
Power BI Dashboard Development
        │
        ▼
Netlify Hosted Dashboard Access Page
