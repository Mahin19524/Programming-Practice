import itertools

def calculate_distance(route, distances):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[route[i]][route[i+1]]
    total_distance += distances[route[-1]][route[0]]  # Return to the starting city
    return total_distance

def find_shortest_route(N, distances):
    shortest_distance = float('inf')
    shortest_route = None
    
    # Generate all permutations of cities
    for route in itertools.permutations(range(N)):
        distance = calculate_distance(route, distances)
        if distance < shortest_distance:
            shortest_distance = distance
            shortest_route = route
    
    return shortest_route

# Sample input
N = 4
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Find the shortest route
shortest_route = find_shortest_route(N, distances)

# Print the shortest route
print("Shortest Route:", shortest_route)
print("Shortest Distance:", calculate_distance(shortest_route, distances))
