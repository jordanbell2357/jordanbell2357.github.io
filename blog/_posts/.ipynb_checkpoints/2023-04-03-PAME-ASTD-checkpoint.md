---
layout: post
title: PAME Arctic Ship Traffic Data (ASTD)
topic: maps
---

[Arctic Shipping Status Reports \| PAME](https://pame.is/projects-new/arctic-shipping/pame-shipping-highlights/411-arctic-shipping-status-reports)

[Arctic Ship Traffic Data - ASTD \| PAME](https://pame.is/index.php/projects/arctic-marine-shipping/astd)

[Arctic Ship Traffic Data - ASTD](https://map.astd.is/)

![Arctic Ship Traffic Data - ASTD](/images/ASTD/ASTD-Arctic-Ship-Traffic-Database.png)

![Ports](/images/ASTD/ASTD-Arctic-Ship-Traffic-Database-Ports.png)

`Ports.csv`

```
head -n 5 Ports.csv
```

```
﻿havn   havn_en terminalna      terminalna_en   geom_wkt
Tiksi                           POINT(128.872523555144 71.6443193634454)
Ust-Kara                                POINT(64.9155175661919 69.2491104220271)
Nuuk-Godthaab                           POINT(-51.720420892676 64.1708873011146)
Sisimiut                                POINT(-53.6753882255269 66.9414846843146)
```

```bash
cut -d$'\t' -f1,5 Ports.csv > ASTD_Ports_2023.tsv
```

{% assign table_rows1 = site.data.ASTD_Ports_2023 %}

<div style="overflow-x:auto;">
  <table>
      {% for row in table_rows1 %}
          {% if forloop.first %}
              <tr>
                  {% for pair in row %}
                      <th>
                          {{ pair[0] }}
                      </th>
                  {% endfor %}
              </tr>
          {% endif %}

          {% tablerow pair in row %}
              {{ pair[1] }}
          {% endtablerow %}
      {% endfor %}
  </table>
</div>

Murmansk (Мурманск)

![Murmansk](/images/ASTD/Murmansk.jpg)

Arkhangelsk (Арха́нгельск)

![Arkhangelsk](/images/ASTD/Arkhangelsk.jpg)

Novaya Zemlya Archipelago

![Novaya Zemlya archipelago](/images/ASTD/NovayaZemlya.jpg)

Yamal Peninsula

![Yamal Peninsula](/images/ASTD/YamalPeninsula.jpg)

Taymyr Peninsula

![Taymyr Peninsula](/images/ASTD/TaymyrPeninsula.jpg)

Bering Strait

![Bering Strait](/images/ASTD/BeringStrait.jpg)