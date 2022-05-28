class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.change_name = str(name)
        self.change_age = int(age)
        self.add_track = list(tracks)
        self.get_score = float(score)
        print ("My name is ", self.change_name)
        print("I am ", self.change_age)
        print("My track is ", self.add_track)
        print("My score is ", self.get_score)
    def change_name(self, name):
            self.name = name
            print ("My updated name is ", self.name)

    def change_age(self, age):
                self.age = age
                print ("My updated age is ", self.age)
            
    def add_track(self, tracks):
                    self.tracks = tracks
                    print ("My updated tracks are ", self.tracks)
                    self.tracks = tracks.append(list(tracks))

    def get_score(self, score):
                        self.score = score
                        print ("My updated score is ", self.score)
                        return self.score
pass

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Student.change_name(self = Student, name = "Peter")
Student.change_age(self = Student, age = 34)
Student.add_track(self = Student, tracks = ["UI/UX"])
Student.get_score(self = Student, score = 50.00 )

Student.change_name(self = Student, name = input("Type in your name: "))
Student.change_age(self = Student, age = input("Type in your age: "))
Student.add_track(self = Student, tracks = [input("Type in your tracks: ")])
Student.get_score(self = Student, score = input("Type in your score: "))
