from geosolver.utils import display_graph

__author__ = 'minjoon'


class SemanticForest(object):
    def __init__(self, grounded_syntax, graph_nodes, forest_graph):
        self.grounded_syntax = grounded_syntax
        self.forest_graph = forest_graph
        self.basic_ontology = grounded_syntax.basic_ontology
        self.grounded_tokens = grounded_syntax.grounded_tokens
        self.graph_nodes = graph_nodes

    def display_graph(self):
        display_graph(self.forest_graph)


class SemanticRelation(object):
    def __init__(self, from_grounded_token, to_grounded_token,
                 arg_idx, grounded_syntax_path, ontology_path):
        self.from_grounded_token = from_grounded_token
        self.to_grounded_token = to_grounded_token
        self.arg_idx = arg_idx
        self.grounded_syntax_path = grounded_syntax_path
        self.grounded_syntax = grounded_syntax_path.grounded_syntax
        self.ontology_path = ontology_path
        self.basic_ontology = from_grounded_token.basic_ontology
        self.key = (arg_idx, ontology_path.key)
        self.id = (from_grounded_token.key, to_grounded_token.key) + self.key

    def __repr__(self):
        return "%s(%r, %r)" % (self.__class__.__name__, self.grounded_syntax_path, self.ontology_path)


class TypeRelation(object):
    def __init__(self, from_type, to_grounded_token, ontology_path):
        self.from_type = from_type
        self.to_grounded_token = to_grounded_token
        self.ontology_path = ontology_path
        self.key = ontology_path.key
        self.id = (from_type.name, to_grounded_token.key, self.key)
        self.basic_ontology = to_grounded_token.basic_ontology


class SemanticTree(object):
    def __init__(self, semantic_forest, tree_graph, grounded_syntax_cost, ontology_cost):
        self.semantic_forest = semantic_forest
        self.tree_graph = tree_graph
        self.grounded_syntax_cost = grounded_syntax_cost
        self.ontology_cost = ontology_cost

    def display_graph(self):
        display_graph(self.tree_graph)
