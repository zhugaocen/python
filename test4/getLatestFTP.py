'''
下载网站中最新版本的文件
'''

import ftplib
import os
import socket

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'

def main():
    try:
        f = ftplib.FTP(HOST)
    except (socket.error,socket.gaierror) as e:
        print('ERRO: cannot reach "%s"' % HOST)
        return
    print('...connected to host "%s"' % HOST)

    try:
        f.login()
    except ftplib.error_perm:
        print('ERROR：connot login anonymously')
        f.quit()
        return
    print('...logged in as "annoymous"')

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print('ERROR:connot CD to "%s"' % DIRN)
        f.quit()
        return
    print('...changed to "%s" folder' % DIRN)

    try:
        f.retrbinary('RETR %s' % FILE, open(FILE, 'wb') .write)
    except ftplib.error_perm:
        print('ERROR:cannot read file "%s"' % FILE)
        os.unlink(FILE)
    else:
        print('... Downloaded "%s" to CWD' % FILE)
        f.quit()

    if __name__ == '__ main__':
        main()
