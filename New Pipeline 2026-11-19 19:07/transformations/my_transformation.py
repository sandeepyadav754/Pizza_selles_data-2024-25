from pyspark import pipelines as dp
from pyspark.sql.functions import *

file_path = "practiceproject.golddata1.enhanced_pizza_sell_data_2024_25"

@dp.table()
def raw_data():
    return (
        spark.readStream.table(file_path)
    )

@dp.materialized_view()
@dp.expect("valid_order ID", "Order_ID IS NOT NULL")
def silver_data_new():
    return (
        spark.read.table("raw_data")
    )

@dp.materialized_view()
def gold_data_new():
    return (
        spark.read.table("silver_data_new")
    )