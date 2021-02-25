import unittest
from DiGraph import DiGraph


from copy import copy, deepcopy

from api.GraphAlgo import GraphAlgo


class Test_GraphAlgo(unittest.TestCase):

    # Add/Remove nodes and edges
    def test_shortestpath(self):
        gg = DiGraph()
        gg.add_node(1)
        gg.add_node(2)
        gg.add_node(3)
        gg.add_node(4)
        gg.add_node(5)
        gg.add_node(6)
        gg.add_node(7)
        gg.add_edge(1, 2, 10)
        gg.add_edge(2, 3, 9)
        gg.add_edge(5, 7, 2)
        gg.add_edge(2, 1, 3)
        gg.add_edge(3, 4, 2)
        gg.add_edge(4, 5, 9)
        gg.add_edge(1, 5, 90)
        graph3 = GraphAlgo(gg)

        self.assertEqual(graph3.shortest_path(1, 5), (30, [1, 2, 3, 4, 5]))
        self.assertEqual(graph3.shortest_path(2, 3), (9, [2, 3]))

    def test_connected_component(self):
        gg = DiGraph()
        gg.add_node(1)
        gg.add_node(2)
        gg.add_node(3)
        gg.add_node(4)
        gg.add_node(5)
        gg.add_node(6)
        gg.add_node(7)
        gg.add_edge(1, 2, 10)
        gg.add_edge(2, 1, 3)
        gg.add_edge(3, 4, 2)
        gg.add_edge(4, 5, 9)
        gg.add_edge(1, 5, 90)
        graph3 = GraphAlgo(gg)
        lis = [1,2, 5]
        lis2 = [5]
        print(graph3.connected_component(1))
        self.assertEqual(graph3.connected_component(1), lis)
        self.assertEqual(graph3.connected_component(5), lis2)

    def test_connected_components(self):
        gg = DiGraph()
        gg.add_node(1)
        gg.add_node(2)
        gg.add_node(3)
        gg.add_node(4)
        gg.add_edge(1, 2, 5)
        gg.add_edge(1, 3, 5)
        gg.add_edge(2, 3, 5)
        gg.add_edge(3, 4, 5)
        gg.add_edge(4, 4, 5)
        lis = [[1,2,3 ,4], [2,3,4], [3,4], [4]]
        graph3 = GraphAlgo(gg)
        print(graph3.connected_components())
        self.assertEqual(graph3.connected_components(), lis)


if __name__ == 'main':
    unittest.main(verbosity=True)