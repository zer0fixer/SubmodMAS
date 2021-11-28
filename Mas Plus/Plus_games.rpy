init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_jokenpo",category=['juegos'],prompt="¿Quieres jugar Piedra, Papel o Tijeras?",aff_range=(mas_aff.HAPPY, None),pool=True, unlocked=True,))

init python in plus_games:
    import random
return

label monika_jokenpo:
    m 1hub "¡Me encantaría jugar!"
    m 1hua "Te deseo suerte, [player]"
    jump game

label game:
    m 1lub "Cuál tienes en mente~{fast}"
    $objeto = ""
    $probabilidad = random.randint(1,3)
    if probabilidad == 1:
        $objeto = "Piedra"
    elif probabilidad == 2:
        $objeto = "Papel"
    elif probabilidad == 3:
        $objeto = "Tijeras"
    menu:
        "Piedra":
            "[m_name] te muestra : [objeto]"
            if probabilidad == 1:
                m 1wua "¡Vaya es un empate!"
                jump gameover
            elif probabilidad == 2:
                m 1efb "Lamento decirte que has perdido."
                jump gameover
            elif probabilidad == 3:
                m 2hua "Me has ganado, [player]."
                jump gameover
        "Papel":
            "[m_name] te muestra : [objeto]"
            if probabilidad == 1:
                m 2hua "Tú ganas, [player]."
                jump gameover
            elif probabilidad == 2:
                m 1wua "¡Quedamos en un empate!"
                jump gameover
            elif probabilidad == 3:
                m 1efb "Lo siento [player] has perdido."
                jump gameover
        "Tijeras":
            "[m_name] te muestra : [objeto]"
            if probabilidad == 1:
                m 1efb "No pudiste contra mí, ¿eh?"
                jump gameover
            elif probabilidad == 2:
                m 2hua "Te otorgo la victoria."
                jump gameover
            elif probabilidad == 3:
                m 1wua "Con que pensamos lo mismo, Jejeje~"
                jump gameover

label gameover:
    m 3eub "Siempre me alegra jugar contigo."
    m 1eta "Quieres jugar nuevamente."
    $ _history_list.pop()
    menu:
        "Si":
            m 1hua "Está bien."
            jump game
        "No":
            m 1ekb "No te preocupes, podemos jugar en otro momento."
return