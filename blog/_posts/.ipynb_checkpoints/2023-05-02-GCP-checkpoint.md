---
layout: post
title: Google Cloud Platform
---

# AWS S3

[Using high-level (s3) commands with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html)

The size of each zip file we download is around 300 MB and decompressed the csv file is around 900 MB. There is not enough
available space in my EC2 instance to do the following in EC2 Instance Connect.

Locally we run the following:

[Download to a file named by the URL](https://everything.curl.dev/usingcurl/downloads/url-named)

> This is the `-O` (uppercase letter o) option, or `--remote-name` for the long name version. The `-O` option selects the local file name to use by picking the file name part of the URL that you provide. This is important. You specify the URL and curl picks the name from this data. If the site redirects curl further (and if you tell curl to follow redirects), it does not change the file name curl will use for storing this.

```bash
for i in {21..27}; do \
curl -O https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2022/AIS_2022_06_${i}.zip; \
unzip AIS_2022_06_${i}.zip; \
done
```

```bash
for i in {21..27}; do aws s3 cp AIS_2022_06_${i}.csv s3://jordanbell2357ais/; done
```

S3 bucket:

![S3 bucket](/images/AWS/jordanbell2357ais.jpeg)

# Google Cloud Storage

[Discover object storage with the gsutil tool](https://cloud.google.com/storage/docs/discover-object-storage-gsutil)

Using EC2 Instance Connect was not possible in my AWS configuration, because the size of each pair of zip file and csv file is
over 1 GB in each case. On the other hand, in my configuration of Google Cloud Platform, the 5 GB available space is enough to 
store one by one the zip file and csv file.

We write out the steps for June 21, 2022, in a general way.

```bash
i=21 # 01-31
curl -O https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2022/AIS_2022_06_${i}.zip
unzip AIS_2022_06_${i}.zip
gsutil cp AIS_2022_06_${i}.csv gs://jordanbell2357marinecadastre/
rm AIS_2022_06_${i}.zip
rm AIS_2022_06_${i}.csv
```

Relevant Google Cloud Self-Paced Labs (GSP): Cloud Storage: Qwik Start - CLI/SDK (**GSP074**),
Ingesting Data Into The Cloud (**GSP194**), Ingesting New Datasets into BigQuery (**GSP 411**), Loading Your Own Data into BigQuery (**GSP865**).

We use `bq` thus:

```bash
for i in {21..27}; do bq load --source_format=CSV --autodetect AIS_2022_06_21_to_27.AIS_2022_06_${i} gs://jordanbell2357marinecadastre/AIS_2022_06_${i}.csv; done
```

Now, to make sure we can do the same task multiple ways, we will do the above locally for June 20, 2022.

```bash
curl -O https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2022/AIS_2022_06_20.zip
unzip AIS_2022_06_20.zip
```

If we now run

```bash
gsutil cp AIS_2022_06_20.csv gs://jordanbell2357/marinecadastre/
```

we get

```
ResumableUploadAbortException: 401 Anonymous caller does not have storage.objects.create access to the Google Cloud Storage object. Permission 'storage.objects.create' denied on resource (or it may not exist).
```

[Initializing the gcloud CLI](https://cloud.google.com/sdk/docs/initializing)

[Install gsutil](https://cloud.google.com/storage/docs/gsutil_install#deb)

We run

```bash
gcloud init
```

and then run

```bash
gsutil cp AIS_2022_06_20.csv gs://jordanbell2357/marinecadastre/
```

with success. Then

```bash
bq load --source_format=CSV --autodetect AIS_2022_06_21_to_27.AIS_2022_06_20 gs://jordanbell2357marinecadastre/AIS_2022_06_20.csv
```

with success. Now we clean up,

```bash
rm AIS_2022_06_20.zip
rm AIS_2022_06_20.csv
```