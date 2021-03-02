import socket

class Server(object):

    # the public network interface
    # HOST = socket.gethostbyname(socket.gethostname())

    # host name and PORT number, this is actually related to our local machine
    HOST = socket.gethostname()
    PORT = None

    def __init__(self, server_sckt = None):

        # creating a socket object
        if server_sckt is None:
            try:
                # AF_INET, is related to the IPv4 IP family while SOCK_STREAM is related to the TCP protocol
                self.server_sckt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                print('Sokcet has been successfully created')

            except : #socket.error as error:
                print('Error(s) in creating socket')
                
            # calling the bind_listen method
            self.bind_listen()
            print('YEAH')

        else:
            self.server_sckt = server_sckt
            print('Cannot initialize the socket object')

    

    # binding the HOST IP and PORT to the socket object, then listening for clients connections
    def bind_listen(self):

        # getting the PORT on which we want to listen for new connections
        self.PORT = int(input('Enter the PORT NUMBER : '))
    
        try:
            # bind method received a tuple as args
            self.server_sckt.bind((self.HOST, self.PORT))
            print(f'[+]Server is bound on [{self.HOST} : {self.PORT}]')
        
        except TypeError:
            print('Binding error, check if you have a valid IP address and if the PORT format is integer')

        # listening to the new connections on the specified port
server = Server()