import pymysql
from conf.meiziku import host,port,username_mysql,password_mysql,database,charset

class ConnectMySQL():
    '''连接数据库获数据库中的值'''

    def openmysql(self):
        '''连接数据库'''

        self.conn=pymysql.Connect(host=host,port=int(port),user=username_mysql,passwd=password_mysql,database=database,charset='utf8')
        return self.conn

    def get_cursor(self,conn):
        '''获取游标'''

        self.cur=conn.cursor()
        return self.cur

    def get_data(self,sql):
        '''
        执行SQL语句获取执行结果
        :param sql: sql 语句
        :return:
        '''
        conn=self.openmysql()
        cur=self.get_cursor(conn)
        cur.execute(sql)
        conn.commit()
        rlt=cur.fetchall()
        if rlt:
            return rlt

    def close_all(self):
        """
        关闭连接
        """
        self.cur.close()
        self.conn.close()

# config_data=ConnectMySQL().get_data()
# print(config_data)
con=ConnectMySQL()

if __name__ == '__main__':
    sql='SELECT * FROM t_config'
    conn=ConnectMySQL()
    print(len(conn.get_data(sql)))
    conn.close_all()