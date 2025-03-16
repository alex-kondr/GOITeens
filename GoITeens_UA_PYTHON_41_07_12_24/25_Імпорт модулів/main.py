# import matplotlib.pyplot as plt
# import numpy as np


# x = np.linspace(0, 2, 100)

# plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
# plt.plot(x, x**2, label='quadratic')  # etc.
# plt.plot(x, x**3, label='cubic')
# plt.xlabel('x label')
# plt.ylabel('y label')
# plt.title("Simple Plot")
# plt.legend()
# plt.show()

import add_numbers


c = add_numbers.calculate(5.1, .3)
print(c)

c2 = add_numbers.calculate2(5, 6)
print(c2)


from add_numbers import calculate, calculate2

c3 = calculate(4, 6)