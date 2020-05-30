class Node:
  pass
  pass

class Edge:
  pass

class DAG:
  def __init__(self,
    node: Node):
    self.refs = None  # list or set ... be able to refer multiple nodes
                      # TODO: creating edges
    self.weights = 0  # TODO: needs default method of calculating weights

    """private"""
    self._n_direct_ref = 0  # number of nodes
    self._n_indirect_ref = 0

  def hops_between(self,  # distance
    other: DAG):
    pass  # returns -1 if no hops

  def ancestors():  # returns all ancestor nodes
    pass

  def is_refer(self,  # returns True if one node refers the other one, otherwise False
    other: DAG):
    pass
