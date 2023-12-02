import pandas as pd
import openpyxl
import pytz
import datetime
import calendar


def get_end_epoch(year, month, timezone='UTC'):
    last_day = calendar.monthrange(year, month)[1]
    end_of_month_naive = datetime.datetime(year, month, last_day, 23, 59, 59)
    timezone_aware = pytz.timezone(timezone).localize(end_of_month_naive)
    return int(timezone_aware.timestamp())


def generate_sql_insert(file_path, slug, brand_value, year, month):
    df = pd.read_excel(file_path)
    today_epoch = int(datetime.datetime.now().timestamp())
    end_epoch = get_end_epoch(year, month)

    for index, row in df.iterrows():
        country_lower = row['Country'].lower()
        language_lower = row['Language'].lower()
        price_formatted = "{:.2f}".format(row['Discount Amount'])
        sql = f"INSERT INTO promo_offers (promo_seo_code, brand, country, language, name, price, uom, promo_offer_img, number_of_redemptions, redeem_by, startdate, enddate, status, creation) VALUES ('{slug}', '{brand_value}', '{country_lower}', '{language_lower}', '{row['Product Name']}', {price_formatted}, '{row['UOM']}', NULL, {row['Redemption Limit']}, '{row['End Date']}', '{today_epoch}', '{end_epoch}', 4, '{today_epoch}';"
        print(sql)


file_path = 'file_name'
slug = "slug_name"
brand_value = 'brand'
generate_sql_insert(file_path, slug, brand_value, 2023, 12)