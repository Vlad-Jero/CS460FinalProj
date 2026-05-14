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

## Entry 2 – [Date]: [Short description]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

_Your entry here._

---

## Entry 3 – [Date]: [Short description]

_Your entry here._

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

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
