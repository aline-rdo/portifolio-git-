# Base inicial — será editada nas branches para gerar conflito

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
    """Adiciona um novo usuário e retorna o objeto criado."""
    novo_id = max(u["id"] for u in USUARIOS) + 1
    novo = {"id": novo_id, "nome": nome, "email": email}
    USUARIOS.append(novo)
    return novo