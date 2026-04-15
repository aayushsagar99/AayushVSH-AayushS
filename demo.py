import os
class Student1: # Changed to singular 'Student' (standard practice)
    def __init__(self, name="Aayush", grade=3, age=8):
        self.name = name
        self.grade = grade
        self.age = age
        # Note: sum() will crash if 'None' is in this list
        self.scores = [202, 234] 

    def add_score(self, score):
        self.scores.append(score)

    def get_average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)
# Create an instance of the class
student1 = Student1("Aayush", 3, 8)

# Add some scores
student1.add_score(202)
student1.add_score(234)


# Print the result so it shows up in your terminal
print(f"Student: {student1.name}")
print(f"Average Score: {student1.get_average()}")
