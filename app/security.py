from argon2 import PasswordHasher

ph = PasswordHasher()

def hash_senha(senha: str) -> str:
    """Gera um hash seguro para a senha utilizando Argon2."""
    return ph.hash(senha)

def verificar_senha(senha_hash: str, senha_digitada: str) -> bool:
    """Verifica se a senha digitada confere com o hash armazenado."""
    try:
        return ph.verify(senha_hash, senha_digitada)
    except Exception:
        return False
