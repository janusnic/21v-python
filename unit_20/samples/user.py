from queue import Queue

unconfirmed_users_queue = Queue()

def user_registration(user):
    global unconfirmed_users_queue
    unconfirmed_users_queue.put(user)
    print("User {0} registered".format(user))
    
def confirm_users():
    print("Confirming users (FIFO)")
    global unconfirmed_users_queue
    while not unconfirmed_users_queue.empty():
        user = unconfirmed_users_queue.get()
        print("User {0} confirmed".format(user))

def register_several_users(): 
    user=''

    while True:
        user = raw_input()
        if user == "quit":
            break
        else:
            user_registration(user)

register_several_users()
confirm_users()