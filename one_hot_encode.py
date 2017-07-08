def one_hot_encode(x):
    """   
    : x: List of sample Labels
    : return: Numpy array of one-hot encoded labels
    """    
    return np.eye(10)[x]
