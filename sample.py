import random
import collections
import itertools
import time
start=time.time()
class Sample:
    def __init__(self): 
        self.prefernces = {} 
        self.randomlist = []
        self.inp = input("Enter min value")
        with open('datatest.txt', 'r') as file:
            data = [line.rstrip('\n') for line in file]
        print(time.time()-start)
        #for user in data:
            #print(user)
        random_list = random.sample(data, 4)
        for user in random_list:
                self.randomlist.append(user.split(','))
        overall_list = list(itertools.chain.from_iterable(self.randomlist))
          
        for i in overall_list:
            if "user" in i:
                overall_list.remove(i)
        #print("ran",*overall_list, sep = '\n')

        final_list = collections.Counter(overall_list)
        print("final", *final_list, sep='\n')
        my_keys = sorted(final_list, key=final_list.get, reverse=True)[:3]
        #print(my_keys)
    def print_list(self):
        for item in self.prefernces:
            print(item)
    
    
if __name__ == "__main__":
    S=Sample()
    S.print_list()
    print(time.time() - start)
