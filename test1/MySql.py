from pymysql import connect

conn=connect(host='localhost',
             user='root',
             password='123456',
             port=3306,
             database='test',
             charset='utf8')

try:
    cursor = conn.cursor()
except Exception as e:
    print("连接失败",str(e))
else:
    print('连接成功')


def excute_sql(command,sql):
    '''
    查询数据库数据
    :param command:
    :param sql:
    :return:
    '''
    if command in ('SELECT','select'):
        #如果为查询指令
        sql = sql.encode('utf-8')
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            conn.close()
    elif command in ('delete','DELETE','update','UPDATE','insert','INSERT'):
        #如果为增删改
        sql = sql.encode('utf-8')
        try:
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            #如果失败则回滚
            conn.rollback()
            print(e)
        finally:
            conn.close()
    else:
        print('Command Error!')

if __name__ == '__main__':
    sel_sql = 'select * from test1;'
    print(excute_sql('select',sel_sql))