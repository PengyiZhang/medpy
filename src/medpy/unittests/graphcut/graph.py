"""
Unittest for the medpy.graphcut.graph methods.

!TODO:
- This is more a test for the medpy.graphcut.generate methods than for the Graph objects!
  Change this by writing new tests. Export the old to medpy.unittests.graphcut.generate
- Update and run

@author Oskar Maier
@version d0.2.0
@since 2011-01-19
@status Development
"""

# build-in modules
import unittest

# third-party modules

# own modules
from medpy.graphcut import GCGraph

# code
class TestGraph(unittest.TestCase):
    
    def test_GCGraph(self):
        """
        Test the @link medpy.graphcut.graph.GCGraph implementation.
        """
        # set test parmeters
        nodes = 10
        edges = 20
        
        # construct graph
        graph = GCGraph(nodes, edges) # nodes edges
        
        # SETTER TESTS
        # set_source_nodes should accept a sequence and raise an error if an invalid node id was passed
        graph.set_source_nodes(range(0, nodes))
        self.assertRaises(ValueError, graph.set_source_nodes, [-1])
        self.assertRaises(ValueError, graph.set_source_nodes, [nodes])
        # set_sink_nodes should accept a sequence and raise an error if an invalid node id was passed
        graph.set_sink_nodes(range(0, nodes))
        self.assertRaises(ValueError, graph.set_sink_nodes, [-1])
        self.assertRaises(ValueError, graph.set_sink_nodes, [nodes])
        # set_nweight should accept integers resp. floats and raise an error if an invalid node id was passed or the weight is zero or negative
        graph.set_nweight(0, nodes-1, 1, 2)
        graph.set_nweight(nodes-1, 0, 0.5, 1.5)
        self.assertRaises(ValueError, graph.set_nweight, -1, 0, 1, 1)
        self.assertRaises(ValueError, graph.set_nweight, 0, nodes, 1, 1)
        self.assertRaises(ValueError, graph.set_nweight, 0, 0, 1, 1)
        self.assertRaises(ValueError, graph.set_nweight, 0, nodes-1, 0, 0)
        self.assertRaises(ValueError, graph.set_nweight, 0, nodes-1, -1, -2)
        self.assertRaises(ValueError, graph.set_nweight, 0, nodes-1, -0.5, -1.5)
        # set_nweights works as set_nweight but takes a dictionary as argument
        graph.set_nweights({(0, nodes-1): (1, 2)})
        graph.set_nweights({(nodes-1, 0): (0.5, 1.5)})
        self.assertRaises(ValueError, graph.set_nweights, {(-1, 0): (1, 1)})
        self.assertRaises(ValueError, graph.set_nweights, {(0, nodes): (1, 1)})
        self.assertRaises(ValueError, graph.set_nweights, {(0, 0): (1, 1)})
        self.assertRaises(ValueError, graph.set_nweights, {(0, nodes-1): (0, 0)})
        self.assertRaises(ValueError, graph.set_nweights, {(0, nodes-1): (-1, -2)})
        self.assertRaises(ValueError, graph.set_nweights, {(0, nodes-1): (-0.5, -1.5)})
        # set_tweight should accept integers resp. floats and raise an error if an invalid node id was passed or the weight is zero or negative
        graph.set_tweight(0, 1, 2)
        graph.set_tweight(nodes-1, 0.5, 1.5)
        graph.set_tweight(0, -1, -2)
        graph.set_tweight(0, 0, 0)
        self.assertRaises(ValueError, graph.set_tweight, -1, 1, 1)
        self.assertRaises(ValueError, graph.set_tweight, nodes, 1, 1)
        # set_tweights works as set_tweight but takes a dictionary as argument
        graph.set_tweights({0: (1, 2)})
        graph.set_tweights({nodes-1: (0.5, 1.5)})
        graph.set_tweights({0: (-1, -2)})
        graph.set_tweights({0: (0, 0)})
        self.assertRaises(ValueError, graph.set_tweights, {-1: (1, 1)})
        self.assertRaises(ValueError, graph.set_tweights, {nodes: (1, 1)})
        
        # SOME MINOR GETTERS
        self.assertEqual(graph.get_node_count(), nodes)
        self.assertEqual(graph.get_edge_count(), edges)
        self.assertSequenceEqual(graph.get_nodes(), range(0, nodes))
        
        
#    
#    __label_image_wr = [[0, 1, 2, 2, 9],
#                        [0, 3, 2, 7, 9],
#                        [4, 4, 5, 6, 9],
#                        [5, 5, 5, 8, 9]]
#    __label_image = [[ 1,  2,  3,  3, 10],
#                     [ 1,  4,  3,  8, 10],
#                     [ 5,  5,  6,  7, 10],
#                     [ 6,  6,  6,  9, 10]]
#    __fg_marker = [[1, 0, 0, 0, 0],
#                   [1, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0]]
#    __bg_marker = [[0, 0, 0, 0, 1],
#                   [0, 0, 0, 0, 1],
#                   [0, 0, 0, 0, 1],
#                   [0, 0, 0, 0, 1]]
#    
#    def _test_graph_from_labels_errors(self):
#        """
#        Tests the attribute and other errors of @link medpy.graphcut.graph.graph_from_labels()
#        to be thrown correctly.
#        """
#        # raise error if the label image is wrongly labeled
#        self.assertRaises(AttributeError, graph_from_labels, self.__label_image_wr, self.__fg_marker, self.__bg_marker, boundary_term=self.__boundary_term)
#        
#    
#    def test_graph_from_labels_w_boundary(self):
#        """
#        Tests the @link medpy.graphcut.graph.graph_from_labels() function using a boundary term and no
#        regional term.
#        """
#        label_image = self.__label_image
#        graph = graph_from_labels(label_image,
#                                  self.__fg_marker,
#                                  self.__bg_marker,
#                                  boundary_term=self.__boundary_term)
#        
#        # recreate expected results
#        mapping = self.__get_mapping()
#        li = scipy.asarray(label_image)
#        nodes = scipy.unique(li)
#        edges = mapping.keys()
#        weights = mapping
#        fg = scipy.asarray(self.__fg_marker)
#        bg = scipy.asarray(self.__bg_marker)
#        fg = scipy.unique(li[fg.astype(scipy.bool_)])
#        bg = scipy.unique(li[bg.astype(scipy.bool_)])
#        
#        # check resulting graph for correctness
#        for node in nodes:
#            self.assertIn(node, graph.get_nodes(), '{} expected, but not in resulting nodes'.format(node))
#        for node in graph.get_nodes():
#            self.assertIn(node, nodes, '{} found in resulting nodes, but not expected'.format(node))
#        
#        sorted_edges = [tuple(sorted(x)) for x in graph.get_edges()]
#        
#        for edge in edges:
#            self.assertIn(edge, sorted_edges, '{} expected, but not in resulting edges'.format(edge))
#        for edge in sorted_edges:
#            self.assertIn(edge, edges, '{} found in resulting edges, but not expected'.format(edge))
#            
#        for key in weights:
#            if key in graph.get_nweights():
#                self.assertEqual(graph.get_nweights()[key], weights[key], 'Expected a weight of {}, found {} for edge {}'.format(weights[key], graph.get_nweights()[key], key))
#            else:
#                key_rev = (key[1], key[0])
#                self.assertEqual(graph.get_nweights()[key_rev], weights[key], 'Expected a weight of {}, found {} for edge {}'.format(weights[key], graph.get_nweights()[key_rev], key))
#            
#        for key in graph.get_tweights():
#            if key in fg:
#                self.assertEqual((graph.MAX, 0), graph.get_tweights()[key], 'Weight of source node {} wrong: is {}, should be {}'.format(key, graph.get_tweights()[key], (graph.MAX, 0)))
#            elif key in bg:
#                self.assertEqual((0, graph.MAX), graph.get_tweights()[key], 'Weight of sink node {} wrong: is {}, should be {}'.format(key, graph.get_tweights()[key], (0, graph.MAX)))
#            else:
#                self.assertEqual((0, 0), graph.get_tweights()[key], 'Weight of source/sink node {} wrong: is {}, should be {}'.format(key, graph.get_tweights()[key], ((0, 0), 0)))
#                
#        # run self test
#        inconsistent = graph.inconsistent()
#        if True == inconsistent: msg = '\n'.join(inconsistent)
#        else: msg = ''
#        self.assertFalse(inconsistent, 'The graph reports itself as being inconsistent. Reasons: {}'.format(msg))
#    
#    def test_graph_from_labels_nd(self):
#        """
#        Check the multi-dimensional capabilities of @link medpy.graphcut.graph.graph_from_labels()
#        up to the fourth dimension. (assuming ndim*2-connectedness)
#        """
#        # 1D
#        image1d = [1,2,2,3]
#        edges1d = [(1,2),(2,3)]
#        graph = graph_from_labels(image1d, scipy.zeros_like(image1d), scipy.zeros_like(image1d))
#        if graph.inconsistent():
#            self.fail('1D: The graph reports itself as being inconsistent. Reasons: {}'.format('\n'.join(graph.inconsistent())))
#        self.__compare_edges(edges1d, graph.get_edges(), '1D: Edge {} expected but did not got extracted.')
#        self.__compare_edges(graph.get_edges(), edges1d, '1D: Edge {} got extracted but was not expected.')
#                
#        # 2D
#        image2d = [[1,2,3,4],
#                   [2,2,3,4],
#                   [2,2,2,5]]
#        edges2d = [(1,2),(2,3),(2,5),(3,4),(4,5)]
#        graph = graph_from_labels(image2d, scipy.zeros_like(image2d), scipy.zeros_like(image2d))
#        if graph.inconsistent():
#            self.fail('2D: The graph reports itself as being inconsistent. Reasons: {}'.format('\n'.join(graph.inconsistent())))
#        self.__compare_edges(edges2d, graph.get_edges(), '2D: Edge {} expected but did not got extracted.')
#        self.__compare_edges(graph.get_edges(), edges2d, '2D: Edge {} got extracted but was not expected.')
#        
#        # 3D
#        image3d = [[[1,2,3,4],
#                    [2,2,3,4],
#                    [2,2,2,5]],
#                   [[2,2,2,5],
#                    [2,2,2,5],
#                    [2,2,2,6]]]
#        edges3d = [(1,2),(2,3),(2,5),(2,6),(3,4),(4,5),(5,6)]
#        graph = graph_from_labels(image3d, scipy.zeros_like(image3d), scipy.zeros_like(image3d))
#        if graph.inconsistent():
#            self.fail('3D: The graph reports itself as being inconsistent. Reasons: {}'.format('\n'.join(graph.inconsistent())))
#        self.__compare_edges(edges3d, graph.get_edges(), '3D: Edge {} expected but did not got extracted.')
#        self.__compare_edges(graph.get_edges(), edges3d, '3D: Edge {} got extracted but was not expected.')
#                
#        # 4D
#        image4d = [[[[1,2,3,4],
#                     [2,2,3,4],
#                     [2,2,2,5]],
#                    [[2,2,2,5],
#                     [2,2,2,5],
#                     [2,2,2,2]]],
#                   [[[2,2,7,7],
#                     [2,7,7,7],
#                     [7,7,7,2]],
#                    [[7,7,7,7],
#                     [7,7,2,2],
#                     [7,7,2,6]]]]
#        edges4d = [(1,2),(2,3),(2,5),(2,6),(2,7),(3,4),(3,7),(4,5),(4,7),(5,7)]
#        graph = graph_from_labels(image4d, scipy.zeros_like(image4d), scipy.zeros_like(image4d))
#        if graph.inconsistent():
#            self.fail('4D: The graph reports itself as being inconsistent. Reasons: {}'.format('\n'.join(graph.inconsistent())))
#        self.__compare_edges(edges4d, graph.get_edges(), '4D: Edge {} expected but did not got extracted.')
#        self.__compare_edges(graph.get_edges(), edges4d, '4D: Edge {} got extracted but was not expected.')
#        
#    def __compare_edges(self, edges1, edges2, message):
#        "Edge comparison taking reversed versions into account."
#        for edge in edges1:
#            if not edge in edges2:
#                if not (edge[1], edge[0]) in edges2:
#                    self.fail(message.format(edge))
#    
#    def __boundary_term(self, label_image, r1_bb, r2_bb, r1_id, r2_id, boundary_term_args):
#        "The boundary term function used for this tests."
#        tpl1 = (r1_id, r2_id)
#        tpl2 = (r2_id, r1_id)
#        
#        mapping = self.__get_mapping()
#    
#        if tpl1 in mapping: return mapping[tpl1]
#        else: return mapping[tpl2]
#    
#    def __get_mapping(self):
#        "Returns a dict holding the edge to weight mappings."
#        mapping = {}
#        mapping[(1, 2)] = 5
#        mapping[(1, 4)] = 7
#        mapping[(1, 5)] = 11
#        mapping[(2, 3)] = 6
#        mapping[(2, 4)] = 4
#        mapping[(3, 4)] = 9
#        mapping[(3, 6)] = 1 # edge that has to be removed later
#        mapping[(3, 8)] = 2
#        mapping[(3, 10)] = 6
#        mapping[(4, 5)] = 3
#        mapping[(5, 6)] = 8
#        mapping[(6, 7)] = 5
#        mapping[(6, 9)] = 3
#        mapping[(7, 8)] = 3
#        mapping[(7, 9)] = 7
#        mapping[(7, 10)] = 1 # edge that has to be removed later
#        mapping[(8, 10)] = 8
#        mapping[(9, 10)] = 5
#        
#        return mapping
    
if __name__ == '__main__':
    unittest.main()
