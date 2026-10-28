import heapq

graph = {}


def add_location():
    name = input("Enter location name: ").strip()

    if not name:
        print("Location name cannot be empty!")
        return

    if name in graph:
        print("Location already exists!")
        return

    graph[name] = []
    print("Location added successfully!")


def add_road():
    source = input("Enter starting location: ").strip()
    destination = input("Enter destination: ").strip()

    if source not in graph or destination not in graph:
        print("Both locations must exist!")
        return

    if source == destination:
        print("Choose two different locations!")
        return

    try:
        distance = float(input("Enter distance in km: "))

        if distance <= 0:
            print("Distance must be positive!")
            return

    except ValueError:
        print("Invalid distance!")
        return

    # Roads are bidirectional
    graph[source].append((destination, distance))
    graph[destination].append((source, distance))

    print("Road added successfully!")


def display_map():
    if not graph:
        print("No locations available!")
        return

    print("\n===== ROAD NETWORK =====")

    for location, roads in graph.items():
        print(location, "->", roads)


def shortest_route():
    start = input("Enter starting location: ").strip()
    end = input("Enter destination: ").strip()

    if start not in graph or end not in graph:
        print("Location not found!")
        return

    distances = {location: float("inf") for location in graph}
    previous = {location: None for location in graph}

    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current = heapq.heappop(priority_queue)

        if current_distance > distances[current]:
            continue

        if current == end:
            break

        for neighbour, weight in graph[current]:
            new_distance = current_distance + weight

            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                previous[neighbour] = current

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbour)
                )

    if distances[end] == float("inf"):
        print("No route exists!")
        return

    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    print("\n===== SHORTEST ROUTE =====")
    print("Route:", " -> ".join(path))
    print("Total Distance:", distances[end], "km")


while True:
    print("\n===== GPS NAVIGATION SYSTEM =====")
    print("1. Add Location")
    print("2. Add Road")
    print("3. Display Road Network")
    print("4. Find Shortest Route")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_location()

    elif choice == "2":
        add_road()

    elif choice == "3":
        display_map()

    elif choice == "4":
        shortest_route()

    elif choice == "5":
        print("Exiting GPS Navigation System!")
        break

    else:
        print("Invalid choice!")