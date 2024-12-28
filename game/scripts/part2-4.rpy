label start2:
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
    return