# label start:
label seguir_pneus:
    scene bg_floresta_obras with fade
    show tata at center
    show rubens at left

    tata "Estão indo na direção da floresta… que estranho!"
    rubens "Pode crer, não tem nem estrada pra essas bandas."

    # Som de trator e motores
    # play sound "trator_motores.ogg"

    tata "Está cercado por fitas de restrição."
    rubens "Isso não me cheira bem, vamos embora, Tatá."
    tata "Ah, não! Agora vamos até o fim."

    # scene bg_trator_destruindo with fade

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
                    # play sound "rasga_mortalha.ogg"

                    show rasgamortalha at right
                    rasgamortalha "..."
                    tata "Uma coruja sinistra está lá dentro pilotando!"
                    hide rasgamortalha

                    "Essa não! Ele continua avançando!"
                    "Mas, a guerreira Tatá não deve ter medo!"

                    menu:
                        "Pare agora!":
                            pass
                        "Passa por cima!!":
                            pass
                    "O trator desacelera até parar, bem na minha frente." 
                    tata "Ufa! Essa foi por pouco!"
                    rubens "Tatá! Estou voltando! Você sobreviveu?!"
                    tata "Não graças a você!"
                    "Alguém sai de dentro do trator"
                    #todo show in
                    jump motorista_fala
                    # billgarca "Boa tarde, senhores. Poderiam me esclarecer o motivo deste alvoroço?" 

                "Agarrar Rubens":
                    tata "Calma aí!! Eles não vão ter coragem de passar por cima da gente!"
                    # Som da rasga mortalha
                    # play sound "rasga_mortalha.ogg"

                    "Dentro do trator há uma coruja com cara de poucos amigos."
                    # rasgamortalha "..."
                    rubens "Me solta! Tentativa de assassinato!! Tentativa de assassinato!!"
                    tata "Ei! Você do trator! Pare agora! Pare já!"
                    jump rubens_fedor

        "Sebo nas canelas!!":
            # play sound "rasga_mortalha.ogg"
            tata "Uma coruja sinistra está lá dentro pilotando!"
            rasgamortalha "..."
            tata "Corre!!"
            rubens "Aaah!"
            "Olho pra trás, Rubens tropeçou e caiu no chão enquanto corríamos."
            "O trator acelerou! Está cada vez mais próximo!"
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
                    # play sound "trator_motores.ogg"
                    "O trator está muito próximo! Vai nos esmagar!"
                    tata "Espera aí, você tem ASAS! Não sabe voar?!"
                    rubens "Foi mal! Eu tô nervoso!!"
                    "É o nosso fim..."
                    # play sound "trator_motores.ogg"
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
    hide rasgamortalha
    show billgarca at right
    billgarca "Boa tarde, senhores. Poderiam me esclarecer o motivo deste alvoroço?" 
    menu:
        "Eu estava esperando que você fizesse o mesmo!":
            tata "Eu estava esperando que você fizesse o mesmo!"
            jump vamos_por_partes
        "Boa tarde...":
            tata "Boa tarde..."
            jump sancoes_juridicas

label sancoes_juridicas:
    billgarca "Vocês não observaram as faixas de restrição?"
    billgarca "Permitam-me adverti-los de que essa violação perigosa em um local de obras é passível de sanção jurídica, com todas as consequências cabíveis."
    menu:
        "Desculpe, senhor...":
            tata "Não foi a nossa intenção cometer infração nenhuma, só viemos atrás de respostas."
            jump vamos_por_partes
        "Que absurdo!":
            jump vamos_por_partes

label vamos_por_partes:
    tata "Quem são vocês? E por que destruindo a floresta da Vila?"
    billgarca "Vamos por partes, senhores. Em primeiro lugar, não se trata de 'destruição', ok?"
    billgarca "Estamos simplesmente otimizando a área para fins de desenvolvimento sustentável. Temos todas as autorizações necessárias..."
    billgarca "Bem, tecnicamente em fase de obtenção, mas consideramos o silêncio administrativo como um deferimento tácito nos termos da legislação."
    menu:
        "Pare de enrolacao!":
            pass
        "Senhor, não estou entendendo...":
            pass
    tata "Quem são vocês? Que obra é essa?"
    tata "Permitam-me apresentar: sou Bill Garça, advogado e representante legal do conglomerado White Wing Enterprises e da empresa associada Asa Branca S.A.; e os senhores?"
    menu:
        "Não é da sua conta!":
            tata "É você que está na nossa Vila, não lhe devemos explicações!"
            billgarca "Quanta hostilidade! Devo lembrá-la de que dispomos dos meios legais para respaldar nossas ações e, se necessário, tomar as devidas medidas judiciais contra você."
            tata "Chega! Vou chamar todo mundo da Vila!"
            billgarca "Espere, senhorita, você chegou em boa hora, (apesar de sua evidente falta de decoro...), pois justo eu me dirigia para a Vila… como era o nome? Mandioca?"
            jump documento
        "Sou Tata e esse é meu amigo Rubens. Somos moradores locais.":
            billgarca "Ora, que maravilha! Pois justo eu me dirigia para a Vila… como era o nome? Mandioca?"
            jump documento

label documento:
    rubens "Vila Macaxeira."
    billgarca "Exatamente. Me dirigia para entregar este documento que trata de uma importante questão. Me faça o favor de levar até lá e consideramos a entrega formalmente registrada."
    "Ele me passa um envelope com uma folha de papel."
    tata "Decreto de Desapropriação por Interesse Social? O que significa isso?!"
    billgarca "Para vocês, nativos, são excelentes novidades!"
    menu:
        "Eu preciso mesmo ouvir uma boa notícia...":
            pass
        "Isso não cheira bem...":
            tata "Nem estou me referindo ao Rubens."
            pass
    billgarca "Temos o prazer de anunciar a construção de uma magnífica pista de pouso para helicópteros e jatinhos particulares. Este projeto trará movimentação à região, oportunidades de empregos, um progresso sem precedentes à esta área tão subdesenvolvida!"
    rubens "Uma pista de pouso? Mas, tão perto da comunidade?"
    billgarca "Ora, entenda. Para uma boa pista precisamos de espaço, estradas… quilômetros que teremos que limpar dessa mata… Isso irá incluir o território do assentamento da Vila Mangabeira."
    tata "O quê?!"
    rubens "É 'Vila Macaxeira'."
    billgarca "Sem contar que não será possível viver tão próximo à pista, imagine o ruído, o risco de voar… Mas, não se preocupem. Nos propomos a comprar as casas, assim vocês terão uma oportunidade adquirir outra propriedade em outro local."
    rubens "Aí... não sei não..."
    menu:
        "Eles não vão aceitar.":
            tata "Os moradores vivem aqui há gerações!"
            pass
        "De quanto dinheiro estamos falando?":
            billgarca "Dinheiro suficiente. Está muito bem detalhado na documentação!"
            rubens "Acho que minha família não vai curtir... vivemos aqui há muitas gerações..."
            pass
    billgarca "Com todo respeito, mas não vejo muita opção para vocês.. o progresso é inevitável!"
    billgarca "Agora, se me dão licença, nós iremos retornar para a cidade. Na próxima semana estremos de volta para completar a obra e esperamos uma resposta da parte de vocês sobre a venda dos terrenos."
    menu:
        "Vai sonhando!":
            pass
        "É a Vila que vai decidir...":
            pass
    billgarca "É o que veremos! Até breve amigos!"
    # rasgamortalha "..."
    "Eles sobem no trator e vão se distanciam, deixando na floresta um rastro de destruição."
    rubens "Que roubada..."
    tata "Vamos, precisamos avisar o pessoal da Vila!"
    jump avisando_vovo
