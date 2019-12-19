# Hierarchical Self-Organizing Maps for Unsupervised Classification 

A hierarchical self-organizing map (HSOM) is an unsupervised neural network that learns patterns from high-dimensional space and represents them in lower dimensions. 

HSOM networks take inputs and feed them into many self-organizing maps, each learning individual features of the input space. 

These maps produce a sparse output vector with only the most responsive nodes set to '1'. This occurs through competitive inhibition that restricts the possible number of 'winners' (i.e. active nodes) at any given time.

Each HSOM layer contains a set of maps that view part of the input space and produce an output which is concatenated with every other output and sent up to the following layer as input. 

Information becomes increasingly abstract as it passes through the network, transforming into a sparse, low-dimensional representation of the original data.

# A Hierarchy of Self-Organizing Maps

Self-organizing maps are useful because they automatically reduce the dimensionality of whatever data is being observed. However, if the dimensionality of the data in question is sufficiently high, a single self-organizing map will fail to reduce it while maintaining an accurate representation in the process.

The solution is to combine many self-organizing maps into one, giant structure. SOMs can be arranged in a hierarchy, wherein each layer of the hierarchy contains a set of SOMs that receive input from the previous layer and produce output to the next. 

![](https://github.com/CarsonScott/self-organizing-map/blob/master/images/layer.PNG)

At the bottom of the hierarchy, SOMs receive raw data as input just as a typical singular SOM would do. Each SOM can only see part of the input space of their layer, and are forced to produce an output based on that. The set of outputs from all the SOMs in a layer are concatenated into a single output vector. This output vector is sparse due to the fact that each SOM has only one node active at any given time. The layer output thus has the same sparsity as an individual SOM. 

By stacking layers on top of one another and reducing the number of SOMs per layer as the hierarchy grows, it is possible to create a system that adequately maps high-dimensional data down to a low-dimensional representation without facing the problems described above. Such a system also behaves externally like an individual SOM, meaning the interface that allows data to be processed by an SOM is the exact same as that which allows a hierarchy of SOMs to process data. The only difference is that the output of the hierachy has passed through multiple stages of dimensionality reduction, whereas the output of an SOM has only gone through a single stage.

# Installation

__Install som:__

    pip install git+https://github.com/CarsonScott/self-organizing-map.git

__Requirements:__

- numpy
- json

# Examples

[Self-Organizing Map](https://github.com/CarsonScott/self-organizing-map/blob/master/examples/self_organizing_map.py)

[Self-Organizing Memory](https://github.com/CarsonScott/self-organizing-map/blob/master/examples/self_organizing_memory.py)

[Documentation](https://github.com/CarsonScott/self-organizing-map/blob/master/DOCUMENTATION.md)
