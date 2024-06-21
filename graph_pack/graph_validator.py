import networkx as nx
from graph_pack.constants import ERR_GRAPH_IS_NOT_INV_TREE

NOT_VISITED = 1
VISITING = 2
VISITED = 3


class GraphValidator:
    """Класс для проверки графа на соответствие различным условиям."""

    @staticmethod
    def is_inverted_trees(graph: nx.Graph) -> bool:
        """Проверяет является ли граф обратно ориентированным деревом или лесом из обратно ориентированных деревьев."""
        if GraphValidator.graph_has_loop(graph):
            return False

        adj_list = {node: [] for node in graph.nodes()}
        visited = {node: False for node in graph.nodes()}
        trees = []

        for u, v in graph.edges():
            adj_list[u].append(v)
            adj_list[v].append(u)

        for node in graph.nodes:
            if not visited[node]:
                tree = []
                GraphValidator.dfs_collect_trees(node, adj_list, visited, tree)
                trees.append(tree)

        inverted_adj_list = {node: [] for node in graph.nodes()}
        for u, v in graph.edges():
            inverted_adj_list[v].append(u)

        for tree in trees:
            has_multiple_roots = len(tree) > 2
            for node in tree:
                visited = {n: False for n in tree}
                GraphValidator.dfs_check_inversion(inverted_adj_list, node, visited)
                if all(visited.values()):
                    has_multiple_roots = False
                    break
            if has_multiple_roots:
                return False
        return True

    @staticmethod
    def get_tree_count(graph: nx.Graph) -> int:
        """Возвращает количество деревьев в графе."""
        if GraphValidator.graph_has_loop(graph):
            raise ValueError(ERR_GRAPH_IS_NOT_INV_TREE)

        tree_count = 0
        for node in graph.nodes:
            is_root = True
            for u, v in graph.edges:
                if node == u:
                    is_root = False
                    break
            if is_root:
                tree_count += 1
        return max(tree_count, 1)

    @staticmethod
    def graph_has_loop(graph: nx.Graph) -> bool:
        """Проверяет наличие цикла в графе."""
        adj_list = {node: [] for node in graph.nodes()}
        for u, v in graph.edges:
            adj_list[u].append(v)

        for node in adj_list.keys():
            state = {n: NOT_VISITED for n in adj_list.keys()}
            if GraphValidator.dfs_check_cycle(node, adj_list, state):
                return True
        return False

    @staticmethod
    def dfs_check_inversion(adj, node, visited):
        visited[node] = True
        for neighbor in adj[node]:
            if not visited[neighbor]:
                GraphValidator.dfs_check_inversion(adj, neighbor, visited)

    @staticmethod
    def dfs_collect_trees(node, adj_list, visited, tree):
        visited[node] = True
        tree.append(node)
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                GraphValidator.dfs_collect_trees(neighbor, adj_list, visited, tree)

    @staticmethod
    def dfs_check_cycle(node, adj_list, state) -> bool:
        if state[node] == VISITING:
            return True
        state[node] = VISITING
        for neighbor in adj_list[node]:
            if state[neighbor] != VISITED:
                if GraphValidator.dfs_check_cycle(neighbor, adj_list, state):
                    return True
        state[node] = VISITED
        return False
