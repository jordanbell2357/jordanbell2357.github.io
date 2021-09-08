#############################
# This a simple example to demonstrate
# usage of basic object oriented design.
#
# In this example, the object represents
# a probability distribution inferred from sample points.
import numpy as np
import math

class KernelDensityEstimator:
    
    ### This is the function that initializes each object. It is called when the object is created.
    def __init__(self, #a reference to the object, an idiosyncrasy of python.
                 sample_points = None, #An optional parameter (can be provided later, see below)
                 weights = None,
                 bandwidth = None):

        if isinstance(sample_points,np.ndarray):
            self.set_samples(sample_points, weights)
            if bandwidth == None:
                self.__compute_bandwidth()
        return
        
    def set_samples(self, 
                    sample_points: np.ndarray,
                    weights: np.ndarray = None):
        self.sample_points = sample_points
        self.__compute_bandwidth()
        if weights != None:
            self.__check_data(weights)
        return
        
    ### double underscore in front of a method name makes it effectively invisible outside of the local context, thereby making it a "private" method.
    def __check_data(self,
                     weights: np.ndarray):
        
        ### Some error handling that won't crash the whole program, but just give the user an "ahem."
        try:
            assert(weights.shape == self.sample_points.shape)
        except AttributeError:
            print("Please check that both the samples and weights vectors are numpy arrays.\n Aborting data update...")
            return
        except AssertionError:
            print("The weight vector is not the same shape as the samples vector.\n Aborting data update... ")
            return
        
        # We do not allow negative weights
        weights[weights < 0] = 0
        
        # Making sure the weights are normalized.
        weights = weights/np.sum(weights)
        
        # The object keeps track of its own weights
        self.weights = weights
        return
    
    def __compute_bandwidth(self):
        std = np.std(self.sample_points)
        # Roughly Silverman's Rule of Thumb
        self.bandwidth = std/np.power(self.sample_points.size, 0.2)
        
    ### Gaussian kernel
    def kernel(self, 
               x: np.float64,
               y: np.float64):
        expon = -0.5*(x-y)*(x-y)/(self.bandwidth*self.bandwidth)
        return np.exp(expon)/(self.bandwidth*np.sqrt(2*math.pi))
        
    ### compute the likelihood of an array of values
    def likelihood(self, 
                 pts: np.ndarray):        
        iterator = (self.kernel(x,y) for x in pts for y in self.sample_points)
        eval = np.fromiter(iterator, float).reshape(pts.size, self.sample_points.size).mean(axis = 1)
        return eval

    ### Approximate the integral of a function defined on a 
    def integrate(self,
                  function):
        pts = np.sort(list(function.keys()))
        interval_lengths = np.diff(pts)
        
        like = self.likelihood(pts)
        likelihood_means = np.mean(np.stack((like[1:], like[:-1])), axis = 0)
        
        interval_masses = interval_lengths*likelihood_means
        interval_masses = interval_masses/np.sum(interval_masses)

        vals = np.array([function[pt] for pt in pts])
        interval_means = np.mean(np.stack((vals[1:], vals[:-1])), axis = 0)
        
        
        return np.sum(interval_means*interval_masses)

    
    
    