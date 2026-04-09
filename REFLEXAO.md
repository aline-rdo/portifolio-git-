# Reflexão Pessoal — Portfólio Git

---

## O que foi difícil

A parte mais complicada de todo o exercício foi o momento do merge conflict. Intelectualmente, eu entendia a ideia: duas branches mudaram o mesmo trecho de código e o Git não sabe qual versão prevalece. O problema foi na prática, quando vi os marcadores `<<<<<<<`, `=======` e `>>>>>>>` aparecendo dentro do arquivo Python no VSCode e travei completamente.
Minha primeira reação foi tentar rodar `git commit` sem resolver os marcadores, achei que o Git faria isso automaticamente. Recebi um erro dizendo que havia conflitos não resolvidos. Tentei então rodar `git merge --abort` por medo de estragar tudo, voltei ao estado anterior e precisei repetir o processo do zero. Só na segunda tentativa entendi que eu precisava primeiro editar o arquivo manualmente, remover os marcadores, deixar o código do jeito que eu queria, e só então rodar `git add` seguido de `git commit`. Outra dificuldade foi entender o estado do HEAD durante esse processo. Quando estou no meio de um merge, o Git fica em um estado intermediário diferente do normal. Os comandos `git status` mostravam mensagens que eu não estava acostumado a ver, como `"both modified"` e `"You have unmerged paths"`, a documentação na pagina do github foi uma ''moda na roda'' nessa hora. 
O padrão de commits semânticos também exigiu mais atenção do que eu esperava. No começo eu escrevia mensagens automáticas e sem pensar, depois percebi que tinha que parar antes de cada commit e perguntar: "o que exatamente estou comunicando aqui? é um feat, um fix ou um refactor?" Essa pausa forçada foi chata no início, mas foi justamente ela que me fez
pensar com mais cuidado sobre o que estava fazendo.

## O que ficou claro

O que ficou mais claro, é a ideia de que uma branch é apenas um ponteiro para um commit. Antes deste exercício eu imaginava branches como cópias separadas do projeto, quase como pastas diferentes no computador. Depois de criar, alternar e mergear várias branches, entendi que o Git não duplica nada, ele só move um ponteiro. Isso explica por que trocar de branch é instantâneo e por que o mesmo arquivo pode ter conteúdos diferentesdependendo de qual branch está ativa.
Os Pull Requests também deixaram de ser apenas um botão no GitHub. Entendi que um PR é uma unidade de revisão. Ele carrega uma proposta de mudança, conta a história dela (título + descrição) e abre espaço para discussão antes de incorporar o código.

## O que ainda é confuso

Ainda não tenho segurança total sobre quando usar `git merge` e quando usar `git rebase`. Sei que ambos integram mudanças de uma branch em outra, mas o rebase "reescreve o histórico" de um jeito que ainda não visualizo claramente. Li que o rebase deixa o histórico mais limpo e linear, mas também que pode causar problemas em branches compartilhadas. Fiz o exercício inteiro com merge e funcionou, mas sinto que estou evitando o rebase por não confiar
nele e não é uma boa razão para evitar uma ferramenta.
