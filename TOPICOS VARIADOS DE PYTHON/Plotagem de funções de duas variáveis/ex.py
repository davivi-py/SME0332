import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def f(x, y):
    return np.cos(x) * np.cos(y)


def df_dx(x, y):
    return -np.sin(x) * np.cos(y)


def df_dy(x, y):
    return -np.cos(x) * np.sin(y)


def main():
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = np.linspace(-2*np.pi, 2*np.pi, 100)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    fig = plt.figure(figsize=(18, 5))

    ax1 = fig.add_subplot(131, projection='3d')
    ax1.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_zlabel('f(x,y)')
    ax1.set_title('Superfície 3D - Vista 1')
    ax1.view_init(elev=30, azim=45)

    ax2 = fig.add_subplot(132, projection='3d')
    ax2.plot_surface(X, Y, Z, cmap='plasma', edgecolor='none')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_zlabel('f(x,y)')
    ax2.set_title('Superfície 3D - Vista 2')
    ax2.view_init(elev=60, azim=120)

    ax3 = fig.add_subplot(133, projection='3d')
    ax3.plot_surface(X, Y, Z, cmap='coolwarm', edgecolor='none')
    ax3.set_xlabel('x')
    ax3.set_ylabel('y')
    ax3.set_zlabel('f(x,y)')
    ax3.set_title('Superfície 3D - Vista 3')
    ax3.view_init(elev=10, azim=0)

    plt.tight_layout()
    plt.show()

    fig2, axes = plt.subplots(1, 3, figsize=(18, 5))

    contour1 = axes[0].contourf(X, Y, Z, levels=20, cmap='viridis')
    axes[0].set_xlabel('x')
    axes[0].set_ylabel('y')
    axes[0].set_title('Curvas de nível - viridis')
    plt.colorbar(contour1, ax=axes[0])

    contour2 = axes[1].contourf(X, Y, Z, levels=20, cmap='plasma')
    axes[1].set_xlabel('x')
    axes[1].set_ylabel('y')
    axes[1].set_title('Curvas de nível - plasma')
    plt.colorbar(contour2, ax=axes[1])

    contour3 = axes[2].contourf(X, Y, Z, levels=20, cmap='coolwarm')
    axes[2].set_xlabel('x')
    axes[2].set_ylabel('y')
    axes[2].set_title('Curvas de nível - coolwarm')
    plt.colorbar(contour3, ax=axes[2])

    plt.tight_layout()
    plt.show()

    x_grad = np.linspace(-2*np.pi, 2*np.pi, 20)
    y_grad = np.linspace(-2*np.pi, 2*np.pi, 20)
    X_grad, Y_grad = np.meshgrid(x_grad, y_grad)
    
    U = df_dx(X_grad, Y_grad)
    V = df_dy(X_grad, Y_grad)

    fig3, ax = plt.subplots(figsize=(10, 8))
    
    contour = ax.contour(X, Y, Z, levels=15, colors='gray', linewidths=0.5, alpha=0.6)
    ax.clabel(contour, inline=True, fontsize=8)
    
    quiver = ax.quiver(X_grad, Y_grad, U, V, color='red', alpha=0.8)
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Gradiente ∇f sobreposto às curvas de nível')
    ax.set_aspect('equal')
    
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()