from src import report

df = report.load_data()

# Создаем сводки
summary = report.sales_summary(df)
top_countries = report.sales_by_country(df)
top_products = report.sales_by_product(df)

# Собираем их в словарь
report_data = {
    "Общая сводка": summary,
    "Страны": top_countries,
    "Товары": top_products
}

# Экспортируем в Excel
report.export_to_excel(report_data)