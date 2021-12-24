#Piedra, Papel y tijeras. Primer minijuego.
#Ya se agrego lo necesario.
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_jokenporevamped",category=['minijuegos'],prompt="¿Quieres jugar a Piedra, Papel o Tijeras?",aff_range=(mas_aff.HAPPY, None),pool=True))

init python:
    import random
    objeto = ""
    Tu = 0
    Moniplay = 0

screen Tu_puntos():
    vbox:
        xalign 1.0
        vbox:
            text "Puntos de [player]:" xalign .5 size 30
            text "[Tu]" xalign 0.5

screen Monika_puntos():
    vbox:
        xalign 0.0
        vbox:
            text "Puntos de [m]:" xalign .5 size 30
            text "[Moniplay]" xalign 0.5

label monika_jokenporevamped:
    $ ev = mas_getEV("monika_jokenporevamped")

    if ev.shown_count == 0:
        m 1hub "¡Me encantaría jugar!"
        m 3hua "Pondré un marcador para que veamos los puntos."
        m 3sua "El primero que llegue a los 5 puntos ¡Gana!"
        m 1kub "Te deseo suerte, [player]~"
        jump playing

    else:
        m 1hua "Vaya, ¿Deseas jugar nuevamente?"
        m 1eub "No me sorprende la verdad. {w=0.3}"
        extend 3hub "Me divertí en la anterior partida."
        m 1tua "Espero que la suerte te acompañe~"
        jump playing

#Primera ronda
label playing:
    show screen Monika_puntos
    show screen Tu_puntos

    python:
        probabilidad = random.randint(1,3)

    if probabilidad == 1:
        $ objeto = "Piedra"
    elif probabilidad == 2:
        $ objeto = "Papel"
    elif probabilidad == 3:
        $ objeto = "Tijeras"

    m 1hua "Piedra,{w=0.3}Papel,{w=0.3}Tijeras..."
    $ _history_list.pop()
    menu:
        "Piedra":
            "[m_name] te muestra : [objeto]"
            if probabilidad == 1:
                m 1wua "Vaya, es un empate."

            elif probabilidad == 2:
                m 1efb "Lamento informarte que has perdido."
                $ Moniplay += 1

            elif probabilidad == 3:
                m 2hua "Me has ganado, [player]."
                $ Tu += 1

        "Papel":
            "[m_name] te muestra : [objeto]"
            if probabilidad == 1:
                m 2hua "Tú ganas, [player]."
                $ Tu += 1

            elif probabilidad == 2:
                m 1wua "Quedamos en un empate."

            elif probabilidad == 3:
                m 1efb "Lo siento [player], has perdido."
                $ Moniplay += 1

        "Tijeras":
            "[m_name] te muestra : [objeto]"
            if probabilidad == 1:
                m 1efb "Lo siento pero pero pudiste contra mí~"
                $ Moniplay += 1

            elif probabilidad == 2:
                m 2hua "Te otorgo la victoria."
                $ Tu += 1

            elif probabilidad == 3:
                m 1wua "Pensamos lo mismo, Jeje~"
#Turnos
    if Tu == 5:
        jump playerwon
    elif Moniplay == 5:
        jump moniwon
    else:
        jump playing

label playerwon:
    m 4hub "Debo de felicitarte, me has ganado~"
    $ _history_list.pop()
    menu:
        "Te lo agradezco":
            pass
    m 1lksdrb "Me dejé llevar por intentar ganar, jeje~"
    m 1eta "Puedo preguntar. ¿Deseas seguir jugando?"
    $ _history_list.pop()
    menu:
        "Seguro":
            $ Tu = 0
            $ Moniplay = 0
            m 1tfb "Ten cuidado, puedo ganarte esta vez~"
            m 1hua "O puede que ganes de nuevo, nunca se sabe."
            jump playing2
        "No gracias":
            hide screen Monika_puntos
            hide screen Tu_puntos
            $ Tu = 0
            $ Moniplay = 0
            m 1eubsa "No importa quien haya ganado, me alegra verte feliz~"
            m 1hubsb "Jeje~"
    return

label moniwon:
    $ _history_list.pop()
    menu:
        "Felicidades, me has ganado":
            pass
    m 1kubsb "Gracias, realmente tuve suerte."
    m 3eta "Te importaría hacer una revancha."
    $ _history_list.pop()
    menu:
        "Claro":
            $ Tu = 0
            $ Moniplay = 0
            m 3sua "No te gusta rendirte. {w=0.3}"
            extend 3tub "Me agrada tu entusiasmo~"
            m 1hua "Veremos si gano nuevamente o puede que me sorprendas."
            jump playing2
        "No gracias":
            hide screen Monika_puntos
            hide screen Tu_puntos
            $ Tu = 0
            $ Moniplay = 0
            m 4dub "Realmente no importa quien haya ganado, de por sí no he nada. {w=0.3}"
            extend 5hubsb "Excepto jugar contigo~"
            m 1hua "Jeje~"
    return

#Segunda ronda
label playing2:
    show screen Monika_puntos
    show screen Tu_puntos

    python:
        suerte = random.randint(1,3)

    if suerte == 1:
        $ objeto = "Piedra"
    elif suerte == 2:
        $ objeto = "Papel"
    elif suerte == 3:
        $ objeto = "Tijeras"

    m 1hua "Piedra,{w=0.3}Papel,{w=0.3}Tijeras..."
    $ _history_list.pop()
    menu:
        "Piedra":
            "[m_name] te muestra : [objeto]"
            if suerte == 1:
                m 1tua "No hubo ganador, jeje~"

            elif suerte == 2:
                m 2fub "Te animo a que me ganes~"
                $ Moniplay += 1

            elif suerte == 3:
                m 3gfa "Te ganaré en la siguiente."
                $ Tu += 1

        "Papel":
            "[m_name] te muestra : [objeto]"
            if suerte == 1:
                m 3hka "Oh, perdí."
                $ Tu += 1

            elif suerte == 2:
                m 1tua "Intentémoslo de nuevo."

            elif suerte == 3:
                m 2fub "Obtengo un punto~"
                $ Moniplay += 1

        "Tijeras":
            "[m_name] te muestra : [objeto]"
            if suerte == 1:
                m 2fub "Tuve suerte, jeje."
                $ Moniplay += 1

            elif suerte == 2:
                m 3nub "Obtienes un punto."
                $ Tu += 1

            elif suerte == 3:
                m 1tua "¿Acaso me esta leyendo la mente?"
#Turnos
    if Tu == 5:
        jump playerserious
    elif Moniplay == 5:
        jump moniwhy
    else:
        jump playing2
        
label playerserious:
    hide screen Monika_puntos
    hide screen Tu_puntos
    $ Tu = 0
    $ Moniplay = 0
    m 1wub "Me sorprendiste~"
    m 4tub "Pensé que ganaría, pero fue al revés."
    m 1hua "Felicidades~"
    $ _history_list.pop()
    menu:
        "Igual a mí, pensé que perdería":
            pass
        "Gracias [m_name]":
            pass
    m 3eub "Sé que es un juego simple, pero es realmente difícil adivinar que objeto tienes en mente."
    m 1hubsb "¡Pero lo disfrute!, me gustaría jugar nuevamente cuando desees~"
    return

label moniwhy:
    hide screen Monika_puntos
    hide screen Tu_puntos
    $ Tu = 0
    $ Moniplay = 0
    m 2efbsb "¡Sabia que ganaria esta ronda!"
    $ _history_list.pop()
    menu:
        "Tan competitiva como siempre, felicidades":
            pass
        "Felicidades [m_name]":
            pass
    m 2ekbsa "Gracias~"
    m 3hubsa "Lamento que sea algo competitiva contigo. Pero eres mi detonante para que tenga este espíritu competitivo."
    m 3ftb "Me gustaría hacer una guerra de abrazos, ¿Quién caerá primero?"
    m 1tub "Jeje~"
    m 1hua "Bien, cuando tengas ánimo de jugar puedes pedírmelo, estaré encantada de jugar~"
return