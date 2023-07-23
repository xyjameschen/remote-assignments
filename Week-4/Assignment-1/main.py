from threading import *
from time import sleep

def do_job(number):
    sleep(3)
    print(f"Job {number} finished")

# rewrite everything inside this main function and keep others untouched
def main():
    for i in range(5):
        Thread(target=do_job, args=(i,)).start()

main()