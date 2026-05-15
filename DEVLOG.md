# Development Log – The Torchbearer

**Student Name:** Vlad Jerohhin
**Student ID:** 10723710

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – May 13: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

_I started by reading the assignment instructions and checking how the code and files are connected. I plan to work in the assignment order; first understand the problem and write the initial explanation, then implement source selection and dijkstra, and then move into the route search and pruning. I expect the hardest part to be making the recursive search explore all valid relic orders without accidentally pruning an optimal route. I will test each step using the provided tests in the torchbearerr file and make any modifications needed from there._

---

## Entry 2 – May 14: Mapping

_Wrote the precompuation logic. I decided which nodes need Dijkstra runs and how the distances should be stored. I chose the entrance and each relic as source nodes because the route search only needs costs from the start and from relic to relic. I used a nested dictionary for the distance table so the search can quickly look up costs. I implemented Dijkstra with a priority queue._

---

## Entry 3 – May 14: Wrong assumption with table

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

_To answer part 4 I had to create a counter example to show greedy fail. I intended to use the example table provided in assignment.md as instrctions stated we can use it, however I came across an issue when tracing the nodes and realised there was an error in the example routes and that the specific table layout was actually perfect for greedy, which would not serve as a counter example. I modified the table; changing C -> T to be value 100 instead of 1, and then changed D -> T to be 1 instead of 100. This modified table showed how greedy can fail and how much better the optimal solution was. Using the provided table would not have been satisfactory to answer part 4._

---

## Entry 4 – May 14: Route search and prune implementation

_I implemented the recursive search for parts 5 and 6 by tracking the current location, remaining relics, visited order, and cost so far. At first, I considered only checking the best so far value after a full route reached the exit, but that would still waste time exploring branches that were already too expensive. I changed the design so the search stops early when the current cost or lower bound estimate cannot beat the best route already found. This final version still considers the relic orders needed to find the best route but it avoids continuing down branches that cannot possibly improve the answer._

---

## Entry 5 – May 14: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_After finishing the implementation, I tested the full pipeline using the provided tests in torchbearer.py. If I had more time I would improve the pruning by using a stronger lower bound estimate such as considering more of the remaining relic to relic costs instead of only the cheapest next move. I would also consider returning the full room by room path, not just the ordered relic list, since Dijkstra currently gives the costs but does not reconstruct the actual paths. Overall, the main design works by precomputing shortest paths first, then searching relic orders while cutting off branches that cannot beat the best route found._

---

## Final Entry – May 14: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | |
| Part 2: Precomputation Design | |
| Part 3: Algorithm Correctness | |
| Part 4: Search Design | |
| Part 5: State and Search Space | |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | |
| **Total** | |
