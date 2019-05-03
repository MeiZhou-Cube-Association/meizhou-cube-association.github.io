def AddId(info, db_path):
    file = open(db_path+'wca_id.csv', encoding='utf-8', mode='r')
    names=file.readlines()
    for i in names:
        if i[:10] == info[1]:
            return
    file = open(db_path+'wca_id.csv', encoding='utf-8', mode='a')
    # print(names)
    del info[-1]
    info[0], info[1] = info[1], info[0]
    file.write(','.join(info)+'\n')
    file.close()