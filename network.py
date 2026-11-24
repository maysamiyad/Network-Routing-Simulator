# Representing the network topology
network = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "D": 5},
    "C": {"A": 2, "D": 3},
    "D": {"B": 5, "C": 3}
}

# Display each router and its neighbors
for router in network:
    print("Router:", router)
    print("Neighbors:", network[router])
    print()