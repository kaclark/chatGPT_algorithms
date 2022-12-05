def belief_propagation(nodes, edges):
  # Initialize the messages
  messages = {}
  for edge in edges:
    messages[edge] = 1

  # Iterate until convergence
  while True:
    # Store the previous messages
    prev_messages = messages.copy()

    # Update the messages
    for edge in edges:
      (i, j) = edge
      messages[edge] = 1
      for k in nodes[i]:
        if k == j:
          continue
        messages[edge] *= prev_messages[(k, i)]

    # Check for convergence
    converged = True
    for edge in edges:
      if abs(messages[edge] - prev_messages[edge]) > 1e-10:
        converged = False
        break

    if converged:
      break

  # Compute the marginals
  marginals = {}
  for i in nodes:
    marginal = 1
    for j in nodes[i]:
      marginal *= messages[(i, j)]
    marginals[i] = marginal

  return marginals
