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
        if GraphValidator.graph_has_loop(graph):
            return False

        obj = {}
        visited = {}
        trees = []

        for node in graph.nodes():
            obj[node] = []
            visited[node] = False
        for edge in graph.edges():
            obj[edge[0]].append(edge[1])
            obj[edge[1]].append(edge[0])

        for node in graph.nodes:
            if not visited[node]:
                tree = []
                visited[node] = True
                GraphValidator.get_trees_dfs(node, obj, visited, tree)
                trees.append(tree)

        inverted_obj = {}
        for node in graph.nodes():
            inverted_obj[node] = []
        for edge in graph.edges():
            inverted_obj[edge[1]].append(edge[0])
        for tree in trees:
            flag = len(tree) > 2
            for node in tree:
                visited = {}
                for node2 in tree:
                    visited[node2] = False
                GraphValidator.dfs_util(inverted_obj, node, visited)
                if all(visited.values()):
                    flag = False
                    break
            if flag:
                return False
        return True

    @staticmethod
    def get_tree_count(graph: nx.Graph) -> int:
        """Возвращает количество деревьев в графе."""
        if GraphValidator.graph_has_loop(graph):
            raise ValueError(ERR_GRAPH_IS_NOT_INV_TREE)
        count = 0
        for node in graph:
            is_root = True
            for edge in graph.edges:
                if node == edge[0]:
                    is_root = False
            if is_root:
                count += 1
        return max(count, 1)

    @staticmethod
    def graph_has_loop(graph: nx.Graph) -> bool:
        """Проверяет наличие цикла в графе."""
        obj = {}
        for node in graph.nodes():
            obj[node] = []
        for edge in graph.edges:
            obj[edge[0]].append(edge[1])

        for node in obj.keys():
            states = {}
            for node2 in obj.keys():
                states[node2] = UNDISCOVERED
            if GraphValidator.dfs(node, obj, states):
                return True
        return False

    @staticmethod
    def dfs_util(adj, node, visited):
        visited[node] = True
        for path in adj[node]:
            if not visited[path]:
                GraphValidator.dfs_util(adj, path, visited)

    @staticmethod
    def get_trees_dfs(key, obj, visited, tree):
        visited[key] = True
        tree.append(key)

        for item in obj[key]:
            if not visited[item]:
                GraphValidator.get_trees_dfs(item, obj, visited, tree)


    @staticmethod
    def dfs(key, obj, states) -> bool:
        if states[key] == DISCOVERED:
            return True
        states[key] = DISCOVERED

        for item in obj[key]:
            if GraphValidator.dfs(item, obj, states):
                return True
        states[key] = PROCESSED
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
          GraphValidator.graph_has_loop(graph_with_loop)