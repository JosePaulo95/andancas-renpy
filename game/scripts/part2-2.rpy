label sai_dona_cuica:
    hide cica with moveoutleft
    pause 1
    show rubens at center with moveinright
    jump encontra_rubens

label encontra_rubens:
    tata "O Seu Mirim disse que viu uma movimentação por aqui, deve haver alguma pista."
    rubens "Bom dia, flor do dia."
    tata "E aí, Rubens!"
    rubens "Suave na nave?"
    
    menu:
        "De boa na lagoa.":
            rubens "Hehehe! Pode crer!"
            jump menu_preocupada

        "Não tanto quanto eu gostaria.":
            rubens "Opa, que vibe é essa? O que tá pegando?"
            tata "Senti um terremoto na toca de manhã. Tenho um mau pressentimento."
            rubens "Tá precisando de um banho de sal"
            jump menu_preocupada

# label quer_praia:
#     rubens "Tô indo pegar umas ondas lá na praia, quer colar junto?"
#     menu:
#         "Sim, vamos lá.":
#             tata "Show! Vai ser massa!"
#             return
#         "Não, tenho que fazer outra coisa.":
#             tata "Hoje não vai dar."
#             jump outros_planos

label menu_preocupada:
    rubens "Tô indo pegar umas ondas lá na praia, quer colar junto?"
    menu:
        "Tenho que ajudar meu avô na plantação.":
            tata "Você está ocupado à tarde? Podia vir ajudar a gente com a colheita também."
            rubens "Tá me chamando pra trabalhar? Nas férias? Que mal que eu te fiz?"
            tata "Verdade, esqueci que você era alérgico..."
            rubens "Ei, é uma condição médica! Intolerância a trabalho, o meu corpo rejeita, juro."
            tata "Claro… Mas, não é pra isso que eu estou aqui. Eu vim pra..."
            jump ver_pena
        "Tenho que fazer uma investigação.":
            tata "Elementar, meu caro Watson... Estou procurando pistas..."
            jump ver_pena

label ver_pena:
    tata "Ah! Olha!"
    tata "Essas marcas no chão…algo grande passou por aqui"
    rubens "Carácoles, nunca vi uma centopeia desse tamanho"
    menu:
        "Não é uma centopeia, é um veículo!":
            tata "Um trator ou um caminhão."
            rubens "Um trator passando pela vila? Isso mesmo que eu não vi."
            rubens "Aqui é onde Judas perdeu as meias, porque as botas foi bem antes."
            tata "Tem mais algo ali no chão."
            "Uma pena no chão"
            tata "De quem será essa pena? Será do seu irmãozinho?"
            rubens "Nam, ele é cinza. Já até começou a ficar vermelho."
            tata "Já? O tempo voa!"
            rubens "Ele entrou numa dieta de caranguejo e se envermelhou rapidinho."
            tata "Então vamos ter que descobrir de quem é. Vem comigo!"
            rubens "Pra praia?"
            tata "Não! Seguir esses rastros!"
            rubens "Poxa..."
            jump seguir_pneus
            
        "Suspirar e revirar os olhos.":
            tata "Claro, e o que será que uma centopeia do tamanho de uma baleia azul veio fazer na nossa vila?"
            rubens "Comprar macaxeira?"
            tata "Tem mais algo ali no chão."
            tata "Sabe, acho que precisamos investigar mais."
            jump seguir_pneus
            
