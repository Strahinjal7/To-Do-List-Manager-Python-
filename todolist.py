tasks = []
index = 0
def show_tasks():
    if not tasks:
        print('Lista je trenutno prazna. ')
    else:
        print('Vaše obaveze: ')
        for index, task in enumerate(tasks):
            print(f'{index}. {task}')

def add_task():
    task = input('Unesite novu obavezu: ')
    tasks.append(task)
    print(f'{index + 1}. {task}')

def delete_task():
    show_tasks()
    try:
        index = int(input('Unesite broj obaveze koju zelite obrisati '))
        if 1 <= index <= len(tasks):
            remove = tasks.pop(index-1)
            print(f'Obrisali ste: {remove}')
        else:
            print('Ne postoji obaveza sa tim brojem')
    except ValueError :
        print('Morate unijeti broj')

def todo_list():
    while True:
        print('TO DO LISTA')
        print('1 - Prikazi sve obaveze: ')
        print('2 - Dodaj novu obavezu: ')
        print('3 - Ukloni obavezu: ')
        print('4 - Izlaz')

        izbor = input('Unesite broj opcije: ')

        if izbor == '1':
            show_tasks()
        elif izbor == '2':
            add_task()
        elif izbor == '3':
            delete_task()
        elif izbor == '4':
            print('Izlaz iz aplikacije. Vidimo se!')
            break

todo_list()

