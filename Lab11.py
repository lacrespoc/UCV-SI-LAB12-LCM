def alphabeta(node, alpha, beta, maximizingPlayer):
    if node.is_terminal_node():
        return node.value
    
    if maximizingPlayer:
        value = float('-inf')
        for child in node.children:
            value = max(value, alphabeta(child, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    else:
        value = float ('inf')
        for child in node.children:
            value = min(value, alphabeta(child, alpha, beta, True))
            beta = min(beta, value)
            if alpha >=beta:
                break
        return value
    
# Clase de Nodo
class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []
    
    def is_terminal_node(self):
        return len(self.children) == 0
    
# Ejemplo de uso
root_node = Node(0)
child1 = Node(3)
child2 = Node(5)
child3 = Node(2)
root_node.children = [child1, child2, child3]

alpha = float('-inf')
beta = float('inf')
maximizingPlayer = True

best_value = alphabeta(root_node, alpha, beta, maximizingPlayer)
print (f"El mejor valor encontrado es:{best_value}")