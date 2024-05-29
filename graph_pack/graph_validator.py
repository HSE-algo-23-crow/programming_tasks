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
        if not nx.is_directed_acyclic_graph(graph):
            return False
        for component in nx.weakly_connected_components(graph):
            subgraph = graph.subgraph(component)
            if not nx.is_tree(subgraph.to_undirected()):
                print(f"Component {component} is not a tree.")
                return False
        return True

    @staticmethod
    def get_tree_count(graph: nx.Graph) -> int:
        """Возвращает количество деревьев в графе."""
        if not nx.is_directed_acyclic_graph(graph):
            raise ValueError(ERR_GRAPH_IS_NOT_INV_TREE)
        return nx.number_weakly_connected_components(graph)

    @staticmethod
    def graph_has_loop(graph: nx.Graph) -> bool:
        """Проверяет наличие цикла в графе."""
        try:
            nx.find_cycle(graph)
            return True
        except nx.NetworkXNoCycle:
            return False


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
