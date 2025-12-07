import numpy as np  

def power_method(A, x0, epsilon, max_iter=1000):  
    A = np.array(A, dtype=float)  
    x = np.array(x0, dtype=float)  
    x = x / np.linalg.norm(x)  

    lambda_old = 0.0  

    for k in range(1, max_iter + 1):  
        y = A @ x  
        x = y / np.linalg.norm(y)  
        lambda_new = x @ (A @ x)  

        if abs(lambda_new - lambda_old) < epsilon:  
            return lambda_new, x, k  

        lambda_old = lambda_new  

    return lambda_new, x, max_iter  

def main():  
    A1 = np.array([  
        [1, 0, 0],  
        [0, 2, 0],  
        [0, 0, 3]  
    ], dtype=float)  

    x0 = np.array([1.0, 1.0, 1.0])  

    epsilon = 1e-8  

    print("--- Matriz A1 fixa ---")  
    lambda_dom, x_dom, k = power_method(A1, x0, epsilon)  
    print(f"Autovalor dominante ≈ {lambda_dom:.8f}")  
    print(f"Autovetor dominante ≈ {x_dom}")  
    print(f"Iterações: {k}")  

    n = 5  
    a_vals = np.random.uniform(0.0, 1.0, size=n)  
    A2 = np.diag(a_vals)  

    x0_random = np.random.rand(n)  

    print("\n--- Matriz diagonal aleatória ---")  
    lambda_dom2, x_dom2, k2 = power_method(A2, x0_random, epsilon)  
    print("a_i =", a_vals)  
    print(f"Autovalor dominante ≈ {lambda_dom2:.8f}")  
    print(f"Autovetor dominante ≈ {x_dom2}")  
    print(f"Iterações: {k2}")  

if __name__ == "__main__":  
    main()