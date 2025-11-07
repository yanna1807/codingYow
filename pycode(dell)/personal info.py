#8/15/2024 and 8/16/2024 and 8/17/2024 - my own code about myself.. :)
class Basic_Profile():
    print("Just a reminder: I made this code about my profile on August 15,16,17,2024 :)")
    print("\nI will make my profile in a form of dictionary, part of the lesson of my first language Python, the data structures.")

    def __init__(self, fname, mname, lname, age):
        self.fname = fname
        self.mname = mname
        self.lname = lname
        self.age = age
        
    def My_Info(self):
        print(f"\nNAME: {self.lname},{self.fname} {self.mname}")
        print(f"\nAGE: {self.age} years old")

class Studies(Basic_Profile):

    def __init__(self, fname, mname, lname, age, year, track, major, school_name):
        super().__init__(fname, mname, lname, age)
        self.year = year
        self.track = track
        self.major = major
        self.school_name = school_name

    def More_Info(self):
        print(f"\nYEAR: Grade {self.year}")
        print(f"\nTRACK: {self.track}")
        print(f"\nMAJOR: {self.major} major")
        print(f"\nSCHOOL: {self.school_name}")

class Days_Passed(Studies):
    print("\nI miss my old school with my old friends so I will also just put it in my profile :'(")

    print("\nCreating Gianna's Profile: :)")

    def __init__(self, fname, mname, lname, age, year, track, major, school_name, year1, year2, year3, year4, school1, school2, school3, school4):
        super().__init__(fname, mname, lname, age, year, track, major, school_name)
        self.year1 = year1
        self.year2 = year2
        self.year3 = year3
        self.year4 = year4
        self.school1 = school1
        self.school2 = school2
        self.school3 = school3
        self.school4 = school4
        
    def Memories(self):
        print("\nMy Senior High Years, for 2 years..")
        print(f"\nYEAR: {self.year1}, SCHOOL: {self.school1}")
        print("\nMy Junior High Years, for 4 years..")
        print(f"\nYEAR: {self.year2}, SCHOOL: {self.school2}") 
        print("\nMy Elementary Years, for 6 years..")
        print(f"\nYEAR: {self.year3}, SCHOOL: {self.school3}")
        print(f"\nYEAR: {self.year4}, SCHOOL: {self.school4}")

class Hobbies(Days_Passed):

    def __init__(self, fname, mname, lname, age, year, track, major, school_name, year1, year2, year3, year4, school1, school2, school3, school4, talentsAndhobbies, likes):
        super().__init__(fname, mname, lname, age, year, track, major, school_name, year1, year2, year3, year4, school1, school2, school3, school4)
        self.talentsAndhobbies = talentsAndhobbies
        self.likes = likes

    def Skills(self):
        print(f"\nTALENTS: {self.talentsAndhobbies}")
        print(f"\nLIKES: {self.likes}")

me = Basic_Profile("Gianna", "Arac", "Culpa", 16)

me = Studies("Gianna", "Arac", "Culpa", 16, 12, "Arts and Design", "Music", "Cabawan Senior High School")

me = Days_Passed("Gianna","Arac","Culpa", 16, 12, "Arts and Design", "Music", "Cabawan Senior High School", ["2023-2024 - Grade 11", "2024-2025 - Grade 12"],
            ["2019-2020 - Grade 7", "2020-2021 - Grade 8", "2021-2022 - Grade 9", "2022-2023 - Grade 10"], ["2017-2018 - Grade 5", "2018-2019 - Grade 6"],
            ["2013-2014 - Grade 1", "2014-2015 - Grade 2", "2015-2016 - Grade 3", "2016-2017 - Grade 4"], "Dr. Cecilio Putong or Cabawan Senior High School",
            "Mansasa National High School", "Mansasa Elementary School", "City East Elementary School")

me = Hobbies("Gianna", "Arac", "Culpa", 16, 12, "Arts and Design", "Music", "Cabawan Senior High School", ["2023-2024 - Grade 11", "2024-2025 - Grade 12"],
            ["2019-2020 - Grade 7", "2020-2021 - Grade 8", "2021-2022 - Grade 9", "2022-2023 - Grade 10"], ["2017-2018 - Grade 5", "2018-2019 - Grade 6"],
            ["2013-2014 - Grade 1", "2014-2015 - Grade 2", "2015-2016 - Grade 3", "2016-2017 - Grade 4"], "Dr. Cecilio Putong or Cabawan Senior High School",
            "Mansasa National High School", "Mansasa Elementary School", "City East Elementary School", ["Playing Piano", "Poetry", "Listening to Music", "Reading Wattpad", "Coding/Programming"],
            ["All sorts of food except mango flavors, veggies and salads", "Eyeglasses", "Matching Necklaces/Rings", "Crescent Moon"])
   
me.My_Info()
me.More_Info()
me.Memories()
me.Skills()

