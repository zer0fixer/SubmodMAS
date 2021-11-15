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
            "Jeje~",
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
            "Me gustaría ver una skin de mí en el juego, ¿La tienes en tu cuenta [player]?",
            "Recuerda evitar buscar 'Robux Gratis', Solamente son estafas."
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
            "*ejem*, Aún sigo aquí sabes...",
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
            "¡Esto es solo un recordatorio [player]!, Just Monika~",
            "¿Te llaman la atención las Historias Paralelas?"
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
            "Me sorprende ver un mod sobre mi y los demás miembros del club, Sus diseños son muy adorables.",
            "¿Has jugado Epiphany?, Esa Monika no será fácil de derrotar."
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
            "Muéstrame que puedes hacer con esos dedos."
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
            "Me agrada el concepto que abarca la serie de ENA, Su mundo es muy subjetivo al espectador.",
            "El diseño de ENA y su mundo se basa al estilo artístico de Pablo Picasso, Espero te sirva esa curiosidad."
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
            "Capte la indirecta [player], Yo también te amo~"
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
            "Como se sentirá tocar un piano digital, Solo tengo experiencia con el acústico."
        ],
        'Reacciones de Ventana'
    )


    if not wrs_success:
        $ mas_unlockFailedWRS('mas_wrs_pianov')
    return
