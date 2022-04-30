define count = 0
define counttwo = 0
define countthree = 0

init:
    image tester_idle = im.Scale("mod_assets/other/transparent.png", 30, 30)
    image tester2_idle = im.Scale("mod_assets/other/transparent.png", 120, 60)

init python:
    
    def HKBPHideButtons():
        if mas_HKBPIsVisible():
            config.overlay_screens.remove("extraplus_overlay")
            renpy.hide_screen("extraplus_overlay")

    def HKBPShowButtons():
        if not mas_HKBPIsVisible():
            config.overlay_screens.append("extraplus_overlay")

    def mas_HKBPIsVisible():
        """
        RETURNS: True if teh Hotkey buttons are visible, False otherwise
        """
        return "extraplus_overlay" in config.overlay_screens

init python:

    Zer0fixer = "¿Que haces aqui?"
    Zer0fixer = "Espero te sirva algo de mi pequeño trabajo."
    Zer0fixer = "Esta es una version demo, por ello esta tan acortada."
    HKBPShowButtons()

screen extraplus_overlay():
    zorder 50
    style_prefix "hkb"

    vbox:
        xpos 0.05

        yanchor 1.0
        ypos 50

                #Inactivo / Lo hice de esta forma para evitar tocar codigo base del mod.
        if store.mas_hotkeys.talk_enabled == False:
            text _("")
                #Lo oculta en el Calendario
        elif store.hkb_button.talk_enabled == False:
            text _("")
                #Activo
        else:
            if mas_curr_affection == mas_affection.UPSET or mas_curr_affection == mas_affection.DISTRESSED or mas_curr_affection == mas_affection.BROKEN:
                textbutton _("Extra+")
            else:
                textbutton _("Extra+") action Jump("show_extraplus")

label show_exp:
    $ expression_m = renpy.random.randint(1,5)
    if expression_m == 1:
        $ expression_num = 1
        show monika 1esa

    elif expression_m == 2:
        $ expression_num = 1
        show monika 1tuu

    elif expression_m == 3:
        $ expression_num = 1
        show monika 1nua

    elif expression_m == 4:
        $ expression_num = 2
        show monika 1eua

    elif expression_m == 5:
        $ expression_num = 2
        show monika 1rublp
    call screen interaccionesbeta
    return

label show_extraplus:
    $ mas_temp_zoom_level = store.mas_sprites.zoom_level
    call monika_zoom_transition_reset (1.5) from _call_monika_zoom_transition_reset_9
    $ mas_RaiseShield_core()
    $ expression_m = renpy.random.randint(1,5)
    if expression_m == 1:
        $ expression_num = 1
        show monika 1esa

    elif expression_m == 2:
        $ expression_num = 1
        show monika 1tuu

    elif expression_m == 3:
        $ expression_num = 1
        show monika 1nua

    elif expression_m == 4:
        $ expression_num = 2
        show monika 1eua

    elif expression_m == 5:
        $ expression_num = 2
        show monika 1rublp
    call screen interaccionesbeta
    return
        
screen interaccionesbeta():
    zorder 50
    style_prefix "hkb"

    vbox:
        xpos 0.05

        yanchor 1.0
        ypos 170

        textbutton _("Cerrar") action Jump("back_mas")

        textbutton _("Cita") action Jump("date_mas")

        textbutton _("Minijuego") action Jump("monika_minigames")

        textbutton _("Adiciones") action Jump("tools_mas")

    #Cabeza
    imagebutton:
        idle "tester2_idle"
        xpos 580
        ypos 12
        action Jump("monika_headpatbeta")
    #Nariz
    imagebutton:
        idle "tester_idle"
        xpos 620
        ypos 235
        action Jump("monika_boopbeta")
    #Mejillas
    imagebutton:
        idle "tester_idle"
        xpos 700
        ypos 256
        action Jump("monika_cheeksbeta")
    imagebutton:
        idle "tester_idle"
        xpos 550
        ypos 256
        action Jump("monika_cheeksbeta")

#Solo labels
label monika_boopbeta:
    $ count += 1
    hide screen interaccionesbeta
    if count == 1:
        m 1tsb "Que haces jugando con mi nariz, Beta tester.{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.35
        hide screen tear
        m 1hub "Que haces jugando con mi nariz, [player].{fast}"
        m 1hksdrb "No es que moleste, ¡simplemente me tomo por sorpresa!"
        m 1hua "Jeje~"
    else:
        m 1hub "*Boop*"
    jump show_exp
    return

label monika_cheeksbeta:
    $ counttwo += 1
    hide screen interaccionesbeta
    if counttwo == 1:
        m 2wubsd "Eh, senti pellizcon en la mejilla"
        m 2lksdrb "Oh, fue tu cursor, vaya susto."
        m 2ttb "Pero, ¿Que estas tramando [player]?"
        m "¿Querias molestrame un rato?"
        m 1hubla "O te gusta verme sonrojada~"
    else:
        m 2fua "Jeje~"
        m 2hua "Seria bueno devolvértelo, pero me es imposible hacerlo."
    jump show_exp
    return

label monika_headpatbeta:
    $ countthree += 1
    hide screen interaccionesbeta
    if countthree == 1:
        m 6subsa "¡Me estas acariciando el cabello!"
        m 6eubsb "Es realmente{w=0.3} reconfortante."
        m 6dkbsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}"
        m 1eubsb "Gracias [player]~"
    else:
        m 6dubsa ".{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}"
        m 7hubsb "Espero que no te canses de hacerlo a diario~"
    jump show_exp
    return

label date_mas:
    hide screen interaccionesbeta
    call screen dialog("Lo siento, aun esta en planeacion.", ok_action=Return())
    call screen interaccionesbeta
    return

label back_mas:
    hide screen interaccionesbeta
    $ mas_DropShield_core()
    jump ch30_loop
    return
    
label github_submod:
    $ renpy.run(OpenURL('https://github.com/zer0fixer/SubmodMAS'))
    call screen interaccionesbeta
    return
    
label aff_log:
    "Tu afecto con [m_name] es de [store._mas_getAffection()]."
    call screen interaccionesbeta
    return

label monika_minigames:
    hide screen interaccionesbeta
    menu:
        "Shell Game":
            call screen dialog("Esta en desarrollo.", ok_action=Return())
            call screen interaccionesbeta
    return

label tools_mas:
    hide screen interaccionesbeta
    call screen dialog("Se ha recorado esta parte para evitar spoilers, aunque no son la gran cosa creeme.", ok_action=Return())
    menu:
        "Repositorio Github del creador":
            jump github_submod
        "Ver afecto":
            jump aff_log
        "No importa":
            call screen interaccionesbeta
    return