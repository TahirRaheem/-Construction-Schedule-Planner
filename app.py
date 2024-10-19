import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import timedelta

# Function to create Gantt chart
def create_gantt_chart(df):
    fig = px.timeline(df, x_start="Start Date", x_end="End Date", y="Task",
                      color="Task", title="Construction Schedule Planner",
                      labels={"Task": "Construction Activities"})
    fig.update_yaxes(categoryorder="total ascending")  # Sort tasks
    fig.update_layout(xaxis_title="Timeline", yaxis_title="Task")
    return fig

# Streamlit app layout
st.title("Construction Schedule Planner")

# Input form for project tasks
st.header("Input Project Tasks")

with st.form("schedule_form"):
    num_tasks = st.number_input("Number of tasks", min_value=1, max_value=20, value=5)
    
    tasks = []
    start_dates = []
    end_dates = []
    
    for i in range(num_tasks):
        st.subheader(f"Task {i+1}")
        task_name = st.text_input(f"Task Name {i+1}", value=f"Task {i+1}")
        start_date = st.date_input(f"Start Date {i+1}")
        duration = st.number_input(f"Duration (days) for Task {i+1}", min_value=1, value=7)
        end_date = pd.to_datetime(start_date) + timedelta(days=duration)
        
        tasks.append(task_name)
        start_dates.append(start_date)
        end_dates.append(end_date)
    
    # Submit button to create the Gantt chart
    submitted = st.form_submit_button("Create Schedule")

# When the form is submitted, display the Gantt chart
if submitted:
    # Create a DataFrame with the inputted tasks and dates
    data = {
        "Task": tasks,
        "Start Date": start_dates,
        "End Date": end_dates
    }
    df = pd.DataFrame(data)
    
    # Display Gantt chart
    st.header("Gantt Chart")
    gantt_chart = create_gantt_chart(df)
    st.plotly_chart(gantt_chart)

    # Display task data in table format
    st.header("Task Schedule Data")
    st.dataframe(df)
