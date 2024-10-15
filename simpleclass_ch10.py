# Define our student class
class Student :
    def __init__(self, major):
        self.major = major        # what's our major?
    
    def study(self):
        print(f"I'm studying {self.major} right now!")

# make or "insantiate" our student!
our_lamb = Student("Humanities")

# tell the student to study!
our_lamb.study()
    