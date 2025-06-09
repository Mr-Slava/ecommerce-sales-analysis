import pandas as pd
from pathlib import Path

# Путь к очищенным данным
DATA_PATH = Path("C:/Python Project/ecommerce-sales-analysis/data/processed/data_clean.csv")


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    return pd.read_csv(path, parse_dates=["InvoiceDate"])

def sales_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
     Возвращает сводку продаж:
    - всего заказов
    - уникальных клиентов
    - суммарную выручку
    """
    return pd.DataFrame({
        "Всего заказов": [df['InvoiceNo'].nunique()],
        "Уникальных клиентов": [df['CustomerID'].nunique()],
        "Суммарная выручка": [df['TotalPrice'].sum()]
    })

def sales_by_country(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """
    Возвращает топ стран по продажам
    """
    return (
        df.groupby('Country')['TotalPrice']
        .sum()
        .sort_values(ascending=True)
        .head(top_n)
        .reset_index()
    )

def sales_by_product(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """
    Возвращает топ товаров по выручке
    """
    return (
        df.groupby('Description')['TotalPrice']
        .sum()
        .sort_values(ascending=True)
        .head(top_n)
        .reset_index()
    )

def export_to_excel(dataframes: dict, filename: str = 'C:/Python Project/ecommerce-sales-analysis/reports/sales_report.xlsx'):
    """
    Сохраняет словарь таблиц (DataFrame) в Excel-файл с разными листами
    """
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        for sheet_name, df in dataframes.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    print(f"Отчёт сохранён: {filename}")