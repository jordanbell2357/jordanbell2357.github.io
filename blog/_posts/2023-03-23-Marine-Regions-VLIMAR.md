---
layout: post
title: Marine Regions VLIMAR
---

[Marine Regions](https://www.marineregions.org/about.php)

> Marine Regions is an integration of the VLIMAR Gazetteer and the VLIZ Maritime Boundaries Geodatabase. The VLIMAR Gazetteer is a database with geographic, mainly marine names such as seas, sandbanks, seamounts, ridges, bays or even standard sampling stations used in marine research. The geographic cover of the VLIMAR gazetteer is global but initially focused on the Belgian Continental Shelf and the Scheldt Estuary and the Southern Bight of the North Sea. Gradually more regional and global geographic information was added to VLIMAR and combining this information with the Maritime Boundaries database, representing the Exclusive Economic Zone (EEZ) of the world, led to the creation of marineregions.org.

![Marine Regions](/images/MarineRegions/Marine-Regions.png)

[Sources](https://www.marineregions.org/sources.php)

> Flanders Marine Institute (2019). Maritime Boundaries Geodatabase, version 11. Available online at https://www.marineregions.org/. https://doi.org/10.14284/382.

> Maritime Boundaries Geodatabase
>
> This geodatabase represents the Maritime Boundaries of the world. The database includes seven global datasets:
>
> 1. Exclusive Economic Zones (200NM), version 11 (including the boundary polylines)
> 1. Territorial Seas (12NM), version 3
> 1. Contiguous Zones (24NM), version 3
> 1. Internal Waters, version 3
> 1. Archipelagic Waters, version 3
> 1. High Seas, version 1
> 1. Extended Continental Shelves, version 1 (including the boundary polylines)

```python3
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap()
map.readshapefile('C:/Users/jorda/repos/MarineRegions/World_EEZ_v11_20191118/eez_v11', 'eez_v11')
plt.savefig('eez_v11.png')
```

![EEZ v11](/images/MarineRegions/eez_v11.png)