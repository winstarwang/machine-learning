
### Part 1 - Planning problems
#### An optimal sequence of actions for each problem
+ *An optimal sequence of actions for Problem 1*:
Load(C1, P1, SFO)
Load(C2, P2, JFK)
Fly(P1, SFO, JFK)
Fly(P2, JFK, SFO)
Unload(C1, P1, JFK)
Unload(C2, P2, SFO)
+ *An optimal sequence of actions for Problem 2*:
Load(C1, P1, SFO)
Load(C2, P2, JFK)
Load(C3, P3, ATL)
Fly(P1, SFO, JFK)
Fly(P2, JFK, SFO)
Fly(P3, ATL, SFO)
Unload(C3, P3, SFO)
Unload(C2, P2, SFO)
Unload(C1, P1, JFK)
+ *An optimal sequence of actions for Problem 3*:
Load(C1, P1, SFO)
Load(C2, P2, JFK)
Fly(P1, SFO, ATL)
Load(C3, P1, ATL)
Fly(P2, JFK, ORD)
Load(C4, P2, ORD)
Fly(P2, ORD, SFO)
Fly(P1, ATL, JFK)
Unload(C4, P2, SFO)
Unload(C3, P1, JFK)
Unload(C2, P2, SFO)
Unload(C1, P1, JFK)

#### Experiment and document metrics for non-heuristic planning solution searches
| problem_search_algorithm    | Expansions | Goal Tests | New Nodes | Plan Length | Time Elapsed        | Optimality |
|-----------------------------|------------|------------|-----------|-------------|---------------------|------------|
| p1_breadth_first_search     | 43         | 56         | 180       | 6           | 0.1479521607980132  | yes        |
| p1_depth_first_graph_search | 12         | 13         | 48        | 12          | 0.04838273394852877 | no         |
| p1_uniform_cost_search      | 55         | 57         | 224       | 6           | 0.15380872970446944 | yes        |
| p2_breadth_first_search     | 3343       | 4609       | 30509     | 9           | 50.67819977691397   | yes        |
| p2_depth_first_graph_search | 582        | 583        | 5211      | 575         | 10.1983476821333172 | no         |
| p2_uniform_cost_search      | 4853       | 4855       | 44041     | 9           | 73.01752573437989   | yes        |
| p3_breadth_first_search     | 14663      | 18098      | 129631    | 12          | 279.72873637313023  | yes        |
| p3_depth_first_graph_search | 627        | 628        | 5176      | 596         | 12.452719144988805  | no         |
| p3_uniform_cost_search      | 18223      | 18225      | 159618    | 12          | 337.77189416997135  | yes        |

### Part 2 - Domain-independent heuristics

#### Experiment and document: metrics of A* searches with these heuristics
| problem_search_algorithm               | Expansions | Goal Tests | New Nodes | Plan Length | Time Elapsed        | Optimality |
|----------------------------------------|------------|------------|-----------|-------------|---------------------|------------|
| p1_astar_search_h_1                    | 55         | 57         | 224       | 6           | 0.1326503618620336  | yes        |
| p1_astar_search_h_ignore_preconditions | 41         | 43         | 170       | 6           | 0.24537542089819908 | yes        |
| p1_astar_search_h_pg_levelsum          | 39         | 41         | 158       | 6           | 0.5477283541113138  | yes        |
| p2_astar_search_h_1                    | 4853       | 4855       | 44041     | 9           | 72.75496851885691   | yes        |
| p2_astar_search_h_ignore_preconditions | 1450       | 1452       | 13303     | 9           | 39.75329904491082   | yes        |
| p2_astar_search_h_pg_levelsum          | 1129       | 1131       | 10232     | 9           | 146.2657456761226   | yes        |
| p3_astar_search_h_1                    | 18223      | 18225      | 159618    | 12          | 346.4180222512223   | yes        |
| p3_astar_search_h_ignore_preconditions | 5040       | 5042       | 44944     | 12          | 163.10902196681127  | yes        |
| p3_astar_search_h_pg_levelsum          | 2024       | 2026       | 17913     | 12          | 499.983169474639    | yes        |

### Part 3: Written Analysis
#### Provide an optimal plan for Problems 1, 2, and 3  
- Problem 1: all the plan is optimal except for depth_first_graph_search
- Problem 2: all the plan is optimal except for depth_first_graph_search
- Problem 3: all the plan is optimal except for depth_first_graph_search
#### Compare and contrast non-heuristic search result metrics (optimality, time elapsed, number of node expansions) for Problems 1,2, and 3
For all problems, breadth_first_search and uninform_cost_search are optimal,depth_first_graph_search is not;depth_first_graph_search has the least number of node expansions, breadth_first_search has the second less number of node expansions, and uninform_cost_search has the most number of node expansions; depth_first_graph_search use the least time, uninform_cost_search use the second less time, and uninform_cost_search use the most time; time elapsed is positively related to number of node expansions.
#### Compare and contrast heuristic search result metrics using A* with the "ignore preconditions" and "level-sum" heuristics for Problems 1, 2, and 3
For all problems, astar_search_h_ignore_preconditions has more number of node expansions than astar_search_h_pg_levelsum, but less time elapsed. I think astar_search_h_pg_levelsum use more time because create planning graph need a lot of time.
#### What was the best heuristic used in these problems?  Was it better than non-heuristic search planning methods for all problems?  Why or why not?
- The best heuristic used in these problems is astar_search_h_pg_levelsum. It has the least number of node expansions and the least number of new nodes, this means it can search fast and use less space.
- It is not always better than non-heuristic search planning methods. Depth_first_graph_search has less number of node expansions and less number of new nodes than astar_search_h_pg_levelsum, but it is not an optimal plan. If we need an optimal plan, astar_search_h_pg_levelsum is the best of all.
- Astar_search_h_pg_levelsum need a lot of time to create planning graph in the first time, once the planning graph is finished, all the search will be fast.

### References
[1]: Stuart Russell, Peter Norvig (2010). [Artificial Intelligence: A Modern Approach(Third edition)](http://aima.cs.berkeley.edu/).
[2]: Dr. Frans A. Oliehoek (2017). [COMP219 - Artificial Intelligence](http://www.fransoliehoek.net/teaching/COMP219/)