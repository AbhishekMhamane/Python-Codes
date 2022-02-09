class UserException(Exception):
    def __init__(self,msg):
        self.msg = msg
    def printException(self):
        print(self.msg)

if __name__ == '__main__':
    try:
        raise UserException("Userdefined Exception Occured")
    except UserException as e:
        e.printException()
    finally:
        print("This is final block")
    