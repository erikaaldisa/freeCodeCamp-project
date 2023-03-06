import numpy as np

def calculate(list):
  if len(list)!=9:
    raise ValueError('List must contain nine numbers.')
    
  # convert list to 3x3 numpy array
  array = np.array(list).reshape(3,3)

  calculations = {}
  # mean
  calculations["mean"] = [array.mean(axis=0).tolist(), array.mean(axis=1).tolist(), array.mean()]

  # variance
  calculations["variance"] = [array.var(axis=0).tolist(), array.var(axis=1).tolist(), array.var()]

  # standard deviation
  calculations["standard deviation"] = [array.std(axis=0).tolist(), array.std(axis=1).tolist(), array.std()]
  
  # min
  calculations["min"] = [array.min(axis=0).tolist(), array.min(axis=1).tolist(), array.min()]

  # max
  calculations["max"] = [array.max(axis=0).tolist(), array.max(axis=1).tolist(), array.max()]

  # sum
  calculations["sum"] = [array.sum(axis=0).tolist(), array.sum(axis=1).tolist(), array.sum()]
  
  return calculations