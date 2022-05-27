class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.change_name = name
        self.change_age = age
        self.add_track = tracks
        self.get_score = score
        print ("My name is ", str(self.change_name), "I am ", int(self.change_age), "My track is ", list(self.add_track), "My score is ", float(self.get_score))
        def change_name(self, name):
            self.name = name
            print ("My name is ", str(self.name))

            def change_age(self, age):
                self.age = age
                print ("My age is ", int(self.age))
            
                def add_track(self, track):
                    self.track = track
                    print ("My track are ", list(self.track))
                    self.track.append(tracks)

                    def get_score(self, score):
                        self.score = score
                        print ("My score is ", float(self.score))
                        return self.score
                        pass

s = Student("John", "20", ["Python", "Java"], "90")
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
(Bob.change_name("Peter"))
#Bob.change_age(34)
#Bob.add_track("UI/UX")
#Bob.get_score()
