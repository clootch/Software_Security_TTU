import threading
import rsa
import hashlib
class MBRC:
    """
    Below is the necessary functions and variables for the MBRC class as described in the HW assignment. 
    """
    def __init__(self,messageBuffer=[],responseBuffer=[]):
        self.messageBuffer = messageBuffer
        self.responseBuffer = responseBuffer
        self.Sender = Sender()
        self.Receiver = Receiver()
        self.signature = ""

    def send(self):
        for message in self.messageBuffer:
            self.Sender.printMessage(message)
            self.signature = self.Sender.sign(message)
            self.receive(message,self.signature)

    def receive(self,message,signature):
        number = self.Receiver.verify(message,signature,self.Sender.publicKey)
        self.Receiver.printResult(number)
        self.reply(number)

    def reply(self,number):
        digest = self.Receiver.generate(number)
        self.Sender.verify(number,digest,self.Receiver.publicKey)

class Sender(threading.Thread):
    def __init__(self):
        (self.publicKey,self.privateKey) = rsa.newkeys(512)

    def printMessage(self,message):
        print(message)

    def printReceivedResult(self,number):
        print(number)

    def sign(self,message):
        message = message.encode()
        return rsa.sign(message,self.privateKey,'SHA-256')

    def verify(self,number,digest,publicKey):
        try:
            rsa.verify(str(number).encode(),digest,publicKey)
        except:
            print("Verification Failed.")
            quit(0)
        self.printReceivedResult(number)

class Receiver(threading.Thread):
    def __init__(self):
        (self.publicKey,self.privateKey) = rsa.newkeys(512)
        self.Adder = AddCalculation()
        self.Multiply = MultiplyCalculation()
    def verify(self,message,signature,publicKey):
        try:
            rsa.verify(message.encode(),signature,publicKey)
        except:
            print("Verification Exception Thrown")
            quit(0)
        word,num = message.split(",")
        if word == "add":
            number = self.Adder.add(int(num))
        else:
            number = self.Multiply.multiply(int(num))
        return number
    def generate(self,number):
        return rsa.sign(str(number).encode(),self.privateKey,'SHA-256')
    def printResult(self,num):
        print(num)

class AddCalculation:
    def __init__(self):
        pass

    def add(self,num):
        return num + 10

class MultiplyCalculation:
    def __init__(self):
        pass

    def multiply(self,num):
        return num * 10

#this is the main method, this will begin the program
if __name__ == "__main__":
    sender = threading.Thread()
    
    test = MBRC(["add,4","multiply,1","multiply,8","add,2","add,3","add,99","multiply,53"])
    test.send()