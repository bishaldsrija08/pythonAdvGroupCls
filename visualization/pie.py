# pie chart
import matplotlib.pyplot as plt


x = [4500, 500, 232, 4839]
y = ["Apple", "Ball", "Cat", "Dog"]

plt.pie(x, labels=y, autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()