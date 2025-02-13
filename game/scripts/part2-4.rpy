define flipped = Transform(xzoom=-1)

# label avisando_vovo:
label start:
    scene bg_colheita with dissolve
    show tata at right, flipped with moveinleft
    # <bg: um campo de macaxeiras em frente à toca de Tatá>
    tata "Vô!! O senhor não vai acreditar!"
    getulio "Eu não acredito mesmo, você estava tentando escapar do trabalho?"
    tata "Eu posso explicar..."
    getulio "Poupe suas palavras, mocinha! Estamos atrasados e essas macaxeiras não vão se colher sozinhas!"
    tata "Ei! Volta aqui, vô!"
    getulio "Você começa por esse lado e eu pelo outro."
    "Acho que ele só vai parar pra me ouvir quando terminarmos isso..."
    # <minigame: clicar nas macaxeiras no solo para colher>
    "Finalmente!"
    getulio "Bom trabalho, Tatá. Não foi tão difícil, afinal!"
    menu:
        "Tem razão, vô.":
            tata "Desculpe por não ter avisado que me atrasaria."
        "Foi sim!":
            tata "Acho que essa vida de agricultora não é pra mim..."
    tata "Mas agora o senhor precisa ver isso."
    "Entrego o documento a ele."
    tata "O tremor que sentimos de manhã... eram tratores. Eles começaram a derrubar a floresta da Vila. Disseram que vão iniciar a construção já na próxima semana."
    getulio "..."
    tata "Vô?"
    getulio "..."
    "Ele está encarando o papel, pálido, olhos arregalados. É a mesma expressão de fez de manhã."
    tata "Vô, o senhor está bem?"
    getulio "Sim, sim... desculpe... Obrigado, Tatá. Vou até a Vila mostrar esse arquivo. Precisamos reunir os moradores com urgência em uma assembleia... oh..."
    "O vô Getúlio cai de joelhos no chão."
    tata "Vô!!"
    tata "Vou chamar um médico!"
    getulio "Não, não, foi só uma tontura… eu já estou bem, está vendo?”"
    getulio "Temos outras prioridades agora. Se quer mesmo me ajudar então termine de guardar a colheita. Eu vou até o Centro Comunitário"
    tata "..."
    getulio "Pode fazer isso por mim?"
    tata "Tudo bem."
    # <Background preto>
    "O vovô passou o resto do dia fora." 
    "Algumas pessoas me ligaram pra saber da notícia. Amigos, moradores, meus pais… eles estão voltando pra vila o mais rápido possível."
    "Disseram que enquanto não chegam eu devo cuidar do vovô."
    # <Background quarto, sons da noite.>
    "Quando o vovô chegou em casa nem quis jantar. Foi direto pro seu quarto, disse que amanhã temos que acordar cedo porque os moradores vão fazer uma assembleia na biblioteca comunitária."
    "Tenho um mau pressentimento..."
    # [[Dormir]]
    # <Backgound fade preto> 
    # <Background floresta sombria tremendo, som de um coração batendo forte>
    "Estou correndo!" 
    "Todo o meu corpo dói! Tenho que ir mais rápido!"
    "Escapar! ... mas... de quê?"
    "Eu..."
    "Paro de correr."
    "Sou a guerreira Tatá Peba… não deveria ter medo de nada..." 
    "Então o que é essa sensação? De que estou fugindo?"
    "Será que sou mesmo digna de empunhar essa espada?"
    menu:
        "Claro que sim!":
            "Eu não posso desistir agora!"
        "Já não sei...":
            "estou com tanto medo!"
    rasgamortalha "Ora, ora…"
    # <som da coruja rasga mortalha, ela aparece com o rosto tapado pelo capuz>
    rasgamortalha "Pode correr, mas não tem pra onde escapar…"
    rasgamortalha "Eu irei destruir a sua Vila!"
    # <O rosto da coruja se revela abaixo do capuz>
    tata "É você!!"
    "A coruja abre as asas para me atacar!"
    menu:
        "Fugir":
            tata "Estou fraca! Não posso lutar agora!"
            rasgamortalha "Adagas de penas!"
            "Penas brancas afiadas como facas começam a chover ao meu redor"
            # <!--Imagem??-->
            "Estou correndo o mais rápido que posso, tento desviar dos ataques mas as penas são muito rápidas!"
            # <!--Imagem??-->
            "Uma delas acerta a minha armadura e eu caio no chão!"
            rasgamortalha "Ha ha ha ha!! Patético!"
            "Ele sai voando, sua risada ecoa na floresta..."
            "Essa não!! Ele está indo pra Vila!"
            "Preciso avisá-los!! Eu preciso..."
            # <Fade out>
        "Defender":
            tata "Estou fraca, mas não posso fugir agora!"
            rasgamortalha "Adagas de penas!"
            "Penas brancas afiadas como facas começam a chover ao meu redor"
            # <!--Imagem-->
            menu:
                "Virar uma bola!":
                    "Bola em modo de defesa!"
                "Usar o escudo!":
                    "Empunho meu escudo na direção dos ataques."
            "As penas me atingem, mas não conseguem ultrapassar minha carapaça!"
            rasgamortalha "Então você ainda tem alguns truques na manga..."
            rasgamortalha "Pode até se defender, mas, vai conseguir salvar a todos!" 
            tata "Não! Deixe a minha Vila em paz!"
            rasgamortalha "Ha ha ha ha!!"
            "Ele sai voando, sua risada ecoa na floresta..."
            "Essa não!! Ele está indo pra Vila!"
            "Preciso avisá-los!! Eu preciso..."
            # <Fade out>
        "Atacar também":
            tata "Não posso fugir! Eu sou uma guerreira!"
            tata "Vou usar o golpe..."
            menu:
                "Rolo compressor!":
                    "Em formato de bola, saio rolando, ganhando velocidade!"
                "Espada vingadora!!":
                    "Puxo a minha espada e corro em sua direção!"
            "Algumas penas me atingem e machucam, mas não posso parar!"
            "Estou cada vez mais perto! Não consigo desviar de seus ataques, mas renho que continuar!!" 
            "Meu inimigo tenta desviar, mas é tarde demais! POW! Eu o atinjo em cheio, lançando-o para trás com minha espada!"
            tata "Vá embora! E não volte mais!"
            rasgamortalha "Ora, então você ainda tem alguns truques na manga..."
            rasgamortalha "Mas, não se iluda!, Você não pode salvar a todos!" 
            tata "Não! Deixe a minha Vila em paz!"
            rasgamortalha "Ha ha ha ha!!"
            "Ele sai voando, sua risada ecoa na floresta..."
            "Essa não!! Ele está indo pra Vila!"
            "Preciso avisá-los!! Eu preciso..."
            # <Fade out>

