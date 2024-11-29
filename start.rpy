define tataguerreira = Character("tataguerreira")
define corujamago = Character("corujamago")
define seumirimcorado = Character("seumirimcorado")
define getulioalivio = Character("getulioalivio")
define getuliopalido = Character("getuliopalido")
define tatatriste = Character("tatatriste")
define seumirimrindo = Character("seumirimrindo")
define tatasono = Character("tatasono")
define tata = Character("tata")
define tatasusto = Character("tatasusto")
define corujasombra = Character("corujasombra")
define seumirim = Character("seumirim")
define tatadormindo = Character("tatadormindo")
define tatabola = Character("tatabola")
define sssocrates = Character("sssocrates")
define getulio = Character("getulio")
define getuliosusto = Character("getuliosusto")
define tatadesconfiada = Character("tatadesconfiada")


label tata_despertando:
    tatadormindo "Sniff sniff..." 
    tatadormindo "Que cheiro bom..."
    "Um delicioso cheiro de café entra pela porta do quarto. Lá fora os passarinhos já estão cantando."
    tatasono "ugh... já amanheceu?"
    "Cocoricóóó"
    tatasono "O Seu Garnizé bem que poderia cantar mais baixo..."
    "Cocoricóóf... cof! cof! cof!"
    tatasono "Parece que ele ainda não se recuperou daquela tosse tambem..."
    getulio "Tatá! Vem tomar café!"
    tatasono "Ah, não, o vovô ja está me chamando."
    tatasono "Eu disse que ia trabalhar com ele na colheita hoje... mas estou com tanto sono."
    getulio "Tatá?"
    tatadormindo "Talvez o vô me deixe dormir mais uma horinha. Eu estava em um sonho tão bom... se eu fechar os olhos agora, acho que consigo retornar pra ele..."
    <!--mudanca de background para sonho-->
    tataguerreira "Estou em uma missão, atravessando a floresta sombria. Com minha armadura redonda de casca eu me sinto invencível." 
    corujasombra "Ei! Você aí!"
    menu:
        "Quem, eu?":
            jump quem_eu
        "Quem ousa falar com Sir Tata Peba, Primeira de seu nome, Paladina das garras, Heroina dos labirintos subterraneos?":
            jump quem_ousa_falar_com_sir_tata_peba_primeira_de_seu_nome_paladina_das_garras_heroina_dos_labirintos_subterraneos

label quem_eu:
    corujamago "Está vendo mais alguém aqui, por acaso?!"
    <!--não se vê o rosto da coruja, uma tunica está cobrindo, apenas o bico com um sorriso sarcástico está a mostra-->
    menu:
        "Saudacoes, amigo mascarado. Que desventuras o conduziram ate esta trilha esquecida por Deus?":
            jump saudacoes_amigo_mascarado_que_desventuras_o_conduziram_ate_esta_trilha_esquecida_por_deus
        "Continue com suas  gracinhas e sentira o peso da minha lamina!":
            jump continue_com_suas__gracinhas_e_sentira_o_peso_da_minha_lamina

label quem_ousa_falar_com_sir_tata_peba_primeira_de_seu_nome_paladina_das_garras_heroina_dos_labirintos_subterraneos:
    <!--não se vê o rosto da coruja, uma tunica está cobrindo, apenas o bico com um sorriso sarcástico está a mostra-->
    corujamago "De que serve um título tão grande?
    corujamago "Teu fim será escrito no silêncio da noite, e nem saberás o nome de quem rasgou tua mortalha."
    "Ele começa a sussurrar palavras mágicas."
    jump preparo_minhas_garras_e_vou_em_direcao_a_ele

label saudacoes_amigo_mascarado_que_desventuras_o_conduziram_ate_esta_trilha_esquecida_por_deus:
    "- Eu serei... o seu fim!"
    Ele levanta os braços e começa a sussurrar palavras mágicas.
    jump preparo_minhas_garras_e_vou_em_direcao_a_ele

label preparo_minhas_garras_e_vou_em_direcao_a_ele:
    <!--Este texto aparece sobre a imagem desbloqueada-->
    "Toda a floresta começa a tremer, um som ensurdecedor. Com o terremoto, eu tropeço  e caio no chão, não consigo levantar!" 
    "Ha ha ha ha!!"
    "Acordar! Preciso acordar!"
    <!--Retornamos ao quarto de Tatá-->
    "Tudo está tremendo! Então aquela sensação foi real?"
    tatasusto "Ah! O que é isso?!"
    "Um barulho muito forte. Do teto da toca começam a cair areias e pedras."
    tatasusto "Socorro!"
    O que faço agora?!
    menu:
        "Virar uma bola":
            jump virar_uma_bola
        "Correr para o Vo Getulio":
            jump correr_para_o_vo_getulio

label continue_com_suas__gracinhas_e_sentira_o_peso_da_minha_lamina:
    corujamago "Então venha... se tiver coragem!"
    "Ele começa a sussurrar palavras mágicas."
    jump preparo_minhas_garras_e_vou_em_direcao_a_ele

label virar_uma_bola:
    tatabola "Me enrrolo e fico quietinha na posição que meus pais me ensinaram: a bola de proteção!"
    tatabola "Um ruído forte treme a terra por alguns momentos, até parece que a toca vai desabar!"
    menu:
        "Continuar na bola":
            jump continuar_na_bola
        "Correr para o Vo Getulio":
            jump correr_para_o_vo_getulio

label correr_para_o_vo_getulio:
    "As panelas e louças tremem fazendo barulho." 
    "O vô Getúlio está em pé na frente do armário segurando a porta para impedir uma pilha de copos de vidro de cair no chão."
    getuliosusto "Tatá! Se proteja! Faça a bola!"
    menu:
        "Ajudar ele a segurar os copos":
            jump ajudar_ele_a_segurar_os_copos
        "Fazer a bola":
            jump fazer_a_bola

label continuar_na_bola:
    "O ruído se distancia até sumir e tudo volta ao normal. Nossa toca segue firme. O vô Getúlio é um ótimo construtor."
    tatasusto "Ufa..."
    tatasusto "Será que o vô está bem?"
    jump ir_para_a_cozinha

label ir_para_a_cozinha:
    "O vô Getúlio está de pé perto do armário, com a mão machucada. Com o tremor vários copos caíram e se quebraram no chão, devem ter machucado ele. Uma bagunça."
    jump santo_tatu_bolinha_o_que_foi_isso

label ajudar_ele_a_segurar_os_copos:
    "Contrariando a ordem, corro para o seu lado. O armário ameaça cair, mas nossas forças combinadas o mantém no lugar."
    "O terremoto se distancia até sumir e tudo volta ao normal. Nossa toca segue firme."
    tatasusto "Ufa!"
    getuliosusto "Tatá! Por que não se protegeu? Você podia ter se machucado!"
    menu:
        "Desculpe, eu queria ajudar!":
            jump desculpe_eu_queria_ajudar
        "E o senhor? Por que nao se protegeu? Poderia ter se machucado tambem!":
            jump e_o_senhor_por_que_nao_se_protegeu_poderia_ter_se_machucado_tambem

label fazer_a_bola:
    "Obedeço o vô Getúlio e me enrolo. Os copos caem no chão em um grande barulho de vidro quebrando."
    "O terremoto se distancia até sumir e tudo volta ao normal. Nossa toca segue firme."
    tatasusto "Vô! Está tudo bem?"
    getuliopalido "Sim." 
    "Uma de suas mãos está machucada, deve ter sido atingida por um caco de vidro."
    tatatriste "Desculpe, vô... eu deveria ter te ajudado..."
    getulioalivio "Claro que não. O mais importante é a nossa segurança."
    jump santo_tatu_bolinha_o_que_foi_isso

label desculpe_eu_queria_ajudar:
    getulio "O mais importante é a sua segurança." 
    jump santo_tatu_bolinha_o_que_foi_isso

label e_o_senhor_por_que_nao_se_protegeu_poderia_ter_se_machucado_tambem:
    getulio "Esse tatu velho aqui sabe se virar, minha filha. O mais importante é a sua segurança!"
    jump santo_tatu_bolinha_o_que_foi_isso

label santo_tatu_bolinha_o_que_foi_isso:
    "O vô Getúlio não me responde. Está pálido, olhos arregalados, pensamento distante. Eu nunca vi ele assim, isso me assusta um pouco."
    tatasusto "Vô...?"
    "Ding Dong"
    getulio "Ah, deve ser o Mirim. Pode entrar!" <!--ha uma mudanca de atmosfera, a trilha sonora fica mais acolhedora-->
    "O Seu Mirim entra na sala trazendo um bolo nas maos."
    seumirim "Licenca... Rapaz, mas que sol que temos hoje, hein? E voces ouviram o Garnize cantando de manha? Ainda ta com aquela tosse, e nao se cuida, a mulher dele ja falou... Ue, que cara e essa voces dois? Viram fantasma?
    tata "O senhor nao sentiu isso?"
    seumirim "Isso o que?"
    tata "O terremoto..."
    seumirimrindo "Terremoto no Brasil? Hahaha" 
    tatadesconfiada "Entao so tremeu aqui porque estamos embaixo do chao..."
    seumirim "Nao senti nada de terremoto. So ouvi um barulho muito alto que foi em direcao a entrada da vila. Mas, barulho aqui e todo dia, aqueles vizinhos papagaios gritando sem parar, isso sim e barulho! Sem contar na cigarra, uma musica altissima logo no comeco do dia..."
    tata "Entao, o senhor nao viu nada de diferente?"
    seumirim "Ver eu nao vi. Isso foi antes de eu sair de casa."
    "Que estranho.. eu deveria ir ate la investigar!"
    getulio "Sentem-se. Vamos comer."
    menu:
        "Sentar-se na mesa do Cafe":
            jump sentarse_na_mesa_do_cafe
        "Sentar-se na mesa do Cafe":
            jump sentarse_na_mesa_do_cafe

label sentarse_na_mesa_do_cafe:
    <!--A mesa esta bonita como sempre, com frutas como pitomba, caju, garrafa de cafe e pratos de macaxeira frita. O bolo aparece no centro. Na frente do jogador ha 3 comidas clicaveis.-->
    "Vou comer rapido, assim posso sair logo!" 
    <!--Clicar em uma comida-->
    seumirimrindo "Eu trouxe o meu tradicional bolo formigueiro, desta vez feito com sauvas."
    menu:
        "Meu preferido!":
            jump meu_preferido
        "Ugh...":
            jump ugh

label meu_preferido:
    seumirim "O meu tambem! Para fazer um bolo dessa qualidade voce tem que pegar as formigas bem fresquinhas. Muita gente tenta fazer com as pretas, mas o gosto nunca fica igual. Uma vez na feira paguei uma nota alta, e acredita que fizeram o bolo com aquelas formigas amarelas, amargas? Canalhas...!"
    <!--Clicar em uma comida-->
    seumirim"E eu ja falei sobre o novo golpe que as raposas do Centro estao aplicando? esse mundo esta perdido mesmo..."
    "O Seu Mirim nao vai parar de conversar, desse jeito nao vou poder sair nunca..."
    "O que devo fazer para encurtar essa conversa?"
    menu:
        "Falar o minimo possivel":
            jump falar_o_minimo_possivel
        "Tocar em um assunto constrangedor":
            jump tocar_em_um_assunto_constrangedor

label ugh:
    seumirim "Que cara e essa minha filha? Esses jovens nao sabem mais apreciar a culinaria de nossa terra, uma comida tradicional, artesanal, saborosissima. Pensa que esse bolo ai e feito daquelas formigas amarelinhas que voce encontra em qualquer lugar? Nao, nao! Essas sao sauvas legitimas! Sabe como e dificil encontrar dessa linhagem? Elas mal grudam na lingua...!"
    <!--Clicar em uma comida-->
    seumirim"E eu ja falei sobre o novo golpe que as raposas do Centro estao aplicando? esse mundo esta perdido mesmo..."
    "O Seu Mirim nao vai parar de conversar, desse jeito nao vou poder sair nunca..."
    "O que devo fazer para encurtar essa conversa?"
    menu:
        "Falar o minimo possivel":
            jump falar_o_minimo_possivel
        "Tocar em um assunto constrangedor":
            jump tocar_em_um_assunto_constrangedor

label falar_o_minimo_possivel:
    tata"hm"
    seumirim""Hm" o que, minha filha? O gato comeu a sua lingua?"
    menu:
        "Aham...":
            jump aham
        "An an...":
            jump an_an

label tocar_em_um_assunto_constrangedor:
    tata"Seu Mirim, a Dona Cuica perguntou do senhor ontem..."
    seumirim"Q-que?"
    tata"Ela perguntou por que o senhor nao aparece mais la pra dancar seresta com ela..."
    seumirimcorado"Ora..."
    tata"Ela disse que o senhor e um dos melhores dancarinos da vila"
    seumirimcorado"Um dos melhores? Entao ha outros?"
    menu:
        "Eu ja vi ela dancando com o Senhor Socrates ":
            jump eu_ja_vi_ela_dancando_com_o_senhor_socrates_
        "Como o senhor eu aposto que nao":
            jump como_o_senhor_eu_aposto_que_nao

label aham:
    seumirim "Que?! que idioma e esse? Esses jovens..."
    getulio"Tata, modos!"
    <!--Clicar na ultima comida-->
    tata "nham nham desculpe e que estava de boca cheia..."
    seumirim"Tambem, comendo com pressa igual um animal selvagem! Ja nao dao importancia as boas maneiras! Se eu tivesse filhos, mandaria pra escola de etiqueta da Cibele Cisne..."
    tata "Desculpem... e com licenca, ja vou indo..."
    seumirim "Mas, ja?"
    getulio "Tata, nao esqueca de me encontrar na plantacao mais tarde!"
    tata"Tudo bem, Tchau vovo! Tchau, Seu Mirim!"
    menu:
        "Ir para a Entrada da Vila":
            jump ir_para_a_entrada_da_vila
        "Ir para a Entrada da Vila":
            jump ir_para_a_entrada_da_vila

label an_an:
    seumirim "Que?! que idioma e esse? Esses jovens..."
    getulio"Tata, modos!"
    <!--Clicar na ultima comida-->
    tata "nham nham desculpe e que estava de boca cheia..."
    seumirim"Tambem, comendo com pressa igual um animal selvagem! Ja nao dao importancia as boas maneiras! Se eu tivesse filhos, mandaria pra escola de etiqueta da Cibele Cisne..."
    tata "Desculpem... e com licenca, ja vou indo..."
    seumirim "Mas, ja?"
    getulio "Tata, nao esqueca de me encontrar na plantacao mais tarde!"
    tata"Tudo bem, Tchau vovo! Tchau, Seu Mirim!"
    menu:
        "Ir para a Entrada da Vila":
            jump ir_para_a_entrada_da_vila
        "Ir para a Entrada da Vila":
            jump ir_para_a_entrada_da_vila

label como_o_senhor_eu_aposto_que_nao:
    seumirimcorado "Ora, nao e pra tanto!"
    getulio"Hahaha!"
    <!--Clicar na ultima comida-->
    tata "Desculpem... e com licenca, ja vou indo..."
    seumirim "Mas, ja?"
    getulio "Tata, nao esqueca de me encontrar na plantacao mais tarde!"
    tata"Tudo bem, Tchau vovo! Tchau, Seu Mirim!"
    menu:
        "Ir para a Entrada da Vila":
            jump ir_para_a_entrada_da_vila
        "Ir para a Entrada da Vila":
            jump ir_para_a_entrada_da_vila

label eu_ja_vi_ela_dancando_com_o_senhor_socrates_:
    seumirim "Mas, que absurdo! Melhor do que eu? Ele nem tem pernas!"
    tata "Ele desliza como ninguem"
    seumirim "Aquele venenoso!" 
    <!--Clicar na ultima comida-->
    tata "Desculpem... e com licenca, ja vou indo..."
    seumirim "Mas, ja?"
    getulio "Tata, nao esqueca de me encontrar na plantacao mais tarde!"
    tata"Tudo bem, Tchau vovo! Tchau, Seu Mirim!"
    menu:
        "Ir para a Entrada da Vila":
            jump ir_para_a_entrada_da_vila
        "Ir para a Entrada da Vila":
            jump ir_para_a_entrada_da_vila

label passagem_sem_titulo:
    <!--bg: uma rua com diferentes casinhas simples, umas no chao, outras nas arvores, essa e a vila macaxeira. Uma cobra verde esta lendo um livro-->
        sssocrates "Ssser ou nao ssser... eiss a quesstao!"
        tata"Bom dia, Seu Socrates."
        sssocrates "Bom dia, sssenhorita. A pronuncia e "Sssocrates"
        tata "Desculpe Seu...
        menu:
        "Sssocrates":
            jump sssocrates
        "Ssssocrates":
            jump ssssocrates

label sssocrates:
    sssocrates "Excsselente, Tata. Estass cada vez melhor."
        tata "Agradecsssida!"
        <!--Seria Uma preguica bem velhinha, Dona Cica esta deitada em uma cadeira de balanco dormindo-->
        tata “Bom dia, dona Clarica!”
        clarica “zzzzz….”
        menu:
        "melhor deixa-la dormir…":
            jump melhor_deixala_dormir
        "BOM DIA, DONA CLARICA":
            jump bom_dia_dona_clarica

label ssssocrates:
    sssocrates "Nao! E Sssocrates! Com "sss"!"
        tata "Desssculpa!"
        <!--Seria Uma preguica bem velhinha, Dona Cica esta deitada em uma cadeira de balanco dormindo-->
        tata “Bom dia, dona Cica!”
        cica “zzzzz….”
        menu:
        "melhor deixa-la dormir…":
            jump melhor_deixala_dormir
        "BOM DIA, DONA CLARICA":
            jump bom_dia_dona_clarica

label bom_dia_dona_clarica:
    ohh… bommm diaa, Tataa… acabei cochilando de novoo…
        Ja amanheceu! E dia de feira!
        E verdade… hoje eu vou… uahhh… eu vou…
        hm… zzzz….
        Hehe, nao tem jeito.
        <!--`Uma cuica com varios filhotes nas costas, Enzo, Lorenzo e Valentina um esta chorando`-->
        lorenzo“Buaaa! Maaae!!!”
        valentina“Maaae! O Enzo puxou a cauda do Lorenzo!”
        enzo“Shhh! Sua cagueta!”
        valentina“Maae! Olha do que ele me chamou!”
        carlacuica “Eu ja falei pra parar, menino!” 
        enzo“Mae, mas ele fica me empurrando!”
        lorenzo “Buaaa!!”
        menu:
        "Bom dia, Dona Cuica. Bom dia, criancas.":
            jump �bom_dia_dona_cuica_bom_dia_criancas
        "(Observar a confusao)":
            jump observar_a_confusao

label melhor_deixala_dormir:
    Me pergunto se ela tem sonhos malucos igual a mim...
        Talvez ela sonha tudo em camera lenta.
        <!--`Uma cuica com varios filhotes nas costas, Enzo, Lorenzo e Valentina um esta chorando`-->
        lorenzo“Buaaa! Maaae!!!”
        valentina“Maaae! O Enzo puxou a cauda do Lorenzo!”
        enzo“Shhh! Sua cagueta!”
        valentina“Maae! Olha do que ele me chamou!”
        carlacuica “Eu ja falei pra parar, menino!” 
        enzo“Mae, mas ele fica me empurrando!”
        lorenzo “Buaaa!!”
        menu:
        "Bom dia, Dona Cuica. Bom dia, criancas.":
            jump �bom_dia_dona_cuica_bom_dia_criancas
        "(Observar a confusao)":
            jump observar_a_confusao

label bom_dia_dona_cuica_bom_dia_criancas:
    cuica “Bom dia, Tata! Aproveitando as ferias?”
        menu:
        "Claro!":
            jump claro
        "Entediada...":
            jump entediada

label observar_a_confusao:
    arlacuica “ Eu vou contar ate 3…”
        enzo “Viu? Fecha a matraca, Valentina!”
        valentina “Fecha a matraca ja morreu, quem manda na minha matraca sou eu!”
        carlacuica “1...”
        enzo “Cara de rato!”
        valentina “Cara de rato e quem me chama!”
        enzo “Cavalo manco e que te ama!”
        carlacuica “2...”
        enzo “eu durmo na cama, tu dorme na lama”
        valentina“A cama quebra, velho do saco de leva!”
        lorenzo “Buaaa!”
        carlacuica “Chega! Vou pegar minha chinela e voces vao ver so!!”
        lorenzo, enzo e valentina “Aaaaaaaa”
        <os filhotes desaparecem de suas costas>
        tata “Bom dia, Dona Cuica”
        carlacuica “Bom dia, Tata. Falta quanto mesmo pra as ferias acabarem?”
        tata “Umas duas semanas.”
        carlacuica “Duas longas semanas...”
        menu:
        "Ir para a Entrada da Vila":
            jump ir_para_a_entrada_da_vila
        "Ir para a Entrada da Vila":
            jump ir_para_a_entrada_da_vila

