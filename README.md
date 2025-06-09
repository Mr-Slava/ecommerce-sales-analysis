# ecommerce-sales-analysis

#Ecommerce Sales Analysis & Forecasting

Анализ и прогнозирование продаж интернет-магазина на основе данных о заказах.
Проект демонстрирует ключевые навыки аналитика данных / Data Scientist: очистку, визуализацию, прогнозирование и моделирование оттока клиентов.

Цели проекта:
/ Изучить поведение покупателей и структуру продаж
/ Выявить сезонность, наиболее прибыльные товары и клиентов
/ Построить прогноз продаж
/ Смоделировать вероятность оттока клиента (churn)

Используемые инструменты и библиотеки

| Область               | Инструменты                             |
| --------------------- | --------------------------------------- |
| Язык программирования | Python 3.10                             |
| Обработка данных      | pandas, numpy                           |
| Визуализация          | matplotlib, seaborn                     |
| Моделирование         | scikit-learn, Prophet (или statsmodels) |
| Среда                 | Jupyter Notebook                        |


Структура проекта

ecommerce-analysis-project/

│
├── data/                     # Данные
│   ├── raw/                  # Сырые CSV-файлы
│   └── processed/            # Очистка и агрегаты
│
├── notebooks/                # Анализ в Jupyter
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_forecasting.ipynb
│   └── 04_classification.ipynb
│
├── src/                      # Скрипты и функции
│   └── utils.py
│
├── README.md                 # Описание проекта
└── requirements.txt          # Зависимости


Источник данных
Датасет: Online Retail Dataset from UCI / Kaggle
