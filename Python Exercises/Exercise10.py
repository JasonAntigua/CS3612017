import matplotlib.pyplot as plt
import numpy as np
print("Exercise 10: ");

x = np.arange(0.0, 2.0, 0.01);
y = np.power(np.sin(x-2),2) * np.power(np.e,- (np.power(x,2)));

plt.xlabel("X-Axis");
plt.ylabel("Y-Axis");
plt.title("Function of sin^2(x-2)e^(-x^2)");
plt.xlim(0,2);
plt.ylim(0,1);
plt.plot(x, y);
plt.show();