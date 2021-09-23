import time

total_time=0

def display():
    global total_time
    total_time=25*60
    while (total_time!=0):
       print(" {0:2d}:{1:2d}".format(int(total_time/60), total_time%60))
       time.sleep(1)
       total_time -=1

def tasks():
   print('Pomodoro begins!')
   display()
   print(' Task done')


def shortbreak():
    global total_time
    total_time=3*60
    print('Short break begins')
    display()
    print ("Break over!")      

def longbreak():
    global total_time
    total_time=10*60
    print('Long break begins')
    display()
    print('Break over!')
           
        
def main():
    carryon= 'y'
    while (carryon=='y' or carryon== 'Y'):
       tasks()
       carryon = input('Do you want to continue? Press y/n')
    print('Bye!')

main()



      
   




