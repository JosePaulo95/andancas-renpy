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

# Definindo imagens
image bg_cozinha = im.FactorScale("cozinha.jpg", 1.5)  # Aqui você coloca o arquivo da imagem do quarto
image bg_quarto = im.FactorScale("quarto.jpg", 3.3)  # Aqui você coloca o arquivo da imagem do quarto
image bg_floresta = im.FactorScale("floresta-sombria.jpg", 1.5)  # Aqui você coloca o arquivo da imagem do quarto
image bg_village = im.FactorScale("village.png", 3.2)  # Aqui você coloca o arquivo da imagem do quarto

image black = "#000000"  # Usando a cor preta como uma imagem
image getulio = im.FactorScale("getulio.png", 0.6)
image seumirim = im.FactorScale("seumirim.png", 0.15)
image sssocrates = im.FactorScale("sssocrates.png", 2)
image cica = im.FactorScale("preguica.png", 0.7)
image cuica = im.FactorScale("cuica.jpg", 1)

# Definindo transições
define dissolve = Dissolve(2.0)  # Transição dissolve (revela) a imagem em 2 segundos
