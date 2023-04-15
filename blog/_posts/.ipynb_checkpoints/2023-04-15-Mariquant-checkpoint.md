---
layout: post
title: Creating sea routes from the sea of AIS data by Mariquant
---

[Creating sea routes from the sea of AIS data. Alexei Novikov. Mariquant. May 15, 2019])(https://towardsdatascience.com/creating-sea-routes-from-the-sea-of-ais-data-30bc68d8530e)

> Mariquant has hourly data from one of the AIS data providers for the bulkers and tankers from the beginning of 2016 to the middle of 2018. This data has information from around 19 000 unique ships with records, occupying approximately 100 Gb as uncompressed parquet file.

> We used distance to the port, distance to the previous port, speed of the ship, radial velocity of the ship (as if circling the port) and speed in the direction to the port, as the features of the classifier. We manually constructed training and testing sets separately marking ‘loitering’, anchoring, port approaching and general voyage points. We had around 6 400 points in the training and 1600 points in the testing set. Anchoring points are less represented in the sets, as they create fewer problems in the distance calculations.

> We found that distance to the port, distance to the previous port, speed of the ship are the most important features, having a score of 0.42, 0.21 and 0.28 correspondingly and radial speed and speed in the direction to the port have a score of 0.04 and 0.05.

```python
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
clf = RandomForestClassifier(n_estimators=20, max_depth=6, random_state=0)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print(clf.feature_importances_)
```

> We found that irrespectively from the scores of the classifiers, additional cleanup is required for our large dataset. Sometimes small parts of the port approach trajectories were mistakenly identified as loitering parts, and we had to apply conservative check requiring anchoring and loitering parts of the trajectories to be long enough and either be self-intersecting, or the distance travelled in the direction to the port should be smaller compared to the total length travelled.
>
> After all these checks we average the position of the vessel for the loitering and anchoring parts of the trajectories.