# -*- coding: utf-8 -*-
# This file is part of hcga.
#
# Copyright (C) 2019, 
# Robert Peach (r.peach13@imperial.ac.uk), 
# Alexis Arnaudon (alexis.arnaudon@epfl.ch), 
# https://github.com/ImperialCollegeLondon/hcga.git
#
# hcga is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# hcga is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with hcga.  If not, see <http://www.gnu.org/licenses/>.

from .feature_class import FeatureClass
from ..feature_utils import summary_statistics
import numpy as np

featureclass_name = 'BasicStats'

class BasicStats(FeatureClass):
    """Basic stats class"""

    def set_infos(self):
        """set class infos"""
        self.modes = ['fast', 'medium', 'slow']
        self.shortname = 'BS'
        self.name = 'basic_stats'
        self.keywords = ''

    def compute_features(self):
        """
        Compute some basic stats of the network

        Computed statistics    
        -----
        Put here the list of things that are computed, with correcponding names

        """

        # basic normalisation parameters
        n_nodes = len(self.graph)
        n_edges = len(self.graph.edges)

        # Adding basic node and edge numbers
        self.features['num_nodes'] = n_nodes
        self.features['num_edges'] = n_edges 

        # Degree stats
        self.features['density'] = 2 * n_edges / (n_nodes * (n_edges - 1))

        degree_vals = list(dict(self.graph.degree()).values())
        summary_statistics(self.features, degree_vals, 'degree')       