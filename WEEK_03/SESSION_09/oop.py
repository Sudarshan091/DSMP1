# class Superhero:
#     team_count = 0  # Static variable

#     def __init__(self, name):
#         self.__name = name  # Private attribute
#         Superhero.team_count += 1

# hero_a = Superhero("Batman")
# hero_b = hero_a
# hero_b.hero_count = 500  # Dynamic attribute creation
# # print(Superhero.team_count)  # Output: 1)
# print(hero_a.__name)


def f(x):
    if x<=1:
        return x-1
        return x+ f(x-2)
f=f(7)
# g=f(f-2)
# h=g()
print(f)   
# print(h)    


# ques no 3
# def function(i):
#     if i>