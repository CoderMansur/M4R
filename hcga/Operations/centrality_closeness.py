
from networkx.algorithms import centrality
from hcga.Operations import utils
import numpy as np



class ClosenessCentrality():
    """
    Closeness centrality class
    """
 
    def __init__(self, G):
        self.G = G
        self.feature_names = []
        self.features = []

    def feature_extraction(self):
        """
        Compute the closeness centrality for nodes.
        
        The closeness centrality for a node is the reciprocal of the mean 
        distance to all other reachable nodes.
        
        Parameters
        ----------
        G : graph
          A networkx graph

        args :
            arg[0] Number of bins for calculating pdf of chosen distribution for SSE calculation

        Returns
        -------
        feature_list :list
           List of features related to closeness centrality.


        Notes
        -----
        Closeness centrality calculations using networkx:
            https://networkx.github.io/documentation/stable/reference/algorithms/centrality.html
        """        
                
        # Defining the input arguments
        bins = [10,20,50]

        """# Defining featurenames
        feature_names = ['mean','std','max','min']
        """

        G = self.G

        feature_list = {}

        #Calculate the closeness centrality of each node
        closeness_centrality = np.asarray(list(centrality.closeness_centrality(G).values()))

        # Basic stats regarding the closeness centrality distribution
        feature_list['mean'] = closeness_centrality.mean()
        feature_list['std'] = closeness_centrality.std()
        feature_list['max'] = closeness_centrality.max()
        feature_list['min'] = closeness_centrality.min()
        
        for i in range(len(bins)):
            """# Adding to feature names
            feature_names.append('opt_model_{}'.format(bins[i]))
            feature_names.append('powerlaw_a_{}'.format(bins[i]))
            feature_names.append('powerlaw_SSE_{}'.format(bins[i]))"""
            
            # Fitting the closeness centrality distribution and finding the optimal
            # distribution according to SSE
            opt_mod,opt_mod_sse = utils.best_fit_distribution(closeness_centrality,bins=bins[i])
            feature_list['opt_model_{}'.format(bins[i])] = opt_mod

            # Fitting power law and finding 'a' and the SSE of fit.
            feature_list['powerlaw_a_{}'.format(bins[i])] = utils.power_law_fit(closeness_centrality,bins=bins[i])[0][-2]# value 'a' in power law
            feature_list['powerlaw_SSE_{}'.format(bins[i])] = utils.power_law_fit(closeness_centrality,bins=bins[i])[1] # value sse in power law

        
        # Fitting normal distribution and finding...


        # Fitting exponential and finding ...
        """
        self.feature_names=feature_names
        """
        self.features = feature_list
