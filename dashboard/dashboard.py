import streamlit as st  
import plotly.express as px  
import pandas as pd  

# Load data  
df = pd.read_csv(r"dashboard/main_data.csv")  # Ganti "bike_sharing.csv" dengan nama file Anda  

# Mapping angka ke nama hari jika diperlukan
weekday_mapping = {"Mon": "Monday", "Tues": "Tuesday", "Wed": "Wednesday", "Thurs": "Thursday", "Fri": "Friday", "Sat": "Saturday", "Sun": "Sunday"}
df['weekday'] = df['weekday'].map(weekday_mapping)

# Sidebar filter hanya ada 2 opsi
selected_option = st.sidebar.radio("Pilih Pertanyaan:", ("Pertanyaan 1", "Pertanyaan 2"))

if selected_option == "Pertanyaan 1":
    st.header("Pertanyaan 1: Bagaimana pola rata-rata jumlah pengguna sepeda (casual dan registered) sepanjang hari dalam seminggu?")
    
    # Pemrosesan data untuk Pertanyaan 1
    df_filtered_q1 = df.groupby(['weekday', 'hour'])[['count', 'casual', 'registered']].mean().reset_index()


    # Grafik 1: Jumlah sepeda per jam berdasarkan hari
    fig = px.line(
        df_filtered_q1,
        x='hour',
        y='count',
        color='weekday',
        title='Count of Bikes during weekdays and weekends',
        markers=True
    )
    fig.update_layout(
        xaxis_title='Hour of the Day',
        yaxis_title='Average Count of Bikes',
        legend_title='Day of the Week',
        template='plotly_white',
        width=1000,
        height=500
    )
    st.plotly_chart(fig)

    st.markdown("**Insight:**")
    st.markdown("""
    - Terdapat dua puncak utama setiap hari: pada pagi hari sekitar pukul 7-8 dan sore hari sekitar pukul 17-18.
    - Aktivitas pengguna sepeda meningkat tajam pada jam sibuk pagi dan sore hari, terutama pada hari kerja (Senin-Jumat).
    - Pada akhir pekan (Sabtu dan Minggu), aktivitas lebih tinggi pada siang hari dibandingkan pagi hari, dengan distribusi yang lebih merata tanpa puncak yang tajam.
    """)

    # Grafik 2: Casual Users
    fig = px.line(
        df_filtered_q1,
        x='hour',
        y='casual',
        color='weekday',
        title='Count of bikes during weekdays and weekends: Unregistered users',
        markers=True
    )
    fig.update_layout(
        xaxis_title='Hour of the Day',
        yaxis_title='Average Casual Users',
        legend_title='Day of the Week',
        template='plotly_white',
        width=1000,
        height=500
    )
    st.plotly_chart(fig)

    st.markdown("**Insight:**")
    st.markdown("""
    - Aktivitas pengguna casual lebih tinggi pada akhir pekan, dengan puncak aktivitas terjadi di siang hari sekitar pukul 12-15.
    - Pada hari kerja, penggunaan cenderung rendah sepanjang hari, tanpa puncak signifikan.
    """)

    # Grafik 3: Registered Users
    fig = px.line(
        df_filtered_q1,
        x='hour',
        y='registered',
        color='weekday',
        title='Count of bikes during weekdays and weekends: Registered users',
        markers=True
    )
    fig.update_layout(
        xaxis_title='Hour of the Day',
        yaxis_title='Average Registered Users',
        legend_title='Day of the Week',
        template='plotly_white',
        width=1000,
        height=500
    )
    st.plotly_chart(fig)

    st.markdown("**Insight:**")
    st.markdown("""
    - Aktivitas pengguna terdaftar sangat terfokus pada jam sibuk pagi (7-8) dan sore (17-18) di hari kerja.
    - Aktivitas menurun pada akhir pekan, dengan distribusi yang lebih merata sepanjang hari.
    """)

    st.header("**Conclusion:**")
    st.markdown("""
    - Pengguna sepeda terdaftar lebih aktif pada jam sibuk hari kerja, sedangkan pengguna casual lebih aktif di akhir pekan pada siang hari.
    - Kondisi ini menunjukkan bahwa pengguna terdaftar cenderung lebih terikat pada rutinitas kerja, sedangkan pengguna casual lebih fleksibel dengan pola waktu yang lebih merata.
    """)

elif selected_option == "Pertanyaan 2":
    st.header("Pertanyaan 2: Bagaimana pengaruh kondisi cuaca dan musim terhadap rata-rata jumlah pengguna sepeda per jam?")

    # Pemrosesan data untuk Pertanyaan 2
    df_filtered_q2 = df.groupby(['weather', 'hour'])['count'].mean().reset_index()
    
    # Grafik 1: Pengaruh Cuaca terhadap Jumlah Pengguna Sepeda
    fig = px.line(
        df_filtered_q2,
        x='hour',
        y='count',
        color='weather',
        title='Count of bikes during different weathers',
        markers=True
    )
    fig.update_layout(
        xaxis_title='Hour of the Day',
        yaxis_title='Average Count of Bikes',
        legend_title='Weather Condition',
        template='plotly_white',
        width=1000,
        height=500
    )
    st.plotly_chart(fig)

    st.markdown("**Insight:**")
    st.markdown("""
    - Pada cuaca clear (cerah), jumlah pengguna sepeda tertinggi sepanjang hari, terutama selama jam sibuk.
    - Cuaca cloudy (berawan) juga menunjukkan pola penggunaan tinggi, tetapi sedikit lebih rendah dibandingkan cuaca cerah.
    - Pada kondisi light rain (hujan ringan), penggunaan sepeda menurun secara signifikan di sepanjang hari.
    - Kondisi heavy rain (hujan lebat) hampir tidak menunjukkan aktivitas pengguna sepeda, terutama pada jam-jam sore hari.
    """)

    # Pemrosesan data untuk musim
    df_filtered_q2_season = df.groupby(['season', 'hour'])['count'].mean().reset_index()

    # Grafik 2: Pengaruh Musim terhadap Jumlah Pengguna Sepeda
    fig = px.line(
        df_filtered_q2_season,
        x='hour',
        y='count',
        color='season',
        title='Count of bikes during different seasons',
        markers=True
    )
    fig.update_layout(
        xaxis_title='Hour of the Day',
        yaxis_title='Average Count of Bikes',
        legend_title='Season',
        template='plotly_white',
        width=1000,
        height=500
    )
    st.plotly_chart(fig)

    st.markdown("**Insight:**")
    st.markdown("""
    - Pada musim spring, penggunaan sepeda lebih rendah dibandingkan musim lainnya di sepanjang hari.
    - Puncak penggunaan sepeda terjadi pada jam sibuk (07:00-09:00 dan 17:00-19:00) dengan jumlah pengguna tertinggi di musim fall dan summer.
    - Setelah jam sibuk pagi, pola penggunaan menurun secara signifikan, tetapi kembali meningkat menjelang sore.
    - Musim winter memiliki pola yang mirip dengan fall dan summer tetapi dengan sedikit lebih sedikit pengguna.
    """)

    st.header("**Conclusion:**")
    st.markdown("""
    - Kondisi cuaca dan musim sangat mempengaruhi jumlah pengguna sepeda, dengan cuaca cerah dan musim fall serta summer menunjukkan puncak tertinggi.
    - Hujan dan musim spring mengurangi jumlah pengguna sepeda secara signifikan.
    - Pengguna sepeda cenderung lebih aktif selama jam sibuk, tetapi cuaca buruk dan musim tertentu mengurangi aktivitas sepeda secara keseluruhan.
    """)
