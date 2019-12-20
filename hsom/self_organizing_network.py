from random import sample
import json
from .self_organizing_map import SelfOrganizingMap
from .util import *


class SelfOrganizingNetwork:

    def __init__(self, input_size=None,
                 layer_sizes=[],
                 input_percents=[],
                 learning_rates=[],
                 boost_factors=[],
                 node_counts=[],
                 winner_counts=[],
                 initial_ranges=[]):

        self.input_size = input_size
        self.training = True
        self.outputs = []
        self.links = []
        self.maps = []

        for i in range(len(layer_sizes)):
            self.outputs.append([])
            self.links.append([])
            self.maps.append([])
            input_percent = ith_if_iterable(input_percents, i)
            learning_rate = ith_if_iterable(learning_rates, i)
            boost_factor = ith_if_iterable(boost_factors, i)
            node_count = ith_if_iterable(node_counts, i)
            winner_count = ith_if_iterable(winner_counts, i)

            if isinstance(initial_ranges[0], list) or isinstance(initial_ranges[0], tuple):
                initial_range = initial_ranges[i]
            else:
                initial_range = initial_ranges

            link_count = int(input_size * input_percent)
            layer_size = layer_sizes[i]

            for j in range(layer_size):
                self.maps[i].append(SelfOrganizingMap(
                    learning_rate=learning_rate,
                    boost_factor=boost_factor,
                    input_size=link_count,
                    node_count=node_count,
                    winner_count=winner_count,
                    initial_range=initial_range))
                options = [k for k in range(input_size)]
                links = sample(options, link_count)
                self.links[i].append(links)
            input_size = layer_size * node_count

    def compute_outputs(self, sample):
        inputs = sample
        outputs = None
        for i in range(len(self.outputs)):
            maps = self.maps[i]
            links = self.links[i]
            outputs = []
            for j in range(len(maps)):
                sample = [inputs[j] for j in links[j]]
                output = maps[j].update(sample)
                outputs += output
            inputs = outputs
            self.outputs[i] = outputs
        return outputs

    def set_training(self, training):
        for i in range(len(self.maps)):
            for j in range(len(self.maps[i])):
                self.maps[i][j].set_training(training)

    def update(self, sample):
        output = self.compute_outputs(sample)
        return output

    def train(self, samples):
        for sample in samples:
            self.update(sample)

    def test(self, samples):
        outputs = []
        training = self.training
        self.set_training(False)
        for sample in samples:
            output = self.update(sample)
            outputs.append(output)
        self.set_training(training)
        return outputs

    def load(self, filename):
        data = json.load(open(filename, 'r'))
        input_size = data['input_size']
        layer_sizes = []
        input_percents = []
        learning_rates = []
        boost_factors = []
        node_counts = []
        winner_counts = []
        initial_ranges = []

        for i in range(len(data['layers'])):
            layer_data = data['layers'][i]
            layer_sizes.append(layer_data['layer_size'])
            input_percents.append(layer_data['input_percent'])

            if 'learning_rate' in layer_data:
                learning_rates.append(layer_data['learning_rate'])
            elif 'learning_rate' in data:
                learning_rates.append(data['learning_rate'])
            if 'boost_factor' in layer_data:
                boost_factors.append(layer_data['boost_factor'])
            elif 'boost_factor' in data:
                boost_factors.append(data['boost_factor'])
            if 'node_count' in layer_data:
                node_counts.append(layer_data['node_count'])
            elif 'node_count' in data:
                node_counts.append(data['node_count'])
            if 'winner_count' in layer_data:
                winner_counts.append(layer_data['winner_count'])
            elif 'winner_count' in data:
                winner_counts.append(data['winner_count'])
            if 'initial_range' in layer_data:
                initial_ranges.append(layer_data['initial_range'])
            elif 'initial_range' in data:
                initial_ranges.append(data['initial_range'])

        self.__init__(
            input_size=input_size,
            layer_sizes=layer_sizes,
            input_percents=input_percents,
            learning_rates=learning_rates,
            boost_factors=boost_factors,
            node_counts=node_counts,
            winner_counts=winner_counts,
            initial_ranges=initial_ranges)
        return self
