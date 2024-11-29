# label sair_de_casa:
label sair_de_casa:
    jump indo_pra_vila

label indo_pra_vila:
    scene bg_village with dissolve
    pause 1
    show tata at left with moveinleft
    pause 1
    show sssocrates at center with moveinright
    pause 1
    sssocrates "Ssser ou nao ssser... eiss a quesstão!"
    pause 1
    tata "Bom dia, Seu Socrates."
    sssocrates "Bom dia, sssenhorita. A pronuncia e 'Sssocrates'"
    tata "Desculpe Seu..."
    menu:
        "Sssocrates":
            jump socrates3s
        "Ssssocrates":
            jump socrates4s

label socrates3s:
    sssocrates "Excsselente, Tata. Estáss cada vez melhor."
    tata "Agradecsssida!"
    jump dona_clarica

label socrates4s:
    sssocrates "Não! É Sssocrates! Com 'sss'!"
    tata "Desssculpa!"
    jump dona_clarica

label dona_clarica:
    hide sssocrates with moveoutleft
    pause 1
    show cica at center with moveinright
    # <!--Seria Uma preguica bem velhinha, Dona Cica esta deitada em uma cadeira de balanco dormindo-->
    tata "Bom dia, dona Cica!"
    cica "zzzzz…."
    menu:
        "melhor deixá-la dormir…":
            jump melhor_deixa_cica_dormir
        "BOM DIA, DONA CLARICA":
            jump grita_pra_cica

label melhor_deixa_cica_dormir:
    "Me pergunto se ela tem sonhos malucos igual a mim..."
    "Talvez ela sonhe tudo em camera lenta."
    jump village_encontra_cuica

label grita_pra_cica:
    cica "ohh… bommm diaa, Tataa… acabei cochilando de novoo…"
    tata "Já amanheceu! É dia de feira!"
    cica "É verdade… hoje eu vou… uahhh… eu vou…"
    cica "hm… zzzz…."
    "Hehe, nao tem jeito."
    jump village_encontra_cuica

label village_encontra_cuica:
    hide cica with moveoutleft
    pause 1
    show cuica at center with moveinright
    # <!--`Uma cuica com varios filhotes nas costas, Enzo, Lorenzo e Valentina um esta chorando`-->
    lorenzo "Buááá! Mãããe!!!"
    valentina "Mãããe! O Enzo puxou a cauda do Lorenzo!"
    enzo "Shhh! Sua cagueta!"
    valentina "Mããe! Olha do que ele me chamou!"
    cuica "Eu já falei pra parar, menino!"
    enzo "Mãe, mas ele fica me empurrando!"
    lorenzo "Buááá!!"
    menu:
        "Bom dia, Dona Cuíca. Bom dia, criancas.":
            jump bom_dia_dona_cuica
        "(Observar a confusão)":
            jump observar_a_confusao

label bom_dia_dona_cuica:
    cuica "Bom dia, Tata! Aproveitando as ferias?"
    # menu:
    #     "Claro!":
    #         jump claro
    #     "Entediada...":
    #         jump entediada

label observar_a_confusao:
    cuica "Eu vou contar até 3…"
    enzo "Viu? Fecha a matraca, Valentina!"
    valentina "Fecha a matraca já morreu, quem manda na minha matraca sou eu!"
    cuica "1..."
    enzo "Cara de rato!"
    valentina "Cara de rato é quem me chama!"
    enzo "Cavalo manco é que te ama!"
    cuica "2..."
    enzo "eu durmo na cama, tu dorme na lama"
    valentina "A cama quebra, velho do saco te leva!"
    lorenzo "Buááá!"
    cuica "Chega! Vou pegar minha chinela e vocês vão ver só!!"
    lorenzo_enzo_valentina "Aaaaaaaa"
    #"os filhotes desaparecem de suas costas"
    tata "Bom dia, Dona Cuíca"
    cuica "Bom dia, Tata. Falta quanto mesmo pra as ferias acabarem?"
    tata "Umas duas semanas."
    cuica "Duas longas semanas..."
