class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.track = tracks
        self.score = score
        print("My name is", name, "I am", age, "my tracks are", tracks, "and I scored", score)

Bob = Student(name = "Bob", age = 26, tracks = ["FE","BE"],score = 20.90)



s = Student("Peter", 34, ["UI", "UX"], 40.9)
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
