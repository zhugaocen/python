from twisted.internet import protocol,reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
    '''
    重写，当客户端连接时就会执行
    '''
    def connectionMade(self):
        #获取主机信息
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from: %s' % clnt)
    '''
    重写，当接收到客户端发送的数据时执行
    '''
    def dataReceived(self,data):
        #给客户端回信
        self.transport.write(('[%s]%s'%(ctime(),data.decode('utf-8'))).encode())

#实例化一个协议工厂
factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waiting for connection...')
#安装Tcp监听器
reactor.listenTCP(PORT,factory)
reactor.run()