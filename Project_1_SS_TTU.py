import threading


class Object:
    def send():
        print("send")
    def recieve():
        print("recieve")
    def reply():
        print("reply")


if __name__ == "__main__":
    sender = threading.Thread()
    
    test = Object
    test.send()