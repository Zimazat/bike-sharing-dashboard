import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# =========================
# Load Data
# =========================
df = pd.read_csv("main_data.csv")

# =========================
# Judul Dashboard
# =========================
st.title("Dashboard Penyewaan Sepeda")

# =========================
# Filter Interaktif
# =========================
selected_weather = st.selectbox(
    "Pilih Kondisi Cuaca",
    df["weathersit"].unique()
)

filtered_df = df[df["weathersit"] == selected_weather]

# =========================
# Grafik 1: Rata-rata per Bulan
# =========================
monthly_avg = filtered_df.groupby("mnth")["cnt"].mean()

st.subheader("Rata-rata Penyewaan Sepeda per Bulan")

fig1, ax1 = plt.subplots()
ax1.plot(monthly_avg.index, monthly_avg.values)
ax1.set_xlabel("Bulan")
ax1.set_ylabel("Rata-rata Penyewaan")
st.pyplot(fig1)
plt.close()

# =========================
# Grafik 2: Rata-rata Berdasarkan Cuaca
# =========================
weather_avg = filtered_df.groupby("weathersit")["cnt"].mean()

st.subheader("Rata-rata Penyewaan Berdasarkan Kondisi Cuaca")

fig2, ax2 = plt.subplots()
ax2.bar(weather_avg.index, weather_avg.values)
ax2.set_xlabel("Kondisi Cuaca")
ax2.set_ylabel("Rata-rata Penyewaan")
st.pyplot(fig2)
plt.close()




