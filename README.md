# Hierarchical Self-Organizing Maps

A hierarchical self-organizing map (HSOM) is an unsupervised neural network that learns patterns from high-dimensional space and represents them in lower dimensions. 

HSOM networks recieve inputs and feed them into a set of self-organizing maps, each learning individual features of the input space. These maps produce sparse output vectors with only the most responsive nodes activating, a result of competitive inhibition which restricts the number of 'winners' (i.e. active nodes) allowed at any given time.

Each layer in an HSOM network contains a set of maps that view part of the input space and generate sparse output vectors, which together form the input for the next layer in the hierarchy. Information becomes increasingly abstract as it is passed through the network and ultimately results in a low-dimensional sparse representation of the original data.

# Description 
Self-organizing maps are useful because they automatically reduce the dimensionality of whatever data is being observed. However, if the dimensionality of the data in question is sufficiently high, a single self-organizing map will fail to reduce it while maintaining an accurate representation in the process.

The solution is to combine many self-organizing maps into one, giant structure. SOMs can be arranged in a hierarchy, wherein each layer of the hierarchy contains a set of SOMs that receive input from the previous layer and produce output to the next. 

![](https://github.com/CarsonScott/self-organizing-map/blob/master/images/layer.PNG)

At the bottom of the hierarchy, SOMs receive raw data as input just as a typical singular SOM would do. Each SOM can only see part of the input space of their layer, and are forced to produce an output based on that. The set of outputs from all the SOMs in a layer are concatenated into a single output vector. This output vector is sparse due to the fact that each SOM has only one node active at any given time. The layer output thus has the same sparsity as an individual SOM. 

By stacking layers on top of one another and reducing the number of SOMs per layer as the hierarchy grows, it is possible to create a system that adequately maps high-dimensional data down to a low-dimensional representation without facing the problems described above. Such a system also behaves externally like an individual SOM, meaning the interface that allows data to be processed by an SOM is the exact same as that which allows a hierarchy of SOMs to process data. The only difference is that the output of the hierachy has passed through multiple stages of dimensionality reduction, whereas the output of an SOM has only gone through a single stage.

# Installation

__Install hsom:__

    pip install git+https://github.com/CarsonScott/HSOM.git

__Requirements:__

- numpy
- json

# Examples

[Self-Organizing Map](https://github.com/CarsonScott/self-organizing-map/blob/master/examples/self_organizing_map.py)

[Self-Organizing Network](https://github.com/CarsonScott/self-organizing-map/blob/master/examples/self_organizing_network.py)

[Documentation](https://github.com/CarsonScott/self-organizing-map/blob/master/DOCUMENTATION.md)
