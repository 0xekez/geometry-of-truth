import numpy as np

# N samples of dimension P
#
# a -> N*P matrix
def normalize(a):
    # This produces a matrix with with dimensions P. For example if
    # `len(P.shape)==2`, index (i,j) in `mean` is the average value of
    # index (i,j) of all N samples.
    mean = np.mean(a,axis=0,keepdims=True)
    return a-mean

# Computes the covariance matrix for `a`, assuming each row contains
# an observation and each column a variable.
#
# For the intented use case, each row is the output of a given layer
# (an observation), and each column an activation (a variable). This
# function has the same behavior as `np.cov(a, rowvar=False)`.
def covariance(a):
    # return np.cov(a,rowvar=False)
    centered = normalize(a)
    return (centered.T @ centered) / (centered.shape[0] - 1)

    # were the columns observations, and the rows variables, we'd find
    # the mean along each column (axis=1)
    mean = np.mean(a,axis=1,keepdims=True)
    centered = a - mean
    # then divide by the number of columns and invert the multiply.
    return (centered @ centered.T) / (centered.shape[1] - 1)

# Computes the top N principal components of `a`, where each row
# contains an observation and each column a variable. Returns (basis,
# residuals) where basis is the top two principal components, one per
# column, and residuals[i] the R^2 value (percentage of oriinal
# variance retained) when using the top `i` principal components.
def PCA2d(a,n=2):
    covarience = np.cov(normalize(a),rowvar=False)
    eigenvalues, eigenvectors = np.linalg.eigh(covarience)

    topNIndicies = sorted(range(len(eigenvalues)),key=lambda i: eigenvalues[i],reverse=True)[:n]

    original_variance = sum(eigenvalues)
    residuals = []
    rs = 0
    for eigen in sorted(eigenvalues,reverse=True):
        residuals.append((rs + eigen)/original_variance)
        rs += eigen

    # variance = sum([eigenvalues[i] for i in topNIndicies])
    # original_variance = sum(eigenvalues)
    # r_squared = variance / original_variance

    return np.array(eigenvectors[:,topNIndicies]), residuals
