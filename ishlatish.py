from function import register,  login

k = int(input('Sign up / Sign in (0/1): '))
is_registered = False

if k == 0:
    is_registered = register()

if (k == 0 and is_registered) or k == 1:
    user_id = login()
    print(user_id)

else:
    is_registered = register()
    print('User cannot registered! Please try again')

