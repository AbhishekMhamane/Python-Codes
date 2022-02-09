import time
import multiprocessing

result = list()
def cal_square(numbers):
    global result
    print("Calculating the square of numbers")
    for i in numbers:
        time.sleep(0.2)
        print("square : ",i*i)
        result.append(i*i)
    print(result)
        
def cal_cube(numbers):
    print("Calculating the cube of numbers")
    for i in numbers:
        time.sleep(0.2)
        print("cube : ",i*i*i)

if __name__ == "__main__":
    numbers = [1,2,3,4,5]
    t1 = multiprocessing.Process(target=cal_square,args=(numbers,))
    t2 = multiprocessing.Process(target=cal_cube,args=(numbers,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(result)
    print("done")
