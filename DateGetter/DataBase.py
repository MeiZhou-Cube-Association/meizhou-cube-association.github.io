def AddName(name, db_path):
    file = open(db_path+'name.csv', encoding='utf-8', mode='r')
    names=file.readlines()
    for i in names:
        if i[:-1] == name:
            return
    file = open(db_path+'name.csv', encoding='utf-8', mode='a')
    print(names)
    file.write(name+'\n')
    file.close()