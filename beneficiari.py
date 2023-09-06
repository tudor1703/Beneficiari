def show_the_cfile():
   with open('Client.txt', 'r') as cfile:
       content = cfile.read()
       print(content)

def show_the_lfile():
   with open('Location.txt', 'r') as lfile:
       content = lfile.read()
       print(content)

def add_one_client():
     name = input('Introdu numele beneficiarului. ')
     id = input('Introdu id-ul localitatii. ')
     new_client = [name, ' ', id, '\n']
     with open('Client.txt', 'a+') as cfile:
         cfile.writelines(new_client)

def add_one_location():
    id = input('Introdu id-ul localitatii. ')
    name = input('Introdu numele localitatii. ')
    address = input('Introdu adresa localitatii. ')
    tipe = input('Introdu tipul localitatii urban/rural. ')
    new_location = [ id, ' ', name, ' ', address, ' ', tipe, '\n']
    with open('Location.txt', 'a+') as lfile:
        lfile.writelines(new_location)

def delete_one_client():
    with open('Client.txt', 'r') as cfile:
        filelines = cfile.readlines()
        lineindex = 1
        deleteLine = int(input('Introdu numarul de ordine  '))
        with open('Client.txt', 'w') as cfile:
            for textline in filelines:
                if lineindex != deleteLine:
                    cfile.write(textline)
                    lineindex += 1
    print('Linia',deleteLine,'a fost stearsa cu succes\n')

def delete_one_location():
    id_delet = input('Introdu ID-ul localitatii care vrei sa o stergi. ')
    with open('Location.txt', 'r') as lfile:
        filelines = lfile.readlines()
    with open('Location.txt', 'w') as lfile:
        for line in filelines:
            if not line.startswith(id_delet):
                lfile.write(line)
    print('localitatea a fost stearsa cu succes.')

def update_one_client():
    line_number = int(input('Introduceti linia care vreti sa o stergeti. '))
    nume = input('introduceti noul nume. ')
    id = int(input('Introduceti noul ID. '))
    new_line = nume + ' ' + id + '\n'
    with open('Client.txt', 'r') as cfile:
        lines = cfile.readlines()
    del lines[line_number - 1]
    lines.insert(line_number - 1, new_line + '\n')
    with open('Client.txt', 'w') as cfile:
        cfile.writelines(lines)

def update_one_location():
    id_update = input('Introduceti ID-ul localitati care doriti sa fie actualizata. ')
    id = input('Introduceti noul ID. ')
    name = input('Introduceti noul nume. ')
    address = input('Introduceti noua adresa. ')
    tip = input('Introduceti tipul urba/rural. ')
    new_line = id + ' ' + name + ' ' + address + ' ' + tip + '\n'
    with open('Location.txt', 'r') as lfile:
        lines = lfile.readlines()
    with open('Location.txt', 'w') as lfile:
        for line in lines:
            if line.startswith(id_update):
                lfile.write(new_line)
            else:
                lfile.write(line)

def create_vip_clients_file():
    with open('Client.txt', 'r') as cfile:
        client_lines = cfile.readlines()

    with open('Location.txt', 'r') as lfile:
        location_lines = lfile.readlines()

    locations_with_5_or_more_clients = []
    for location_line in location_lines:
        location_id = location_line.split()[0]
        matching_clients = [client_line for client_line in client_lines if client_line.split()[-1] == location_id]
        if len(matching_clients) >= 5:
            locations_with_5_or_more_clients.append(location_line)

    with open('VipClient.txt', 'w') as vipfile:
        vipfile.writelines(locations_with_5_or_more_clients)

def location_tipe_urban():
    urban_localities = []
    with open('Location.txt', 'r') as lfile:
        lines = lfile.readlines()
        for line in lines:
            data = line.split()
            if data[-1] == 'urban':
                urban_localities.append(line)

    if not urban_localities:
        print("Nu exista localitati de tip urban in fisierul Location.txt.")
        return

    sorted_urban_localities = sorted(urban_localities, key = lambda x: x.split()[2])

    print("Localitatile de tip urban in ordinea alfabetica dupa nume:")
    for locality in sorted_urban_localities:
        print(locality)

def calculate_percentage_localities():
    total_localities = 0
    urban_localities = 0
    rural_localities = 0

    with open('Location.txt', 'r') as lfile:
        lines = lfile.readlines()
        for line in lines:
            data = line.split()
            if data[-1] == 'urban':
                urban_localities += 1
            elif data[-1] == 'rural':
                rural_localities += 1
            total_localities += 1

    if total_localities == 0:
        print("Nu exista localitati in fisierul Location.txt.")
    else:
        urban_percentage = (urban_localities / total_localities) * 100
        rural_percentage = (rural_localities / total_localities) * 100

        print(f"Procentaj localitati urbane: {urban_percentage:.2f}%")
        print(f"Procentaj localitati rurale: {rural_percentage:.2f}%")


choice = ''
while choice != '0':
    print('-------------Meniu----------------')
    print('1. Vedeti fisierul clientilor. ')
    print('2. Vedeti fisierul localitatilor. ')
    print('3. Adauga un client nou in fisier. ')
    print('4. Adauga o localitate noua in fisier. ')
    print('5. Sterge un client din fisier. ')
    print('6. Sterge o localitate din fisier')
    print('7. Actualizeaza datele unui client. ')
    print('8. Actualizaaza datele unei localitati. ')
    print('9. Creaza fisierul VipClienti.txt ')
    print('10. Afiseaza localitatile de tip urban in ordinea alfabetica. ')
    print('11. afiseaza procentajul de localitati urbane si rurale')
    print('0. Exit')
    choice = input('Introduceti: ')

    match choice:
        case '1':
            show_the_cfile()
        case '2':
            show_the_lfile()
        case '3':
            add_one_client()
        case '4':
            add_one_location()
        case '5':
            delete_one_client()
        case '6':
            delete_one_location()
        case '7':
            update_one_client()
        case '8':
            update_one_location()
        case '9':
            create_vip_clients_file()
        case '10':
            location_tipe_urban()
        case '11':
            calculate_percentage_localities()    
        case '0':
            break
        case _:
            print('Valoarea introdusa nu exista.')