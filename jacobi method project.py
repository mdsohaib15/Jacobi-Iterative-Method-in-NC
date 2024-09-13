import numpy as np

def jacobi(A, b, tol=1e-2, max_iter=1000):
    n = A.shape[0]
    x = np.zeros(n)
    D = np.diag(A)
    R = A - np.diagflat(D)
    iteration_table = []

    for iteration in range(max_iter):
        x_new = (b - np.dot(R, x)) / D
        iteration_table.append(x_new.copy())
        
        # Check for tolerance
        if np.linalg.norm(x - x_new) < tol:
            break
        
        # Check if values are repeating
        if np.array_equal(x, x_new):
            print(f"Values repeated at iteration {iteration + 1}")
            break
        
        x = x_new

    return x, iteration_table

# Get user input
n = int(input("Enter the number of equations: "))

A = np.zeros((n, n))
b = np.zeros(n)

print("Enter the coefficients of the matrix A row by row:")
for i in range(n):
    row = input().split()
    A[i] = [float(x) for x in row]

print("Enter the constants of the vector b:")
b = np.array([float(x) for x in input().split()])

# Call the Jacobi function
x, iteration_table = jacobi(A, b)

# Print the solution
print("Solution:", x)

# Print the iteration table
print("\nIteration Table:")
print("Iteration\t", "\t".join([f"x{i+1}" for i in range(n)]))
for idx, iter_values in enumerate(iteration_table):
    print(f"{idx+1}\t\t", "\t".join([f"{val:.6f}" for val in iter_values]))