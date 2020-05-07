"""Assortativity class."""
import networkx as nx
from networkx.algorithms import assortativity

from ..feature_class import FeatureClass, InterpretabilityScore

featureclass_name = "Assortativity"


class Assortativity(FeatureClass):
    """Assortativity class."""

    modes = ["fast", "medium", "slow"]
    shortname = "AS"
    name = "assortativity"
    encoding = "networkx"

    def compute_features(self):
        """Compute the assortativity of the network structure.

        Computed statistics
        -----
        Put here the list of things that are computed, with corresponding names
        """

        # Adding basic node and edge numbers
        self.add_feature(
            "degree_assortativity_coeff",
            lambda graph: nx.degree_assortativity_coefficient(graph),
            "Similarity of connections in the graph with respect to the node degree",
            InterpretabilityScore(4),
        )

        self.add_feature(
            "degree_assortativity_coeff_pearson",
            lambda graph: nx.degree_pearson_correlation_coefficient(graph),
            "Similarity of connections in the graph with respect to the node degree",
            InterpretabilityScore(4),
        )

        average_neighbor_degree = lambda graph: list(
            assortativity.average_neighbor_degree(graph).values()
        )
        self.add_feature(
            "degree assortativity",
            average_neighbor_degree,
            "average neighbor degree",
            InterpretabilityScore(4),
            statistics="centrality",
        )
