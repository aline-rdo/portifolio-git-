from usuarios import listar_usuarios, buscar_por_id
from validacao import validar_usuario, validar_email


def exibir_usuarios():
    print("=== Lista de Usuários ===")
    for u in listar_usuarios():
        status = "✓" if validar_email(u["email"]) else "✗"
        print(f"  [{status}] #{u['id']} — {u['nome']} ({u['email']})")


def buscar_usuario(usuario_id: int):
    usuario = buscar_por_id(usuario_id)
    if usuario:
        erros = validar_usuario(usuario)
        print(f"\nUsuário encontrado: {usuario}")
        if erros:
            print(f"  ⚠ Problemas: {erros}")
    else:
        print(f"\nUsuário #{usuario_id} não encontrado.")


if __name__ == "__main__":
    exibir_usuarios()
    buscar_usuario(1)
    buscar_usuario(99)