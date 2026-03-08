import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(page_title="Machine Health Dashboard",layout="wide")

st.title("Predictive Maintenance Dashboard")

st.write("Next Day Machine Degradation Prediction System")


# ==========================================================
# LOAD DATA
# ==========================================================

df = pd.read_csv("machine_health_report.csv")

st.subheader("Machine Health Table")

st.dataframe(df)


# ==========================================================
# RISK DISTRIBUTION
# ==========================================================

st.subheader("Risk Distribution")

risk_counts = df["Risk_Level"].value_counts()

fig, ax = plt.subplots()

risk_counts.plot(kind="bar",ax=ax)

ax.set_title("Machine Risk Distribution")

st.pyplot(fig)


# ==========================================================
# HEALTH SCORE DISTRIBUTION
# ==========================================================

st.subheader("Health Score Distribution")

fig, ax = plt.subplots()

sns.histplot(df["Health_Score"],bins=20,ax=ax)

ax.set_title("Machine Health Score")

st.pyplot(fig)


# ==========================================================
# TOP RISK MACHINES
# ==========================================================

st.subheader("Top Critical Machines")

critical = df.sort_values("Health_Score")

st.dataframe(critical.head(10))


# ==========================================================
# MACHINE FILTER
# ==========================================================

st.subheader("Machine Analysis")

machine = st.selectbox("Select Machine",df["MachineName"].unique())

machine_df = df[df["MachineName"] == machine]

st.write(machine_df)


# ==========================================================
# ACTION RECOMMENDATION
# ==========================================================

st.subheader("Recommended Actions")

if not machine_df.empty:

    st.write("Operator Action:")
    st.info(machine_df["Operator_Action"].values[0])

    st.write("Shift Incharge Action:")
    st.warning(machine_df["Shift_Incharge_Action"].values[0])

    st.write("Manager Action:")
    st.success(machine_df["Manager_Action"].values[0])