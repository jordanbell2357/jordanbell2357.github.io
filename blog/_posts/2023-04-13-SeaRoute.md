---
layout: post
title: SeaRoute
---

[eurostat/searoute](https://github.com/eurostat/searoute)

`test_input.csv`

```
route name,olon,olat,dlon,dlat
Marseille-Shanghai,5.3,43.3,121.8,31.2
Marseille-Saint-Petersburg,5.3,43.3,30.2,59.9
Marseille-Auckland,5.3,43.3,174.8,-36.8
Marseille-New-York,5.3,43.3,-74.1,40.7
Marseille-Los Angeles,5.3,43.3,-118.3,33.7
Shanghai-Saint-Petersburg,121.8,31.2,30.2,59.9
Shanghai-Auckland,121.8,31.2,174.8,-36.8
Shanghai-New-York,121.8,31.2,-74.1,40.7
Shanghai-Los Angeles,121.8,31.2,-118.3,33.7
Saint-Petersburg-Auckland,30.2,59.9,174.8,-36.8
Saint-Petersburg-New-York,30.2,59.9,-74.1,40.7
Saint-Petersburg-Los Angeles,30.2,59.9,-118.3,33.7
Auckland-New-York,174.8,-36.8,-74.1,40.7
Auckland-Los Angeles,174.8,-36.8,-118.3,33.7
New-York-Los Angeles,-74.1,40.7,-118.3,33.7
```

`searoute.sh`

```bash
#!/usr/bin/env bash
java -jar searoute.jar -i "test_input.csv" -res 5 -panama 0
```

Output is `out.geojson`

Combining `out.geojson` with `ne_10m_land` we get the following:

![SeaRoute geojson output with test input](/images/SeaRoute/test_input.png)

<table>
<thead>
  <tr>
    <th>Port</th>
    <th>Latitude</th>
    <th>Longitude</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Port of Melbourne</td>
    <td>-37.85</td>
    <td>144.90</td>
  </tr>
  <tr>
    <td>Port of Kaohsiung</td>
    <td>22.61</td>
    <td>120.28</td>
  </tr>
  <tr>
    <td>Yantian International Container Terminals</td>
    <td>22.57</td>
    <td>114.27</td>
  </tr>
  <tr>
    <td>Port of Singapore</td>
    <td>1.26</td>
    <td>103.84</td>
  </tr>
  <tr>
    <td>Mundra Port</td>
    <td>22.75</td>
    <td>69.70</td>
  </tr>
  <tr>
    <td>Port of Jebel Ali</td>
    <td>25.01</td>
    <td>55.06</td>
  </tr>
  <tr>
    <td>Port of Piraeus</td>
    <td>37.94</td>
    <td>23.64</td>
  </tr>
  <tr>
    <td>Marseille-Fos Port</td>
    <td>22.75</td>
    <td>69.70</td>
  </tr>
  <tr>
    <td>Port Newark–Elizabeth Marine Terminal</td>
    <td>40.68</td>
    <td>-74.15</td>
  </tr>
  <tr>
    <td>Port of Santos</td>
    <td>-23.98</td>
    <td>-46.29</td>
  </tr>
  <tr>
    <td>Puerto de San Antonio</td>
    <td>-33.59</td>
    <td>-71.62</td>
  </tr>
  <tr>
    <td>Port of Los Angeles</td>
    <td>33.73</td>
    <td>-118.26</td>
  </tr>
</tbody>
</table>


```
routename,olon,olat,dlon,dlat
Melbourne,144.90,-37.85,120.28,22.61
Kaohsiung,120.28,22.61,114.27,22.57
Yantian,114.27,22.57,103.84,1.26
Singapore,103.84,1.26,69.70,22.75
Mundra,69.70,22.75,55.06,25.01
JA,55.06,25.01,23.64,37.94
Piraeus,23.64,37.94,69.70,22.75
Marseille,69.70,22.75,-74.15,40.68
Newark,-74.15,40.68,-46.29,-23.98
Santos,-46.29,-23.98,-71.62,-33.59
Antonio,-71.62,-33.59,-118.26,33.73
```

![Route from Port of Melbourne to Port of Los Angeles](/images/SeaRoute/route1.png)