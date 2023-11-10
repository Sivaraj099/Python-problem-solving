def strange_vs_covid(n, m, portals, demon_patrols):
    time_to_reach = [float('inf')] * n
    time_to_reach[0] = 0
    demon_interaction = 0

    for start_node in range(n):
        for end_node in range(n):
            if portals[start_node][end_node] != -1:
                if time_to_reach[start_node] + portals[start_node][end_node] in demon_patrols[end_node]:
                    demon_interaction = 1
                else:
                    demon_interaction = 0
                if time_to_reach[end_node] > time_to_reach[start_node] + demon_interaction + portals[start_node][end_node]:
                    time_to_reach[end_node] = time_to_reach[start_node] + demon_interaction + portals[start_node][end_node]

    if time_to_reach[n - 1] != float('inf'):
        return time_to_reach[n - 1]
    else:
        return -1

if __name__ == '__main__':
    n, m = map(int, input().split())  # Read n and m
    portals = [[-1] * n for _ in range(n)]  # Initialize the portal matrix with -1
    
    for _ in range(m):
        start, end, time = map(int, input().split())
        portals[start - 1][end - 1] = time
    
    demon_patrols = []

    for _ in range(n):
        patrol_info = set(input().split())
        demon_patrols.append(patrol_info)

    result = strange_vs_covid(n, m, portals, demon_patrols)
    print(result)