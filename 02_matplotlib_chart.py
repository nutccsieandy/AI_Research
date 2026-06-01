import matplotlib.pyplot as plt

students = ["A", "B", "C", "D"]
scores = [80, 90, 70, 95]

plt.bar(students, scores)
plt.title("Score Analysis")
plt.xlabel("Student")
plt.ylabel("Score")
plt.show()
