# Registro de Resolução de Conflito

## Arquivo com conflito
`projeto/hello-world/usuarios.py`

## Trecho que gerou conflito
A lista `USUARIOS` foi editada em duas branches diferentes ao mesmo tempo.

## Como resolvi
Mantive a versão que combinava os dados das duas branches, preservando
todos os usuários adicionados em cada uma.

## Comando usado para finalizar
```bash
git add projeto/hello-world/usuarios.py
git commit -m "fix(ex03): resolve conflito na lista de usuarios"
```