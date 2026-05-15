# The Torchbearer

**Student Name:** Vlad Jerohhin
**Student ID:** 130785223
**Course:** CS 460 – Algorithms | Spring 2026

---

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**
  _A standard shortest-path algorithm can find the cheapest way to reach one specific spot, but cannot determine which relic should be visited first and so on to minimize the overall journey. It lacks the logic to decide which relic to grab first, second, etc to make the entire trip more efficient._

- **What decision remains after all inter-location costs are known:**
  _After knowing the cheapst travel costs, we still have to figure out the best order to visit them._

- **Why this requires a search over orders (one sentence):**
  _This problem requires a search over orders because different relic orders can have different total costs even when we know the distance from point to point._

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source |
|---|---|
| _Entrance; S_ | _We have to know the fuel cost to reach the first relic from our starting point._ |
| _Relic chambers; M_ | _We need the travel costs between every relic to decide which sequence is the cheapest._ |

### Part 2b: Distance Storage

| Property | Your answer |
|---|---|
| Data structure name | Nested dictionary |
| What the keys represent | The "from" and "to" nodes |
| What the values represent | The minimum fuel cost |
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Using nested hash table dictionaries allows us to jump straight to a pre calulcated value without searching.|

### Part 2c: Precomputation Complexity

- **Number of Dijkstra runs:** _k + 1_
- **Cost per run:** _O(m log n)_
- **Total complexity:** _O((k+1) * m log n)_
- **Justification (one line):** _Dijkstra is run once for the entrance and once for each of the k relic chambers._

---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means


- **For nodes already finalized (in S):**
  _Once a node is finalized, its distance value is locked in as the cheapest possible distance from the source and we are sure there is no better path that exists._

- **For nodes not yet finalized (not in S):**
  _These nodes can still improve, their current distance value is the best path found so far based on finalized nodes._

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
  _Before the first loop, no nodes have been finalized and the source starts at distance 0. Every other node starts at infinity, which is technically the shortest path in an empty set of finalized nodes._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _By always picking the node with the smallest current distance, we ensure it's finalized because nonnegative edge weights mean no future path could ever loop back and be cheaper than the one we just found._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _When the priority queue is empty, every reachable node has been finalized with its confirmed shortest path distance._

### Part 3c: Why This Matters for the Route Planner

_Correct shortest path distances matter because the route planner uses those distances to compare relic orders and choose the lowest fuel route to ensure the torchbearerr does not run out fuel before the exit._

---

## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:** _A greedy strategy only looks at the next closest relic and ignores how that choice might lead to a dead end or an expensive path later in the sequence._
- **Counter-example setup:** _Using this example table, assume we have 2 algoritms; greedy and optimal._

| From \ To | B   | C   | D   | T   |
|-----------|-----|-----|-----|-----|
| S         | 1   | 2   | 2   | --  |
| B         | --  | 100 | 1   | 1   |
| C         | 1   | --  | 100 | 100 |
| D         | 1   | 1   | --  | 1   |

- **What greedy picks:** _Greedy picks S -> B -> D -> C -> T which ends up costing 1+1+1+100 = 103._
- **What optimal picks:** _Optimal picks S - > C -> B -> D -> T which ends up costing 2+1+1+1 =5._
- **Why greedy loses:** _Greedy only considers the next move and saving fuel there making it choose S -> B instead of C or D. This single choice already locks it in place to end up choosing 100 fuel to get to T. Choosing to use an extra 1 fuel at the start saves having to use 100 in the end._

### What the Algorithm Must Explore

- _It must explore different relic orders as the order is what determines the total fuel cost._

---

## Part 5: State and Search Space

### Part 5a: State Representation

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | current_loc | node | The node where the torchbearer is currently locacted.|
| Relics already collected | relics_visited_order | list[node] | The relics collected so far, stored in the order they were visited.|
| Fuel cost so far | cost_so_far | float | The total fuel used by the current route.|

### Part 5b: Data Structure for Visited Relics

| Property | Your answer |
|---|---|
| Data structure chosen | Set |
| Operation: check if relic already collected | Time complexity: O(1) |
| Operation: mark a relic as collected | Time complexity: O(1) |
| Operation: unmark a relic (backtrack) | Time complexity: O(1) |
| Why this structure fits | A set makes it fast to remove a relic when it is chosen and add it back when backtracking. |

### Part 5c: Worst-Case Search Space

- **Worst-case number of orders considered:** _k!._
- **Why:** _In the worst case, the algorithm may need to try every possible ordering of the k relics._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

- **What is tracked:** _The algorithm tracks the cheapest complete route found during a search._
- **When it is used:** _It is used every time the search considers moving to a new relic. It compares the current fuel to this best known total._
- **What it allows the algorithm to skip:** _It allows the algorithm to skip any partial route whose current cost is already greater than or equal to the best complete route found so far._

### Part 6b: Lower Bound Estimation

- **What information is available at the current state:** _The algorithm knows the current location, the relics still remaining, and the fuel already spent._
- **What the lower bound accounts for:** _The lower bound uses the current fuel cost plus the cheapest possible next move._
- **Why it never overestimates:** _It only adds a minimum possible required cost so the real cost to finish the route can only be equal to or higher than this estimate._

### Part 6c: Pruning Correctness

- _Pruning is safe because we only discard a branch when its current cost or lower bound estimate cannot beat the best complete route already found._

---

## References

- _Lecture notes only._