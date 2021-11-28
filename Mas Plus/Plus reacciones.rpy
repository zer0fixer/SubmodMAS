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
            "~A little bit of Monika in my life\n~.~A little bit of Monika by my side\n~.Jeje~",
            "¿Podrías aumentar el volumen [mas_get_player_nickname()]?, ¡Me encanta esta canción!"
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
            "Probablemente exista una skin de mí,\n ¿Tienes una en tu cuenta [player]?",
            "Recuerda evitar buscar Robux Gratis,\n Solamente son estafas."
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
            "*ejem*, aún sigo aquí sabes...",
            "¿Podrías por favor ver estas cosas en privado?"
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
            "¡Solo es un recordatorio [player]!,\n Just Monika~",
            "¿Te llaman la atención las 'Historias Paralelas'?"
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
            "Me sorprende ver un mod sobre mi y los demás miembros del club,\n Sus diseños son muy adorables.",
            "¿Has jugado Epiphany? Esa Monika no será fácil de derrotar."
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
            category=["animeflv"],
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
            "Recuerda ver anime de manera moderada, Jeje~"
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
            category=["animefenix"],
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
            "¿Que anime se te ocurre ver hoy [mas_get_player_nickname()]?"
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
            "¿Eres bueno jugando a los juegos rítmicos [player]?",
            "Podrías mostrarme que puedes hacer con esos dedos."
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
            category=["ENA"],
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
            "Me agrada el concepto que abarca la serie de ENA, su mundo es muy subjetivo al espectador.",
            "El diseño de ENA y su mundo se basa al estilo artístico de Pablo Picasso,\n ¡Espero te sirva esa curiosidad!"
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
            "Capte la indirecta [player],\n Yo también te amo~"
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
            "Sería mejor que solamente yo invada tu pantalla, [player]~"
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
            "¿Estas interesado en tocar el piano [player]?",
            "Como se sentirá tocar un piano digital,\n Solo tengo experiencia con el acústico."
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
            eventlabel="mas_wrs_halo",
            category=["Halo"],
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

label mas_wrs_halo:
    $ wrs_success = mas_display_notif(
        m_name,
        [
            "Master Chief es muy querido, ¿Verdad?",
            "¿Te gusta la saga Halo [player]?"
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_halo')
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
            "¿Posees una videoconsola en tu cuarto?",
            "¿Tienes DDLC+ para tu videoconsola?"
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
            "¿Enviando mensajes a tus tus amigos?",
            "¿Enviando mensajes a tus familiares?",
            "¿Colocarás un 'Estado' sobre nuestra relación, [player]?"
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
            "¿Tus amigos utilizan Telegram?"
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
            "¿No te importará que mire un rato en tu cuenta?"
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
            "¿De que empresa es tu teléfono inteligente?",
            "Espero que tengas una funda de mí en tu celular~"
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_smartphone')
    return