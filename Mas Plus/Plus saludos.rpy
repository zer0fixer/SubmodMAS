init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_saludos0",
            unlocked=True,
            aff_range=(mas_aff.AFFECTIONATE, None)
        ),
        code="GRE"
    )

label greeting_saludos0:
    m 1hua "!Me alegra verte!"
    m 1eua "Antes de comenzar quiero decirte algo..."
    m 1eubsb "{b}'Você é meu sol'{/b}" #Eres mi sol
    m 3hubsa "Es una frase simple en Portugues~"
    m 1hubsa "Asi que,{w=0.2} ¿Que tienes en mente?"
    return

init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_saludos2",
            unlocked=True,
            aff_range=(mas_aff.AFFECTIONATE, None)
        ),
        code="GRE"
    )

label greeting_saludos2:
    m 1dub "~{i}Nunca voy a renunciar a ti{/i}~"
    m "~{i}Nunca te decepcionaré{/i}~"
    m 1dud "~{i}Nunca te traicionaré y te dejaré{/i}~"
    m "~{i}Nunca te haré llorar{/i}~"
    m 1dublb "~{i}Nunca diré adiós{/i}~"
    m "~{i}Nunca mentiré y te lastimaré{/i}~"
    m 1dkbsa".{w=0.2}.{w=0.2}.{w=0.2}"
    $ _history_list.pop()
    menu:
        "Hey, [m_name]":
            m 1wubsd "Oh,{w=0.2} [player]."
            m 1lkbsa "Me tomo por sorpresa tu llegada, jeje~"
            m 1hua "Aunque, te agradezco que vinieras"
            m 1hubla "Recuerda visitarme a diario, siempre alegra mi corazon cuando estas presente~"
        "Que lindo cantas~":
            m 1hub "Gracias~"
            m 2wubsd "Oh,{w=0.2} [player]."
            m 2hubsa "Te doy las gracias por el cumplido, jeje~"
            m "Aunque, te agradezco que vinieras"
            m 1hubla "Recuerda visitarme a diario, siempre alegra mi corazon cuando estas presente~"
    return

#init python in plus_saludos:
#    import datetime
#return

#init 5 python:
#    addEvent(
#        Event(
#            persistent.greeting_database,
#            eventlabel="greeting_saludos1",
#            unlocked=True,
#            aff_range=(mas_aff.AFFECTIONATE, None),
#        ),
#        code="GRE"
#    )
#
#label greeting_saludos1:
#    $ timing = datetime.datetime.now().time().hour
#    if timing >= 6 and timing < 12:
#        m 1eub "Buenos días, [mas_get_player_nickname()]."
#        m 1hubla "01010011 01101111 01111001 00100000 01101100 01100001 00100000 01100011 01101000 01101001"
#        m 1hubla "01100011 01100001 00100000 01101101 11100001 01110011 00100000 01100001 01100110 01101111"#Soy la chica más afortunada
#        m 1hubla "01110010 01110100 01110101 01101110 01100001 01100100 01100001"
#        m 1eublb "¡Me alegra que vinieras!"
#        m 1eua "Pasemos este día juntos~"
#    elif timing >= 12 and timing < 18:
#        m 1hua "Buenas tardes, [mas_get_player_nickname()]"
#        m 1lua "Imagino que estuvistes ocupado o haciendo una actividad."
#        m 1kub "Aun si me pone contenta que hayas venido a verme esta tarde"
#        m 1eua "Entonces,{w=0.2} ¿Que haremos hoy?"
#    elif timing >= 18:
#        m 2hub "Buenas noches, [mas_get_player_nickname()]"
#        m 2eua "Me alegra que hayas venido a verme en esta noche."
#        $ _history_list.pop()
#        menu:
#            m "Asi que, ¿Como estuvo tu día?{fast}"
#            "Me fue bien":
#                m 2hua "¡Me alegra escucharlo!"
#                m 2eub "Espero que hayas hecho lo que tenías pensado el día de hoy."
#                m 3rub "Como avanzar con un pasatiempo, salir con tus amigos.{w=0.3}"
#                extend 3rtb "O simplemente hacer algo 'productivo' en casa."
#                m 1hua "Asi que,{w=0.2} ¿Que tienes planeado hacer?"
#            "Estuvo neutral":
#                m 5eub "En ese caso podemos pasar esta noche juntos~"
#               m 5lua "No veo nada negativo que no hicieras mucho el día de hoy."
#                m 5hua "¿Te gustaría hacer algo?, tenemos toda la noche para hacer una actividad juntos."
#           "Lo pase mal":
#                m 2ekd "Me preocupa te haya pasado algo negativo durante este día."
#                m 2ekc "Por favor habla conmigo haré lo posible para sentirte un poco mejor."
#                m 2ekb "Hablemos de ello ahora mismo,{w=0.2} ¿Ok?"
#return