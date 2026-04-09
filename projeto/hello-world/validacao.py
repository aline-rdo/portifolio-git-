# Adicionado na branch feat/validacao-email

def validar_email(email: str) -> bool:
    """Valida se o e-mail tem formato básico nome@dominio.extensao."""
    if "@" not in email:
        return False
    partes = email.split("@")
    if len(partes) != 2:
        return False
    dominio = partes[1]
    if "." not in dominio:
        return False
    return True


def validar_usuario(usuario: dict) -> list[str]:
    """
    Valida os campos de um usuário.
    Retorna lista de erros (vazia se válido).
    """
    erros = []
    if not usuario.get("nome"):
        erros.append("Nome é obrigatório.")
    if not validar_email(usuario.get("email", "")):
        erros.append("E-mail inválido.")
    return erros