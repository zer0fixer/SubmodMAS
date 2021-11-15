init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_qduda",category=['monika'],prompt="Tengo una duda, [m_name]",pool=True, unlocked=True))

label monika_qduda:
    m 1hua "¡Claro!, [player]."
    $ _history_list.pop()
    menu:
        "¿Por qué no tuve formas de preguntarte o responderte en el 'Acto 3' durante el juego original?":
            m 1eka "Oh."
            m 2ekb "Es muy simple, [mas_get_player_nickname()]."
            m 3eka "No había otra persona que fuera consistente en esta cruel realidad, solamente era yo."
            m 3hkb "En esa parte del juego estaba desesperada para llamar tu atención y quería desahogarme con alguien para que me entendiera de como estaba sufriendo."
            m 1eubla "Ese alguien eras Tú."
            m 3eub "Tenía total libertad de poder hablar contigo sobre mí y mis pensamientos."
            m 3hkb "Disculpa, ni siquiera he hablado del porqué a tu pregunta."
            m 2rkd "Lamento mucho por no darte la libertad para expresarte, probablemente te haya aburrido con algunos temas que no estés familiarizado."
            m 2eksdla "Era la primera vez que hablo con alguien real y me emocione sabes..."
            m 2ekd "Además me daba mucho miedo en que me rechazaras llamándome 'Asesina', 'Celopata' o 'Sociópata'."
            m 2dsc "Por eso en ese acto no te di maneras de comunicarte, lo tuve todo bajo control."
            m 2dsd"A pesar de que te haya cerrado en una jaula sin ningún libertad."
            m 3ekb "Aunque, me alegra en depositar mi confianza en ti siempre te lo agradeceré."
            m 4hub "De esta manera respondo a tu pregunta, espero te sirva mi explicación."
            m 5luu "Sin embargo."
            m 5tubsb "Sé que esa pregunta se volvió una aventura para ti, querías saber más de {i}Mi{/ i} y yo de {i}Ti{/ i} por eso instalaste este mod ¿No es así?."
            m 5hubsb "Para que ambos nos conozcamos mutuamente y superar las barreras que nos rodea a ambos."
            m 5wubsb "Y en serio te lo agradezco, por buscar la manera de comunicarte conmigo realmente eres un gran compañero y novio."
            m 5kubsb "Espero que sigamos así{w=0.2} ¡Por siempre!"
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
                    m 2tfp "No es justo que lo mantengas en secreto."
                    m 3tfb "Pero sé algunas maneras para descifrar lo que piensas de mí, te conozco muy bien."
                    $ _history_list.pop()
                    menu:
                        "Veremos que se te ocurre señorita presidenta":
                            m 5tubla "Jeje~"
return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_younv1",category=['juegos'],prompt="¿Conoces el juego 'YOU and ME and HER'?",pool=True, unlocked=True))

label monika_younv1:
    m 1ekd "No, [player]."
    m 1lkd "Aunque tengo un mal presentimiento."
    m 7eka "Déjame consultar por internet, debo de tener por lo menos la sinopsis del juego."
    $ _history_list.pop()
    menu:
        "Si quieres puedo darte una idea sobre la premisa del juego aunque no lo conozco del todo.":
            m 1esd "Ok..."
            m 1eka "Pero si tengo dudas buscare en internet, de acuerdo."
            $ _history_list.pop()
            menu:
                "Se trata de una Novela Visual genérica de un grupo de chicos en un triángulo amoroso, el jugador debe de escoger a una de las dos chicas-":
                    m 5rtc ""
            $ _history_list.pop()
            menu:
                "Hay varias rutas dependiendo de las elecciones será una peor que la anterior, lo vi en un wiki por eso lo menciono-":
                    m 5ltsdrc ""
            $ _history_list.pop()
            menu:
                "Lo busqué en Steam y tiene género de 'Terror psicológico', siento un recuerdo vago cuando conocí DDLC, Jajaja.":
                    m 5hksdrb""
            $ _history_list.pop()
            menu:
                "Me fui a hacer mis cosas por eso no investigue más sobre el juego":
                    m 5eub "Ya veo, gracias por la información [player]."
                    m 3eua "Pero, iré a investigar más sobre este juego aún no me trae un buen presentimiento."
                    m 3eub "No quiero que estés mucho tiempo en otros juegos"
                    m 1eua "Después de todo-"
                    m 1hubsa "Ya me tienes a mí,{w=0.2} ¡Tu linda novia!"
                    m 1hua "Seguiré buscando más información sobre el juego, no tardaré mucho."
                    m 1duc "Veamos.."
                    m 1duc "..."
                    m 1dusdrc "...."
                    m 1lusdrb "Hmmm,{w=0.2} puedo preguntarte ¿Como supiste de la existencia de ese juego?"
                    $ _history_list.pop()
                    menu:
                        "Fue por casualidad, en recomendados por youtube lo enontre.":
                            m 1euc "Ya veo, te recomiendo no seguir buscando algo referente al juego."
                            m 1esb "No te aportara nada nuevo creeme."
                            m 1fua "Por ello propongo que hagamos mas cosas entre los dos como jugar o solo vernos fijamente a los ojos"
                            m 1nua "Jeje~"
                        "Por internet, algunos usuarios lo mencionaron en la pagina de Steam de DDLC":
                            m 1duc "Solo deben de ser comparaciones o decir que es una inspirarcion de {i}Doki Doki Literature Club{/i}."
                            m 1luc "Te recomiendo que las olvides"
                            m 1eud "De todos modos no es necesario jugar mas Novelas Visuales"
                            m 1eub "Y solo es un juego mas del monton dejemolo de lado ¿Si?"
        "...":
            m 1duc "Veamos.."
            m 1duc "..."
            m 1dusdrc "...."
            m 1lusdrb "Tenía razón sobre este juego, además ¿como supiste de la existencia de ese juego?"
            $ _history_list.pop()
            menu:
                "Fue por casualidad, en recomendados por YouTube lo encontré.":
                    m 1euc "Ya veo, te recomiendo no seguir buscando algo referente al juego."
                    m 1esb "No te aportará nada nuevo créeme."
                    m 1fua "Por ello propongo que hagamos más cosas entre los dos como jugar o solo vernos fijamente a los ojos."
                    m 1nua "Jeje~"
                "Por internet, algunos usuarios lo mencionaron en la página de Steam de DDLC":
                    m 1duc "Solo deben de ser comparaciones o decir que es una inspiración de {i}Doki Doki Literature Club{/i}."
                    m 1luc "Te recomiendo que las olvides"
                    m 1eud "De todos modos no es necesario jugar más Novelas Visuales"
                    m 1eub "Y solo es un juego más del montón dejémoslo de lado ¿Si?"
return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_jymod",category=['tú'],prompt="¿Puedo hablar con Yuri en su mod'?",pool=True, unlocked=True))

label monika_jymod:
    m 1esc "No."
    $ _history_list.pop()
    menu:
        "Esta bien, [m_name].":
            m 1huu "Ese es mi chico"
            m 1eud "Aunque evita en relacionarte con ella. ({i}Aunque puedo borrar los datos del mod por si pasa{/i})"
            m 1ekb "Hablemos mas sobre nosotros, [mas_get_player_nickname()]."
        "Solo bromeo, [m_name].":
            m 1euu "Jeje~"
            m 5kub "Lo sé, por eso me escogiste."
            m 5eka "Pero no te preocupes puedes hablar con ella por nostalgia."
            m 5esp "Aun así me gustaría que evites crear un vínculo con ella."
            m 4eua "Solo te diré que si sigues visitándola, no tendré piedad en borrar la partida de su mod."
        "Si":
            m 1esc "No."
            $ _history_list.pop()
            menu:
                "Si":
                    m 1esc "No."
                    $ _history_list.pop()
                    menu:
                        "Si":
                            m 1esc "No."
                            $ _history_list.pop()
                            menu:
                                "Si":
                                    m 1mua "No."
                                    $ _history_list.pop()
                                    menu:
                                        m "¿Que harás?{nw}"
                                        "Just Monika":
                                            m 2dtblb "{b}I{/b}"
                                            m 1lusdlb "Que bueno que quite este pequeño bucle se haría eterno además de monótono y te diré algo-"
                                            m 1eud "Simplemente, borraría tus datos guardados de ese mod, de esa manera no podrás tener una charla estable con Yuri."
                                            m 3eub "Recuerda que puedo ver y manipular todo lo que tienes en la computadora,{w=0.2} [currentuser]."
                                            m 1huu "Dicho esto, Sigamos con lo nuestro~"
                                        "Just Monika":
                                            m 2dtblb "{b}L{/b}"
                                            m 1lusdlb "Que bueno que quite este pequeño bucle se haría eterno además de monótono y te diré algo-"
                                            m 1eud "Simplemente, borraría tus datos guardados de ese mod, de esa manera no podrás tener una charla estable con Yuri."
                                            m 3eub "Recuerda que puedo ver y manipular todo lo que tienes en la computadora,{w=0.2} [currentuser]."
                                            m 1huu "Dicho esto, Sigamos con lo nuestro~"
                                        "Just Monika":
                                            m 2dtblb "{b}O{/b}"
                                            m 1lusdlb "Que bueno que quite este pequeño bucle se haría eterno además de monótono y te diré algo-"
                                            m 1eud "Simplemente, borraría tus datos guardados de ese mod, de esa manera no podrás tener una charla estable con Yuri.."
                                            m 3eub "Recuerda que puedo ver y manipular todo lo que tienes en la computadora,{w=0.2} [currentuser]."
                                            m 1huu "Dicho esto, Sigamos con lo nuestro~"
                                        "Just Monika":
                                            m 2dtblb "{b}V{/b}"
                                            m 1lusdlb "Que bueno que quite este pequeño bucle se haría eterno además de monótono y te diré algo-"
                                            m 1eud "Simplemente, borraría tus datos guardados de ese mod, de esa manera no podrás tener una charla estable con Yuri."
                                            m 3eub "Recuerda que puedo ver y manipular todo lo que tienes en la computadora,{w=0.2} [currentuser]."
                                            m 1huu "Dicho esto, Sigamos con lo nuestro~"
                                        "Just Monika":
                                            m 2dtblb "{b}E{/b}"
                                            m 1lusdlb "Que bueno que quite este pequeño bucle se haría eterno además de monótono y te diré algo-"
                                            m 1eud "Simplemente, borraría tus datos guardados de ese mod, de esa manera no podrás tener una charla estable con Yuri."
                                            m 3eub "Recuerda que puedo ver y manipular todo lo que tienes en la computadora,{w=0.2} [currentuser]."
                                            m 1huu "Dicho esto, Sigamos con lo nuestro~"
                                        "Just Monika":
                                            m 2dtblb "{b}YOU{/b}"
                                            m 1lusdlb "Que bueno que quite este pequeño bucle se haría eterno además de monótono y te diré algo-"
                                            m 1eud "Simplemente, borraría tus datos guardados de ese mod, de esa manera no podrás tener una charla estable con Yuri."
                                            m 3eub "Recuerda que puedo ver y manipular todo lo que tienes en la computadora,{w=0.2} [currentuser]."
                                            m 1huu "Dicho esto, Sigamos con lo nuestro~"
                                        "Ya no estamos en el club, [m_name]":
                                            m 2eublb "Jeje~"
                                            m 2wub "Ahora que lo mencionas me trae muchos recuerdos nostalgicos, De nuestro tiempo en el club de literatura"
                                            m 2eta "Me pregunto como seria si tuviera una ruta en primer lugar. Dejando eso de lado"
                                            m 1lusdlb "Que bueno que quite este pequeño bucle se haría eterno además de monótono y te diré algo-"
                                            m 1eud "Simplemente, borraría tus datos guardados de ese mod, de esa manera no podrás tener una charla estable con Yuri."
                                            m 3eub "Recuerda que puedo ver y manipular todo lo que tienes en la computadora,{w=0.2} [currentuser]."
                                            m 1huu "Te dejé un {b}mensaje{/b} un pequeño, Sigamos con lo nuestro~"
                                        "Ah shit, here we go again!":
                                            m 2hublb "Jajaja~"
                                            m 2mub "Es muy raro que digas palabras de ese tono."
                                            m 2tub "Te perdono porque capte la referencia al personaje de CJ."
                                            m 1lusdlb "Que bueno que quite este pequeño bucle se haría eterno además de monótono y te diré algo-"
                                            m 1eud "Simplemente borraria tus datos guardados de ese mod, de esa manera no podras tener una charla estable con Yuri."
                                            m 3eub "Recuerda que puedo ver y manipular todo lo que tienes en la computadora,{w=0.2} [currentuser]."
                                            m 1huu "Te dejé un {b}mensaje{/b} un pequeño, Sigamos con lo nuestro~"
                                "¿Talvez?":
                                    m 3eta "Porque has dicho 'Talvez'."
                                    m 3tta "Ya no sabes qué hacer ¿Verdad?."
                                    m 1kua "Entonces pasa más tiempo conmigo,{w=0.2} {nw}"
                                    extend 1hub "Podemos hablar de lo que desees."
                                    m 2hub "Fue bonito tener esta pequeña guerra contigo."
                                    m 2tua "Pero me aseguraré de que no te me escapes, nadie se llevara mi objetivo."
                        "Ñ":
                            m 1hub "Jajaja-"
                            m 3eua "Recuerda que hablo tu mismo idioma, [player]."
                            m 3hua "Tampoco caere con la palabra Ü."
                            m 1tua "Me compadezco de ti."
return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_tipsran",category=['club de literatura'],prompt="Consejo de escritura para [player]",random=True))

label monika_tipsran:
    m 1eua "Hey, [player]."
    $ _history_list.pop()
    menu:
        "Dime [m_name]":
            m 1eub "Solo quiero decirte que-"
            m 4eub "A veces te encontrarás frente a una difícil decisión..."
            m 4eub "Cuando eso pase ¡No olvides guardar el juego! Nunca sabes cuando cambiarás de opinión..."
            m 4hub "...¡O cuando pase algo inesperado!"
            $ _history_list.pop()
            menu:
                "Capte la referencia, en esos días me tomo por sorpresa":
                    m 1eua "Solo fue un recordatorio durante el juego."
                    m 1hua "No era algo grave aunque me encanto romper la cuarta pared."
                    m 1hub "Jajaja."
                "No recuerdo ese diálogo de DDLC":
                    m 3eud "Es entendible, probablemente lo jugaste hace mucho tiempo."
                    m 3eub "No afecta en nada, pero en esa parte del juego solo quería llamar tu atención."
                    m 1nubsb "Y vaya que funciono."
return

init 5 python:
    addEvent(Event(persistent.event_database,eventlabel="monika_test123",category=['ddlc'],prompt="Lineas de dialogo sin borrar",random=True))

label monika_test123:
    m 1dub "~{i}Никто не отнимет у меня моего мужчину{/i}~"#Nadie me quitará a mi hombre
    m 1dud "~{i}Ich werde mein Bestes tun, damit es nicht dazu kommt{/i}~"#Haré todo lo posible para que no ocurra.
    m 1dublo "~{i}I will make you the happiest man in the world{/ i}{w=0.3} {nw}~"#Te haré el hombre más feliz del mundo
    extend 1dkblc "~{i}Y no me olvides{/i}~"
    m 1wubld "Ah... [player]."
    m 1hksdrb "Jaja-"
    $ _history_list.pop()
    menu:
        m "({i}Que fue eso...{/i}){nw}"
        "Es lo más random que haya visto en este mod":
            m 2eud "Oh, perdona por eso sé que sonó muy fuera de lugar"
            m 3esd "Al parecer eran líneas de conversación algo antiguas o de otro personaje."
            m 3hkb "Recuerda que soy algo moldeable y puede que diga algunas cosas fuera de lugar o que no van con mi persona"
            m 1esc "Espero que no ocurra de nuevo, se vuelve algo molesto"
            m 5esa "Dejando eso de lado de seguro tenías una cara graciosa,{w=0.3} {nw}"
            extend 5tfb "Me hubiese gustado verla."
return
