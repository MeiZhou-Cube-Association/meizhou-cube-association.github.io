def AddId(id, db_path):
    file = open(db_path+'wca_id.csv', encoding='utf-8', mode='r')
    names=file.readlines()
    for i in names:
        if i[:-1] == id:
            return
    file = open(db_path+'wca_id.csv', encoding='utf-8', mode='a')
    # print(names)
    file.write(id+'\n')
    file.close()