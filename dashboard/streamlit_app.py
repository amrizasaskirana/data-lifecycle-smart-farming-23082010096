import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import os

st.set_page_config(page_title="Smart Farming Dashboard", layout="wide")

# ===============================
# Header
# ===============================
st.title("🌱 Smart Farming Monitoring Dashboard")
st.markdown("Dashboard ini menampilkan monitoring sensor pertanian seperti **soil moisture**, tren sensor, korelasi antar sensor, serta sistem peringatan untuk membantu pengambilan keputusan irigasi.")

# ===============================
# Load Dataset
# ===============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "..", "data", "raw", "Smart_Farming_Crop_Yield_2024.csv")

df = pd.read_csv(data_path)

# ===============================
# Sidebar
# ===============================
st.sidebar.header("⚙️ Sensor Settings")

threshold = st.sidebar.slider(
    "Soil Moisture Alert Threshold",
    min_value=0,
    max_value=100,
    value=20
)

# ===============================
# Key Metrics
# ===============================
st.subheader("📊 Current Sensor Summary")

col1, col2, col3 = st.columns(3)

current_moisture = df['soil_moisture_%'].iloc[-1]
avg_moisture = df['soil_moisture_%'].mean()
max_moisture = df['soil_moisture_%'].max()

col1.metric("Current Soil Moisture", f"{current_moisture:.2f}%")
col2.metric("Average Soil Moisture", f"{avg_moisture:.2f}%")
col3.metric("Maximum Soil Moisture", f"{max_moisture:.2f}%")

st.divider()

# ===============================
# Layout 2 Columns
# ===============================
left, right = st.columns(2)

# ===============================
# Gauge Meter
# ===============================
with left:
    st.subheader("🌡 Current Soil Moisture Gauge")

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
# Time Series Trend
# ===============================
with right:
    st.subheader("📈 Soil Moisture Trend Over Time")

    daily_avg = df.groupby('total_days')['soil_moisture_%'].mean().reset_index()

    fig2 = px.line(
        daily_avg,
        x="total_days",
        y="soil_moisture_%",
        markers=True,
        labels={
            "total_days": "Days",
            "soil_moisture_%": "Average Soil Moisture (%)"
        }
    )

    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ===============================
# Heatmap Correlation
# ===============================
st.subheader("🔥 Sensor Correlation Heatmap")

corr = df.corr(numeric_only=True)

fig3, ax = plt.subplots(figsize=(10,6))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    ax=ax
)

st.pyplot(fig3)

st.divider()

# ===============================
# Alert System
# ===============================
st.subheader("🚨 Soil Moisture Alert System")

df['alert'] = df['soil_moisture_%'] < threshold

fig4 = px.scatter(
    df,
    x="total_days",
    y="soil_moisture_%",
    color="alert",
    color_discrete_map={True: "red", False: "green"},
    labels={
        "total_days": "Days",
        "soil_moisture_%": "Soil Moisture (%)",
        "alert": "Alert Status"
    }
)

fig4.add_hline(y=threshold, line_dash="dash")

st.plotly_chart(fig4, use_container_width=True)

# ===============================
# Alert Message
# ===============================
if current_moisture < threshold:
    st.error("⚠️ Soil moisture below threshold! Irrigation needed.")
else:
    st.success("✅ Soil moisture level is normal.")