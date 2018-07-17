"""class User:
    pass #Pass is a way to type a line when necessary, when defining a class you need at least one line.

user1 = User()
user1.first_name = "Dave"
user1.last_name = "Bowman"

print(user1.first_name)

print(user1.last_name)

first_name = "Arthur"
last_name = "Clarke"

print(first_name, last_name)
print(user1.first_name, user1.last_name)


user2 = User()
user2.first_name = "Frank"
user2.last_name = "Poole"

print(first_name, last_name)

user1.age = 37
user2.favorite_book = "2001: A Space Odyssey"

print(user1.age)

"""

import datetime

class User:
    """A member of FriendFace. For now we are
        only storing their name and birthday.
        But soon we will store an uncomfortable
        amount of user information."""

    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday #yyyymmdd

        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.middle_name = name_pieces[1]
        self.last_name = name_pieces[-1]

    def age(self):
        """Return the age of the user in years."""
        today = datetime.date(2018, 6, 18)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = datetime.date(yyyy, mm, dd)
        age_in_days = (today - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)


user = User("Dave Bowman", "19710315")
print(user.age())
