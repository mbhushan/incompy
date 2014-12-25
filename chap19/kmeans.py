import random
from cluster import Cluster


def kmeans(examples, exampleType, k, verbose):
    """Assumes examples is a list of examples of type exampleType,
    k is a positive int, verbose is a Boolean
    Returns a list containing k clusters. If verbose is
    True it prints result of each iteration of k-means"""
    # Get k randomly chosen centroids
    initialCentroids = random.sample(examples, k)

    # create a singleton cluster for each centroid
    clusters = []
    for e in initialCentroids:
        clusters.append(Cluster([e], exampleType))

    # Iterate until centroid do not change
    converged = False
    numIter = 0
    while not converged:
        numIter += 1
        # create a list containing k empty list
        newClusters = []
        for i in range(k):
            newClusters.append([])

        # Associate each cluster with nearest centroid
        for e in examples:
            # Find the centroid closes to e
            smallestDist = e.distance(clusters[0].getCentroid())
            index = 0
            for i in range(1, k):
                distance = e.distance(clusters[i].getCentroid())
                if distance < smallestDist:
                    smallestDist = distance
                    index = i
            # Add e to the list of examples for the appropriate cluster
            newClusters[index].append(e)

        # update each cluster; check if a centroid has changed
        converged = True
        for i in range(len(clusters)):
            if clusters[i].update(newClusters[i]) > 0.0:
                converged = False
        if verbose:
            print 'Iteration #' + str(numIter)
            for c in clusters:
                print c
                print ''  # blank line
    return clusters


def dissimilarity(clusters):
    totDist = 0.0
    for c in clusters:
        totDist += c.variance()
    return totDist


def tryKMeans(examples, exampleType, numClusters, numTrials, verbose=False):
    """Calls kmeans numTrials times and returns the result with the
    lowest dissimilarity"""
    best = kmeans(examples, exampleType, numClusters, verbose)
    minDissimilarity = dissimilarity(best)
    for trail in range(1, numTrials):
        clusters = kmeans(examples, exampleType, numClusters, verbose)
        currDissimilarity = dissimilarity(clusters)
        if currDissimilarity < minDissimilarity:
            best = clusters
            minDissimilarity = currDissimilarity
    return best
