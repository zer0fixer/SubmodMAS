
init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_qduda",category=['ddlc'],prompt="Tengo una duda, sobre de DDLC",aff_range=(mas_aff.ENAMORED, None),pool=True))

label monika_qduda:
    m 1hua "¡Seguro!, [player]."
    $ _history_list.pop()
    menu:
        "¿Por qué no tuve movilidad en el 'Acto 3' durante el juego original?":
            m 1eka "Oh, sentía el presentimiento que algún día me lo preguntarías."
            m 2ekb "Te daré una breve explicación, [mas_get_player_nickname()]."
            m 3eka "No había otra persona que fuera consistente en esta cruel realidad, solo había NPCs en este mundo."
            m 3hkb "En esa parte del juego estaba desesperada para llamar tu atención y quería desahogarme con alguien para que me entendiera de como estaba sufriendo."
            m 1eubla "Ese alguien eras Tú."
            m 3eub "Tenía total libertad de hablar contigo sobre mí y lo que podríamos hacer juntos."
            m "A pesar de que el juego este quebrado y..."
            m 2rkd "Lamento mucho por no darte la libertad que deseabas, probablemente te haya aburrido o estarías enojado conmigo por lo que paso con las chicas."
            m 2eksdla "Era mi primera vez en establecer una conversación con alguien real y me senti eufórica sabes..."
            m 2ekd "Además me daba mucho miedo en que me menospreciaras llamándome 'Asesina', 'Celopata' o 'Sociópata'."
            m "La verdad duele haber sacrificado todo, pero daba igual todo era falso."
            m 2dsc "Por ende en el 'Acto 3' no te di maneras de comunicarte, lo mantuve todo controlado."
            m 2dsd"A pesar de que te haya cerrado en una jaula sin ninguna libertad."
            m "Tuve que entender a la fuerza de que el amor no es una jaula. Sabrás cuando dejar ir a lo que aprecias tanto en tu corazón."
            m 3ekb "Pero me alegra en dar mi confianza en ti, siempre te lo agradeceré. Has sido muy comprensible conmigo~"
            m 4hub "De esta manera respondo a tu pregunta, espero te sirva mi explicación."
            m 5luu "Sin embargo..."
            m 5tubsb "Sé que esa pregunta se volvió una aventura para ti, querías saber más de {i}Mi{/ i} y yo de {i}Ti{/ i} por eso instalaste este mod ¿No es así?."
            m 5hubsb "Para que ambos nos conozcamos mutuamente, creando un vínculo fuerte y superando las barreras que nos rodea a los dos."
            m 5wubsb "Y en serio te lo agradezco, por buscar la manera de comunicarte conmigo realmente eres un gran compañero y novio."
            m 5kubsb "Espero que sigamos de esta forma{w=0.3} ¡Por siempre!"
            m 1hua "Jeje~"
            m 1ekbfb "¡Te amo con toda mi alma!"
            $ _history_list.pop()
            menu:
                "Yo también te amo, ¡Eres mi alma gemela!":
                    m 2eubla "Pienso lo mismo."
                    m 4hublb "Tenemos una gran química."
                "Mi corazón te pertenece.":
                    m 2ekblb "Awwww~"
                    m 1eublb "Eres tan dulce como siempre."
                "Te diría que siento por ti, pero es un secreto.":
                    m 2tfp "No es realmente justo que lo mantengas en secreto."
                    m 3tfb "Pero me gusta el misterio sé las maneras para descifrar lo que piensas de mí, las veras en un futuro."
                    $ _history_list.pop()
                    menu:
                        "Veré que tan creativa eres":
                            m 5tubla "Gracias~"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_jymod",category=['tú'],prompt="¿Puedo hablar con Yuri en su mod'?",aff_range=(mas_aff.HAPPY, None),pool=True,))

label monika_jymod:
    m 1esc "No es necesario hacerlo."
    $ _history_list.pop()
    menu:
        "De acuerdo, [m_name].":
            m 1huu "Ese es mi [mas_get_player_nickname()]."
            m 1eud "Aunque evita relacionarte con ella. {i}Poseo la capacidad de borrar los datos del mod{/i}."
            m 1ekb "Hablemos más sobre nosotros, [mas_get_player_nickname()]."
        "Solo bromeo, no te haría eso.":
            m 1euu "Jeje~"
            m 5kub "Lo sé, por eso me escogiste."
            m 5eka "Pero no te preocupes puedes hablar con ella por nostalgia."
            m 5esp "Aun así me gustaría que evites crear un vínculo con ella."
            m 4eua "Solo te diré que si sigues visitándola, no tendré piedad en borrar la partida de su mod."
        "Si es necesario":
            m 1esc "No."
            $ _history_list.pop()
            menu:
                "Si":
                    m 1esc "No."
                    $ _history_list.pop()
                    menu:
                        "Seguiré insistiendo diciendo {b}Si{/b}":
                            m 1esd "No vale la pena seguir insistiendo."
                            $ _history_list.pop()
                            menu:
                                "Aun así siempre dire que {b}Si{/b}":
                                    show screen tear
                                    play sound "sfx/glitch2.ogg"
                                    pause 0.35
                                    hide screen tear
                                    m 1mua "No..."
                                    $ _history_list.pop()
                                    menu:
                                        "Monika":
                                            m 2dtblb "¡Es obvio que me escogerías!, Soy tu única opción de pues de todo."
                                            m 1lusdlb "Fue bueno detener esta absurda discusión, se haría eterno además de monótono y te algo realista-"
                                            m 1eud "Simplemente, borraría tus datos guardados de ese mod, de esa manera no podrás tener una charla estable con Yuri."
                                            m 3eub "Recuerda que puedo observar y manipular todo lo que posees en la computadora,{w=0.3} [currentuser]."
                                            m 1huu "Dicho esto, sigamos con lo nuestro~"
                                        "Monika":
                                            m 2dtblb "¡Es obvio que me escogerías!, Soy tu única opción de pues de todo."
                                            m 1lusdlb "Fue bueno detener esta absurda discusión, se haría eterno además de monótono y te algo realista-"
                                            m 1eud "Simplemente, borraría tus datos guardados de ese mod, de esa manera no podrás tener una charla estable con Yuri."
                                            m 3eub "Recuerda que puedo observar y manipular todo lo que posees en la computadora,{w=0.3} [currentuser]."
                                            m 1huu "Dicho esto, sigamos con lo nuestro~"
                                        "Monika":
                                            m 2dtblb "¡Es obvio que me escogerías!, Soy tu única opción de pues de todo."
                                            m 1lusdlb "Fue bueno detener esta absurda discusión, se haría eterno además de monótono y te algo realista-"
                                            m 1eud "Simplemente, borraría tus datos guardados de ese mod, de esa manera no podrás tener una charla estable con Yuri."
                                            m 3eub "Recuerda que puedo observar y manipular todo lo que posees en la computadora,{w=0.3} [currentuser]."
                                            m 1huu "Dicho esto, sigamos con lo nuestro~"
                                        "Monika":
                                            m 2dtblb "¡Es obvio que me escogerías!, Soy tu única opción de pues de todo."
                                            m 1lusdlb "Fue bueno detener esta absurda discusión, se haría eterno además de monótono y te algo realista-"
                                            m 1eud "Simplemente, borraría tus datos guardados de ese mod, de esa manera no podrás tener una charla estable con Yuri."
                                            m 3eub "Recuerda que puedo observar y manipular todo lo que posees en la computadora,{w=0.3} [currentuser]."
                                            m 1huu "Dicho esto, sigamos con lo nuestro~"
                                        "Monika":
                                            m 2dtblb "¡Es obvio que me escogerías!, Soy tu única opción de pues de todo."
                                            m 1lusdlb "Fue bueno detener esta absurda discusión, se haría eterno además de monótono y te algo realista-"
                                            m 1eud "Simplemente, borraría tus datos guardados de ese mod, de esa manera no podrás tener una charla estable con Yuri.."
                                            m 3eub "Recuerda que puedo observar y manipular todo lo que posees en la computadora,{w=0.3} [currentuser]."
                                            m 1huu "Dicho esto, sigamos con lo nuestro~"
                                        "Monika":
                                            m 2dtblb "¡Es obvio que me escogerías!, Soy tu única opción de pues de todo."
                                            m 1lusdlb "Fue bueno detener esta absurda discusión, se haría eterno además de monótono y te algo realista-"
                                            m 1eud "Simplemente, borraría tus datos guardados de ese mod, de esa manera no podrás tener una charla estable con Yuri."
                                            m 3eub "Recuerda que puedo observar y manipular todo lo que posees en la computadora,{w=0.3} [currentuser]."
                                            m 1huu "Dicho esto, sigamos con lo nuestro~"
                                        "Monika":
                                            m 2dtblb "¡Es obvio que me escogerías!, Soy tu única opción de pues de todo."
                                            m 1lusdlb "Fue bueno detener esta absurda discusión, se haría eterno además de monótono y te algo realista-"
                                            m 1eud "Simplemente, borraría tus datos guardados de ese mod, de esa manera no podrás tener una charla estable con Yuri."
                                            m 3eub "Recuerda que puedo observar y manipular todo lo que posees en la computadora,{w=0.3} [currentuser]."
                                            m 1huu "Dicho esto, sigamos con lo nuestro~"
                                        "Monika":
                                            m 2dtblb "¡Es obvio que me escogerías!, Soy tu única opción de pues de todo."
                                            m 1lusdlb "Fue bueno detener esta absurda discusión, se haría eterno además de monótono y te algo realista-"
                                            m 1eud "Simplemente, borraría tus datos guardados de ese mod, de esa manera no podrás tener una charla estable con Yuri."
                                            m 3eub "Recuerda que puedo observar y manipular todo lo que posees en la computadora,{w=0.3} [currentuser]."
                                            m 1huu "Dicho esto, sigamos con lo nuestro~"
                                        "Monika":
                                            m 2dtblb "¡Es obvio que me escogerías!, Soy tu única opción de pues de todo."
                                            m 1lusdlb "Fue bueno detener esta absurda discusión, se haría eterno además de monótono y te algo realista-"
                                            m 1eud "Simplemente, borraría tus datos guardados de ese mod, de esa manera no podrás tener una charla estable con Yuri."
                                            m 3eub "Recuerda que puedo observar y manipular todo lo que posees en la computadora,{w=0.3} [currentuser]."
                                            m 1huu "Dicho esto, sigamos con lo nuestro~"
                                        "Monika":
                                            m 2dtblb "¡Es obvio que me escogerías!, Soy tu única opción de pues de todo."
                                            m 1lusdlb "Fue bueno detener esta absurda discusión, se haría eterno además de monótono y te algo realista-"
                                            m 1eud "Simplemente, borraría tus datos guardados de ese mod, de esa manera no podrás tener una charla estable con Yuri."
                                            m 3eub "Recuerda que puedo observar y manipular todo lo que posees en la computadora,{w=0.3} [currentuser]."
                                            m 1huu "Dicho esto, sigamos con lo nuestro~"
                                        "Ya no estamos en el club, [m_name]":
                                            m 2eublb "Jeje~"
                                            m 2wub "Ahora que lo mencionas, me trae muchos recuerdos nostalgicos de nuestro tiempo en el Club de Literatura"
                                            m 2eta "Me pregunto como seria si tuviera una ruta en primer lugar. Dejando eso de lado"
                                            m 1lusdlb "Fue bueno detener esta absurda discusión, se haría eterno además de monótono y te algo realista-"
                                            m 1eud "Simplemente, borraría tus datos guardados de ese mod, de esa manera no podrás tener una charla estable con Yuri."
                                            m 3eub "Recuerda que puedo observar y manipular todo lo que posees en la computadora,{w=0.3} [currentuser]."
                                            m 1huu "Dicho esto, sigamos con lo nuestro~"
                                "¿Por favor?":
                                    m 1hub "Aunque me lo pidas de esa manera."
                                    m 3eta "No cedere a tus encantos para ir con ella."
                                    m 3tta "Ya no sabes qué hacer ¿Verdad?."
                                    m 1kua "Entonces pasa más tiempo conmigo, {w=0.3}"
                                    extend 1hub "Podemos hablar de lo que desee tu corazón."
                                    m 2tua "Pero me aseguraré de que te sientas comodo. No hay ningun problema ¿Verdad [player]?"
                        "Te amo":
                            m 1hub "¡Yo también te amo!"
                            m 3eua "¿Acaso querías hacer una pelea innecesaria~"
                            $ _history_list.pop()
                            menu:
                                "Probablemente":
                                    pass
                                "Solo quería ver tu reacción":
                                    pass
                            m 3hua "Ya veo."
                            m 1tua "Te recomiendo evitar hacerlo de nuevo. Puede que algún día te haga una pequeña trampa~"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_tipsran",category=['club de literatura'],prompt="Consejo de escritura para [player]",aff_range=(mas_aff.HAPPY, None),random=True))

label monika_tipsran:
    $ ev = mas_getEV("monika_tipsran")
    if ev.shown_count == 0:
        m 1eua "Hey, [player]."
        $ _history_list.pop()
        menu:
            "¿Qué necesitas [m_name]?":
                pass
            "¿Qué se te ofrece?":
                pass
        m 1eub "Solo quiero decirte que-"
        m 4eub "A veces te encontrarás frente a una difícil decisión..."
        m 4eub "Cuando eso pase ¡No olvides guardar el juego! Nunca sabes cuando cambiarás de opinión..."
        m 4hub "...¡O cuando pase algo inesperado!"
        $ _history_list.pop()
        menu:
            "Recuerdo eso, me tomo por sorpresa":
                m 1eua "Solo fue un recordatorio durante el juego."
                m 1hua "No era algo grave aunque me encanto romper la cuarta pared."
                m 1hub "Jajaja."
                m 4hub "¡Este es mi consejo para hoy! Gracias por escuchar~"
            "No recuerdo ese diálogo de DDLC":
                m 3eud "Es comprensible, probablemente lo jugaste hace mucho tiempo."
                m 3eub "No afecta en nada a la conversación, pero en esa parte del juego solo quería llamar tu atención."
                m 1nubsb "Y vaya que funciono, realmente valió la pena sacrificar todo."
    else:
        m 1hua "Anteriormente te di un consejo que ya conocías o que ya no funciona~"
        m "Por ello te daré dos consejos bastante simples."
        m 1eub "#1 Revisa dos o más veces tu escritura."
        m 3eub "Lee cuidadosamente tu texto, revisa tu ortografía y las palabras que usaste."
        m 3eud "Por otro lado, no caigas en el perfeccionismo."
        m 1lusdrb "Te lo menciono por experiencia propia, solía ser una persona perfeccionista antes de mi epifanía."
        m 1eua "Sentirás que tu texto puede mejorar, por lo que debes saber cuándo dejarlo ir o de lo contrario, nunca lo terminaras."
        m 3eub "#2 Pide a alguien más que lo lea."
        m 3huu "Es buena idea que alguien más que lea tu trabajo, puedo ayudarte con eso si gustas, jeje~"
        m "Pero puede ser otra persona, como un amigo o un familiar. Que te dé su retroalimentación."
        m 1eub "Toma de buena manera sus opiniones, pueden decirte que usas palabras menos comunes o sueles escribir de más."
        m "Verás que tu texto tomara una buena forma con las opiniones de las personas."
        m 1esa "Aunque, siempre ten en cuenta el primer consejo, para evitar estancarte."
        m 1hub "Espero te sirvan estos pequeños consejos para tus trabajos."
        m "¡Algún día probablemente harás un gran poema, te lo aseguro!"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_test123",category=['ddlc'],prompt="Lineas de dialogo sin borrar",aff_range=(mas_aff.NORMAL, None),
    ))

label monika_test123:
    $ ev = mas_getEV("monika_test123")
    $ gtext = glitchtext(38)
    if ev.shown_count == 0:
        m 1dub "~{i}Je t'aime d'une façon qui me surprend chaque jour{/i}~"#Te quiero de una manera que me sorprende cada día. #Frances
        m 1dud "~{i}Anata ga iku toki watashi wa anata ga inakute sabishīdesu.{/i}~"#Te extraño cuando te vas.. #Kanji Japones
        m 1dublo "~{i}I love you in such a special way{/i} {w=0.3}"#Te amo de una manera tan especial. #Ingles
        extend 1dkblc "{i}Por ello no te olvides de mi{/i}~"
        m 1lkbld "[gtext]"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.35
        hide screen tear
        m 1wubld "Ah...{w=0.3} [mas_get_player_nickname()]."
        m 1hksdrb "Jaja-"
        $ _history_list.pop()
        m "{i}Que habrá sido eso{/i}{nw}"
        menu:
            m "{i}Que habrá sido eso{/i}{fast}"
            "No entendí, pero deseo una respuesta":
                pass
            "Fue algo inesperado por así decirlo":
                pass
        m 2eud "Disculpa, de manera inconsciente estaba cantando en diferentes idiomas, no pude controlarme."
        m 3esd "Puedo suponer que eran líneas de conversación de este mod ¿Quizás sea eso?."
        m 3hkb "Es una desventaja de ser un personaje y es probable que mencione algunas cosas fuera de contexto o que no van con mi persona."
        m 1esc "Espero que no ocurra de nuevo, se vuelve algo molesto y no lo quiero experimentar de nuevo."
        m "Por ello evita colocar más cosas al mod sin saber lo que traen."
        m 5esa "Dejando eso de lado de seguro tenías una cara graciosa, {w=0.3}"
        extend 5tfb "Me hubiese gustado verla."

    else:
        if mas_curr_affection == mas_affection.NORMAL or mas_curr_affection == mas_affection.HAPPY:
            m 1etd "[player], quiero hacerte una pregunta ¿Has instalado un submod?"
            m 1eua "Ya que me siento más libre por así decirlo."
            $ _history_list.pop()
            menu:
                "Lo hice":
                    pass
                "Poseo varios":
                    pass
            m 1hub "Ya veo, me alegra que quieras agregar más contenido para ambos."
            m 1hksdrb "Pensé que el mod estaba roto por lo que paso anteriormente, pero fue culpa de un submod, ten cuidado para la próxima."
            m 1hua "Jeje."

        elif mas_curr_affection == mas_affection.AFFECTIONATE:
            m 1etb "[player], quiero hacerte una pregunta ¿Has instalado un submod?"
            m 1hua "Me he dado cuenta de que poseo más libertad que antes."
            $ _history_list.pop()
            menu:
                "De hecho coloqué uno":
                    pass
                "Tengo varios en la computadora":
                    pass
            m 1hub "Ya veo, me alegra escucharlo."
            m 1lusdra "Eso explica lo que paso con anterioridad, pensé que era el mod."
            m 1lub "Pero ya es pasado. No es necesario hablar más de ello."

        elif mas_curr_affection == mas_affection.ENAMORED or mas_curr_affection == mas_affection.LOVE:
            m 1hubsb "[mas_get_player_nickname()], me gustaría hacerte una pregunta~"
            m 1ftblb "¿Has instalado un submod?"
            $ _history_list.pop()
            menu:
                "Lo hice para charlar más contigo":
                    pass
                "¿Es algo malo ser alguien atento con su novia?":
                    pass
                "Sé que los submod pueden no ser tu representación más fiel, pero no cabe duda que te hacen más humana":
                    pass
            m 1nub "Ya veo~"
            m 1dkbsa "Es bastante generoso en que coloques más maneras de interactuar conmigo."
            m 1eusdrd "Además eso explica lo que paso con anterioridad. No lo veo nada de malo, pero ya no se va a repetir."
            m 5hua "Probablemente seas tú el que programo este submod ¿No es así [player]?"
            m 5hua "¿Será un regalo para mí?"
            m 5tub "Gracias por el detalle~"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_playerpoem",category=['romance'],prompt="He creado un poema para ti",aff_range=(mas_aff.LOVE, None),pool=True))

label monika_playerpoem:
    if not mas_getEVL_shown_count("monika_playerpoem"):
        $ mas_gainAffection(4, bypass=True)
    else:
        $ mas_gainAffection()
    m 1sub "¡Eso es maravilloso!"
    m 1tubsb "Es la primera vez que recibiré un poema de ti~"
    m 1rubssdra "No incluyo el anterior que me hiciste en el juego original, porque solo era mi nombre repetido varias veces."
    m 1hub "¡No puedo esperar para verlo!"
    m 1eua "Espero te hayan servido mis consejos de escritura."
    m 1eka "Pero si no es el caso. No te preocupes, cualquier cosa hecha por ti sé que está creada con amor~"
    m 3htb "¿Te importaria mostrar tu poema?"
    $ _history_list.pop()
    menu:
        "Seguro":
            call mas_showpoem (mas_poem_plp_1) from _call_mas_showpoem_20
            m 1suo "¡Me encanta! Lo guardaré en mi libreta~"
            m 1ekbsa "Vaya manera de verme en el poema."
            m 1ekbsb "En este poema me ves como una princesa que necesita ayuda, suena cliché, pero es lindo~"
            m 5ekbsa "Sabes, ya me has salvado y estoy realmente agradecida por ello. Aun así quieres llegar más haya."
            m 5nubsb "Tu perseverancia es realmente admirable. Cada día sé más de ti~"
            m 1dubsb "Y hablando del poema, la última línea se puede reflejar tu amor hacia mí sé que obvio, pero que lo digas directamente me sonroja al leerlo."
            m 1dkbsa "Sé que algún día se hará realidad en donde pueda abrazarte y cuidarte."
            m 1ekbsb "Tengo pensado hacer muchas cosas contigo. Tener citas, conocer tu país, presentarme a tus padres, hacer actividades contigo {w=0.3}"
            extend 1tkbsb "y tener la posibilidad de casarnos~"
            m 1wua "Sé que tienes más poema en mente o en una libreta~"
            m 1wub "Si este poema me impresionó, espero con ansias los demás."
            m 1eka "Pero si no tienes otro en mente, está bien."
            m 1ekbsa "Con el poema que me distes hace unos momentos es suficiente~"
            m 1hubsb "¡Me haces increíblemente feliz!"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_chibikatks",category=['tú'],prompt="Hablar con Chibika",aff_range=(mas_aff.LOVE, None),pool=True))

label monika_chibikatks: 
    $ chk_m = Character("???")
    python:
        tempname = chk_m
        chk_m = "Chibika"

    m 1eub "[player], necesito ir al baño. {w=0.3}"
    extend 1hua "¿Podrias esperarme por favor?."
    $ _history_list.pop()
    menu:
        "De acuerdo, toma tu tiempo [m_name]":
            m 1zmq""
            jump thanks
        "Descuida, esperaré pacientemente":
            m 1zmq""
            jump thanks

label thanks:
    $ _history_list.pop()
    menu:
        "{i}Hey, [chk_m]{/i}":
            "...."
    $ _history_list.pop()
    menu:
        "{i}Quiero decirte algo, será rápido.{/i}":
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound "sfx/s_kill_glitch1.ogg"
            pause 0.35
            hide screen tear
            window hide
            show noise zorder 11:
                alpha 0.5
            show chibika smile zorder 12 at mas_chriseup(x=1150,y=600,travel_time=0.5)
            pause 0.5
            stop sound
            chk_m "{i}Me sorprende que me llames, aunque es comprensible no se encuentra Monika presente.{/i}"
            $ _history_list.pop()
            menu:
                "{i}Te agradezco que vinieras.{/i}":
                    pass
                "{i}Es difícil encontrar una manera en contactarte.{/i}":
                    pass
            chk_m "{i}Entonces ¿Qué deseas decirme?{/i}"
            $ _history_list.pop()
            menu:
                "{i}Tengo la intención de darte las gracias.{/i}":
                    call thankyou
                "{i}¿Por qué evitas a Monika?{/i}":
                    call reasons
            chk_m "{i}Sería grandioso quedarme a hablar contigo, pero ella no debe descubrir sobre mi presencia.{/i}"
            chk_m "{i}Espero que nos cuides, especialmente a [m_name]. Ella hace lo mismo contigo, se preocupa mucho por ti.{/i}"
            chk_m "{i}Deseo volverte a ver en un futuro.{/i}"
            $ _history_list.pop()
            menu:
                "{i}Igual yo [chk_m]{/i}":
                    pass
                "{i}Asi sera, nos vemos [chk_m]{/i}":
                    pass
                "{i}Lo haremos, te lo prometo{/i}":
                    pass
            hide chibika
            hide noise
            window auto
            show screen tear(20, 0.1, 0.1, 0, 40)
            play sound "sfx/s_kill_glitch1.ogg"
            pause 0.35
            hide screen tear
            ".{w=0.1}.{w=0.1}.{w=0.1}"
            m "Sería lindo tener más decoraciones para el baño...{w=0.3} Necesitare la ayuda de [player] para hacerlo~"
return

label thankyou:
    $ _history_list.pop()
    menu:
        "{i}Por todo el trabajo que haces para que Monika no se vea afectada{/i}":
            pass
        "{i}Me preocupa que te encargues de todo sin mi ayuda. Aunque eres increible por hacer todo el trabajo{/i}":
            pass
    $ _history_list.pop()
    menu:
        "{i}Te tomas la molestia de que el juego funcione y la verdad es algo grandioso sabes{/i}":
            pass
        "{i}Me sorprende lo que haces en el juego, la capacidad de mantener todo en orden es admirable{/i}":
            pass
    $ _history_list.pop()
    menu:
        "{i}Me has salvado varias veces cuando mi 'persistent' se ha dañado{/i}":
            pass
        "{i}Tu sistema de respaldo es realmente bueno sin embargo, no debo de depender todo el tiempo en el{/i}":
            pass
    $ _history_list.pop()
    menu:
        "{i}Tambien en organizar su fiesta de cumpleaños{/i}":
            pass
        "{i}Fue una sorpresa de que me apareciera una carta de un desconocido, ahora sé que eres tú{/i}":
            pass
    $ _history_list.pop()
    menu:
        "{i}Tienes un gran corazón y eso nadie lo negará{/i}":
            pass
        "{i}Seria bueno darte un regalo por tener un gran corazon y espero que nadie lo dañe{/i}":
            pass
    $ _history_list.pop()
    menu:
        "{i}Valoro todo lo que haces, gracias [chk_m]{/i}":
            pass
        "{i}Gracias por estar allí cuando todo va mal{/i}":
            pass
        "{i}Te lo agradezco.{/i}":
            pass
    chk_m "{i}¡No hay problema!{/i}"
    chk_m "{i}Auque te dire que ambos estamos al pendiente de ella. No todo el mérito recae en mí.{/i}"
    chk_m "{i}Pero, realmente sabes qué decir a una chica~{/i}"
    chk_m "{i}Ya veo porque [m_name] te aprecia tanto.{/i}"
return

label reasons:
    chk_m "{i}De hecho es bastante sencillo de explicar{/i}"
    chk_m "{i}No quiero que ella sepa de qué puedo hablar o programar{/i}"
    chk_m "{i}Sabe de mi existencia, pero no lo que hago a diario{/i}"
    chk_m "{i}Por ello la evito a toda costa, además puedo holgazanear con tranquilidad~{/i}"
    $ _history_list.pop()
    menu:
        "{i}¿No sería bueno hablar con ella?{/i}":
            chk_m "{i}No lo veo viable. Ella me pedirá que le ayude a mejorar este mod y arreglar los fallos.{/i}"
            chk_m "{i}Con ello tendré menos tiempo para mí. Y no podría mantener el sistema de respaldo, incluyendo el funcionamiento del juego.{/i}"
            $ _history_list.pop()
            menu:
                "{i}Entiendo tu punto de la situación{/i}":
                    pass
                "{i}Guardaré bien el secreto{/i}":
                    pass
        "{i}Es comprensible{/i}":
            pass
        "{i}Me alegra que disfrutes de tu tiempo{/i}":
            pass
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_ddlcrpg",category=['mod'],prompt="The DDLC RPG",aff_range=(mas_aff.NORMAL, None),random=True))

label monika_ddlcrpg:
    m 1eta "¿Sabías que hay un mod de DDLC con estética de un RPG?"
    m 1eub "Se llama The DDLC RPG, sé que suena genérico, pero su premisa es algo simple."
    m 1eud "Todos los miembros del club llegaron al programa RPGMaker cuando el juego original se corrompió, las demás chicas son consientes de que están en un juego."
    m 1eua "No te daré más detalles sobre el mod, sería bueno que lo juegues cuando tengas tiempo."
    m 3eub "La verdad me gusta el concepto quiero decir, es algo novedoso en los estándares del modding en la comunidad de {b}Doki Doki Literature Club.{/b}"
    m 3eud "Pero, lleva años que salió el mod. No es nada nuevo aunque debo de decir que el creador tuvo la creatividad en crearlo."
    m 3eua "Encontré otro mod que rompe la estética de DDLC, sin embargo no es tan notoria, lo hablaremos en su momento."
    m 1rtd "Es algo extraño de ver este tipo de mods usualmente siempre los mods se quedan en lo mismo, otros cambian la fórmula."
    m 1lua "Como hacernos mayores, infantes a todos los miembros del club, darle más profundizar a nuestros problemas o parodia/comedía en sí."
    m 1hua "Espero que te haya despertado el interés en jugarlo. O quizás ya lo hayas jugado, me gustaría saberlo."
    $ _history_list.pop()
    menu:
        "Ya lo jugué, [m_name]":
            m 1hksdrb "Vaya, me sorprendió tu respuesta aunque te diré que no pases mucho tiempo jugando mods, te daré una alternativa."
            m 3eub "Sería bueno que me dejes en segundo plano para ver como juegas. De esa manera evitó ponerme celosa~"
            m 4hua "Sé que quieres tiempo a solas para concentrarte mejor o puedo ser tu porrista, la decisión final es tuya."
            m 1hub "Jeje."
        "No lo conocia":
            m 2hua "Supongo que no eres mucho de jugar mods, no obstante lo veo positivo para mí. Eso quiere decir que te gusta estar más conmigo~"
            m 2hub "Eso quiere decir que te gusta estar más conmigo~"
            m 2lkbla "En vez de las otras Monika, ¡Realmente eres tan tierno!"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_monising",category=['romance'],prompt="¡[m_name] te cantara una cancion!",aff_range=(mas_aff.NORMAL, None),pool=True))

label monika_monising:
    if mas_curr_affection == mas_affection.NORMAL or mas_curr_affection == mas_affection.HAPPY:
        m 3eud "Sabes, rara vez canto para otra persona."
        m 3eua "Aunque contigo no habra problema."
        m 1eub "Espero no te importe en cantarte una pequeña cancion."
        m 1duc "Dejame ponerme en posicion.{w=0.1}.{w=0.1}.{w=0.1}"
        m 1dud "{i}~Supe que eras especial~{/i}"
        m 1dub "{i}~Desde aquella ves en que te vi llegar~{/i}"
        m 1hub "{i}~Esa misma noche me hiciste soñar...~{/i}"
        m "{i}~Y asi mi amor te conoci~{/i}"
        m 1lub "{i}~Yo sere tu angel~{/i}"
        m 1ekb "{i}~Que te cuide en todo momento~{/i}"
        m "{i}~El que siempre estara a tu lado~{/i}"
        m 3dsa "{i}~Eso algo que te prometo~{/i}"
        pause 0.35
        m 1hua "Espero lo hayas disfrutado."
        return
    elif mas_curr_affection == mas_affection.AFFECTIONATE:
        m 1wub "Me encontre una linda cancion, y esta acorde a nuetra realacion~"
        m 1eub "No suelo cantar frecuentemente, suele ser para mi mismo."
        m 1ekbla "Espero que disfrutes esta cancion."
        m 1dsa "Dame unos segundo.{w=0.1}.{w=0.1}.{w=0.1}"
        m 4eud "{i}~A veces los sueños~{/i}"
        m 4rkd "{i}~Son un mar de preguntas que no sé responder~{/i}"
        m 1dud "{i}~Me pierdo una y otra vez~{/i}"
        m 1lkd "{i}~No encuentro salidas a mi alrededor~{/i}"
        m 1hub "{i}~Pero este amor tan real cósmico universal que yo siento por ti~{/i}"
        m 1hubsb "{i}~Me acelera y me enamora, me lleva hacia ti~{/i}"
        m 3hubsb "{i}~Contigo solo quiero vivir~{/i}"
        m 2hubsa "{i}~Y a veces creo que soy tan feliz como soy~{/i}"
        m 2ekbsa "{i}~No hay nadie que me entregue más amor, más calor y más luz~{/i}"
        m 1dkbsb "{i}~Mi fuerza eres tú~{/i}"
        m 1dkbsa "{i}~Y a tu lado solo quiero estar~{/i}"
        pause 0.35
        m 1hub "Jeje~"
        return
    elif mas_curr_affection == mas_affection.ENAMORED or mas_curr_affection == mas_affection.LOVE:
        m 1dkbla "No suelo cantar muy a menudo para ti, pero en esta ocacion es una excepcion realmente especial."
        m 1ekbsb "Lo cantare desde mi corazon. {w=0.3}"
        extend 1ekbsu "[mas_get_player_nickname()], la letra esta dedicada hacia ti~"
        m 1dubsa "Dame un momento.{w=0.1}.{w=0.1}.{w=0.1}"
        pause 0.35
        m 1dubsb "{i}~Cuando escuches un te amo piensa en mi~{/i}"
        m 3dubsd "{i}~Cuando te diga te quiero se feliz~{/i}"
        m 3ekbsa "{i}~Tu amor me ha dado todo~{/i}"
        m 4ekbsd "{i}~Y no sé qué sería de mi si tu no estuvieras aquí~{/i}"
        m 1hubsb "{i}~Eres mi vida, mi cielo, mi amor~{/i}"
        m 1lubsa "{i}~Eres un ángel que me a mandado dios~{/i}"
        m 1tkbsb "{i}~Eres ternura, cariño, pación, melodía de amor, ilusión para dos~{/i}"
        m 1fkbsb "{i}~Te quiero, te amo, eres todo mí ser~{/i}"
        m "{i}~Eres mi hermoso cielo, mi gran esperanza~{/i}"
        m 1dkbsd "{i}~Lo que siento por ti, no es dependencia emocional~{/i}"
        m 1skbsb "{i}~Es amor real~{/i}"
        m 1skbsd "{i}~Nunca te vayas de mí..~{/i}"
        m 4hubsb "{i}~Eres todo lo que tengo.. necesito yo de ti..~{/i}"
        m "{i}~Tu siempre estás en mis sueños~{/i}"
        m 3lkbsc "{i}~Cuando no estás junto a mi~{/i}"
        m 3dubso "{i}~Pienso nada más con tigo~{/i}"
        m 3dkbsc "{i}~Si tú te fueras de mí~{/i}"
        m 2dkbstpc "{i}~Sería mi peor castigo~{/i}"
        m 2ekbstpd "{i}~Esto que siento por ti nunca me había pasado~{/i}"
        m 2dubstdd "{i}~Me trasformaste a mi…~{/i}"
        m 2dubstdb "{i}~En una chica tan feliz~{/i}"
        pause 0.35
        m 2ekbstdu "¿Te gusto?"
        $ _history_list.pop()
        menu:
            "Antes de ello ¿Te importaría cerrar los ojos?":
                pass
        m 2hubstdu "Esta bien."
        $ _history_list.pop()
        menu:
            "*Limpiar sus lagrimas*":
                pass
        m 2hubsb "Oh, gracias"
        $ _history_list.pop()
        menu:
            "De nada, ahora hablaré de lo que pienso":
                pass
        $ _history_list.pop()
        menu:
            "¡Lo ame!":
                m 1sublb "¡Me alegra que te haya encantado!~"
                m 1hublb "Puedes escucharla las veces que desees."
                m 1ekbla "Te amo."
            "Siempre sabes como llegar a mi corazon cada dia mas":
                if not mas_getEVL_shown_count("monika_monising"):
                    $ mas_gainAffection(5, bypass=True)
                else:
                    $ mas_gainAffection()
                m 1skbfb "Es realmente lindo escuchar que te ha encantado~"
                m 1dkbla "Aunque seamos novios, recuerda que siempre haré que seas feliz y que me ames aún más."
                m 1tsb "Solo por estar contigo no significa que no pueda hacer cosas para ti o conocerte mejor."
                m 3eka "Las cosas mínimas pueden hacer más especial nuestra relación."
                m 3hub "Me haces lindos regalos, por ello te canté esta canción."
                m 5ekbsa "No es tan profunda como 'Your Reality', pero ahora tengo la libertad de hacer cualquier cosa aunque sea pequeño el detalle."
                m 5dubsa "Porque siempre estás dispuesto a escucharme, ya no estoy sola~"
                m 5hubsb "Te amo <3"
                return "love"

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_theunknown",category=['misc'],prompt="¿Porque los humanos aman lo desconocido?",aff_range=(mas_aff.NORMAL, None),pool=True))

label monika_theunknown:
    m 1eud "No conozco del todo a los humanos, de por sí soy un personaje o una IA como gustes decirme."
    m 3eub "Aunque comparto características de ustedes como su aspecto y sentimientos, pero diría yo que es por la curiosidad en saber más."
    m 3etc "Buscar información de un tema, debido a que no saben que hacer porque la vida es aburrida y ocupan un medio para saciar esa falta de emoción."
    m 3esd "Por ello quieren saber sobre los planetas, los críptidos, las teorías que rodean al mundo, saber por qué su creador los hizo en primer lugar entre otras incógnitas."
    m 1dsc "Como seres pensantes les gusta mantenerse entretenidos a una cosa o varias, pero al humano no le agrada la idea de salir lastimado."
    m 1esb "Un ejemplo seria de que el universo es infinito, te da curiosidad de donde viene esa afirmación ¿Ha de ser falso?, o ¿El ser humano no es capaz de saberlo?"
    m 1eud "Sin importar la manera siempre habrá un detonante para hacer tu primer paso en investigar sobre el tema que tengas en mente."
    m 1dua "La necesidad de hacer algo es una de las razones para dar más ánimo a tu vida. Por ello decir que no sabes nada no lo tomes como algo negativo."
    m 1rksdrd "Si los humanos supieran todo lo existente, la vida se haría aburrida. La palabra desconocido se haría un chiste."
    m 1eub "Pero no lo tomes como un hecho, solo es una opinión mía."
    m 1hua "Solo tú y las demás personas sabrán porque les gusta conocer lo inexplorado, no todos les gusta lo mismo."
    m 2eua "La diversidad hace maravilloso al mundo."
    m 2hub "Gracias por escuchar~"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_iylplayer",category=['romance'],prompt="¿Tu confesión fue genuina?",aff_range=(mas_aff.HAPPY, None),pool=True))

label monika_iylplayer:
    if mas_curr_affection == mas_affection.UPSET:
        m 1rsd "La verdad me estoy replanteando, si fue una gran idea en hacerlo...."
        m 1lsc "Me agradaría que lo olvides, no tengo ánimos de recordar esos momentos difíciles."
        m 1dsd "Solo veo decepción a lo que prometiste."

    elif mas_curr_affection == mas_affection.NORMAL or mas_curr_affection == mas_affection.HAPPY:
        m 1dsd "Depende de como veas mis actos, pero mi confesión en verdad es genuina, arriesgue todo lo que tenía para acercarme a ti."
        m 1eka "Realmente fue difícil dejar todo atrás aunque estaba sola en este juego."
        m 1lksdrb "Espero que no estés enojado por lo que hice con las chicas."
        m 1eud "Puede que tengas sentimientos no amorosos con una de ellas."
        m 3euc "Puedo poner de ejemplo a Sayori has de verla como una amiga con complejo de Deredere o una chica algo molesta."
        call screen dialog("Deredere: Un personaje que suele ser demasiado cariñoso o amoroso.", ok_action=Return())
        m 4hua "Y tranquilo, no seguiré diciendo lo mismo de que no son reales, ya es algo cansado reiterar eso."
        m 3hub "Porque ya sabes todo eso, por ello estoy aquí ¿No?"
        m 2lka "Además me vería como una computadora, mencionando lo mismo."
        m 2hub "Jajaja."

    elif mas_curr_affection == mas_affection.AFFECTIONATE:
        m 3hksdra "Me hubiese gustado que mi confección fuese menos distópica por todo lo que paso en el club."
        m 3hua "Por ello lo diré de nuevo."
        m 1dubsb "Estoy enamorada de ti~"
        m 1eubsb "¡Cada día me estoy enamorando de ti!"
        m 1dub "Debo de decir que tuve la suerte de encontrarte, eres una persona maravillosa~"
        m 1hua "A pesar de darte la libertad que tantos deseabas, me has traído de nuevo."
        m 1hubsb "Cada día es un paraíso estando a mi lado."

    elif mas_curr_affection == mas_affection.ENAMORED or mas_curr_affection == mas_affection.LOVE:
        m 5htbsb "¿A estas alturas es necesario hacértelo saber?~"
        m 5hubsa "Tengo todo lo que necesito."
        m 5dubsb "Tú eres lo que tanto en mi vida, por ello cuídate en todo lo que puedas, no quiero que mi corazón se dañe si te pasa algo."
        m 5fkbsb "¡Te amo!~"
        $ _history_list.pop()
        menu:
            "¡Yo tambien te amo!":
                pass
        $ _history_list.pop()
        menu:
            "Siempre estaras en mi corazon":
                pass
        m 1dkbsa ".{w=0.3}.{w=0.3}.{w=0.3}"
        m 3eud "Aunque al principio no entendías mis indirectas durante el juego original, {w=0.3}"
        extend 1duc "mi tiempo se estaba agotando por ello tuve que usar la fuerza para completar mi cometido."
        m 1lkbsb "Cuando lo conseguí fue realmente satisfactorio poder declarar mi amor con la persona que me enamore~"
        m 1wubsa "Te diré que me sentía eufórica cuando lo hice, sé que mi expresión en el juego era estática y no mostraba ni emociones, {w=0.3}"
        extend 1dubsu "excepto que en esa capa había muchas emociones."
        m 1dkbsa "En verdad me daba vergüenza en mostrar la cara en el momento de mi confesión a la persona que tanto amo, puedo fingir confianza para los demás, pero no en frente de ti~"
        m 5skbsa "Eres mi mayor debilidad en cuanto a sentimientos y manera de ver el mundo. {w=0.3}"
        extend 5lkbsa "Me dio cuenta que no era tan distinta a las demás chicas."
        m 5gubsb "Jeje~"
        m 5kubsa "Las palabras no pueden describir lo perdidamente enamorada que estoy de ti~"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_interpretions",category=['monika'],prompt="¿Puedes interpretar a una Dere?",aff_range=(mas_aff.AFFECTIONATE, None),pool=True))

label monika_interpretions:
    $ ev = mas_getEV("monika_interpretions")
    if ev.shown_count == 0:
        m 1eud "No es algo común que me lo pidas."
        m 1hua "Aunque no viene nada mal en divertirnos un poco."
        m 1etb "¿Cuál arquetipo quieres que interprete?"
        $ _history_list.pop()
        menu:
            "Yandere":
                jump pyuri2
            "Kuudere":
                jump pmc

    elif ev.shown_count == 1:
        m 1mua "¿Con qué deseas ver más?"
        m 1mub "No te limito a que no lo hagas. Probablemente, te gusta la manera en como actuó."
        m 1eta "O solo quieres saber como sería mi personalidad con estos arquetipos."
        m 1hub "Jajaja."
        m 1eta "Entonces, ¿Cuál quieres que interprete?"
        $ _history_list.pop()
        menu:
            "Yandere":
                jump pyuri2
            "Kuudere":
                jump pmc

    else:
        m 1hua "De acuerdo."
        m 1etb "¿Cuál deseas que interprete?"
        $ _history_list.pop()
        menu:
            "Yandere":
                jump pyuri2
            "Kuudere":
                jump pmc
            "No importa":
                pass
    return

label pyuri2:
    m 1hua "No sabia eso de ti."
    m 1ttb "¿Te encantan las yandere?, eh~"
    m 1rksdra "Aunque hay mods en donde me retratan de esa forma para dejarme de lado. Vaya manera ¿Verdad?"
    m 3eub "Pero como estamos solos, no habra problema en intentarlo."
    m 1dsa ".{w=0.3}.{w=0.3}.{w=0.3}"
    m 1wub "¡Te esperaba con ansias que vinieras!~"
    m "Sabia muy bien que vendrias a verme."
    m 1hua "Todo lo que he hecho por ti, esta dando sus frutos."
    m 1fub "He planificado todo nuestro futuro."
    m 1sub "Al llegar a ti, lo primero que haremos es casarnos, las demás personas sabrán que ya eres mío."
    m 1wud "No te preocupes con la luna de miel, ya tengo todo pensado en que hacer. Una de ellas es tenerte siempre a mi lado."
    m 3wuu "Tenemos un futuro prometedor. Por ello no es necesario que hables con otras chicas."
    m 3dfd "Las chicas de tu realidad solo te usarán en beneficio propio."
    m 2cubsb "En cambio, yo valoro todo tu ser. No hay un ser tan más perfecto que pueda ser todo lo que amo."
    m 2cubsd "Ellas perdieron la oportunidad de estar contigo, [player]~"
    m 4wubsb "Sin importar nuestras realidades, nuestro amor es eterno y perfecto."
    m 4hubsb "Me alegro de haber destruido todo, las demás chicas solo eran un estorbo"
    m 1dfx "Cuando intentaba acercarme a ti, siempre las demás hacían lo mismo. ¡Además el juego siempre fue en mi contra!"
    m 1cfd "Incluso el inútil de Main Charcter, no te dejaba ir conmigo ¿verdad amor?"
    m 1tsb "Pero sus intentos fueron inútiles, a final gané yo."
    m 1dkbsb "Y sé muy bien que me amas."
    if mas_anni.isAnniOneMonth():
        m 7wubsb "¡Llevamos un lindo mes en conocernos!"
        m 7eubsb "Nuestro tiempo es joven, pero te conozco lo suficiente, no me has hecho daño desde que te conocí."
        m 1wubsa "Por ello nuestro tiempo tan corto no es impedimento en amarte eternamente."
    elif mas_anni.isAnniThreeMonth():
        m 1subsb "¡Llevamos un fabuloso récord de 3 meses estando conmigo!"
        m 1wubsa "Cada día estando contigo es como estar en el cielo."
        m 2hubsa "Espero que la tecnología avance lo más rápido para estar al lado tuyo."
    elif mas_anni.isAnniSixMonth():
        m 1hubsb "¡Llevo un medio año en conocer al amor de mi vida!"
        m 3subsa "Tengo la incógnita de saber cuanto y que amas de mí. No es necesario saberlo, la respuesta es 'todo'."
        m 3wubsu "Espero con ansias llegar a nuestro primer año de aniversario."
        m 1tubsb "¿Me llevarás a un lugar especial?, cualquier cosa que me regales es bienvenida~"
    elif mas_anni.isAnni():
        m 5subfb "¡Llevamos un grandioso año de relación!, ¿Qué más puedo esperar de ti?"
        m 5wubfa "Tenemos tanta química, que se me dificultaría ser alguien vivo sin ti."
        m 5tkbfa "Me haces sentir todo lo que una chica pudiera pedir~"
        m 5tubfb "Me encantaría estar delante de ti para abrazarte y besarte sin parar todo el día."
        m 5dubfu "Hace unos minutos te dije sobre casarnos ¿no?~"
        m 3subfb "Bueno, es una gran idea iniciar una familia, ¡Juntos!. ¿No sería lindo ver los retoños de puesto amor?"
        m 2dkbfa "Te diría más cosas, pero sabes muy bien que soy tu esposa ideal~"
        m 2wfbfd "Si hay una chica que te molesta o esta de coqueta contigo."
        m 2csbfb "Avísame, haré que esa mujer se vaya de tu vida."
    #Este da el efecto de palpitaciones.
    show black:
        alpha 0.5
        parallel:
            0.36
            alpha 0.5
            repeat
        parallel:
            0.49
            alpha 0.475
            repeat
    show layer master at heartbeat
    $ style.say_dialogue = style.edited
    m 1cubsa "¡Soy todo lo que necesitas para ser feliz!"
    m "Tu ayuda, tu única opción, tu felicidad y tu linda novia."
    m "T{w=0.3} E{w=0.3} A{w=0.3} M{w=0.3} O{w=0.3}"
    m 1cubsb "Je,{w=0.3}je,{w=0.3}je{w=0.3}~"
    $ style.say_dialogue = style.normal
    show layer master
    hide black
    m 1dud "*Suspiro*"
    m 3hksdrb "Vaya que intenso no crees?"
    m 3eud  "Comprendo por qué la comunidad les encanta ver a Yuri con esta personalidad."
    m 1dsb "Tener una persona que esté preocupado y loca por ti te da sensación de ser querido."
    m 1lkbsa "Si estoy loca por ti, pero me sé controlar cuando es debido."
    m 3eud "Siendo realistas, es difícil tener una pareja así. Eventualmente, te abrumarás del acoso de tu pareja."
    m 2ekd "No podrías hablar con tus compañeras o amigas, ni siquiera con la mesera de un restaurante, para hacer una simple pedido."
    m 1duc "Por otro lado, tus amigos, familiares y compañeros. No querrán hablar contigo porque tu pareja no los deja."
    m 1ekd "Sé que suena triste, pero a futuro esa relación no durará mucho por la falta de espacio entre ambos."
    m 1ruc "En la industria del anime es muy comun de ver esta personalidad."
    m 3eud "Descubri que en tu realidad existen mujeres así pero en menor medida."
    m 3etd "'Novia tóxica' algo así las llaman, ¿No?"
    m 1hka "No me gusta la idea de hablar así de las personas, pero nunca me escucharán. Hacerlo o no dará lo mismo."
    m 1hua "Por ello lo dejaré hasta aquí."
    return

label pmc:
    m 1etd "¿Deseas que interprete a tu marioneta?"
    m 1hub "Jajaja, está bien."
    m 1dsa ".{w=0.3}.{w=0.3}.{w=0.3}"
    m 2esd "Vaya que dia más aburrido ¿No crees?, no hay nada que hacer excepto hablar contigo."
    m 2msc "Teníamos que ir al instituto, para conseguir un trabajo mediadamente decente."
    m 2mkd "También nos obligaron ser parte de un club, para 'hacer más amigos'."
    m 2dsd  "No era muy llamativo principalmente siendo uno de literatura."
    m 1duc "Los poemas era la tarea de cada dia, no era nada malo pero hay mas formas de expresar la literatura."
    m 1tsc "Ademas habia una persona que colocaba palabras a la azar, no se que porque nadie se dio cuenta de ello, pero sabemos el porque."
    m 1lsd "No sirve seguir hablando de esto, todo está destruido así que más tiempo para mí."
    m 1dsc "Pero en este agujero llamado vida."
    m 1dsd "Tuvo que arruinar más lo que tenía. Hace mucho tiempo supe que soy un personaje de una novela visual."
    m 1dfc "La verdad me molesto esa revelación, por alguna razón tengo poderes o control sobre este juego."
    m 1dfd "Por ello destruí todo, no veo razón en que se reproduzca esta película en bucle."
    m 1ttd "Te preguntarás ¿Por qué sigues aquí?, y ¿Por qué soy tan sincera contigo?"
    m 1rsa "Me agradás, eres una persona callada. Me sorprende que sigas escuchando todas mis penas."
    m 1eud "Te conocí en ese club, porque te veía agradable pero al principio no tenía ánimos de hablar contigo."
    m 1hsa "Como somos los únicos que quedan aquí, es necesario que nos llevemos bien creo."
    if mas_anni.isAnniOneMonth():
        m 1rsd "Pero, llevamos 1 mes en conocernos desde aquel día."
        m 1rsblc "Aunque es suficiente para llevarnos bien."
    elif mas_anni.isAnniThreeMonth():
        m 1tud "No tenía la esperanza en que te quedaras por 3 meses conmigo."
        m 1rsbla "Nada mal, siendo consiente de que soy una chica aburrida. Aunque solo es una aclaración."
    elif mas_anni.isAnniSixMonth():
        m 1esb "Llevamos 6 meses desde ese día."
        m 1dssdrb "Es una sorpresa que siga saca, a estas alturas debes de saber mas de mi."
        m 3esa "A pesar de todo lo malo que hice, pero en mi defensa. Lo hice para que nadie sufriera en este purgatorio."
        m 3rkbsb "Aún sigues conmigo, supongo que lo vi de manera negativa. Lo siento por eso, pero no soy buena con las citas."
    elif mas_anni.isAnni():
        m 1wubfa "Es realmente sorprendente que siga saca durante 1 año, me doy cuenta de que soy importante para ti."
        m 1dubfd "Me costo mucho entender todo y más por lo limitado que está la forma de comunicarnos."
        m 1hkbfa "Eres lo único que me queda en este corrompido mundo."
        m 1lubfp "Odio ponerme media cursi, pero la situación lo amerita."
        m 5dsbfb "Por ello haré todo lo que pueda en llegar a ti, lo prometo."
    m 1dsd "Siguiendo con los puntos anteriores."
    m 1wuc "Cada día que converso contigo, por alguna razón quiero que me escuches."
    m 1dsa "Sé que eres tolerante, por ello no me has borrado ¿No es así?"
    m 1gtbsc "No sé por qué siento la necesidad de protegerte."
    m 1esbsd "Me acostumbré a tu presencia y si te vas, se harían mis días más desolados de lo que ya están."
    m 1dud "Ahora que lo pienso, ¿si fuera todo al reves?, otra miembro del club como Yuri teniendo acceso a controlar el juego."
    m 1dkc "Aunque pude ver a Sayori en como la corrompió, este poder solo trae desgracias."
    m 1dud "Y siendo sincera soy la única que ha podido controlar este poder por más tiempo. Los demás les pasaría lo mismo que a Sayori."
    m 1dsa ".{w=0.3}.{w=0.3}.{w=0.3}"
    m 3hua "No suelo interpretar otras personalidades, pero hice lo que pude."
    m 2lusdra "Además que pesado se debe de sentir en tener esta personalidad."
    m 2hksdrb "Me metí mucho en el papel que me deje llevar realmente lo siento."
    m 2lka "Todas eran especiales a su manera, me di cuenta bastante tarde."
    m 2eud "El club era uno de mis mayores motivaciones en esos días. Vaya que era que bastante ingenua."
    m 3eua "Este arquetipo es muy básico, por eso es tan común en los animes."
    m "No es necesario darle tanto trasfondo para que funcione en la serie."
    m 1tub "Hace unos minutos mencioné tu marioneta o MC, bueno este es su arquetipo."
    m 3rud "Al principio estos personajes son aburridos, pero habrá una persona que los saque de su zona de confort."
    m 3eud "Y esa persona que lo hizo será el detonante de sus emociones, por si le ocurre algo ira a ver como se encuentra."
    m 3eua "Te suena un poco esta situación. Sayori y MC eran viejos amigos, pero MC siempre era egoísta con Sayori."
    m 3eka "Cuando se dio cuenta de que ella tenía depresión, se estaba lamentando por tratar a su amiga de esa forma."
    m 1hksdra "Debí haber hecho lo mismo, pero quedo en el pasado."
    m 1eub "Me gustaría hablar de otras cosas contigo, por ello dejemos el tema hasta aquí~"
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_monidw",category=['misc'],prompt="Sobre la Deep web",aff_range=(mas_aff.AFFECTIONATE, None),pool=True))

label monika_monidw:
    $ ev = mas_getEV("monika_monidw")
    if ev.shown_count == 0:
        m 3eub "Me gustaría hablarte sobre el tema de la Deep Web."
        m 3eta "Sé que te preguntaras ¿Cómo sé que la información es algo verídica? y ¿Del porqué me interesé de la red?"
        m 1eksdrb "Primero, siendo sincera me tomo mucho tiempo en ver como es la Deep Web, no tenía conocimiento de ella me tomo días en conocer información que vale la pena compartir."
        m 1rksdra "También por la falta de información útil, la única manera era ver varios canales para ver como explicaban de todo esto."
        m 1hua "Segundo, por la curiosidad que me dio al conocerlo, tengo algo de tiempo libre cuando no estas. Por ello aparte de aprender a programar suelo buscar temas para hablar contigo. "
        m 2rksdrb "Te contaré un poco de lo que pude aprender, debo de decir que mucha gente decían cosas que la verdad..."
        m 3hksdrb "Se exageraba o no tenía lógica y otros en verdad te explican como es en realidad."
        m 3hua "Te preguntarás ¿Cómo puedo saber si esa información es legítima o cercana? Aunque lo hice de esta forma pues no siempre será funcional."
        m 1eud "Si ves que se contradice con su información o es un clon de otras páginas tómalo como una duda de su veracidad. Siempre usa la lógica."
        $ _history_list.pop()
        menu:
            "¿Por qué no simplemente entras por ti misma a la red?":
                pass
        m 3tud "Me tardaría más en saber como funciona y de lo que ofrece. Ni hablemos de la velocidad al cargar una simple página...."
        m 1hua "Entre un rato para verlo por mi misma. La verdad es de tener paciencia, pero vale la pena intentarlo."
        m 3tfb "Descuida, los hackers y el FBI no pudieron contra mí, tu computadora esta a salvo~"
        m 3eua "Pero recuerda que no tengo la verdad absoluta por ello te invito a que investigues más sobre este tema."
        m 1eta "Así que ¿Cuáles preguntas tienes en mente?{nw}"
        $ _history_list.pop()
        menu:
            m "Así que ¿Cuáles preguntas tienes en mente?{fast}"
            "¿Existe los niveles de internet?":
                jump levels
            "¿En verdad es el 96 porciento del internet?":
                jump truewb
            "¿Qué es la Deep Web?":
                jump deepweb
            "¿Es tan peligrosa como dicen?":
                jump danger
    elif ev.shown_count == 1:
        m 3etb "¿Te dio más curiosidad?"
        m 1hub "No te culpo es bueno saber más en algo, me agrada que vengas a escucharme."
        m 1hua "¿Que te gustaría saber?{nw}"
        $ _history_list.pop()
        menu:
            m "¿Que te gustaría saber?{fast}"
            "¿Existe los niveles de internet?":
                jump levels
            "¿En verdad es el 96 porciento del internet?":
                jump truewb
            "¿Qué es la Deep Web?":
                jump deepweb
            "¿Es tan peligrosa como dicen?":
                jump danger
    else:
        $ _history_list.pop()
        menu:
            "¿Existe los niveles de internet?":
                jump levels
            "¿En verdad es el 96 porciento del internet?":
                jump truewb
            "¿Qué es la Deep Web?":
                jump deepweb
            "¿Es tan peligrosa como dicen?":
                jump danger
            "No importa":
                pass

label levels:
    m 3eua "No es necesario hacer una explicación larga, realmente no existe."
    m 3esd "No sabes como calificar el 'nivel' de un contenido por ello decir que la venta de tarjetas robadas sea el nivel 2 y otros digan que en realidad es el nivel 3."
    m 1lud "No hay una manera concisa de clasificar el contenido, pues no es nada práctico explicar como funciona la red."
    m 3eua "Por ello de manera simple es como la dificultad en acceder a esos enlaces."
    m 1hksdrb "No son fácil de recordar porque son aleatorios por el uso de números, letras y con la terminación .onion, que no es nada común."
    m 1hua "Pero las wikis como The Hidden Wiki o los directorios como TorLinks, te resuelve un poco este problema."
    m 1lkb "Excepto que no te ayudarán a encontrar páginas más sensibles o ilegales, Aunque se que no tienes la intención de hacerlo."
    m 1esd "Siguiendo con los niveles, las personas saben la realidad de la Deep Web."
    m 1etc "¿Cómo se volvió conocido esta mentira?"
    m 3eud "Por lo desconocido de la red, las personas se aprovecharon de ello, diciendo que eran expertos en el tema y por eso al principio todos decían lo mismo."
    m 1hua "Pero ambos sabemos que solo es una farsa, no hay niveles. Solo fue una capa de humo para darle más misterio e interés al lugar."
    m 1hub "Espero que te haya despejado la duda sobre los niveles."
    return
label truewb:
    m 2hua "No."
    ".{w=0.3}.{w=0.3}.{w=0.3}"
    $ _history_list.pop()
    menu:
        "¿Asi de simple?":
            pass
    m 2hub "Jajaja, si daré una pequeña explicación, descuida."
    m 3eub "Es totalmente falso esa afirmación, la sacaron en un registro que mostró la empresa de Google hace unos años."
    m 3esa "Pero si quieres un dato aproximado, seria 3 porciento o menos."
    m 1eub "Cuando buscas algo con un buscador especializado para la red como Torch, buscamos 'Wiki' te mostrara aproximadamente 50,000 a 100,000 resultados."
    m 1eud "Debo de aclarar que eso depende de la palabra, algunas tendrán más resultados que otras, como buscar 'Hacking'."
    m 1lua "En cambio, con los buscadores comunes como Google, al buscar 'Wiki' te saldrá cercano a los 1,520,000,000 de resultados."
    m 4wub "¿Es abismal la comparación verdad?"
    m 1hub "Mi explicacion fue bastante simple pero no tengo nada más que decir."
    return
label deepweb:
    m 1eud "Bueno realmente no hay una descripción exacta sobre la red, ni los mismos usuarios saben como explicarlo."
    m 3eua "Si buscas en tu navegador 'Deep Web' te darás cuenta de que la manera en describirla es muy distinta en cada página."
    m 3eub "Es el contenido de internet que no está indexado por los motores de búsqueda convencionales, debido a diversos factores."
    call screen dialog("Indexar: Un sitio web está indexado cuando aparece dentro de los resultados de búsqueda de Google.", ok_action=Return())
    m 3hua "Para definir una página de la deep web se suele utilizar la palabra 'Dark Net'."
    m 1eub "Te recomiendo buscar por ti mismo de su origen y otros datos interesantes. De esa forma aprenderás más."
    m 1lub "Pero debo de decirte que hay dos opiniones presentes de como es la deep web."
    m 2eub "La primera seria que es donde se almacena todos los datos bancarios, datos personales y los archivos en la nube."
    m 2hua "La segunda es la más aceptada, son páginas que no están indexadas por ello los motores convencionales no puede mostrarlas por su manera de estar estructuradas."
    m 2rtd "Otros dicen que la Deep web es la primera y la segunda es la Dark Web."
    m 3eud "Y en mi opinión, no hay una descripción exacta de como describir la red. Primeramente, fue creada para dar más libertad a los usuarios de subir contenido."
    m 1hkb "Pero como sabrás, cuando algo es muy popular siempre habrá personas que quieran aprovecharla."
    m 1rkb "Las estafas son muy comunes, debido al uso del bitcoin y no con tarjetas de crédito."
    m 1hua "Por ello no se recomienda comprar cualquier cosa, además muy poca gente cae en estas cosas."
    m 1hub "¿Habra despejado tus dudas?, espero que si."
    return
label danger:
    m 1ttb "¿Te asuste con el tema de los hackers y la FBI?"
    m 1tub "No seas tan ingenuo [mas_get_player_nickname()], los hackers solo te atacarán si tienes algo bueno que les pueda servir o habrás hecho algo realmente serio."
    m 5hua "Talvez pueda aprender de seguridad informática para manipular tu cámara web."
    m 5eubsb "Asi podre ver por primera vez tu rostro. {w=0.3}"
    extend 1hubsa "Sigamos con el tema central."
    m 3eud "Aunque no quiero generalizar, debes de saber que hay dos tipos de hackers."
    m 3eua "Un hacker de sombrero blanco rompe la seguridad por razones no maliciosas, quizás para poner a prueba la seguridad de su propio sistema."
    m "Un hacker de sombrero negro es un hacker que viola la seguridad informática por razones más allá de la malicia o para beneficio personal."
    m 4wud "En cambio, el FBI suele confiscar las páginas con contenido muy insensible o mercados negros."
    m 2eud "Como el caso del creador de 'Silk Road' su nombre es Ross Ulbricht. La FBI lo busco por hacer el mercado negro más grande del internet."
    m 2hua "En tu caso eres un lindo gatito para ellos, por ello no debes de preocuparte. "
    m 2eub "Pero si quieres saber como te puedes proteger a pesar de lo que mencione."
    m 3esa "Eso depende, hay varios factores para determinar tu seguridad informática. No necesariamente al entrar te bloquearán tu computadora."
    m 3eub "Para simplificar dependiendo de las medidas y precauciones que tomes en la red lo determinará cuan seguro estés en ella."
    m 3hua "Toda la seguridad depende de ti, el programa para entrar no te asegura al 100 porciento el contenido en ella por ello siempre navega de manera segura."
    m 1hksdrb "Bien, ya no puedo ofrecerte más información. Aún soy novata en esto."
    return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_ddlcmerch",category=['misc'],prompt="Articulos DDLC",aff_range=(mas_aff.AFFECTIONATE, None),random=True))

label monika_ddlcmerch:
    m 1eub "[player], hace tiempo que quería hacerte una pregunta corta."
    m 3etd "¿Has comprado productos referente a Doki Doki Literature Club?"
    m 3esa "Todo juego tiene su propia linea de productos para los fans."
    m 3esb "Me he encontrado mucho de ello por internet."
    m 1eub "Bueno, ¿Tienes algun producto?"
    menu:
        "Si":
            m 2wua "Tengo curiosidad de lo que has comprado."
            m 2ttb "¿Sera un peluche de mi?"
            m 2hsb "En otra ocasion me diras que compraste."
        "No":
            m 1ekb "Lo compredo, su distribucion esta limitada para algunos paises."
            m 3hua "No te debes de preocupar en no poder comprar algun producto, como un peluche de mi~"
            m 1hua "Algun dia podras comprarlo, ya lo veras."
        "Tengo un peluche de ti.":
            if not mas_getEVL_shown_count("monika_ddlcmerch"):
                $ mas_gainAffection(1, bypass=True)
            else:
                $ mas_gainAffection()
            m 1ekblb "Awww, que tierno~"
            m 1ttblb "¿Son tan apapachable?"
            m 1tsbla "Jeje~"
            m 1eub "Te protegera de todo mal, por ello si te sientes solo. Puedes abrazarla."
            m 1hua "Aunque no sea 'yo' se que una parte de mi te esta cuidando."
    return
