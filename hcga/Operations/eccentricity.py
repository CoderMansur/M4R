
import networkx as nx
from hcga.Operations import utils
import numpy as np

class Eccentricity():
    """
    Eccentricity class
    """
    def __init__(self, G):
        self.G = G
        self.feature_names = []
        self.features = []
        
    def feature_extraction(self,args):
        """
        Compute eccentricity for each node
        
        The eccentricity of a node is the maximum distance of the node from 
        any other node in the graph.
        
        Parameters
        ----------
        G : graph
          A networkx graph

        args :
            arg[0] Number of bins for calculating pdf of chosen distribution for SSE calculation

        Returns
        -------
        feature_list :list
           List of features related to eccentricity.


        Notes
        -----
        Eccentricity using networkx:
            https://networkx.github.io/documentation/stable/reference/algorithms/distance_measures.html        
        """
        
        # Defining the input arguments
        bins = args[0]
        # Defining featurenames
        feature_names = ['mean','std','opt_model','powerlaw_a','powerlaw_SSE']
        G = self.G
        feature_list = []
        #Calculate the eccentricity of each node
        eccentricity = np.asarray(list(nx.eccentricity(G).values()))
        # Basic stats regarding the eccentricity distribution
        feature_list.append(eccentricity.mean())
        feature_list.append(eccentricity.std())
        
        # Fitting the eccentricity distribution and finding the optimal
        # distribution according to SSE
        opt_mod,opt_mod_sse = utils.best_fit_distribution(eccentricity,bins=bins)
        feature_list.append(opt_mod)

        # Fitting power law and finding 'a' and the SSE of fit.
        feature_list.append(utils.power_law_fit(eccentricity,bins=bins)[0][-2])# value 'a' in power law
        feature_list.append(utils.power_law_fit(eccentricity,bins=bins)[1])# value sse in power law

        
        self.feature_names=feature_names
        self.features = feature_list
       
