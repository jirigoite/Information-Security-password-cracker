import hashlib

def crack_sha1_hash(hash, use_salts=False):

    # Cargar la lista de contraseñas
    with open("top-10000-passwords.txt", "r", encoding="utf-8") as f:
        passwords = [line.strip() for line in f.readlines()]

    # Cargar salts si corresponde
    if use_salts:
        with open("known-salts.txt", "r", encoding="utf-8") as f:
            salts = [line.strip() for line in f.readlines()]
    else:
        salts = [""]  # Sin salt, tratamos como salt vacío

    # Brute force
    for password in passwords:

        for salt in salts:
            # probar salt + password
            attempt = hashlib.sha1((salt + password).encode()).hexdigest()
            if attempt == hash:
                return password

            # probar password + salt (si hay salt)
            if salt != "":
                attempt = hashlib.sha1((password + salt).encode()).hexdigest()
                if attempt == hash:
                    return password

    return "PASSWORD NOT IN DATABASE"
