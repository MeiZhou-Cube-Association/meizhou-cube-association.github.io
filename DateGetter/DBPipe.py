# 用于从自己的远程db 获得数据
# 类似管道
import getpass
import pymysql

class DBPipe:
    def __init__(self):
        def Connect()->bool:
            self.db_server = input("Server [localhost]:")
            self.db_database = input("Dataase [wca_db]:")
            self.db_port = input("Port [3306]:")
            self.db_username = input("Username [wca_db_onlooker]:")
            self.db_password = getpass.getpass("Password:")
            # 设置默认值
            if not self.db_server:
                self.db_server = "localhost"
            if not self.db_database:
                self.db_database = "wca_db"
            if not self.db_port:
                self.db_port = 3306
            if not self.db_username:
                self.db_username = "wca_db_onlooker"
            try:
                self.db = pymysql.connect(self.db_server, self.db_username, 
                                self.db_password, self.db_database,port=self.db_port)
            except Exception as e:
                print("Except Error {0}".format(e))
                return False
            return True
        while True:
            status = Connect()
            if status:
                break
    # def Select(table)