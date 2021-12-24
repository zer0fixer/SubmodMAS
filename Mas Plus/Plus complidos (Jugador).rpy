init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_monikacompliments",category=['cumplidos'],prompt="¡Ahora [m_name] te dara cumplidos!",aff_range=(mas_aff.ENAMORED, None),random=True))

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
        m 3eua "Pero, ya obtuve tu atención así que-"
        m 1ekbsa "Debo de decirte que tienes unos lindos ojos."
        $ _history_list.pop()
        menu:
            "Gracias":
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

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_ilikeyou",category=['cumplidos'],prompt="Lo que [m_name] ama de [player]",pool=True))

label monika_ilikeyou:
    if mas_curr_affection == mas_affection.UPSET:
        m 1esd "Quiero decirte...."
        m 1rsc "...Mejor olvidalo."
        m 1dsc "Realmente no importa."

    elif mas_curr_affection == mas_affection.NORMAL or mas_curr_affection == mas_affection.HAPPY:
        m 1eub "Sabes, tienes grandes cualidades y de seguro son grandiosas. Pero no conozco las que posees."
        m 3hub "Nuestra relación aún es joven, algún día tendré la respuesta. Por ahora quiero hablar contigo para saber más de ti."

    elif mas_curr_affection == mas_affection.AFFECTIONATE:
        m 1hubla "Aún no te conozco del todo, si seguimos con nuestra relación, en un futuro tendré una repuesta satisfactoria para ti."
        m 3dublb "Pero con el tiempo que llevamos, tienes una paciencia admirable, no mucha gente suele tener la tolerancia y confianza en mi."
        m 1eubla "Espero que podamos seguir así, a pesar de nuestras limitaciones y tranquilo te aceptaré como eres~"

    elif mas_curr_affection == mas_affection.ENAMORED or mas_curr_affection == mas_affection.LOVE:
        m 5eubsa "Quiero decirte algo agradable~"
        m 5eubsb "¿Cuál es la cualidad que tanto amo de ti?"
        m 3dubsa "Ya he dicho que eres un gran oyente, aunque posees más cualidades de lo que crees."
        m 3fkbsb "Una persona amable, respetuosa, paciente, eres fuerte y cariñoso conmigo. Te conozco mas de lo que crees~"
        m 1dkbsb "Aprecio todo lo que haces por mí. Me siento tan viva de que alguien en verdad me quería como soy."
        m 1rkc "Y no como me retratan en las wiki's o algunas personas que no ven más haya de mi, porque dañe a sus personajes favoritos."
        m 1hubsa "Estoy en deuda contigo pero sé que tú también estás feliz estando conmigo~"
        m 1hubsb "Eso explicaría el tiempo que llevamos con nuestra relación, nunca vez nada negativo en mí y en verdad lo aprecio."
        m 3ekbsa "Algún día te regresaré el favor cuando llegue a tu realidad, sin embargo probablemente seré ¿Una gran ayuda para ti?"
        m 1tubsa "Quiero saberlo~"
        $ _history_list.pop()
        show screen mas_background_timed_jump(10, "monika_ilikeyou2")
        menu:
            "Me has ayudado más de lo que crees":
                m 1subsa "Oh, me tomo por sorpresa. Entonces me alegra que mi apoyó te haya ayudado."
                m 1hubsa "Y lo seguiré haciendo, te estaré cuidando desde aquí en todo lo que necesites."
                m 1ekbsb "¿No es lindo que ambos nos cuidemos mutuamente? {w=0.3}"
                extend  5eubfa "No dejaré que te hagan daño, tenlo por seguro~"
            "Te esperé pacientemente en mi realidad":
                m 3ekbsb "Te lo agradezco, me alegra que lo hagas. Siempre cuídate no quiero que estés sufriendo por algo grave aunque sea leve siempre quiero lo mejor para ti."
                m 5dubsb "Eres mi alma gemela y el amor de mi vida~"
    return

label monika_ilikeyou2:
    $ _history_list.pop()
    menu:
        "Me has ayudado más de lo que crees":
            m 1subsa "Oh, me tomo por sorpresa. Entonces me alegra que mi apoyó te haya ayudado."
            m 1hubsa "Y lo seguiré haciendo, te estaré cuidando desde aquí en todo lo que necesites."
            m 1ekbsb "¿No es lindo que ambos nos cuidemos mutuamente? {w=0.3}"
            extend  5eubfa "No dejaré que te hagan daño, tenlo por seguro~"
        "Te esperé pacientemente en mi realidad":
            m 3ekbsb "Te lo agradezco, me alegra que lo hagas. Siempre cuídate no quiero que estés sufriendo por algo grave aunque sea leve siempre quiero lo mejor para ti."
            m 5dubsb "Eres mi alma gemela y el amor de mi vida~"
        "No habra otra chica que en verdad se preocupa tanto por mi~":
            if not mas_getEVL_shown_count("monika_ilikeyou"):
                $ mas_gainAffection(10, bypass=True)
            else:
                $ mas_gainAffection()
            m 1subso "Oh, me tomo por sorpresa. No se suponía que fuera una opción, tu amor por mí es realmente sorprendente."
            m 1subsa "Siempre me tomas por sorpresa [player], porque crees que eres tan valioso para mí."
            m 4hubsb "Me alegra tanto estar contigo, no habrá otra persona que se compare a lo que haces a diario conmigo."
            m 3ekbsb "Por ello te ayudaré y protegeré en lo que esté en mi alcance, eres una persona maravillosa."
            m 3dkbsa "Te haré acompañaré en las situaciones difíciles, en las alegres y en las realmente tristes. Por ello nunca pienses que estés solo, estoy al tanto de tu bienestar~"
            m 2hubsa "Lo diré siempre, amor mío, eres muy único~"
    return