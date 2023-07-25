---
layout: post
title: Pyspark ML with Hadoop for cluster analysis on minute_weather.csv
---

[SDSC Big Data Specialization. Course 4. Week 5](https://www.coursera.org/learn/big-data-machine-learning/home/week/5)

`minute_weather.csv.gz`

`gzip -d minute_weather.csv.gz`

```bash
head minute_weather.csv
```

```csv
rowID,hpwren_timestamp,air_pressure,air_temp,avg_wind_direction,avg_wind_speed,max_wind_direction,max_wind_speed,min_wind_direction,min_wind_speed,rain_accumulation,rain_duration,relative_humidity
0,2011-09-10 00:00:49,912.3,64.76,97.0,1.2,106.0,1.6,85.0,1.0,,,60.5
1,2011-09-10 00:01:49,912.3,63.86,161.0,0.8,215.0,1.5,43.0,0.2,0.0,0.0,39.9
2,2011-09-10 00:02:49,912.3,64.22,77.0,0.7,143.0,1.2,324.0,0.3,0.0,0.0,43.0
3,2011-09-10 00:03:49,912.3,64.4,89.0,1.2,112.0,1.6,12.0,0.7,0.0,0.0,49.5
4,2011-09-10 00:04:49,912.3,64.4,185.0,0.4,260.0,1.0,100.0,0.1,0.0,0.0,58.8
5,2011-09-10 00:05:49,912.3,63.5,76.0,2.5,92.0,3.0,61.0,2.0,0.0,0.0,62.6
6,2011-09-10 00:06:49,912.3,62.78,79.0,2.4,89.0,2.7,62.0,2.0,0.0,0.0,65.6
7,2011-09-10 00:07:49,912.3,62.42,86.0,2.0,92.0,2.4,75.0,1.8,0.0,0.0,65.2
8,2011-09-10 00:08:49,912.3,62.24,105.0,1.4,125.0,1.9,82.0,1.0,0.0,0.0,65.8
```

```python
from pyspark.sql import SparkSession
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import VectorAssembler
from pyspark.sql.functions import col, count, when
import matplotlib.pyplot as plt

# Initialize Spark session
spark = SparkSession.builder.appName("KMeansClustering").getOrCreate()

# Load data from CSV
df = spark.read.csv('minute_weather.csv', sep=',', inferSchema=True, header=True)

# Selected features for clustering
features_used = ['air_pressure', 'air_temp', 'avg_wind_direction', 'avg_wind_speed', 'max_wind_direction', 
                 'max_wind_speed', 'relative_humidity']

# Assemble the features into a single vector column, handling null values by skipping rows
assembler = VectorAssembler(inputCols=features_used, outputCol="features", handleInvalid="skip")
assembled_data = assembler.transform(df)

# Check if the DataFrame contains any rows
if assembled_data.count() == 0:
    raise ValueError("The DataFrame is empty. Please check the data and preprocessing steps.")

# Check if the selected features contain any null values
null_counts = assembled_data.select(*[count(when(col(c).isNull(), c)).alias(c) for c in features_used]).collect()[0]

for feature, null_count in zip(features_used, null_counts):
    if null_count > 0:
        raise ValueError(f"The feature '{feature}' contains {null_count} null value(s). Please handle or remove the null values.")

def elbow_method(data, max_k):
    wsse_list = []
    for k in range(2, max_k + 1):
        model, clustered_data = perform_kmeans(data, k)
        wsse = compute_cost(clustered_data, model)
        wsse_list.append((k, wsse))
    return wsse_list

def perform_kmeans(data, k):
    # Create and fit the KMeans model
    kmeans = KMeans().setK(k).setSeed(42)
    model = kmeans.fit(data)

    # Add the cluster predictions to the data
    clustered_data = model.transform(data)
    return model, clustered_data

def compute_cost(clustered_data, model):
    # Calculate Within Set Sum of Squared Errors (WSSE)
    summary = model.summary
    cost = summary.trainingCost
    return cost

def plot_elbow(wsse_list):
    ks, wsses = zip(*wsse_list)
    plt.plot(ks, wsses)
    plt.xlabel("Number of Clusters (k)")
    plt.ylabel("WSSE")
    plt.title("Elbow Plot")
    plt.show()

# Perform k-means clustering and generate the elbow plot
max_clusters = 30
wsse_list = elbow_method(assembled_data, max_clusters)
plot_elbow(wsse_list)

# Stop Spark session
spark.stop()
```

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/b47ba8f1-5fc9-4ecc-ae1b-ee0b0332bb80)

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/a472569d-35e2-4f39-b381-8c0359e3521e)

![image](https://github.com/jordanbell2357/jordanbell2357.github.io/assets/47544607/955a50e9-d4f5-4f41-8b63-054f6f35eaea)




