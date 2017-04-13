import pymysql
from consts import HOSTNAME, DATABASE, USERNAME, PASSWORD

try:
    con = pymysql.connect(HOSTNAME, USERNAME, PASSWORD, DATABASE)
    cur = con.cursor()
    cur.execute("SELECT VERSION()")
    ver = cur.fetchone()
    print "Datebase version : %s " % ver
except pymysql.Error as e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    exit(1)
finally:
    if con:
        con.close()