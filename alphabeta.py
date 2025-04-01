def alphabeta(node, depth, alpha, beta, maximizing_player):
    if isinstance(node, int):  # Base case: leaf node
        return node

    if maximizing_player:
        max_eval = float('-inf')
        for child in node:
            eval_score = alphabeta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break  # Beta cutoff (pruning)
        return max_eval
    else:
        min_eval = float('inf')
        for child in node:
            eval_score = alphabeta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if beta <= alpha:
                break  # Alpha cutoff (pruning)
        return min_eval

# Example tree (depth 2)
tree = [[3, 5], [2, 9]]

# Running the algorithm
print("Game Score:", alphabeta(tree, 2, float('-inf'), float('inf'), True))
