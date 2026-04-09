# Base inicial — será editada nas branches para gerar conflito
from validacao import validar_usuario  

USUARIOS = [
    {"id": 1, "nome": "Alice", "email": "alice@email.com"},
    {"id": 2, "nome": "Bob",   "email": "bob@email.com"},
]


def listar_usuarios():
    """Retorna todos os usuários cadastrados."""
    return USUARIOS


def buscar_por_id(usuario_id: int):
    """Busca um usuário pelo ID. Retorna None se não encontrado."""
    for usuario in USUARIOS:
        if usuario["id"] == usuario_id:
            return usuario
    return None

def adicionar_usuario(nome: str, email: str) -> dict:
    """Adiciona usuário apenas se os dados forem válidos."""
    novo = {"nome": nome, "email": email}
    erros = validar_usuario(novo)
    if erros:
        raise ValueError(f"Dados inválidos: {erros}")
    novo_id = max(u["id"] for u in USUARIOS) + 1
    novo["id"] = novo_id
    USUARIOS.append(novo)
    return novo
