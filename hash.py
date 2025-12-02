def buscar_usuario(usuarios, username):
    return usuarios.get(username, None)

usuarios = {
    "emilia01": "emilia01@correo.com",
    "leo_prog": "leo_prog@correo.com",
    "valen_dev": "valen_dev@correo.com",
    "admin": "admin@sistema.com"
}

print("USUARIOS REGISTRADOS (username -> correo):")
for user, correo in usuarios.items():
    print(f"{user:10s} -> {correo}")

username = input("\nIngresa el nombre de usuario a buscar: ")

correo = buscar_usuario(usuarios, username)

if correo is not None:
    print(f"\nUsuario encontrado. Correo asociado: {correo}")
else:
    print("\nEl usuario NO está registrado en el sistema.")
