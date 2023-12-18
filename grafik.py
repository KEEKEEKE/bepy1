import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Пример данных о расписании контейнерных поездов
data = {
    'Номер поезда': [101, 102, 103, 104],
    'Отправление': [datetime(2023, 1, 1, 8, 0), datetime(2023, 1, 1, 10, 30), datetime(2023, 1, 1, 15, 45), datetime(2023, 1, 1, 18, 20)],
    'Прибытие': [datetime(2023, 1, 1, 12, 0), datetime(2023, 1, 1, 14, 30), datetime(2023, 1, 1, 19, 45), datetime(2023, 1, 1, 22, 10)],
    'Отправление из': ['Грузовой станции A', 'Грузовой станции B', 'Грузовой станции C', 'Грузовой станции D'],
    'Прибытие в': ['Грузовую станцию X', 'Грузовую станцию Y', 'Грузовую станцию Z', 'Грузовую станцию W'],
}

df = pd.DataFrame(data)

def rasp():
    st.title("Расписание контейнерных поездов BALTIJAS EKSPRESIS")

    # Отображение таблицы
    st.dataframe(df)

if __name__ == "__main__":
    rasp()