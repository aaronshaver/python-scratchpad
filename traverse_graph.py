import unittest

graph = {
    "a": ["b", "c"],
    "b": ["f"],
    "c": ["h"],
    "d": [],
    "e": ["g", "d"], # bidirectional
    "f": [],
    "g": ["e"], # bidirectional
    "h": ["d"]
}

def traverse(graph, start, nodes=None):
    """ returns list of all connected nodes beginning from node entry point """
    if not nodes:
        nodes = []
        nodes.append(start)
    if graph[start] == []:
        return nodes
    for child in graph[start]:
        if not child in nodes:  # prevent infinite loop
            nodes.append(child)
            traverse(graph, child, nodes)
    return nodes


class TestTraverse(unittest.TestCase):

    def test_start_node_has_0_children(self):
        self.assertEqual(['d'], traverse(graph, 'd'))

    def test_start_node_has_1_child(self):
        self.assertEqual(['b', 'f'], traverse(graph, 'b'))

    def test_start_node_has_1_child_which_in_turn_has_1_child(self):
        self.assertEqual(['c', 'h', 'd'], traverse(graph, 'c'))

    def test_bidirectional_edge_case0(self):
        self.assertEqual(['g', 'e', 'd'], traverse(graph, 'g'))

    def test_bidirectional_edge_case1(self):
        self.assertEqual(['e', 'g', 'd'], traverse(graph, 'e'))

if __name__ == "__main__":
    unittest.main()
