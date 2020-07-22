from scipy.optimize import fmin_l_bfgs_b
import numpy as np

def U(A, B, alpha=1/3):
    return -(B**alpha * A**(1-alpha))
A = np.linspace(1, 10, 100).reshape(100,1)
B = np.linspace(1, 20, 100).reshape(100,1)
fmin_l_bfgs_b(U, np.array([2,1]), fprime=None, args=(A,B), approx_grad=0, bounds=[(0,10), (0, 20)], m=10, factr=10000000.0, pgtol=1e-05, epsilon=1e-08, iprint=-1, maxfun=15000, maxiter=15000, disp=None, callback=None, maxls=20)
