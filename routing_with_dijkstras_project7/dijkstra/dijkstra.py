import sys
import json
import math  # If you want to use math.inf for infinity
import netfuncs_routing as netfuncs

def dijkstras_shortest_path(routers, src_ip, dest_ip):
    """
    This function takes a dictionary representing the network, a source
    IP, and a destination IP, and returns a list with all the routers
    along the shortest path.

    The source and destination IPs are **not** included in this path.

    Note that the source IP and destination IP will probably not be
    routers! They will be on the same subnet as the router. You'll have
    to search the routers to find the one on the same subnet as the
    source IP. Same for the destination IP. [Hint: make use of your
    find_router_for_ip() function from the last project!]

    The dictionary keys are router IPs, and the values are dictionaries
    with a bunch of information, including the routers that are directly
    connected to the key.

    This partial example shows that router `10.31.98.1` is connected to
    three other routers: `10.34.166.1`, `10.34.194.1`, and `10.34.46.1`:

    {
        "10.34.98.1": {
            "connections": {
                "10.34.166.1": {
                    "netmask": "/24",
                    "interface": "en0",
                    "ad": 70
                },
                "10.34.194.1": {
                    "netmask": "/24",
                    "interface": "en1",
                    "ad": 93
                },
                "10.34.46.1": {
                    "netmask": "/24",
                    "interface": "en2",
                    "ad": 64
                }
            },
            "netmask": "/24",
            "if_count": 3,
            "if_prefix": "en"
        },
        ...

    The "ad" (Administrative Distance) field is the edge weight for that
    connection.

    **Strong recommendation**: make functions to do subtasks within this
    function. Having it all built as a single wall of code is a recipe
    for madness.
    """

    shortest_path = []
    
    dest_router = netfuncs.find_router_for_ip(routers, dest_ip)
    src_router = netfuncs.find_router_for_ip(routers, src_ip)

    if dest_router == src_router:
        return shortest_path
    
    dist, parents = dijkstras(routers, src_router)

    shortest_path = get_shortest_path(parents, src_router, dest_router)
    
    return shortest_path

def dijkstras(routers, src_router):
    to_visit = set()
    dist = dict()
    parent = dict()

    for router in routers:
        dist[router] = math.inf
        parent[router] = None
        to_visit.add(router)

    dist[src_router] = 0

    # print(routers)
    # print(routers.items())

    # conn = routers.get("router").get("connections")
    # print (conn)

    # for conn in to_visit:
    #     if conn not in to_visit:
    #         break
    while len(to_visit) != 0:

        # print(routers)
        # conn_json = routers.get("connections")
        # print(conn)
        curr_node, curr_dist = find_min_dist(dist, to_visit)
        to_visit.remove(curr_node)
        # print(to_visit)
        # print(curr_node)

        # print(routers.get(curr_node))
        
        conn = routers.get(curr_node).get("connections")
        # print(conn.items())

        # neighbours = conn.get("connections")
        for neighbour, neighbour_attr in conn.items():
            # print(neighbour)
            if neighbour not in to_visit:
                continue

            #might need to tune this for lean
            alt = dist.get(curr_node) + neighbour_attr.get("ad")
            if alt < dist[neighbour]:
                dist[neighbour] = alt
                parent[neighbour] = curr_node
        
    return dist, parent

def find_min_dist(dist, to_visit):
    # print(dist)

    min_dist = math.inf
    min_conn = None

    #TODO fix this search, conn is only a string why is that?
    for node, d in dist.items():

        if node not in to_visit:
            continue

        if d < min_dist:
            min_dist = d
            min_conn = node
    
    return min_conn, min_dist

def get_shortest_path(parent, src_node, dest_node):

    # print(parent)
    
    curr_node = dest_node
    path = []
    while curr_node != src_node:
        print(curr_node)
        print(parent[curr_node])
        path.append(curr_node)
        curr_node = parent[curr_node]


    return path.reverse()

#------------------------------
# DO NOT MODIFY BELOW THIS LINE
#------------------------------
def read_routers(file_name):
    with open(file_name) as fp:
        data = fp.read()

    return json.loads(data)

def find_routes(routers, src_dest_pairs):
    for src_ip, dest_ip in src_dest_pairs:
        path = dijkstras_shortest_path(routers, src_ip, dest_ip)
        print(f"{src_ip:>15s} -> {dest_ip:<15s}  {repr(path)}")

def usage():
    print("usage: dijkstra.py infile.json", file=sys.stderr)

def main(argv):
    try:
        router_file_name = argv[1]
    except:
        usage()
        return 1

    json_data = read_routers(router_file_name)

    routers = json_data["routers"]
    routes = json_data["src-dest"]

    find_routes(routers, routes)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
    
