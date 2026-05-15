"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Vlad Jerohhin
Student ID:   130785223

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.
    """
    return (
        "Part 1: Problem Analysis\n"
        "--------------------------\n"
        "1. Why a single shortest-path run from S is not enough:\n"
        "- A standard shortest-path algorithm can find the cheapest way to reach one specific spot, "
        "but cannot determine which relic should be visited first and so on to minimize the overall journey. "
        "It lacks the logic to decide which relic to grab first, second, etc to make the entire trip more efficient.\n"
        "2. What decision remains after all inter-location costs are known:\n"
        "- After knowing the cheapst travel costs, we still have to figure out the best order to visit them.\n"
        "3. Why this requires a search over orders (one sentence):\n"
        "- This problem requires a search over orders because different relic orders can have different total costs "
        "even when we know the distance from point to point."
    )


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    """
    sources = []

    if spawn not in sources:
        sources.append(spawn)

    for relic in relics:
        if relic not in sources:
            sources.append(relic)

    return sources


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').
    """
    dist = {}

    # Start every node as unreachable
    for node in graph:
        dist[node] = float('inf')

    dist[source] = 0
    pq = [(0, source)]

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        if curr_dist > dist[curr_node]:
            continue

        for v, cost in graph[curr_node]:
            new_dist = curr_dist + cost

            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.
    """
    dist_table = {}
    sources = select_sources(spawn, relics, exit_node)

    for source in sources:
        dist_table[source] = run_dijkstra(graph, source)

    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.
    """
    return (
        "Part 3: Algorithm Correctness\n"
        "--------------------------\n"
        "3a - 1. For nodes already finalized (in S):\n"
        "- Once a node is finalized, its distance value is locked in as the cheapest possible distance "
        "from the source and we are sure there is no better path that exists.\n"
        "3a - 2. For nodes not yet finalized (not in S):\n"
        "- These nodes can still improve, their current distance value is the best path found so far based on finalized nodes.\n"
        "3b - 1. Initialization : why the invariant holds before iteration 1:\n"
        "- Before the first loop, no nodes have been finalized and the source starts at distance 0. "
        "- Every other node starts at infinity, which is technically the shortest path in an empty set of finalized nodes.\n"
        "3b - 2. Maintenance : why finalizing the min-dist node is always correct:\n"
        "- By always picking the node with the smallest current distance, we ensure it's finalized because "
        "nonnegative edge weights mean no future path could ever loop back and be cheaper than the one we just found.\n"
        "3b - 3. Termination : what the invariant guarantees when the algorithm ends:\n"
        "- When the priority queue is empty, every reachable node has been finalized with its confirmed shortest path distance.\n"
        "3c. Why Correctness Matters:\n"
        "- Correct shortest path distances matter because the route planner uses those distances to compare relic orders and "
        "choose the lowest fuel route to ensure the torchbearerr does not run out fuel before the exit."
    )


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.
    """
    return (
        "Part 4: Search Design\n"
        "--------------------------\n"
        "1. The failure mode:\n"
        "- A greedy strategy only looks at the next closest relic and ignores how that choice might lead to a dead end or an expensive path later in the sequence.\n"
        "2. Counter-example setup:\n"
        "- Using this example table, assume we have 2 algoritms; greedy and optimal.\n"
        "| From / To | B   | C   | D   | T   |\n"
        "|-----------|-----|-----|-----|-----|\n"
        "| S         | 1   | 2   | 2   | --  |\n"
        "| B         | --  | 100 | 1   | 1   |\n"
        "| C         | 1   | --  | 100 | 100 |\n"
        "| D         | 1   | 1   | --  | 1   |\n"
        "3. What greedy picks:\n"
        "- Greedy picks S -> B -> D -> C -> T which ends up costing 1+1+1+100 = 103\n"
        "4. What optimal picks:\n"
        "- Optimal picks S - > C -> B -> D -> T which ends up costing 2+1+1+1 =5.\n"
        "5. Why greedy loses:\n"
        "- Greedy only considers the next move and saving fuel there making it choose S -> B "
        "instead of C or D. This single choice already locks it in place to end up choosing 100 fuel to get to T. "
        "Choosing to use an extra 1 fuel at the start saves having to use 100 in the end.\n"
        "6. What the algorithm must explore:\n"
        "- It must explore different relic orders as the order is what determines the total fuel cost."
    )


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.
    """
    current_loc = spawn
    relics_remaining = set(relics)
    relics_visited_order = []
    cost_so_far = 0

    # Best stores lowest cost found, best relic order for that cost
    best = [float('inf'), []]

    _explore(
        dist_table,
        current_loc,
        relics_remaining,
        relics_visited_order,
        cost_so_far,
        exit_node,
        best
    )

    return best[0], best[1]


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    # Stop this branch if it is already worse than the best complete route
    if cost_so_far >= best[0]:
        return

    # Base case
    if not relics_remaining:
        exit_cost = dist_table[current_loc][exit_node]

        if exit_cost == float('inf'):
            return

        total_cost = cost_so_far + exit_cost

        if total_cost < best[0]:
            best[0] = total_cost
            best[1] = relics_visited_order.copy()

        return

    # Find the cheapest next move
    cheapest_next = min(
        dist_table[current_loc][relic]
        for relic in relics_remaining
    )

    lower_bound = cost_so_far + cheapest_next

    # This pruning is safe because lower_bound only adds the cheapest required next move
    # so it cannot be larger than the actual remaining cost. If it cannot beat best,
    # this branch cannot become the optimal route.

    if lower_bound >= best[0]:
        return

    # Try each remaining relic as the next relic in the order
    for relic in list(relics_remaining):
        travel_cost = dist_table[current_loc][relic]

        if travel_cost == float('inf'):
            continue

        relics_remaining.remove(relic)
        relics_visited_order.append(relic)

        _explore(
            dist_table,
            relic,
            relics_remaining,
            relics_visited_order,
            cost_so_far + travel_cost,
            exit_node,
            best
        )

        # Undo the choice so the next branch starts clean
        relics_visited_order.pop()
        relics_remaining.add(relic)


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.
    """
    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    return find_optimal_route(dist_table, spawn, relics, exit_node)


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
