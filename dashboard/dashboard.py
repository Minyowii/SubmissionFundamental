import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Bike Sharing Dashboard", layout="wide")
sns.set(style="whitegrid")

# Membaca data bersih
df = pd.read_csv("dashboard/main_data.csv")
df["dteday"] = pd.to_datetime(df["dteday"])

# Sidebar untuk filter interaktif
st.sidebar.header("Filter Data")
min_date = df["dteday"].min()
max_date = df["dteday"].max()

start_date, end_date = st.sidebar.date_input(
    label="Rentang Tanggal",
    min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date]
)

selected_season = st.sidebar.multiselect(
    label="Pilih Musim",
    options=df["season"].unique(),
    default=df["season"].unique()
)

main_df = df[
    (df["dteday"] >= pd.to_datetime(start_date)) &
    (df["dteday"] <= pd.to_datetime(end_date)) &
    (df["season"].isin(selected_season))
]

# Judul dan Ringkasan Metrik
st.title("Bike Sharing Analytics Dashboard")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Penyewaan", f"{main_df['cnt'].sum():,}")
with col2:
    st.metric("Pengguna Registered", f"{main_df['registered'].sum():,}")
with col3:
    st.metric("Pengguna Casual", f"{main_df['casual'].sum():,}")

st.markdown("---")

# Visualisasi 1: Penyewaan berdasarkan Musim
st.subheader("Perbandingan Penyewaan Sepeda Harian Berdasarkan Musim")
daily_season = main_df.groupby(["dteday", "season"])[["casual", "registered"]].sum().reset_index()
season_avg = daily_season.groupby("season")[["casual", "registered"]].mean().reset_index()
season_melted = season_avg.melt(id_vars="season", var_name="Tipe Pengguna", value_name="Rata-rata Penyewaan")

fig1, ax1 = plt.subplots(figsize=(10, 4))
sns.barplot(
    data=season_melted,
    x="season",
    y="Rata-rata Penyewaan",
    hue="Tipe Pengguna",
    palette=["#8ECAE6", "#219EBC"],
    ax=ax1
)
ax1.set_xlabel("Musim")
ax1.set_ylabel("Rata-rata Penyewaan Harian")
st.pyplot(fig1)

# Visualisasi 2: Pola Penyewaan Per Jam
st.subheader("Pola Rata-rata Penyewaan Per Jam: Hari Kerja vs Akhir Pekan/Libur")
hourly_pattern = main_df.groupby(["workingday", "hr"])["cnt"].mean().reset_index()

fig2, ax2 = plt.subplots(figsize=(10, 4))
sns.lineplot(
    data=hourly_pattern,
    x="hr",
    y="cnt",
    hue="workingday",
    marker="o",
    palette=["#FB8500", "#023047"],
    ax=ax2
)
ax2.set_xticks(range(0, 24))
ax2.set_xlabel("Jam (0 - 23)")
ax2.set_ylabel("Rata-rata Penyewaan")
handles, _ = ax2.get_legend_handles_labels()
if len(handles) == 2:
    ax2.legend(handles, ["Akhir Pekan / Libur", "Hari Kerja"], title="Kategori Hari")
st.pyplot(fig2)

# Visualisasi 3: Clustering Kelompok Waktu
st.subheader("Rata-rata Penyewaan Berdasarkan Kelompok Waktu")
waktu_summary = main_df.groupby("kelompok_waktu", observed=False)["cnt"].mean().reset_index()

fig3, ax3 = plt.subplots(figsize=(10, 4))
sns.barplot(data=waktu_summary, x="cnt", y="kelompok_waktu", color="#219EBC", ax=ax3)
ax3.set_xlabel("Rata-rata Penyewaan per Jam")
ax3.set_ylabel("Kelompok Waktu")
st.pyplot(fig3)
