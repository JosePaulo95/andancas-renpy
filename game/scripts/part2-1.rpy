label sair_de_casa:
    jump indo_pra_vila

label indo_pra_vila:
    scene bg_village_manha with dissolve
    pause 1
    show tata at left with moveinleft
    pause 1
    show sssocrates at center with moveinright
    pause 1
    sssocrates "Ssser ou não ssser... eiss a quesstão!"
    pause 1
    tata "Bom dia, Seu Sócrates."
    sssocrates "Bom dia, sssenhorita. A pronúncia e 'Sssócrates'"
    tata "Desculpe Seu..."
    menu:
        "Sssócrates":
            jump socrates3s
        "Ssssócrates":
            jump socrates4s

label socrates3s:
    sssocrates "Excsselente, Tatá. Estáss cada vez melhor."
    tata "Agradecsssida!"
    jump dona_clarica

label socrates4s:
    sssocrates "Não! É Sssócrates! Com 'sss'!"
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
        "Melhor deixá-la dormir…":
            jump melhor_deixa_cica_dormir
        "BOM DIA, DONA CLARICA":
            jump grita_pra_cica

label melhor_deixa_cica_dormir:
    "Me pergunto se ela tem sonhos malucos igual a mim..."
    "Talvez ela sonhe tudo em câmera lenta."
    jump village_encontra_cuica

label grita_pra_cica:
    cica "ohh… bommm diaa, Tataa… acabei cochilando de novoo…"
    tata "Já amanheceu! É dia de feira!"
    cica "É verdade… hoje eu vou… uahhh… eu vou…"
    cica "hm… zzzz…."
    "Hehe, não tem jeito."
    jump village_encontra_cuica

label village_encontra_cuica:
    hide cica with moveoutleft
    pause 1
    show cuica at center with moveinright
    # <!--`Uma cuica com varios filhotes nas costas, Enzo, Lorenzo e Valentina um esta chorando`-->
    lorenzo "Buááá! Mãããe!!!"
    valentina "Mãããe! O Enzo puxou a cauda do Lorenzo!" with hpunch
    enzo "Shhh! Sua cagueta!"
    valentina "Mããe! Olha do que ele me chamou!"
    cuica "Eu já falei pra parar, menino!"
    enzo "Mãe, mas ele fica me empurrando!"
    lorenzo "Buááá!!"
    menu:
        "Bom dia, Dona Cuíca. Bom dia, crianças.":
            jump bom_dia_dona_cuica
        "(Observar a confusão)":
            jump observar_a_confusao

# label start:
label bom_dia_dona_cuica:
    cuica "Bom dia, Tatá! Aproveitando as férias?"
    menu:
        "Claro!":
            jump claro
        "Entediada...":
            jump entediada

label claro:
    "Eu amo…"
    menu:
        "acordar tarde!":
            tata "Eu amo acordar tarde!"
            tata "Nós tatus somos mais ativos à noite. Ter que acordar cedo e ainda tomar banho com água gelada... ai não!"
            valentina "Nós também somos noturnas!"
            enzo "Mas, a gente gosta de acordar cedo!"
            lorenzo "5 da manhã já estamos acordados"
            enzo "Acordados e pulando!"
            cuica "Eu te entendo perfeitamente, Tatá..."
            tata "Tenho que ir, até mais, pessoal!"
            lorenzo_enzo_valentina "Até mais!"
        "ter tempo livre!":
            tata "Agora eu posso ler Harry Potro, jogar Liga das Lontras, assistir Tatunic..."
            lorenzo "E podemos fazer bolo de lama, pular na cama, caçar insetos!"
            enzo "Viva férias!!!"
            valentina "Vivaa!"
            cuica "Falta quanto mesmo pra as férias acabarem?"
            tata "Umas duas semanas."
            cuica "Duas longas semanas..."
        "não precisar pegar onibus!":
            tata "Indo pra cidade e voltando tenho que pegar quatro ônibus por dia! São horas e horas, todo dia!"
            cuica "Oh, pobrezinha. Por sorte as crianças estão tendo aulas na Biblioteca Comunitária com o professor Sssócrates"
            valentina "Ele é muito legal!"
            lorenzo "É nada!"
            enzo "Eu preferia pegar um milhão ônibus!"
            cuica "Meninos! Modos!"
            tata "Até mais, pessoal!"
            lorenzo_enzo_valentina "Até mais, Tatá!"
    jump sai_dona_cuica

label entediada:
    "eu sinto falta..."
    menu:
        "dos meus colegas":
            tata "Principalmente a Bia Ben-te-vi e o André Jacaré."
            cuica "Pelo menos o Rubens Guará também mora aqui na Vila. Ele não é da sua turma?"
            tata "Ele é turista. Escolhe uns 3 dias na semana pra ir e falta o resto."
            enzo "Mamãe eu também quero fazer isso!"
            lorenzo "Eu também!"
            cuica "Larga de conversa menino! Por que vocês não seguem o exemplo da Tatá?"
            tata "Hehehe vou me esforçar pra ser um bom exemplo! Até logo, pessoal!"
            lorenzo_enzo_valentina "Até logo!"
        "de ir pra cidade":
            tata "Aqui na vila não tem nada pra fazer"
            tata "Em São Luís tem o Centro Histórico, e museus, e shoppings!"
            enzo "Mamãe eu quero ir pra cidade!"
            lorenzo "Eu também!"
            valentina "Vamos mamãe!!"
            cuica "A Tatá que deu a ideia, ela vai levar vocês!"
            menu:
                "Claro! Vamos combinar!":
                    pass
                "Er... acho que ouvi alguem me chamando...":
                    pass
    tata "Até logo, pessoal!"
    carlacuica "Até logo!"
    jump sai_dona_cuica

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
    jump sai_dona_cuica

label sai_dona_cuica:
    hide cica with moveoutleft
    pause 1
    jump encontra_rubens