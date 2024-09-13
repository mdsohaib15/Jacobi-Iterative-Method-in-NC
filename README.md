### **Title: Jacobi Method Solver for Linear Systems**

### **Description:**

The Jacobi Method Solver for Linear Systems is a Python application designed to solve systems of linear equations using the Jacobi iterative method. It provides an interactive way to input equations, perform iterative computations, and analyze the results. The application is particularly useful for educational purposes and numerical analysis tasks. Key features include:

- **User Input Handling**:
  - **Matrix Input**: Users can input the coefficient matrix \( A \) for the system of equations.
  - **Vector Input**: Users provide the constants of the vector \( b \) corresponding to the system of equations.

- **Jacobi Iterative Method**:
  - **Algorithm Implementation**: Executes the Jacobi iterative method to solve \( Ax = b \).
  - **Convergence Checks**: Monitors convergence using a specified tolerance and a maximum number of iterations.

- **Output and Reporting**:
  - **Solution Display**: Shows the final computed solution vector \( x \).
  - **Iteration Table**: Displays a table of values for each iteration, helping users visualize the convergence process.

- **Convergence Checks**:
  - **Tolerance Check**: Ensures that the solution converges within the given tolerance.
  - **Repetition Check**: Detects if values are repeating across iterations, indicating potential convergence issues.

### **Numpy's Role in the Project:**

`numpy` is a fundamental package for numerical computing in Python and plays a crucial role in this project by providing essential functions and operations:

1. **Matrix and Vector Operations**:
   - **Array Creation**: `np.zeros` is used to initialize matrices and vectors with zeros, which is essential for setting up the coefficient matrix \( A \) and the constant vector \( b \).
   - **Array Manipulation**: `np.array` is used to convert lists into numpy arrays, allowing for efficient mathematical operations.

2. **Matrix Decomposition**:
   - **Diagonal Extraction**: `np.diag` extracts the diagonal elements from the matrix \( A \), which are used in the Jacobi method to update the solution vector.

3. **Matrix Calculations**:
   - **Matrix Subtraction**: `np.diagflat` creates a diagonal matrix from the diagonal elements of \( A \) to facilitate the separation of the diagonal part from the rest of the matrix.
   - **Matrix-Vector Multiplication**: `np.dot` performs matrix-vector multiplication, which is crucial for the iterative calculations in the Jacobi method.

4. **Convergence Checking**:
   - **Norm Calculation**: `np.linalg.norm` computes the norm of the difference between successive iterations to check if the solution has converged within the specified tolerance.

5. **Iteration Tracking**:
   - **List Handling**: Numpy arrays are used to store and manage the iteration results, which are then printed in a structured table format.

By leveraging numpy's powerful array operations and mathematical functions, the project efficiently handles matrix and vector computations, making the implementation of the Jacobi method straightforward and effective.
