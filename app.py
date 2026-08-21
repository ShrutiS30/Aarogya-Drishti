import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Aarogya Drishti",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp {
    background-color: #183563;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1450px;
}

/* Hide default Streamlit elements */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Title */
.main-title {
    color: white;
    font-size: 48px;
    font-family: Georgia, serif;
    font-weight: 700;
    letter-spacing: 1px;
    line-height: 1;
}

.subtitle {
    color: white;
    font-size: 20px;
    font-family: Georgia, serif;
    margin-top: 8px;
    margin-bottom: 25px;
}

/* KPI Cards */
.kpi-card {
    background: linear-gradient(135deg, #f8f8f8, #e6e7eb);
    border-radius: 3px;
    padding: 18px;
    margin-bottom: 14px;
    min-height: 85px;
    box-shadow: 0px 2px 5px rgba(0,0,0,0.18);
}

.kpi-value {
    color: #454545;
    font-size: 28px;
    font-weight: 700;
    line-height: 1.2;
}

.kpi-label {
    color: #666666;
    font-size: 14px;
    margin-top: 5px;
}

/* Make charts fit nicely */
div[data-testid="stPlotlyChart"] {
    background-color: #f4f4f4;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():
    df = pd.read_csv("HealthPulse_Final_Data.csv")

    df["Date"] = pd.to_datetime(df["Date"])

    return df


df = load_data()


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.markdown(
    '<div class="main-title">AAROGYA DRISHTI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Personal Wellness Analytics Dashboard</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# MAIN DASHBOARD LAYOUT
# --------------------------------------------------

left_col, right_col = st.columns([1, 4], gap="medium")


# ==================================================
# LEFT SIDE - KPIs
# ==================================================

with left_col:

    # Gender Filter
    st.markdown(
        "<h4 style='color:white; margin-bottom:5px;'>Gender</h4>",
        unsafe_allow_html=True
    )

    gender_options = sorted(df["Gender"].dropna().unique())

    selected_gender = st.radio(
        "",
        gender_options,
        horizontal=True,
        label_visibility="collapsed"
    )

    # Filter data
    filtered_df = df[df["Gender"] == selected_gender].copy()

    # Calculate KPIs
    total_users = filtered_df["User_ID"].nunique()
    total_steps = filtered_df["Steps_Taken"].sum()
    total_calories = filtered_df["Calories_Burned"].sum()
    total_stress = filtered_df["Stress_Level (1-10)"].sum()
    total_sleep = filtered_df["Hours_Slept"].sum()

    # KPI Card Function
    def show_kpi(value, label):

        st.markdown(
            f"""
            <div class="kpi-card">
                <div class="kpi-value">{value}</div>
                <div class="kpi-label">{label}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    show_kpi(
        f"{total_users}",
        "Number of Users"
    )

    show_kpi(
        f"{total_steps / 1_000_000:.0f}M",
        "Sum of Steps Taken"
    )

    show_kpi(
        f"{total_calories / 1_000_000:.0f}M",
        "Sum of Calories Burned"
    )

    show_kpi(
        f"{total_stress / 1_000:.0f}K",
        "Sum of Stress Level"
    )

    show_kpi(
        f"{total_sleep / 1_000:.2f}K",
        "Sum of Hours Slept"
    )


# ==================================================
# RIGHT SIDE - CHARTS
# ==================================================

with right_col:

    # ----------------------------------------------
    # TOP ROW - THREE CHARTS
    # ----------------------------------------------

    chart1, chart2, chart3 = st.columns(3, gap="small")

    # ==============================================
    # SLEEP VS STRESS LEVEL
    # ==============================================

    with chart1:

        sleep_stress = (
            filtered_df
            .groupby("Stress_Level (1-10)", as_index=False)
            ["Hours_Slept"]
            .mean()
        )

        fig_sleep = px.scatter(
            sleep_stress,
            x="Stress_Level (1-10)",
            y="Hours_Slept",
            title="Sleep v/s Stress Level"
        )

        fig_sleep.update_traces(
            marker=dict(
                size=10,
                color="#234d7d"
            )
        )

        fig_sleep.update_layout(
            height=300,
            paper_bgcolor="#f4f4f4",
            plot_bgcolor="#f4f4f4",
            font=dict(color="#444444"),
            margin=dict(l=40, r=20, t=50, b=40),
            title=dict(
                font=dict(size=17)
            ),
            xaxis_title="Stress Level",
            yaxis_title="Average Hours Slept"
        )

        st.plotly_chart(
            fig_sleep,
            use_container_width=True,
            config={"displayModeBar": False}
        )


    # ==============================================
    # ACTIVITY SEGMENT DISTRIBUTION
    # ==============================================

    with chart2:

        activity_data = (
            filtered_df["Activity_Segment"]
            .value_counts()
            .reset_index()
        )

        activity_data.columns = [
            "Activity Segment",
            "Count"
        ]

        fig_activity = px.pie(
            activity_data,
            names="Activity Segment",
            values="Count",
            hole=0.55,
            title="User by Activity Level",
            color_discrete_sequence=[
                "#1F77B4",
                "#254F7E",
                "#65A9B9"
            ]
        )

        fig_activity.update_layout(
            height=300,
            paper_bgcolor="#f4f4f4",
            font=dict(color="#444444"),
            margin=dict(l=10, r=10, t=50, b=10),
            title=dict(
                font=dict(size=17)
            ),
            legend=dict(
                font=dict(size=10)
            )
        )

        st.plotly_chart(
            fig_activity,
            use_container_width=True,
            config={"displayModeBar": False}
        )


    # ==============================================
    # MONTHLY STEPS TREND
    # ==============================================

    with chart3:

        month_order = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]

        monthly_steps = (
            filtered_df
            .groupby("Month", as_index=False)
            ["Steps_Taken"]
            .sum()
        )

        monthly_steps["Month"] = pd.Categorical(
            monthly_steps["Month"],
            categories=month_order,
            ordered=True
        )

        monthly_steps = monthly_steps.sort_values("Month")

        fig_month = px.line(
            monthly_steps,
            x="Month",
            y="Steps_Taken",
            title="Monthly Steps Trend"
        )

        fig_month.update_traces(
            line=dict(
                color="#234d7d",
                width=3
            ),
            marker=dict(size=6)
        )

        fig_month.update_layout(
            height=300,
            paper_bgcolor="#f4f4f4",
            plot_bgcolor="#f4f4f4",
            font=dict(color="#444444"),
            margin=dict(l=40, r=20, t=50, b=55),
            title=dict(
                font=dict(size=17)
            ),
            xaxis_title="Month",
            yaxis_title="Sum of Steps Taken"
        )

        st.plotly_chart(
            fig_month,
            use_container_width=True,
            config={"displayModeBar": False}
        )


    # ----------------------------------------------
    # BOTTOM ROW
    # ----------------------------------------------

    bottom_left, bottom_right = st.columns([2.2, 1], gap="small")

    # ==============================================
    # AVERAGE STEPS BY WORKOUT
    # ==============================================

    with bottom_left:

        workout_steps = (
            filtered_df
            .groupby("Workout_Type", as_index=False)
            ["Steps_Taken"]
            .mean()
            .sort_values("Steps_Taken")
        )

        fig_workout = px.bar(
            workout_steps,
            x="Steps_Taken",
            y="Workout_Type",
            orientation="h",
            title="Average Steps by Workout"
        )

        fig_workout.update_traces(
            marker_color="#234d7d"
        )

        fig_workout.update_layout(
            height=300,
            paper_bgcolor="#f4f4f4",
            plot_bgcolor="#f4f4f4",
            font=dict(color="#444444"),
            margin=dict(l=50, r=20, t=50, b=40),
            title=dict(
                font=dict(size=17)
            ),
            xaxis_title="Average Steps Taken",
            yaxis_title="Workout Type"
        )

        st.plotly_chart(
            fig_workout,
            use_container_width=True,
            config={"displayModeBar": False}
        )


    # ==============================================
    # GENDER FILTER PANEL
    # ==============================================

    with bottom_right:

        st.markdown(
            """
            <div style="
                background:#f4f4f4;
                padding:20px;
                min-height:300px;
            ">
                <h3 style="
                    color:#444444;
                    margin-bottom:20px;
                ">
                    Gender
                </h3>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div style="
                background:#234d7d;
                color:white;
                padding:18px;
                text-align:center;
                font-size:18px;
                font-weight:bold;
                margin-bottom:10px;
            ">
                {selected_gender}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("</div>", unsafe_allow_html=True)
