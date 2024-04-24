import networkx as nx

from graph_pack.constants import ERR_GRAPH_IS_NOT_INV_TREE

UNDISCOVERED = 1
DISCOVERED = 2
PROCESSED = 3


class GraphValidator:
    """Класс для проверки графа на соответствие различным условиям.

    Methods
    -------
    is_inverted_trees(graph: nx.Graph) -> bool:
        Проверяет является ли граф обратно ориентированным деревом или
        лесом из обратно ориентированных деревьев.

    get_tree_count(graph: nx.Graph) -> int:
        Возвращает количество деревьев в графе.

    graph_has_loop(graph: nx.Graph) -> bool:
        Проверяет наличие цикла в графе.
    """

    @staticmethod
    def is_inverted_trees(graph: nx.Graph) -> bool:
        """Проверяет является ли граф обратно ориентированным деревом или
        лесом из обратно ориентированных деревьев."""
        pass

    @staticmethod
    def get_tree_count(graph: nx.Graph) -> int:
        """Возвращает количество деревьев в графе."""
        pass

    @staticmethod
    def graph_has_loop(graph: nx.Graph) -> bool:
        adj = GraphValidator.convert_graph_to_adjacency_list(graph)
        for node in adj.keys():
            states = {node: UNDISCOVERED for node in adj.keys()}
            has_loop = GraphValidator.dfs(node, adj, states)
            if has_loop:
                return True
        return False

    @staticmethod
    def dfs(edge: str, adj: dict[str, set[str]], states: dict[str, int]) -> bool:
        if states[edge] == DISCOVERED:
            return True
        states[edge] = DISCOVERED
        has_loop = False
        for path in adj[edge]:
            has_loop = has_loop or GraphValidator.dfs(path, adj, states)
        states[edge] = PROCESSED
        return has_loop

    @staticmethod
    def convert_graph_to_adjacency_list(graph: nx.Graph) -> dict[str, set[str]]:
        adj = {node: set() for node in graph.nodes()}
        for u, v in graph.edges:
            adj[u].add(v)
        return adj


if __name__ == '__main__':
    graph = nx.DiGraph()
    graph.add_nodes_from(['a', 'b', 'c', 'd'])
    graph.add_edges_from([('c', 'b'), ('b', 'a')])
    matrix = nx.adjacency_matrix(graph).toarray()
    print('Матрица смежности для графа:')
    print(matrix)
    print('Граф является обратно ориентированным деревом/лесом:',
          GraphValidator.is_inverted_trees(graph))
    print('Количество деревьев в графе:',
          GraphValidator.get_tree_count(graph))
    print('Граф содержит петли:',
          GraphValidator.graph_has_loop(graph))

    graph_with_loop = nx.DiGraph()
    graph_with_loop.add_nodes_from(['a', 'b', 'c', 'd'])
    graph_with_loop.add_edges_from([('a', 'b'), ('b', 'c'), ('c', 'd'),
                                    ('d', 'a')])
    matrix = nx.adjacency_matrix(graph_with_loop).toarray()
    print('\nМатрица смежности для графа:')
    print(matrix)
    print('Граф содержит петли:',
          GraphValidator.graph_has_loop(graph_with_loop))
