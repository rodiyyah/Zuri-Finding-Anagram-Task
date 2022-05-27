class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score

    def change_name(self, new_name):
        self.name = new_name
        print(self.name)
    def change_age(self, new_age):
        self.age = int(new_age)
        print(self.age)
    def add_track(self, new_track):
        self.track.append(new_track)
        print(self.track)
    def get_score(self):
        print(self.score)

h = Student("Bob", "26", ["FE","BE"], "20.90")
h.change_name("peter")
h.change_age("34")
h.add_track("ui/ux")
h.get_score()


# d = Student("Bob", "26", ["FE", "BE "], "20.90")


# Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# # Expected methods
# Bob.change_name("Peter")
# Bob.change_age(34)
# Bob.add_track("UI/UX")
# Bob.get_score()
