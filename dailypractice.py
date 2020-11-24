from collections import namedtuple

User = namedtuple("User",["name","age"])
user = User(name="haha",age="233")
a= user.name