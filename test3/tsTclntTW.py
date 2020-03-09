from twisted.internet import protocol,reactor

HOST ='localhost'
PORT = 21567

class TSClntPortocol(protocol.Protocol):
    def sendData(self):
        data = input('>')
        if data:
            print('...sending %s...' % data)
            self.transport.write(data.encode())
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self,data):
        print(data.decode('utf-8'))
        self.sendData()

class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntPortocol
    ClientConnectionLost = clientConnectionFailed = lambda self,connector,reason:reactor.stop()

reactor.connectTCP(HOST,PORT,TSClntFactory())
reactor.run()