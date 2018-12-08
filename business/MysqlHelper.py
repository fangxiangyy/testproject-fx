import pymysql as pymysql


class MysqlHelper:
    def __init__(self,host='localhost',port=3306,db ='test01',user='root',passwd = 'root',charset = 'utf8' ):
        self.conn = pymysql.connect(host=host,port=port,db=db,user=user,passwd=passwd,charset=charset)

    def insert(self,sql,params):
        return self.__cud(sql,params)

    def update(self,sql,params):
        return self.__cud(sql,params)

    def delete(self,sql,params):
        return self.__cud(sql,params)

    def __cud(self,sql,params=[]):
        try:
            cs1 = self.conn.cursor()
            rows = cs1.execute(sql,params)
            self.conn.commit()
            cs1.close()
            self.conn.close()
            return rows
        except Exception as e:
            print(e)
            self.conn.rollback()

    def fetchone(self, sql, params=[]):
            # 一次只返回一行查询到的数据
        try:
            cs1 = self.conn.cursor()
            cs1.execute(sql, params)
            row = cs1.fetchone()
            # 把查询的结果集中的下一行保存为序列
            # print(row)
            # row是查询的值
            cs1.close()
            self.conn.close()
            return row
        except Exception as e:
            print("None", e)

    def fetchall(self, sql, params):
        # 接收全部的返回结果行
        # 返回查询到的全部结果值
        try:
            cs1 = self.conn.cursor()
            cs1.execute(sql, params)
            rows = cs1.fetchall()
            cs1.close()
            self.conn.close()

            return rows
        except Exception as e:
            print("None", e)
