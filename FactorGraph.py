class FactorGraph:
  def __init__(self):
    self.variables = {}
    self.factors = {}

  def add_variable(self, var, neighbors):
    self.variables[var] = neighbors

  def add_factor(self, factor, neighbors):
    self.factors[factor] = neighbors

  def get_variable_neighbors(self, var):
    return self.variables[var]

  def get_factor_neighbors(self, factor):
    return self.factors[factor]
