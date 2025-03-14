# label start2:
label start:
    # Mostra fundo preto inicialmente
    # $ renpy.music.set_volume(1.0, delay=0, channel='music')
    scene black with dissolve
    
    tata "Sniff sniff..." 
    tata "Que cheiro bom..."
    
    # O café é sentido enquanto a tela ainda está preta
    "Um delicioso cheiro de café entra pela porta do quarto. Lá fora os passarinhos já estão cantando."
    play music "audio/Devonshire Waltz Moderato.mp3" loop
    # Revela gradualmente o quarto
    scene bg_quarto_com_tata with dissolve
    
    tata "ugh... já amanheceu?"
    
    # Sons de galos cantando
    "Cocoricóóó"
    tata "O Seu Garnizé bem que poderia cantar mais baixo..."
    "Cocoricóóf... cof! cof! cof!"
    tata "Parece que ele ainda não se recuperou daquela tosse também..."
    getulio "Tatá! Vem tomar café!"
    tata "Ah, não, o vovô já está me chamando."
    tata "Eu disse que ia trabalhar com ele na colheita hoje... mas estou com tanto sono."
    # Volta ao fundo preto
    scene black with dissolve
    getulio "Tatá?"
    stop music fadeout 2.0
    tata "Talvez o vô me deixe dormir mais uma horinha. Eu estava em um sonho tão bom... se eu fechar os olhos agora, acho que consigo retornar pra ele..."
    play sound "audio/The Complex.mp3" fadein 2.0 loop
    tata "Estou em uma missão, atravessando a floresta sombria. Com minha armadura redonda de casca eu me sinto invencível."
    scene bg_floresta with dissolve
    show coruja_sonho at right
    coruja_sonho "Ei! Você aí!"
    menu:
        "Quem, eu?":
            show tata
            tata "Quem, eu?"
            jump sonho_resposta_humilde
        "Quem ousa falar com Sir Tata Peba, Primeira de seu nome, Paladina das garras, Heroína dos labirintos subterrâneos?":
            show tata
            tata "Quem ousa falar com Sir Tata Peba, Primeira de seu nome, Paladina das garras, Heroína dos labirintos subterrâneos?"
            jump sonho_resposta_ostentosa

label sonho_resposta_humilde:
    coruja_sonho "Está vendo mais alguém aqui, por acaso?!"
    # Não se vê o rosto da coruja_sonho; uma túnica está cobrindo, apenas o bico com um sorriso sarcástico está à mostra.
    menu:
        "Saudações, amigo mascarado. Que desventuras o conduziram até esta trilha esquecida por Deus?":
            tata "Saudações, amigo mascarado. Que desventuras o conduziram até esta trilha esquecida por Deus?"
            jump saudacoes_amigo
        "Continue com suas gracinhas e sentirá o peso da minha lâmina!":
            tata "Continue com suas gracinhas e sentirá o peso da minha lâmina!"
            jump ameaca

label sonho_resposta_ostentosa:
    # Não se vê o rosto da coruja_sonho; uma túnica está cobrindo, apenas o bico com um sorriso sarcástico está à mostra.
    coruja_sonho "De que serve um título tão grande?"
    coruja_sonho "Teu fim será escrito no silêncio da noite, e nem saberás o nome de quem rasgou tua mortalha."
    "Ele começa a sussurrar palavras mágicas."
    jump preparo_garras

label saudacoes_amigo:
    coruja_sonho "- Eu serei... o seu fim!"
    "Ele levanta os braços e começa a sussurrar palavras mágicas."
    jump preparo_garras

label ameaca:
    coruja_sonho "Então venha... se tiver coragem!"
    "Ele começa a sussurrar palavras mágicas."
    jump preparo_garras

label preparo_garras:
    "Toda a floresta começa a tremer, um som ensurdecedor." with hpunch
    "Com o terremoto, eu tropeço e caio no chão, não consigo levantar!"
    hide coruja_sonho
    scene black with dissolve
    stop music fadeout 2.0
    window show
    "Ha ha ha ha!!" with fade
    "Acordar! Preciso acordar!"
    # Retornamos ao quarto de Tatá.
    show bg_quarto_sem_tata with hpunch
    # with h_punch
    show tata
    play sound "audio/Failing Defense.mp3" fadein 1.0
    tata "Tudo está tremendo! Então aquela sensação foi real?"
    tata "Ah! O que é isso?!"
    "Um barulho muito forte. Do teto da toca começam a cair areias e pedras."
    tata "Socorro!"
    tata "O que faço agora?!"
    menu:
        "Virar uma bola":
            jump quarto_virar_bola
        "Correr para o Vô Getúlio":
            jump quarto_correr_vo_getulio

label quarto_virar_bola:
    "Me enrolo e fico quietinha na posição que meus pais me ensinaram: a bola de proteção!"
    "Um ruído forte treme a terra por alguns momentos, até parece que a toca vai desabar!"
    menu:
        "Continuar na bola":
            jump quarto_continuar_bola
        "Correr para o Vô Getúlio":
            jump quarto_correr_vo_getulio

label quarto_correr_vo_getulio:
    scene bg_cozinha_clean
    show getulio at center
    "As panelas e louças tremem fazendo barulho." 
    "O vô Getúlio está em pé na frente do armário segurando a porta para impedir uma pilha de copos de vidro de cair no chão."
    show tata at left:
        xpos 0.1
    getulio "Tatá! Se proteja! Faça a bola!"
    menu:
        "Ajudar ele a segurar os copos":
            jump ajudar_segurar_copos
        "Fazer a bola":
            jump nao_ajudar_fazer_a_bola

label quarto_continuar_bola:
    "O ruído se distancia até sumir e tudo volta ao normal."
    "Nossa toca segue firme. O vô Getúlio é um ótimo construtor."
    tata "Ufa..."
    tata "Será que o vô está bem?"
    jump ir_para_a_cozinha

label ir_para_a_cozinha:
    scene bg_cozinha_clean
    show getulio at center
    show tata at left with moveinleft:
        xpos 0.1
    "O vô Getúlio está de pé perto do armário, com a mão machucada. Com o tremor vários copos caíram e se quebraram no chão, devem ter machucado ele. Uma bagunça."
    jump meu_deus_o_que_foi_isso

label ajudar_segurar_copos:
    "Contrariando a ordem, corro para o seu lado. O armário ameaça cair, mas nossas forças combinadas o mantém no lugar."
    "O terremoto se distancia até sumir e tudo volta ao normal. Nossa toca segue firme."
    tata "Ufa!"
    getulio "Tatá! Por que não se protegeu? Você podia ter se machucado!"
    menu:
        "Desculpe, eu queria ajudar!":
            tata "Desculpe, eu queria ajudar!"
            jump responde_vovo_desculpe
        "E o senhor? Por que nao se protegeu? Poderia ter se machucado também!":
            tata "E o senhor? Por que nao se protegeu? Poderia ter se machucado também!"
            jump responde_vovo_saliente

label nao_ajudar_fazer_a_bola:
    "Obedeço o vô Getúlio e me enrolo. Os copos caem no chão em um grande barulho de vidro quebrando."
    "O terremoto se distancia até sumir e tudo volta ao normal. Nossa toca segue firme."
    tata "Vô! Está tudo bem?"
    getulio "Sim." 
    "Uma de suas mãos está machucada, deve ter sido atingida por um caco de vidro."
    tata "Desculpe, vô... eu deveria ter te ajudado..."
    getulio "Claro que não. O mais importante é a nossa segurança."
    jump meu_deus_o_que_foi_isso

label responde_vovo_desculpe:
    getulio "O mais importante é a sua segurança." 
    jump meu_deus_o_que_foi_isso

label responde_vovo_saliente:
    getulio "Esse tatu velho aqui sabe se virar, minha filha. O mais importante é a sua segurança!"
    jump meu_deus_o_que_foi_isso

label meu_deus_o_que_foi_isso:
    tata "Santo Tatu Bolinha! O que foi isso?"
    "O vô Getúlio não me responde. Está pálido, olhos arregalados, pensamento distante. Eu nunca vi ele assim, isso me assusta um pouco."
    tata "Vô...?"
    "Ding Dong"
    getulio "Ah, deve ser o Mirim. Pode entrar!"
    play sound "audio/Devonshire Waltz Moderato.mp3"
     # sound há uma mudança de atmosfera, a trilha sonora fica mais acolhedora
    "O Seu Mirim entra na sala trazendo um bolo nas mãos."
    show seumirim at right with moveinright
    seumirim "Licença... Rapaz, mas que sol que temos hoje, hein?"
    seumirim "E vocês ouviram o Garnizé cantando de manhã? Ainda tá com aquela tosse, e não se cuida, a mulher dele já falou..."
    seumirim "Ué, que cara é essa, vocês dois? Viram fantasma?"
    tata "O senhor não sentiu isso?"
    seumirim "Isso o quê?"
    tata "O terremoto..."
    seumirim "Terremoto no Brasil? Hahaha" 
    tata "Então só tremeu aqui porque estamos embaixo do chão..."
    seumirim "Não senti nada de terremoto."
    seumirim "Só ouvi um barulho muito alto que foi em direção à entrada da vila."
    seumirim "Mas, barulho aqui é todo dia, aqueles vizinhos papagaios gritando sem parar, isso sim é barulho, cinco filhos eles têm! Sem contar na cigarra, uma música altíssima logo no começo do dia..."
    tata "Então, o senhor não viu nada de diferente?"
    seumirim "Ver eu não vi. Isso foi antes de eu sair de casa."
    tata "Que estranho..."
    # sound de aventura
    tata "Eu deveria ir até lá investigar!"
    getulio "Sentem-se. Vamos comer."
    "Vou comer rápido, assim posso sair logo!"
    jump sentarse_na_mesa_do_cafe

label sentarse_na_mesa_do_cafe:
    # A mesa está bonita como sempre, com frutas como pitomba, caju, garrafa de café e pratos de macaxeira frita. O bolo aparece no centro.
    seumirim "Eu trouxe o meu tradicional bolo formigueiro, desta vez feito com saúvas."
    menu:
        "Meu preferido!":
            jump meu_preferido
        "Ugh...":
            jump ugh

label meu_preferido:
    seumirim "O meu também! Para fazer um bolo dessa qualidade você tem que pegar as formigas bem fresquinhas."
    seumirim "Muita gente tenta fazer com as pretas, mas o gosto nunca fica igual."
    seumirim "Uma vez na feira paguei uma nota alta, e acredita que fizeram o bolo com aquelas formigas amarelas, super amargas? Canalhas...!"
    jump annoyed

label ugh:
    seumirim "Que cara é essa, minha filha?"
    seumirim "Esses jovens não sabem mais apreciar a culinária de nossa terra, uma comida tradicional, artesanal, saborosíssima."
    seumirim "Pensa que esse bolo aí é feito daquelas formigas amarelinhas que você encontra em qualquer lugar? Não, não! Essas são saúvas legítimas! Sabe como é difícil encontrar dessa linhagem? Elas mal grudam na língua...!"
    jump annoyed

label annoyed:
    "O Seu Mirim nao vai parar de conversar, desse jeito nao vou poder sair nunca..."
    "O que devo fazer para encurtar essa conversa?"
    menu:
        "Falar o minimo possivel":
            jump falar_o_minimo_possivel
        "Tocar em um assunto constrangedor":
            jump tocar_em_um_assunto_constrangedor

label falar_o_minimo_possivel:
    tata "hm"
    seumirim "Hm o que, minha filha? O gato comeu a sua lingua?"
    menu:
        "Aham...":
            jump aham
        "An an...":
            jump an_an

label tocar_em_um_assunto_constrangedor:
    tata "Seu Mirim, a Dona Cuíca perguntou do senhor ontem..." #emotion
    seumirim "Q-quê?"
    tata "Ela perguntou por que o senhor não aparece mais lá pra dançar seresta com ela..."
    seumirim "Ora..." #emotion corado
    tata "Ela disse que o senhor é um dos melhores dançarinos da vila."
    seumirim "Um dos melhores? Então há outros?"
    menu:
        "Eu ja vi ela dancando com o Senhor Sócrates ":
            jump eu_ja_vi_ela_dancando_com_o_senhor_socrates
        "Como o senhor eu aposto que nao":
            jump como_o_senhor_eu_aposto_que_nao

label aham:
    seumirim "Quê?! Que idioma é esse? Esses jovens..."
    getulio "Tatá, modos!"
    jump tata_pede_desculpa_mirim

label an_an:
    seumirim "Quê?! Que idioma é esse? Esses jovens..."
    getulio "Tatá, modos!"

label tata_pede_desculpa_mirim:
    tata "nham nham, desculpe, é que estava de boca cheia..."
    seumirim "Também, comendo com pressa igual um animal selvagem! Já não dão importância às boas maneiras!"
    seumirim "Se eu tivesse filhos, mandaria pra escola de etiqueta da Cibele Cisne..."
    jump scape_mirim

label como_o_senhor_eu_aposto_que_nao:
    seumirim "Ora, não é pra tanto!"
    getulio "Hahaha!"
    jump scape_mirim

label eu_ja_vi_ela_dancando_com_o_senhor_socrates:
    seumirim "Mas, que absurdo! Melhor do que eu? Ele nem tem pernas!"
    tata "Ele desliza como ninguém"
    seumirim "Aquele venenoso!" 
    # <!--Clicar na última comida-->
    jump scape_mirim

label scape_mirim:
    tata "Desculpem... e com licença, já vou indo..."
    seumirim "Mas, já?"
    getulio "Tatá, não esqueça de me encontrar na plantação mais tarde!"
    tata "Tudo bem, Tchau vovô! Tchau, Seu Mirim!"
    menu:
        "Ir para a Entrada da Vila":
            jump sair_de_casa
        "Ir para a Entrada da Vila":
            jump sair_de_casa
