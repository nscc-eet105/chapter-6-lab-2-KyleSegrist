#Kyle Segrist
#Chapter 6 Lab 2
# 7-5-2025

import matplotlib.pyplot as plt
print("This program will graph a line when given the slope and intercept")

m = int(input(f'Please enter the slope of the line: '))
b = int(input(f'Please enter the y intercept of the line: '))

#Create the list of x coordinates
x_coord = []
for num in range(-20,21):
    x_coord.append(num)

#use the x values and the slope and intercept variables to generate the y coordinates
y_coord = [num*m+b for num in x_coord]

plt.plot(x_coord, y_coord)
plt.grid(True)
plt.title('Linear graph')
plt.ylabel('Y Value')
plt.xlabel('X Value')
plt.axis('square')
plt.ylim(-20,20)
plt.xlim(-20,20)
plt.axvline(x = 0, color='k')
plt.axhline(y = 0, color='k')
plt.show()