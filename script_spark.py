from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("IcebergTest") \
    .getOrCreate()

# Crea la tabla si no existe
spark.sql("""
    CREATE TABLE IF NOT EXISTS demo.default.test_from_python (
        id INT,
        nombre STRING
    )
    USING iceberg
""")

# Inserta datos
spark.sql("""
    INSERT INTO demo.default.test_from_python VALUES
        (1, 'Carlos'),
        (2, 'Lucía')
""")

# Consulta los datos
df = spark.sql("SELECT * FROM demo.default.test_from_python")
df.show()
