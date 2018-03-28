
## STRIPS
In artificial intelligence, STRIPS (Stanford Research Institute Problem Solver) is an automated planner developed by Richard Fikes and Nils Nilsson in 1971 at SRI International. STRIPS represents the world as a set of formulae in first-order logic. Each state in the search space consists of a world model and set of goals to be achieved. STRIPS had a mechanism for learning, which consisted of generalizing found plans and storing them. This was essentially a form of explanation-based learning in which constants were changed to variables whenever possible. STRIPS was later used to refer to the formal language of the inputs to this planner. This language is the base for most of the languages for expressing automated planning problem instances in use today; such languages are commonly known as action languages.

## Graphplan
Graphplan is a planner which plans in STRIPS-like domains.The algorithm begins by explicitly constructing a compact structure we call a Planning Graph. A Planning Graph encodes the planning problem in such a way that many useful constraints inherent in the problem become explicitly available to reduce the amount of search needed. Graphplan outperforms the total-order planner, Prodigy, and the partial-order planner, UCPOP,on a variety of interesting natural and artificial planning problems. Since searches made by this approach are fundamentally different from the searches of other common planning methods, they provide a new perspective on the planning problem.

## HSP
Heuristic search planners like HSP transform planning problems into problems of heuristic search by automatically extracting heuristics from Strips encodings. They differ from specialized problem solvers in use of a general declarative language for stating problems and a general mechanism for extracting heuristics from these representations. Planners must offer good modeling language for expressing problems in a convenient way, and general solvers for operating on those representations and producing efficient solutions.A concrete challenge is to reduce the gap in performance between heuristic search planners and specialized problem solvers.

### References
[1]: Richard E. Fikes, Nils J. Nilsson (Winter 1971). [STRIPS: A New Approach to the Application of Theorem Proving to Problem Solving](http://ai.stanford.edu/~nilsson/OnlinePubs-Nils/PublishedPapers/strips.pdf).
[2]: Avrim L. Blum, Merrick L. Furst (1997). [Fast Planning Through Planning Graph Analysis](http://www.cs.cmu.edu/~avrim/Papers/graphplan.pdf)
[3]: Blai Bonet ∗, Héctor Geffner (15 February 2000). [Planning as heuristic search](http://www.cs.toronto.edu/~sheila/2542/s14/A1/bonetgeffner-heusearch-aij01.pdf)

