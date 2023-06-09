import math
import matplotlib.pyplot as plt

def f(x):
    return x**3

a = 2
b = 3

tolerance = 1e-6
max_iterations = 100

for i in range(max_iterations):
    c = (a+b)/2
    print("Iteration: ", i)
    print(f"a={a:.6f} b={b:.6f} c={c:.6f}")

    if abs(f(c)) < tolerance:
        print(f"Root found at x={c:.6f}")
        break
    elif f(c) * f(a) < 0:
        b =c
    else:
        a =c

x_values = []
y_values = []
for i in range(-20,20):
    x_values.append(i)
    y_values.append(f(i))

plt.plot(x_values,y_values)
plt.grid(True)
plt.show()