import streamlit as st  
import plotly.express as px  
import pandas as pd  
  
# Load data  
df = pd.read_csv("main_data.csv")  # Ganti "bike_sharing.csv" dengan nama file Anda  
  
# Mapping angka ke nama hari jika diperlukan
weekday_mapping = {"Mon": "Monday", "Tues": "Tuesday", "Wed": "Wednesday", "Thurs": "Thursday", "Fri": "Friday", "Sat": "Saturday", "Sun": "Sunday"}
df['weekday'] = df['weekday'].map(weekday_mapping)

# Sidebar filter untuk memilih weekday, rentang jam, year, season, dan weather
if st.sidebar.checkbox("Select All Days", value=True):
    selected_weekdays = df['weekday'].unique()
else:
    selected_weekdays = st.sidebar.multiselect(
        "Select Days of the Week:", options=df['weekday'].unique(), default=df['weekday'].unique()
    )

hour_range = st.sidebar.slider(
    "Select Hour Range:", min_value=int(df['hour'].min()), max_value=int(df['hour'].max()), value=(0, 23)
)

if st.sidebar.checkbox("Select All Years", value=True):
    selected_years = df['year'].unique()
else:
    selected_years = st.sidebar.multiselect(
        "Select Year:", options=df['year'].unique(), default=df['year'].unique()
    )

if st.sidebar.checkbox("Select All Seasons", value=True):
    selected_seasons = df['season'].unique()
else:
    selected_seasons = st.sidebar.multiselect(
        "Select Season:", options=df['season'].unique(), default=df['season'].unique()
    )

if st.sidebar.checkbox("Select All Weather Conditions", value=True):
    selected_weather = df['weather'].unique()
else:
    selected_weather = st.sidebar.multiselect(
        "Select Weather:", options=df['weather'].unique(), default=df['weather'].unique()
    )

# Filter data sesuai pilihan user
df_filtered = df[(df['weekday'].isin(selected_weekdays)) &
                 (df['hour'].between(hour_range[0], hour_range[1])) &
                 (df['year'].isin(selected_years)) &
                 (df['season'].isin(selected_seasons)) &
                 (df['weather'].isin(selected_weather))]

# Mengelompokkan data berdasarkan weekday dan hour, menghitung rata-rata setelah filter diterapkan
df_aggregated = df_filtered.groupby(['weekday', 'hour'])['count'].mean().reset_index()

# Membuat plot interaktif
fig = px.line(
    df_aggregated,
    x='hour',
    y='count',
    color='weekday',
    title='Count of Bikes by Hour and Day of the Week',
    markers=True
)

# Kustomisasi layout
fig.update_layout(
    xaxis_title='Hour of the Day',
    yaxis_title='Average Count of Bikes',
    legend_title='Day of the Week',
    template='plotly_white',
    width=1000,
    height=500
)

# Menampilkan plot
st.plotly_chart(fig)
