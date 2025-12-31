"""
AIM:
Simulate an organization-style login authentication
system 
The-system validates user credentials amd limits
login 
to protect against unauthorized access
"""
Max_attempts=2
Valid_usernames='Raeeschishty'
Valid_password='786786'

def authenticate(username,password):
    """
    Checks whether  provided credential are valid.
    """
    return username==Valid_usernames and password==Valid_password

def login_system():
    """
    Handles login attempts and user interaction.
    """
    attempt_left=Max_attempts

    while attempt_left >0:
        print('\n Login Required::')
        username=input('Username::')
        password=input('Password.')

        if authenticate(username,password):
            print('\n login successful:')
            print('Welcome to system!')
            return 
        else:
            attempt_left-=1 
            print(f'\n invalid credentials:')
            print(f'Attempts remaining {attempt_left}')
        print('\n Account locked due to multiple failed attempts')
        print('Please contect system administrator')


def main():
    """
    Programm entry point 
    """
    print('Organization Access Portal')
    login_system()
if __name__=='__main__':
    main()
