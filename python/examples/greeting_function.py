# A lesson on scope

a_message = "Hello World"

def get_greeting():
    x = "Hello New World"
    return x


a_message = get_greeting()
print(a_message)


