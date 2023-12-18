import streamlit as st
import pandas as pd

def main():
    st.title("Отображение таблицы ")

    # Загрузка данных
    file = st.file_uploader("Выберите файл с таблицей (CSV, Excel, etc.)", type=["csv", "xlsx"])

    if file is not None:
        # Чтение данных
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.name.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file, engine='openpyxl')
        
        # Отображение таблицы
        st.dataframe(df)

if __name__ == "__main__":
    main()
