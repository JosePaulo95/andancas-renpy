﻿init python:
    def tata_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("click_003.ogg")

    def getulio_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("select_004.ogg")
    
    def coruja_voice(event, interact=True, **kwargs):
        if not interact:
            return
        if event == "show":
            renpy.sound.play("scroll_005.ogg")

define tata = Character("Tatá", color="#E91940")
define coruja_sonho = Character("Coruja", color="#2B6B9C", window_xalign=2.0, window_right_padding=50)
define getulio = Character("Getúlio", color="#E7B58A")
define seumirim = Character("Seu Mirim", color="#E59EAD")
define sssocrates = Character("Sssócrates", color="#BDA0CB")   # Lilás claro, para um tom misterioso e excêntrico
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
image bg_cozinha_clean = im.FactorScale("v3/cozinha_clean.png", 1)  # Aqui você coloca o arquivo da imagem do quarto
# image bg_cozinha_clean = im.FactorScale("v3/cozinha_clean.png", 1)  # Aqui você coloca o arquivo da imagem do quarto
image bg_quarto_com_tata = im.FactorScale("v3/quarto_com_tata.png", 1.05)  # Aqui você coloca o arquivo da imagem do quarto
image bg_quarto_sem_tata = im.FactorScale("v3/quarto_sem_tata.png", 1.05)  # Aqui você coloca o arquivo da imagem do quarto
image bg_floresta = im.FactorScale("v1/floresta-sombria.png", 1.05)  # Aqui você coloca o arquivo da imagem do quarto
image bg_colheita = im.FactorScale("v1/bg_colheita.jpg", 3.2)  # Aqui você coloca o arquivo da imagem do quarto
image bg_floresta_obras = im.FactorScale("v1/bg_floresta_obras.jpg", 3)  # Aqui você coloca o arquivo da imagem do quarto
image bg_village_manha = im.FactorScale("v3/vila_manha.png", 1.1)
image bg_village_tarde = im.FactorScale("v3/vila_tarde.png", 1.1)
image bg_entrada_vila = im.FactorScale("v1/bg_entrada_vila.png", 4)

image black = "#000000"  # Usando a cor preta como uma imagem
image tata = im.FactorScale(im.Flip("v2/tata.png", horizontal=True), 1)
image getulio = im.FactorScale("v3/getulio.png", 1)
image seumirim = im.FactorScale(im.Flip("v2/seumirim.png", horizontal=True), 1)
image sssocrates = im.FactorScale("v3/sssocrates.png", 1)
image cica = im.FactorScale("v2/preguica.png", 0.7)
image cuica = im.FactorScale("v3/cuica.png", 1)
image rubens = im.FactorScale("v2/rubens.png", 1.5)
image rasgamortalha = im.FactorScale("v2/rasgamortalha.png", 0.8)
image billgarca = im.FactorScale("v2/bill-garca.png", 1.2)
image coruja_sonho = im.FactorScale("v1/coruja_sonho.png", 1)

# Definindo transições
define dissolve = Dissolve(2.0)  # Transição dissolve (revela) a imagem em 2 segundos

init:
    transform left_slightly:
        xalign 0.2  # Posição mais à esquerda, mas não no extremo.
        yalign 1.0  # Alinhado na base da tela.

    transform left_more:
        xalign 0  # Um pouco mais para o centro, mas ainda à esquerda.
        yalign 1.0