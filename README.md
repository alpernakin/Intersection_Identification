I have used intersection numbers in my predictive data model to predict traffic accidents. However, there is no data source giving intersection points in a city so that I developed a python script to find intersection locations in a specific area by using OSM json data.

Firstly, run the given code below in overpass-turbo.eu in a specific area. Then, download json data to roadways.json file.

```
[out:json][timeout:25];
// fetch results
(
  // query part for: “highway=primary”
  node["highway"="primary"]({{bbox}});
  way["highway"="primary"]({{bbox}});
  relation["highway"="primary"]({{bbox}});
  // query part for: “highway=secondary”
  node["highway"="secondary"]({{bbox}});
  way["highway"="secondary"]({{bbox}});
  relation["highway"="secondary"]({{bbox}});
  // query part for: “highway=tertiary”
  node["highway"="tertiary"]({{bbox}});
  way["highway"="tertiary"]({{bbox}});
  relation["highway"="tertiary"]({{bbox}});
  // query part for: “highway=residential”
  node["highway"="residential"]({{bbox}});
  way["highway"="residential"]({{bbox}});
  relation["highway"="residential"]({{bbox}});
  // query part for: “highway=unclassified”
  node["highway"="unclassified"]({{bbox}});
  way["highway"="unclassified"]({{bbox}});
  relation["highway"="unclassified"]({{bbox}});
  // query part for: “highway=trunk”
  node["highway"="trunk"]({{bbox}});
  way["highway"="trunk"]({{bbox}});
  relation["highway"="trunk"]({{bbox}});
  // query part for: “highway=motorway”
  node["highway"="motorway"]({{bbox}});
  way["highway"="motorway"]({{bbox}});
  relation["highway"="motorway"]({{bbox}});
);
out body;
>;
out skel qt;
```

The data includes ways and nodes.
Each street has multiple ways whereas each way has multiple nodes.
If a node is contained by different ways belong to different streets. It means that this node is an intersection point.
