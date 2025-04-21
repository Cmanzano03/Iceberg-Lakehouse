# Moodle Lakehouse Analytics

A portable data lakehouse stack—Apache Iceberg + MinIO + Apache Spark (cluster mode)—designed for Educational Data Mining (EDM) and student-dropout prediction.

## 1. Project Goals

- Ingest structured data from the operational Moodle MySQL database.
- Persist raw & curated datasets in an S3-compatible bucket (MinIO) using the transactional Apache Iceberg table format.
- Process & transform data with a multi-node Spark cluster that can be scaled horizontally.
- Enable analytics & ML workflows: classroom resource clustering and student-dropout prediction.
- Keep the architecture simple, reproducible, and deployable in under 5 minutes on any VM.

## 2. Stack Overview

| Layer         | Technology         | Purpose                                              |
|---------------|--------------------|------------------------------------------------------|
| **Storage (Lake)** | MinIO             | S3-compatible object store (warehouse bucket)       |
| **Table Format**   | Apache Iceberg    | ACID transactions, schema evolution, time-travel    |
| **Catalog**        | Iceberg REST Catalog | Metadata & namespace service                        |
| **Compute**        | Apache Spark 3.5  | Distributed batch/ML processing (master + workers)  |
| **Orchestration**  | Docker Compose    | One-command local/VM deployment                     |
| **(Optional) Notebooks** | Jupyter Lab      | Interactive exploration (add later)                 |

## 3. Quick Start

```bash
# 1. Clone repository
$ git clone https://github.com/<you>/Iceberg-lakehouse.git && cd Iceberg-lakehouse

# 2. Build custom Spark + Iceberg image and start the stack
$ docker-compose build
$ docker-compose up -d        # master, 2 workers, MinIO, REST Catalog

# 3. Check services
$ docker-compose ps           # status
$ docker exec -it spark-master spark-sql    # connect to Spark
spark-sql> SHOW NAMESPACES;
```

**Default credentials:** `admin/password` (MinIO & REST Catalog)

## 4. Directory Structure

```
.
├─ docker-compose.yml          # cluster definition
├─ spark-defaults.conf         # Iceberg/S3 configs auto-loaded by Spark
├─ requirements.txt            # Python deps (PySpark, PyIceberg, etc.)
└─ spark/
      └─ Dockerfile               # extends bitnami/spark with Iceberg JARs
```

## 5. Scaling the Cluster

- **Vertical:** Give the VM more CPUs/RAM.
- **Horizontal:** `docker-compose up -d --scale spark-worker=<N>`.
- **Iceberg optimizations:** Compaction, partition evolution, etc.

## 6. Typical Use-Cases

- ETL / ELT of Moodle event logs into fact tables.
- Time-travel analysis of course resources.
- Clustering classrooms by resource usage via Spark MLlib.
- Predicting student dropout with gradient-boosted trees.

## 7. Troubleshooting

| Symptom                          | Fix                                                      |
|----------------------------------|---------------------------------------------------------|
| `AccessDenied: Invalid AccessKeyId` | Verify `MINIO_ROOT_USER/PASSWORD` in environment variables. |
| Spark workers don’t register     | Check `SPARK_MASTER_URL` env; ensure ports 7077 are open. |
| Slow queries                     | Tune `spark.sql.shuffle.partitions`, enable Iceberg vectorization. |

## 8. Roadmap

- **Ansible automation:** Provide an optional playbook to provision the VM (install Docker/Compose, clone repo, launch services) for repeatable, one-command deployments.
- **JupyterLab integration:** Add a JupyterLab container pre-wired with PySpark + Iceberg.
- **MLflow integration:** Experiment tracking and model registry.

## 9. Contributing

Pull requests are welcome! Please open an issue first to discuss your idea.

## 10. License

This project is licensed under the Apache 2.0 License.
