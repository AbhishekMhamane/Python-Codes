import time
import threading

def cal_square(numbers):
    print("Calculating the square of numbers")
    for i in numbers:
        time.sleep(0.2)
        print("square : ",i*i)
        
def cal_cube(numbers):
    print("Calculating the cube of numbers")
    for i in numbers:
        time.sleep(0.2)
        print("cube : ",i*i*i)


numbers = [1,2,3,4,5]
t = time.time()
t1 = threading.Thread(target=cal_square, args=(numbers,))
t2 = threading.Thread(target=cal_cube, args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Time needed",time.time()-t)
        