import json

def all_same(items):
    return all(x == items[0] for x in items)

with open('C:\\Users\\alper\\Desktop\\Research\\datasets\\road\\json\\osm_london_central_roadways.json') as json_data:    
    data = json.load(json_data)

ways = []
nodes = []

# There are two types of objects: Ways and Nodes.
# Each street is represented by multiple ways.
# Each way is represented by multiple nodes.
for element in data["elements"]:
    if element["type"] == "way":
        ways.append(element)
    elif element["type"] == "node":
        nodes.append(element)

node_list = list(map(lambda r: ((int(r["id"])), (r["lat"], r["lon"])), nodes))

way_list = []
for way in ways:
    if "tags" in way:
        if "name" in way["tags"]:
            way_list.append([way["id"], way["tags"]["name"], way["nodes"]])

ways_and_nodes = []
for way in way_list:
    for way_node in way[2]:
        ways_and_nodes.append((int(way_node), (way[0], way[1])))

node_list.sort(key=lambda x: x[0])
ways_and_nodes.sort(key=lambda x: x[0])

# If a node is found in multiple ways belong to different streets.
# In other words, if two different streets have a common node, it means that this node is an intersection point.
f = open('C:\\Users\\alper\\Desktop\\Research\\datasets\\road\\osm_london_central_intersections.csv','a+')
for node in node_list:
    intersecting_ways = [x for x in ways_and_nodes if x[0] == node[0]]
    intersecting_streets = list(map(lambda r: r[1][1], intersecting_ways))

    if all_same(intersecting_streets) is False:
        row = "%d,%9.7f,%9.7f\n" % (node[0], node[1][0], node[1][1])
        f.write(row)
        print(row)
f.close()
