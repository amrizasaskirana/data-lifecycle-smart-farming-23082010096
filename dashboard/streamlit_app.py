import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import os

st.set_page_config(page_title="Smart Farming Business Dashboard", layout="wide")

# ===============================
# HEADER
# ===============================
st.title("🌱 Smart Farming Business Intelligence Dashboard")

st.markdown("""
Dashboard ini digunakan untuk **monitoring kondisi lahan pertanian secara real-time** berdasarkan data sensor.

Dashboard membantu pengelola lahan dalam:
- Mengontrol **kelembaban tanah**
- Mendeteksi **kebutuhan irigasi**
- Menganalisis **korelasi antar sensor**
- Melihat **tren kondisi lahan**
""")

# ===============================
# LOAD DATASET
# ===============================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "..", "data", "raw", "Smart_Farming_Crop_Yield_2024.csv")

df = pd.read_csv(data_path)

# ===============================
# SIDEBAR CONTROL
# ===============================
st.sidebar.header("⚙️ Monitoring Settings")

threshold = st.sidebar.slider(
    "Soil Moisture Alert Threshold (%)",
    0,
    100,
    20
)

# ===============================
# KPI DASHBOARD
# ===============================
st.subheader("📊 Farm Performance Overview")

col1, col2, col3, col4 = st.columns(4)

current_moisture = df['soil_moisture_%'].iloc[-1]
avg_moisture = df['soil_moisture_%'].mean()
min_moisture = df['soil_moisture_%'].min()
max_moisture = df['soil_moisture_%'].max()

col1.metric("Current Moisture", f"{current_moisture:.1f}%")
col2.metric("Average Moisture", f"{avg_moisture:.1f}%")
col3.metric("Lowest Moisture", f"{min_moisture:.1f}%")
col4.metric("Highest Moisture", f"{max_moisture:.1f}%")

st.divider()

# ===============================
# GAUGE + TREND
# ===============================
col1, col2 = st.columns(2)

with col1:

    st.subheader("💧 Current Soil Moisture Status")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=current_moisture,
        title={'text': "Soil Moisture (%)"},
        gauge={
            'axis': {'range': [0,100]},
            'bar': {'color': "green"},
            'steps': [
                {'range': [0, threshold], 'color': "red"},
                {'range': [threshold, 100], 'color': "lightgreen"}
            ],
        }
    ))

    st.plotly_chart(fig, use_container_width=True)

with col2:

    st.subheader("📈 Soil Moisture Trend")

    daily_avg = df.groupby("total_days")["soil_moisture_%"].mean().reset_index()

    fig2 = px.line(
        daily_avg,
        x="total_days",
        y="soil_moisture_%",
        markers=True,
        title="Daily Soil Moisture Trend"
    )

    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ===============================
# ALERT SYSTEM
# ===============================
st.subheader("🚨 Irrigation Alert Monitoring")

df['alert'] = df['soil_moisture_%'] < threshold

fig3 = px.scatter(
    df,
    x="total_days",
    y="soil_moisture_%",
    color="alert",
    color_discrete_map={
        True:"red",
        False:"green"
    },
    title="Soil Moisture Alert Detection"
)

fig3.add_hline(y=threshold, line_dash="dash")

st.plotly_chart(fig3, use_container_width=True)

st.divider()

# ===============================
# HEATMAP SENSOR
# ===============================
st.subheader("🔥 Sensor Relationship Analysis")

corr = df.corr(numeric_only=True)

fig4, ax = plt.subplots(figsize=(10,6))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    ax=ax
)

st.pyplot(fig4)

st.divider()

# ===============================
# BUSINESS INSIGHT
# ===============================
st.subheader("📌 Farm Insight & Recommendation")

if current_moisture < threshold:

    st.error("""
⚠️ **Low Soil Moisture Detected**

Recommendation:
- Activate irrigation system
- Monitor moisture level frequently
- Check rainfall forecast
""")

else:

    st.success("""
✅ **Soil Moisture Within Optimal Range**

Recommendation:
- No irrigation required
- Continue daily monitoring
""")

st.divider()

# ===============================
# DATASET PREVIEW
# ===============================
st.subheader("📂 Dataset Preview")

st.markdown("""
Bagian ini menampilkan **cuplikan dataset sensor** yang digunakan untuk analisis dashboard.
Dataset berisi data pengamatan kondisi tanah pada beberapa hari.
""")

col1, col2 = st.columns(2)

col1.write("Total Rows:", df.shape[0])
col2.write("Total Columns:", df.shape[1])

show_data = st.checkbox("Show Raw Dataset")

if show_data:
    st.dataframe(df, use_container_width=True)