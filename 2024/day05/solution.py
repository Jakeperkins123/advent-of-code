from collections import defaultdict, deque

with open("input.txt") as f:
    s = f.read().strip()

ans = 0
adj_list = defaultdict(list)
updates = []

for line in s.split("\n"):
    if "|" in line:
        before, after = line.split("|")
        adj_list[int(before)].append(int(after))
    if "," in line:
        update = [int(val) for val in line.split(",")]
        updates.append(update)


def topo_sort(graph, nodes):
    indegree = {node: 0 for node in nodes}
    for node in nodes:
        for neighbor in graph[node]:
            if neighbor in nodes:
                indegree[neighbor] += 1

    q = deque([node for node in nodes if indegree[node] == 0])

    result = []
    while q:
        node = q.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if neighbor in nodes:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

    return result


for update in updates:
    sorted_update = topo_sort(adj_list, update)
    if sorted_update != update:
        mid = len(update) // 2
        ans += int(sorted_update[mid])


print(ans)
