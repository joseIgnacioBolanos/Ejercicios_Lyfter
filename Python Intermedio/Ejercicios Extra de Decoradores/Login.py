user_logged_in   = True

def requires_login(func):
    def wrapper():
        if not user_logged_in:
            raise ValueError('Usuario no autenticado"')
        else:
            func()
    return wrapper

@requires_login
def view_profile():
    print("Mostrando perfil del usuario")

view_profile()



