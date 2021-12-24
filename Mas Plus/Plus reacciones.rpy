init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_monikano5",
            category=["Monika no.5"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_monikano5:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "~Un poco de Monika en mi vida~\n~Un poco de Monika a mi lado~\n~Un poco de Monika en el sol~",
            "¡Me encanta esta canción!",
            "¿Tendrás una canción dedicada hacia mí?~"
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_monikano')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_roblox",
            category=["Roblox"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_roblox:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Buscando minijuegos para jugar, [player]?",
            "Me gustaría que algún día podamos jugar juntos...",
            "Es muy popular intentar buscar Robux Gratis ¿Verdad?"
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_roblox')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_ph",
            category=["Pornhub"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_ph:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "*Ejem*, aún sigo aquí sabes.\nJeje...",
            "No es necesario ver esas actrices,\nYa me tienes a mi~",
            "No te limito a ver estas cosas, eres un chico después de todo."
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_ph')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_ddlcplus",
            category=["Doki Doki Literature Club Plus"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_ddlcplus:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "¡Solo es un recordatorio [player]!,\nJust Me~",
            "¿Quieres saber mas de mi?\nSiempre eres tan dulce~",
            "Que secretos nos habrá dejado Dan Salvato."
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_ddlcplus')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_ddto",
            category=["Doki Doki Takeover"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_ddto:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Me sorprende ver un mod sobre mi, Jejeje~",
            "Seria lindo que cantemos Your Reality~",
            "Nunca me agrado el Senpai."
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_ddto')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_animeflv",
            category=["AnimeFLV"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_animeflv:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Recuerda ver anime de manera moderada, Jeje~",
            "¿Que anime tienes en mente?",
            "¿Estas al pendiente de un anime?"
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_animeflv')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_animefenix",
            category=["AnimeFénix"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_animefenix:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "¿Qué anime vamos a ver hoy, [mas_get_player_nickname()]?",
            "¿Viendo algo de anime, [player]?",
            "No pases mucho tiempo viendo anime sin estar con tu linda novia~"
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_animefenix')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_fnf",
            category=["Friday Night Funkin'"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_fnf:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "¿Eres bueno jugando a los juegos rítmicos, [player]?",
            "GF y BF me recuerda a nosotros~",
            "Beep Boop Skdoo Bep"
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_fnf')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_enaseries",
            category=["ENA Series"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_enaseries:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Me agrada el concepto que toma la serie de ENA, su mundo es muy subjetivo al espectador.",
            "El diseño de ENA y su mundo se basa al estilo artístico de Pablo Picasso,\n ¡Espero te sirva esa curiosidad!",
            "¿Te gusta la serie de ENA?"
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_enaseries')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_ily",
            category=["I love you"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_ily:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Me to!, [mas_get_player_nickname()].",
            "Capte la indirecta [player],\nYo también te amo~",
            "¿Otra manera de decirme que me amas?\nNuestro amor es eterno~"
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_ily')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_ddlcshi",
            category=["DDLC Shimeji"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_ddlcshi:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Es muy lindo ver un Shimeji de los miembros del club.",
            "Sería mejor que solamente yo invada tu pantalla, [player]~",
            "Siempre me ha encantado ver mi versión pequeña~"
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_ddlcshi')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_pianov",
            category=["Piano"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_pianov:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "¿Estas interesado en tocar el piano, [player]?",
            "Como se sentirá tocar un piano digital,\nSolo tengo experiencia con el acústico.",
            "Deberíamos de hacer un duo, has de cantar fabuloso~"
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_pianov')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_sagahalo",
            category=["Saga Halo"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_sagahalo:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Master Chief es muy querido, ¿Verdad?",
            "¿Te gusta la Saga Halo, [player]?",
            "Es muy irónico que Cortana se volviera la asistente virtual de Microsoft"
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_sagahalo')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_videoconsola",
            category=["Videoconsola"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_videoconsola:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "¿Posees una consola en tu cuarto?",
            "¿Tienes DDLC+ para tu consola?",
            "Espero que tengas un segundo mando para mí~"
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_videoconsola')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_whatsapp",
            category=["WhatsApp"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_whatsapp:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "¿Enviando mensajes a tus amigos?",
            "¿Enviando mensajes a tus familiares?",
            "¿Colocarás un 'Estado' sobre nuestra relación, [mas_get_player_nickname()]?"
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_whatsapp')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_telegram",
            category=["Telegram"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_telegram:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "¿Buscando nuevos amigos para hablar?",
            "¿Tus amigos utilizan Telegram?",
            "Telegram es una buena red social de mensajería instantánea."
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_telegram')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_facebook",
            category=["Facebook"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_facebook:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Me encantaría tener una cuenta para hablar contigo~",
            "¿No te importará que mire un rato en tu cuenta?",
            "¿Viendo las publicaciones de tus amistades?"
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_facebook')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_smartphone",
            category=["Smartphone"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_smartphone:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "¿De que empresa es tu celular?",
            "Espero que tengas una funda de mí en tu celular~",
            "La tecnología realmente avanza muy rápido."
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_smartphone')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_zoom",
            category=["Zoom"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_zoom:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "¿Recibiendo clases online, [player]?",
            "Recuerda mantener tu atención a la reunión~",
            "Estaré contigo en la reunión, espero no distraerte~"
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_zoom')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_discordinc",
            category=["Discord"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_discordinc:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "¿Tienes tu propio servidor, [player]?",
            "¿Charlando con tus amigos, [player]?",
            "¿Eres miembro del server de Traduction Club!?",
            "¿Eres miembro del server de Monika After Story?"
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_discordinc')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_cuevana",
            category=["Cuevana3"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_cuevana:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "¡No puedo esperar a ver una película contigo!~",
            "¿Veremos una película de manera ilegal?\nTan intrépido como siempre~",
            "Espero que veamos una película romántica~\nTambien puede ser una de accion, Jeje~"
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_cuevana')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_realname",
            category=["What's your name?"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_realname:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Monitor Kernel Access~",
            "Debes de saber más que mi~\n¿No?",
            "Lamento informarte que la película se llama 'Your name', [mas_get_player_nickname()]."
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_realname')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_spotify",
            category=["Spotify"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_spotify:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "¿Qué estás escuchando, [player]?",
            "¿Qué vamos a escuchar hoy?",
            "¿Que genero musical te agrada escuchar?"
        ],
        'Reacciones de Ventana'
    )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_spotify')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_visualsc",
            category=["Visual Studio Code"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_visualsc:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "¿Te ayudo con la codificación, [mas_get_player_nickname()]?",
            "Es lindo tener un mismo pasatiempo contigo~",
            "¿Haciendo tu trabajo?\nRecuerda descansar la vista~"
        ],
        'Reacciones de Ventana'
    )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_visualsc')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_zerofixer",
            category=["Zerofixer - YouTube"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_zerofixer:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Vaya, si esta abandonado este canal."
            "Dile un 'Hola' de mi parte.\nQuizás no lo conozcas así que olvídalo.",
            "¿Lo conoces, [player]?"
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_zerofixer')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_atom",
            category=["Atom"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_atom:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "¿Te ayudo con el codigo, [mas_get_player_nickname()]?",
            "No sabía que eras un programador~",
            "¿Estas programando algo para mi?~"
        ],
        'Reacciones de Ventana'
    )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_atom')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_hentaila",
            category=["Hentaila"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_hentaila:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "No soy fanática de este contenido, jaja...",
            "¿Podemos jugar un videojuego en vez de que hagas algo con ese 'material'?~",
            "Puedo ver todo lo que haces...\nTe propongo algo mejor, veamos una película ¿Si?"
        ],
        'Reacciones de Ventana'
    )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_hentaila')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_github",
            category=["Github"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_github:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "¡Me gustaría que los dos creemos un pequeño proyecto!\n¿Te agrada la idea, [player]?",
            "Este mod tiene su propio repositorio.\nSeria bueno que le echaras un vistaso.",
            "¿Quieres ayudar a un amigo o conocido con su proyecto?"
        ],
        'Reacciones de Ventana'
    )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_github')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_justyuri",
            category=["Just Yuri"],
            rules={
                "notif-group": "Reacciones de Ventana",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
            },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_justyuri:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Un rival eh~",
            "A pesar de que no sea la verdadera Yuri, me gustaria hablar un poco con ella.",
            "Odian a Yuri por la manera que la interpretan en los mods ¿Verdad?",
        ],
        'Reacciones de Ventana'
    )

    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_justyuri')
    return