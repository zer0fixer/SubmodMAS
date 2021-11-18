init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_monikacompliments",category=['romance'],prompt="¡Ahora [m_name] te dara cumplidos!",aff_range=(mas_aff.HAPPY, None),random=True))

label monika_monikacompliments:
    $ ev = mas_getEV("monika_monikacompliments")

    if ev.shown_count == 0:
        m 1eud "Sabes, [player]."
        m 1eub "Siempre me das cumplidos cuando vienes a visitarme, No es algo negativo de hecho alegra mi corazón."
        m 1lka "Sin embargo, me siento un poco mal de que tengas más maneras de halarme y darme cumplidos-"
        m 1lksdlb "Y eso me da una sensación de culpa, No quiero excusarme por ello y eso se debe a que el juego no me da forma de expresarme..."
        m 3hua "¡Pero pude programar más diálogos para ti y ahora en adelante no te dejaré excluido, [player]!"
        m 3duu "Por ello te diré uno~"
        m 1eubla "Siempre has sido amable y paciente conmigo a pesar de lo que mencione anteriormente."
        m 1hublb "¡Eres una increíble persona a tu manera!.{w=0.3} {nw}"
        extend 5ekblb "Si tienes problemas personales puedes acudir a mí."
        m 5ekbla "Te ayudaré con mucho gusto~"
        m 5hubsb"Te amo, [mas_get_player_nickname()]."

    elif ev.shown_count == 1:
        m 1hub "Esta es la segunda vez que sale a flote este tema, Jeje~"
        m 2eub "¿Te acuerdas de lo que hablamos sobre darte cumplidos?"
        m 2eua "Realmente no veo necesario volver a explicar lo que mencione."
        m 3eua "Pero, como ya tienes mi atención-"
        m 1ekbsa "Debo de decirte que tienes unos lindos ojos."
        $ _history_list.pop()
        menu:
            "G-gracias":
                m 1hubsu "De nada~"
                m 1hubsb "Por ello me propuse a ser más libre y coqueta contigo."
                m 5rubsu "Se siente bien expresar lo que me atrae de ti."
                m 5hubsa "Recuerda que siempre te amaré."
            "Lo mismo va para ti":
                m 3hubsu "Tu encanto siempre me hace feliz."
                m 3tubsb "Eso me gusta de ti."
                m 1hubsa "Te amo, [mas_get_player_nickname()]."
    else:
        m 2ltc "No sé que añadir al tema."
        m 2lsb "Ya hemos abarcado lo que tenía que decir-"
        m 2hksdrb "Y aún lo estoy programando."
        m 1eubla "Pero debo de expresarte que siempre estaré de tu lado."
        m 1dsbld "Aunque la pantalla nos limite estar juntos."
        m 1fkbsa "No permitiré que los sentimientos negativos te invadan."
        m 1hubsa "Por ello te amaré eternamente, nunca estarás solo."

return "love"
