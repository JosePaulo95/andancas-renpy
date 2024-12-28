label seguir_pneus:
    scene bg_floresta with fade

    tata "Estão indo na direção da floresta… que estranho!"
    rubens "Pode crer, não tem nem estrada pra essas bandas."

    # Som de trator e motores
    play sound "trator_motores.ogg"

    tata "Está cercado por fitas de restrição."
    rubens "Isso não me cheira bem, vamos embora, Tatá."
    tata "Ah, não! Agora vamos até o fim."

    scene bg_trator_destruindo with fade

    tata "Ai, meu Santo Tatu Bolinha! Estão destruindo tudo!"
    rubens "Está vindo na nossa direção! Vamos meter o pé daqui!!"

    menu:
        "Espera! Temos que investigar!!":
            rubens "A gente vai é virar purê! Vou bater as asas!!"
            menu:
                "Deixar Rubens ir":
                    tata "Pode ir, covardão!"
                    tata "Ei! Você aí! Pare agora!"

                    # Som da rasga mortalha
                    play sound "rasga_mortalha.ogg"

                    tata "Uma coruja sinistra está lá dentro pilotando!"
                    rasgamortalha "..."

                    "Essa não! Ele continua avançando!"
                    "Mas, a guerreira Tatá não deve ter medo!"

                    menu:
                        "Pare agora!" or "Passa por cima!!":
                            "O trator desacelera até parar, bem na minha frente." 
                            tata "Ufa! Essa foi por pouco!" 
                            rubens "Tatá! Estou voltando! Você sobreviveu?!"
                            tata "Não graças a você!"
                            "Alguém sai de dentro do trator”
                            #todo show in
                            jump motorista_fala
                            # billgarca "Boa tarde, senhores. Poderiam me esclarecer o motivo deste alvoroço?" 

                "Agarrar Rubens":
                    tata "Calma aí!! Eles não vão ter coragem de passar por cima da gente!"
                    # Som da rasga mortalha
                    play sound "rasga_mortalha.ogg"

                    "Dentro do trator há uma coruja com cara de poucos amigos."
                    # rasgamortalha "..."
                    rubens "Me solta! Tentativa de assassinato!! Tentativa de assassinato!!"
                    tata "Ei! Você do trator! Pare agora! Pare já!"
                    jump rubens_fedor

        "Sebo nas canelas!!":
            play sound "rasga_mortalha.ogg"
            tata "Uma coruja sinistra está lá dentro pilotando!"
            rasgamortalha "..."
            tata "Corre!!"
            rubens "Aaah!"
            narrator "Olho pra trás, Rubens tropeçou e caiu no chão enquanto corríamos."
            narrator "O trator acelerou! Está cada vez mais próximo!"
            rubens "Vá, Tatá... salve sua vida!!"

            menu:
                "Que drama...":
                    "Antes de atropelar Rubens, o trator estaciona. Alguém está descendo da cabine!"
                    show billgarca
                    billgarca "Boa tarde, senhores. Poderiam me esclarecer o motivo deste alvoroço?" 
                    rubens "O quê? Eu quase morri!"
                    tata "Rubens, você tem ASAS! Poderia só ter voado!"
                    rubens "Na hora da adrenalina é difícil de pensar, tá bom?!"
                    jump sancoes_juridicas

                "Eu não vou sem você!":
                    "Volto correndo para ajudar Rubens a se levantar."
                    tata "Ugh! Você é muito pesado!"
                    rubens "Acho que ganhei quilinhos nessas férias..."
                    tata "Vem logo!"
                    play sound "trator_motores.ogg"
                    "O trator está muito próximo! Vai nos esmagar!"
                    tata "Espera aí, você tem ASAS! Não sabe voar?!"
                    rubens "Foi mal! Eu tô nervoso!!"
                    "É o nosso fim..."
                    play sound "trator_motores.ogg"
                    jump rubens_fedor

label rubens_fedor:
    "O veículo desacelera até parar, bem na nossa frente."
    "Ufa! Essa foi por pouco!"
    tata "Nossa, que fedor é esse?"
    rubens "Foi mal..."
    tata "Shh! Tem alguém saindo lá de dentro!"
    jump motorista_fala

# label deixar_rubens:
label motorista_fala:
    billgarca "Boa tarde, senhores. Poderiam me esclarecer o motivo deste alvoroço?" 
    menu:
        "Eu estava esperando que você fizesse o mesmo!":
            tata "Eu estava esperando que você fizesse o mesmo!"
            jump vamos_por_partes
        "Boa tarde...":
            tata "Boa tarde..."
            jump sancoes_juridicas

label sancoes_juridicas:
    billgarca "Vocês não observaram as faixas de restrição? Permitam-me adverti-los de que essa violação perigosa em um local de obras é passível de sanção jurídica, com todas as consequências cabíveis."
    menu:
        "Desculpe, senhor...":
            tata "Não foi a nossa intenção cometer infração nenhuma, só viemos atrás de respostas."
            jump vamos_por_partes
        "Que absurdo!":
            jump vamos_por_partes

label vamos_por_partes:
    tata "Quem são vocês? E por que destruindo a floresta da Vila?"
    billgarca "Vamos por partes, senhores. Em primeiro lugar, não se trata de 'destruição', ok? Estamos simplesmente otimizando a área para fins de desenvolvimento sustentável. Temos todas as autorizações necessárias... bem, tecnicamente em fase de obtenção, mas consideramos o silêncio administrativo como um deferimento tácito nos termos da legislação.":
    jump conversa_motorista
