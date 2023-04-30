---
layout: post
title: AWS
---

[AWS Cloud Practitioner Essentials](https://www.coursera.org/learn/aws-cloud-practitioner-essentials)

[Certificate](https://coursera.org/share/fd1209f15f536370715adfbbc2939a26)

[AWS Fundamentals Specialization](https://www.coursera.org/specializations/aws-fundamentals)

[Download to a file named by the URL](https://everything.curl.dev/usingcurl/downloads/url-named)

> This is the `-O` (uppercase letter o) option, or `--remote-name` for the long name version. The `-O` option selects the local file name to use by picking the file name part of the URL that you provide. This is important. You specify the URL and curl picks the name from this data. If the site redirects curl further (and if you tell curl to follow redirects), it does not change the file name curl will use for storing this.

```bash
for i in {21..27}; do \
curl -O https://coast.noaa.gov/htdata/CMSP/AISDataHandler/2022/AIS_2022_06_${i}.zip; \
unzip AIS_2022_06_${i}.zip; \
done
```

[Using high-level (s3) commands with the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html)

```bash
for i in {21..27}; do aws s3 cp AIS_2022_06_${i}.csv s3://jordanbell2357ais/; done
```

S3 bucket:

![S3 bucket](/images/AWS/jordanbell2357ais.jpeg)

