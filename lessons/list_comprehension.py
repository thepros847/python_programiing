# Python 3: List comprehensions
teachers = ['Eric', 'Appoh', 'Little', 'Regina', 'Theo', 'Ellen', 'Yankah',]
loud_teachers = [teachers.upper() for teachers in teachers]
print(loud_teachers)


# List and the enumerate function
list(enumerate(teachers))
[(0, 'Eric'), (1, 'Ellen'), (2, 'Theo')]

