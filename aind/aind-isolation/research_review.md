### Research review for AlphaGo

#### Goals

1. To solve a problem which has an intractable search space and can't be directly approximate using a policy or value function.
2. To make machine can reach a professional level in Go.

#### Techniques

AlphaGo is based on deep neural networks that are trained by a novel combination of supervised and reinforcement learning. It use a new search algorithm that successfully combines neural network evaluations with Monte Carlo rollouts. Finally it integrates these components together, at scale, in a high-performance tree search engine.

1. **Deep Convolutional Neural Networks**
    - use convolutional layers to construct a representation of the position in the board.
    - use these neural networks to reduce the effective depth and breadth of the search tree: evaluating positions using a value network, and sampling actions using a policy network.
2. **Supervised learning of policy networks**:
    - use supervised learning build on prior work on predicting expert moves in the game of Go.
    - finally,trained a 13-layer policy network, which is called SL policy network. 
3. **Reinforcement learning of policy networks**:
    - use reinforcement learning to train a reinforcement learning (RL) policy network pρ that improves the SL policy network by optimizing the final outcome of games of selfplay.
4. **Reinforcement learning of value networks**:
    - use reinforcement learning to train a value network vθ that predicts the winner of games played by the RL policy network against itself.
5. **Monte Carlo tree search (MCTS)**:
    - combines the policy and value networks in an MCTS algorithm that selects actions by lookahead search.
    - uses Monte Carlo rollouts to estimate the value of each state in a search tree.
6. **Asynchronous multi-threaded search** 
    - To efficiently combine MCTS with deep neural networks, AlphaGo uses an asynchronous multi-threaded search that executes simulations on CPUs, and computes policy and value networks in parallel on GPUs.

#### Results

By combining tree search with policy and value networks, AlphaGo has finally reached a professional level in Go, providing hope that human-level performance can now be achieved in other seemingly intractable artificial intelligence domains.


