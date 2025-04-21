

# ────────────────────────────────────────────────────────────────
#  Spark + Iceberg (Bitnami) – GPG bypass
# ────────────────────────────────────────────────────────────────
FROM bitnami/spark:3.5.0

# ─ Vars de versión
ARG ICEBERG_VER=1.8.1
ARG SPARK_MAJ=3.5
ARG SCALA_VER=2.12

USER root

# ─ (1)  Desactivar verificación de firmas APT  ───────────────────
RUN echo 'Acquire::AllowUnauthenticated "true";' > /etc/apt/apt.conf.d/99insecure

# ─ (2)  Instalar dependencias + Python libs  ─────────────────────
COPY requirements.txt /tmp/requirements.txt
RUN apt-get update \
 && apt-get install -y curl unzip python3-pip gnupg \
 && pip install --no-cache-dir -r /tmp/requirements.txt \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# ─ (3)  Descargar JARs de Iceberg (runtime + AWS bundle) ─────────
RUN mkdir -p /opt/bitnami/spark/jars \
 && curl -L -o /opt/bitnami/spark/jars/iceberg-spark-runtime.jar \
      https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-${SPARK_MAJ}_${SCALA_VER}/${ICEBERG_VER}/iceberg-spark-runtime-${SPARK_MAJ}_${SCALA_VER}-${ICEBERG_VER}.jar \
 && curl -L -o /opt/bitnami/spark/jars/iceberg-aws-bundle.jar \
      https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-aws-bundle/${ICEBERG_VER}/iceberg-aws-bundle-${ICEBERG_VER}.jar \
 && chown -R 1001:0 /opt/bitnami/spark/jars

 # vuelve al user no‑root de Bitnami
USER 1001   

