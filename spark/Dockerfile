FROM bitnami/spark:3.5.0

# --- Versions ---
ARG ICEBERG_VER=1.8.1
ARG SCALA_VER=2.12
ARG SPARK_MAJ=3.5

USER root

# --- Python dependencies & system utils ---
COPY requirements.txt /tmp/requirements.txt
RUN apt-get update && apt-get install -y curl unzip python3-pip gnupg \
    && pip install --no-cache -r /tmp/requirements.txt \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


# --- Iceberg runtime & AWS bundle ---
RUN mkdir -p /opt/bitnami/spark/jars \
    && curl -L -o /opt/bitnami/spark/jars/iceberg-spark-runtime.jar \
       https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-${SPARK_MAJ}_${SCALA_VER}/${ICEBERG_VER}/iceberg-spark-runtime-${SPARK_MAJ}_${SCALA_VER}-${ICEBERG_VER}.jar \
    && curl -L -o /opt/bitnami/spark/jars/iceberg-aws-bundle.jar \
       https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-aws-bundle/${ICEBERG_VER}/iceberg-aws-bundle-${ICEBERG_VER}.jar \
    && chown -R 1001:0 /opt/bitnami/spark/jars

USER 1001
