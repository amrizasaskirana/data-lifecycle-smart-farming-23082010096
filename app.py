import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

st.set_page_config(page_title="Smart Farming Dashboard", layout="wide")

st.title("🌱 Smart Farming Sensor Dashboard")

# Load dataset
df = pd.read_csv("Smart_Farming_Crop_Yield_2024.csv")

# ===============================
# Sidebar
# ===============================
st.sidebar.header("Sensor Settings")

threshold = st.sidebar.slider(
    "Soil Moisture Alert Threshold",
    min_value=0,
    max_value=100,
    value=20
)

# ===============================
# Gauge Meter
# ===============================
st.subheader("Current Soil Moisture")

current_moisture = df['soil_moisture_%'].iloc[-1]

fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=current_moisture,
    title={'text': "Soil Moisture (%)"},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "green"},
        'steps': [
            {'range': [0, threshold], 'color': "red"},
            {'range': [threshold, 100], 'color': "lightgreen"}
        ],
    }
))

st.plotly_chart(fig, use_container_width=True)

# ===============================
# Time Series
# ===============================
st.subheader("Soil Moisture Trend Over Time")

daily_avg = df.groupby('total_days')['soil_moisture_%'].mean().reset_index()

fig2, ax = plt.subplots()

ax.plot(
    daily_avg['total_days'],
    daily_avg['soil_moisture_%'],
    marker='o'
)

ax.set_xlabel("Days")
ax.set_ylabel("Average Soil Moisture (%)")

st.pyplot(fig2)

# ===============================
# Heatmap Correlation
# ===============================
st.subheader("Sensor Correlation Heatmap")

corr = df.corr(numeric_only=True)

fig3, ax2 = plt.subplots(figsize=(10,6))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    ax=ax2
)

st.pyplot(fig3)

# ===============================
# Alert System
# ===============================
st.subheader("Soil Moisture Alert System")

df['alert'] = df['soil_moisture_%'] < threshold

fig4, ax3 = plt.subplots()

sns.scatterplot(
    x=df['total_days'],
    y=df['soil_moisture_%'],
    hue=df['alert'],
    palette={True:'red', False:'green'},
    ax=ax3
)

ax3.axhline(threshold, linestyle="--")

st.pyplot(fig4)

# ===============================
# Alert Message
# ===============================

if current_moisture < threshold:
    st.error("⚠️ Soil moisture below threshold! Irrigation needed.")
else:
    st.success("✅ Soil moisture level is normal.")
