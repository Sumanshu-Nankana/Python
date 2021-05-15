import time

def two():
    print("Starting Two")
    time.sleep(2)
    print("hey Two")
    
def four():
    print("Starting four")
    time.sleep(4)
    print("hey four")
    

start = time.time()
two()
four()
end = time.time()
print(f"{end-start}")  # this will run for 6 seconds