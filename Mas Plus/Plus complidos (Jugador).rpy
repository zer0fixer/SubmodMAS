init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_monikacompliments",
            category=['romance'],
            prompt="¡Ahora [m_name] te dara cumplidos!",
            random=True
        )
    )

label monika_monikacompliments:
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
return "love"
