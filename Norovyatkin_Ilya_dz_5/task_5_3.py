tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Паша', 'Виталий', 'Олег', 'Оксана']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '1B', '6Б']


def check_gen(tutors: list, klasses: list):
    
    if len(tutors) > len(klasses):
        x = len(klasses) - len(tutors)
        for i in range(len(tutors)):
            if i < len(klasses):
                yield (tutors[i], klasses[i])
            else:
                for g in range(x, 0):
                    i += 1
                    yield (tutors[g], None)
                

    else:
        for i in range(len(tutors)):
            yield (tutors[i], klasses[i])


generator = check_gen(tutors, klasses)
# добавьте здесь доказательство, что создали именно генератор
print(type(generator)) 
for _ in range(len(tutors)):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration