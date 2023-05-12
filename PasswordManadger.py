


def write_data():
    bd = []
    template = open(r'E:\Данные\Обучения\Python\Менеджер паролей\list1.txt','a')
    
    
    site = input('Введите сайт: ')
    login = input('Введите логин: ')
    passworld = input('Введите пароль: ')
    
    bd = ['Сайт:', site, 'Логин:', login, 'Пароль:', passworld]
    template.write (str(bd) + '\n')
    template.close()
    
    
#wrie_data()
    
def read_data():
    data = open(r'E:\Данные\Обучения\Python\Менеджер паролей\list1.txt','r')
    file_data = data.read()
    data.close()
    
    print(type(file_data))
    print(file_data)
    
    list_data = (file_data.split(','))
    #list_data = list(''.join(file_data.split(",")))
    print(type(list_data))
    print(list_data)
    
    site = input('Введите название асйта: ')
    
    print(list_data[site])
    
    
read_data()