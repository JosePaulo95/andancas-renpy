define tata = Character("Tatá", color="#E91940")
define coruja = Character("Coruja", color="#2B6B9C", window_xalign=1.0, window_right_padding=50)
define getulio = Character("Getúlio", color="#E7B58A")
define seumirim = Character("Seu Mirim", color="#E59EAD")
define sssocrates = Character("Sssocrates", color="#BDA0CB")   # Lilás claro, para um tom misterioso e excêntrico
define cica = Character("Dona Clariça", color="#CC7A5B")       # Marrom claro, para um personagem sábio e com experiência
define cuica = Character("Carla", color="#DBA159")             # Âmbar, simbolizando energia e calma materna
define lorenzo = Character("Lorenzo", color="#FF7F7F")         # Rosa vibrante, para dar destaque ao personagem emotivo
define valentina = Character("Valentina", color="#6EB5FF")     # Azul claro, representando tranquilidade com um toque de rebeldia
define enzo = Character("Enzo", color="#7BC97B")               # Verde, indicando traquinagem e curiosidade infantil
define lorenzo_enzo_valentina = Character("Lorenzo, Enzo e Valentina", color="#FFAE42")  # Laranja, um tom que combina o caos dos três juntos
define rubens = Character("Rubens", color="#FF7F7F")
define rasgamortalha = Character("Rasga Mortalha", color="#F5F5F5")
define billgarca = Character("Bill Garça", color="#F5F5F5")

# Definindo imagens
image bg_cozinha = im.FactorScale("cozinha.jpg", 1.5)  # Aqui você coloca o arquivo da imagem do quarto
image bg_quarto = im.FactorScale("quarto.jpg", 3.3)  # Aqui você coloca o arquivo da imagem do quarto
image bg_floresta = im.FactorScale("floresta-sombria.jpg", 1.5)  # Aqui você coloca o arquivo da imagem do quarto
image bg_floresta_obras = im.FactorScale("bg_floresta_obras.jpg", 3)  # Aqui você coloca o arquivo da imagem do quarto
image bg_village = im.FactorScale("village.png", 3.2)  # Aqui você coloca o arquivo da imagem do quarto
image bg_entrada_vila = im.FactorScale("bg_entrada_vila.png", 4)  # Aqui você coloca o arquivo da imagem do quarto

image black = "#000000"  # Usando a cor preta como uma imagem
image getulio = im.FactorScale("getulio.png", 0.6)
image seumirim = im.FactorScale("seumirim.png", 0.15)
image sssocrates = im.FactorScale("sssocrates.png", 2)
image cica = im.FactorScale("preguica.png", 0.7)
image cuica = im.FactorScale("cuica.jpg", 1)
image rubens = im.FactorScale("rubens.png", 1.5)
image rasgamortalha = im.FactorScale("rasgamortalha.png", 0.8)
image billgarca = im.FactorScale("bill-garca.png", 1.2)

# Definindo transições
define dissolve = Dissolve(2.0)  # Transição dissolve (revela) a imagem em 2 segundos

init:
    transform left_slightly:
        xalign 0.2  # Posição mais à esquerda, mas não no extremo.
        yalign 1.0  # Alinhado na base da tela.

    transform left_more:
        xalign 0  # Um pouco mais para o centro, mas ainda à esquerda.
        yalign 1.0