# Portfólio Git — Controle de Versão na Prática

Repositório criado como exercício prático de Git e GitHub, desenvolvido
durante as Semanas 2 e 3 do curso. O objetivo foi demonstrar domínio real
sobre commits semânticos, branches, Pull Requests e resolução de conflitos.

## Estrutura
portifolio-git/
├── exercicios/
│   ├── ex01-commits/notas.md        ← estudo sobre commits semânticos
│   ├── ex02-branches/notas.md       ← registro das branches criadas
│   └── ex03-conflito/REGISTRO.md    ← documentação da resolução de conflito
└── projeto/
|    └── hello-world/
|    ├── main.py                  ← ponto de entrada da aplicação
|    ├── usuarios.py              ← módulo de dados e operações de usuários
|    └── validacao.py             ← módulo de validação de e-mail e campos
├── README.md                        ← este arquivo
├── REFLEXAO.md                      ← reflexão pessoal sobre o processo

## Projeto: Hello World — Gestão de Usuários

Mini-aplicação em Python que simula operações básicas sobre uma lista de
usuários. Foi usada como base prática para todos os exercícios de Git.

### Módulos

| Arquivo | Responsabilidade |
|---|---|
| `main.py` | Orquestra a execução: lista, busca e adiciona usuários |
| `usuarios.py` | Armazena a lista de usuários e expõe funções de leitura e escrita |
| `validacao.py` | Valida formato de e-mail e integridade dos campos de um usuário |

### Como executar

```bash
# Certifique-se de ter Python 3.10+ instalado
python projeto/hello-world/main.py
```
Saída esperada:
=== Lista de Usuários ===
[✓] #1 — Alice (alice@email.com)
[✓] #2 — Bob (bob@email.com)
[✓] #3 — Diana (diana@email.com)
[✓] #4 — Eduardo (eduardo@email.com)

Usuário encontrado: {'id': 1, 'nome': 'Alice', 'email': 'alice@email.com'}

Usuário #99 não encontrado.

=== Adicionando novo usuário ===
Criado: {'id': 5, 'nome': 'Carlos', 'email': 'carlos@email.com'}

## Requisitos Cumpridos

| Requisito | Descrição | Status |
|---|---|---|
| R1 | Mínimo 10 commits semânticos (Conventional Commits) | ✅ |
| R2 | Mínimo 3 branches além da main, todas mergeadas | ✅ |
| R3 | Mínimo 2 Pull Requests com título, descrição e comentário | ✅ |
| R4 | Resolução de merge conflict documentada | ✅ |
| R5 | REFLEXAO.md com 400+ palavras em 3 seções | ✅ |

## Branches Criadas

| Branch | Propósito | Tipo de merge |
|---|---|---|
| `feat/rota-usuarios` | Adiciona função de criar usuário | Pull Request |
| `feat/validacao-email` | Cria módulo de validação e integra ao cadastro | Pull Request |
| `feat/adiciona-diana` | Adiciona usuário Diana (usada para gerar conflito) | Linha de comando |
| `feat/adiciona-eduardo` | Adiciona usuário Eduardo (gerou merge conflict) | Linha de comando |
| `docs/atualiza-readme` | Finaliza documentação do repositório | Linha de comando |

