#Singleton


# class OnlyOne:
#     _instance = None
#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super().__new__(cls, *args, **kwargs)
#         return cls._instance


# a = OnlyOne()
# b = OnlyOne()

# print(a == b)
# print(a)
# print(b)


# Encapsulatio
# class Encap:
#     def __init__(self):
#         self._hval = 10

#     def getter(self):
#         return self._hval

#     def setter(self, hval):
#         self._hval = hval


# c = Encap()
# print(c.getter())
# c.setter(20)
# print(c.getter())



#Polymorphism

# class Dolphin:
#     def swim(self):
#         print('Dolphins Swim slow')

#     def skeleton(self):
#         print('Dolphins have huge skeleton')

# class Titus:
#     def swim(self):
#         print('Titus Swim slow')

#     def skeleton(self):
#         print('Titus have tiny skeleton')

# d = Dolphin()
# t = Titus()

# fishes = (d, t)
# for fish in fishes:
#     print(fish.swim())
#     print(fish.skeleton())


# Inheritance

# class SchoolMember:
#     def __init__(self, age, sex):
#         self.age = age
#         self.sex = sex

#     def tell(self):
#         print('I am a SchoolMember')

# class Teacher(SchoolMember):
#     def __init__(self, age, sex, salary):
#         super().__init__(age, sex)
#         self.salary = salary

#     def tell(self):
#         SchoolMember.tell(self)
#         print('I am a Teacher')


# class Student(SchoolMember):
#     def __init__(self, age, sex, snum):
#         super().__init__(age, sex)
#         self.snum = snum

#     def tell(self):
#         # SchoolMember.tell(self)
#         print('I am a Student')


# s = Student(13, "M", 9074)
# print(s.age)
# print(s.sex)
# print(s.snum)
# s.tell()



#Fibonacci

# def fibonacci(x):
#     if x <= 0:
#         return 0
#     elif x == 1:
#         return 1
#     else:
#         return fibonacci(x - 1) + fibonacci(x-2)

# print(fib(8))


#Factorial

def facto(x):
    answer = 1
    while x > 1:
        answer *= x
        x -= 1
    print(answer)


facto(24444444)
