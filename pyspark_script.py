from pyspark.sql import SparkSession

# Создаем единую SparkSession
spark = SparkSession.builder \
    .appName("ClickHouse and PostgreSQL") \
    .config("spark.jars", "clickhouse-jdbc-0.7.1.jar,postgresql-42.2.23.jar") \
    .getOrCreate()

# Подключение к ClickHouse
CLICKHOUSE_URL = "jdbc:clickhouse://localhost:8123/default"
CLICKHOUSE_USER = "admin"
CLICKHOUSE_PASSWORD = "password"

clickhouse_df = spark.read \
    .format("jdbc") \
    .option("url", CLICKHOUSE_URL) \
    .option("dbtable", "users") \
    .option("user", CLICKHOUSE_USER) \
    .option("password", CLICKHOUSE_PASSWORD) \
    .option("driver", "com.clickhouse.jdbc.ClickHouseDriver") \
    .load()

# Подключение к PostgreSQL
POSTGRES_JDBC_URL = "jdbc:postgresql://localhost:5433/test_db"
POSTGRES_USER = "postgres"
POSTGRES_PASSWORD = "password"

postgres_df = spark.read \
    .format("jdbc") \
    .option("url", POSTGRES_JDBC_URL) \
    .option("dbtable", "users") \
    .option("user", POSTGRES_USER) \
    .option("password", POSTGRES_PASSWORD) \
    .option("driver", "org.postgresql.Driver") \
    .load()

# Пример объединения данных
result_df = clickhouse_df.union(postgres_df)

# Печать объединенных данных
result_df.show()

# Остановка SparkSession
spark.stop()
