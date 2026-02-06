# ═══════════════════════════════════════════════════════════════════════════════
#                    GUI PREMIUM - CTRL+ALT+DELETE
#                    Polices & Menu Améliorés
# ═══════════════════════════════════════════════════════════════════════════════

init -2:
    
    # === POLICES DM SERIF TEXT (ACTIVÉES) ===
    
    # Police principale pour les dialogues
    define gui.text_font = "fonts/DMSerifText-Regular.ttf"
    
    # Police pour les noms des personnages
    define gui.name_text_font = "fonts/DMSerifText-Regular.ttf"
    
    # Police pour l'interface (menus, boutons)
    define gui.interface_text_font = "fonts/DMSerifText-Regular.ttf"
    
    # Police pour le titre du jeu
    define gui.title_text_font = "fonts/DMSerifText-Regular.ttf"
    
    # === TAILLES DE POLICE ===
    define gui.text_size = 24
    define gui.name_text_size = 28
    define gui.interface_text_size = 26
    define gui.title_text_size = 75
    define gui.label_text_size = 30
    define gui.notify_text_size = 20
    
    # === COULEURS ===
    define gui.accent_color = "#00ffff"
    define gui.idle_color = "#888888"
    define gui.idle_small_color = "#aaaaaa"
    define gui.hover_color = "#ffffff"
    define gui.selected_color = "#00ffff"
    define gui.insensitive_color = "#444444"
    define gui.muted_color = "#666666"
    define gui.hover_muted_color = "#999999"
    define gui.text_color = "#ffffff"
    define gui.choice_idle_color = "#00ffff"
    define gui.choice_hover_color = "#ffffff"

# ═══════════════════════════════════════════════════════════════════════════════
#                         TRANSFORMS POUR ANIMATIONS
# ═══════════════════════════════════════════════════════════════════════════════

transform menu_title_appear:
    alpha 0.0
    yoffset -50
    easein 1.5 alpha 1.0 yoffset 0

transform menu_subtitle_appear:
    alpha 0.0
    pause 0.5
    easein 1.0 alpha 1.0

transform menu_button_appear(delay=0):
    alpha 0.0
    xoffset -30
    pause delay
    easein 0.5 alpha 1.0 xoffset 0

transform menu_button_hover:
    on hover:
        easein 0.2 xoffset 10
    on idle:
        easeout 0.2 xoffset 0

transform glitch_title:
    parallel:
        xoffset 0
        linear 0.1 xoffset 2
        linear 0.05 xoffset -2
        linear 0.1 xoffset 0
        pause 3.0
        repeat
    parallel:
        alpha 1.0
        pause 4.0
        linear 0.02 alpha 0.7
        linear 0.02 alpha 1.0
        repeat

transform scanline_move:
    yoffset 0
    linear 2.0 yoffset 1080
    yoffset 0
    repeat

transform pulse_glow:
    alpha 0.3
    easein 2.0 alpha 0.6
    easeout 2.0 alpha 0.3
    repeat

# Style des boutons du menu
style menu_button:
    xalign 0.5
    
style menu_button_text:
    size 28
    color "#00ffff"
    hover_color "#ffffff"
    outlines [(2, "#003333", 0, 0), (4, "#000000", 0, 0)]
    kerning 2

# ═══════════════════════════════════════════════════════════════════════════════
#                         ÉCRAN MENU PRINCIPAL
# ═══════════════════════════════════════════════════════════════════════════════

screen main_menu():
    tag menu
    
    # Fond noir profond
    add Solid("#000000")
    
    # Lignes de scan animées (effet CRT)
    add Solid("#00ffff0D") at scanline_move:
        ysize 2
        xsize 1920
    
    # Lueur subtile derrière le titre
    add Solid("#00ffff") at pulse_glow:
        xalign 0.5
        yalign 0.22
        xsize 600
        ysize 100
        
    # === TITRE PRINCIPAL ===
    vbox at menu_title_appear:
        xalign 0.5 
        yalign 0.22
        spacing 5
        
        # Titre avec effet glitch
        text "CTRL+ALT+DELETE" at glitch_title:
            font "fonts/DMSerifText-Regular.ttf"
            size 85
            color "#ff0040"
            xalign 0.5
            outlines [(3, "#660000", 0, 0), (6, "#000000", 0, 0)]
            kerning 3
        
        # Ligne décorative
        add Solid("#ff0040CC"):
            xalign 0.5
            xsize 400
            ysize 2
    
    # === SOUS-TITRE ===
    vbox at menu_subtitle_appear:
        xalign 0.5
        yalign 0.35
        
        text "« Tu n'aurais jamais dû ouvrir ce fichier. »":
            font "fonts/DMSerifText-Regular.ttf"
            size 22
            color "#666666"
            xalign 0.5
            italic True
        
        null height 10
        
        text "UN JEU D'HORREUR PSYCHOLOGIQUE":
            font "fonts/DMSerifText-Regular.ttf"
            size 14
            color "#333333"
            xalign 0.5
            kerning 5

    # === BOUTONS DU MENU ===
    vbox:
        xalign 0.5
        yalign 0.58
        spacing 15
        
        # Nouvelle Partie
        textbutton "NOUVELLE PARTIE" at menu_button_appear(0.8), menu_button_hover:
            xalign 0.5
            action Start()
            text_font "fonts/DMSerifText-Regular.ttf"
            text_size 30
            text_color "#00ffff"
            text_hover_color "#ffffff"
            text_outlines [(2, "#003333", 0, 0), (4, "#000000", 0, 0)]
            text_kerning 3
        
        # Continuer
        textbutton "CONTINUER" at menu_button_appear(1.0), menu_button_hover:
            xalign 0.5
            action ShowMenu("load")
            text_font "fonts/DMSerifText-Regular.ttf"
            text_size 30
            text_color "#00ffff"
            text_hover_color "#ffffff"
            text_outlines [(2, "#003333", 0, 0), (4, "#000000", 0, 0)]
            text_kerning 3
        
        # Options
        textbutton "OPTIONS" at menu_button_appear(1.2), menu_button_hover:
            xalign 0.5
            action ShowMenu("preferences")
            text_font "fonts/DMSerifText-Regular.ttf"
            text_size 30
            text_color "#00ffff"
            text_hover_color "#ffffff"
            text_outlines [(2, "#003333", 0, 0), (4, "#000000", 0, 0)]
            text_kerning 3
        
        # Quitter
        textbutton "QUITTER" at menu_button_appear(1.4), menu_button_hover:
            xalign 0.5
            action Quit(confirm=False)
            text_font "fonts/DMSerifText-Regular.ttf"
            text_size 30
            text_color "#ff0040"
            text_hover_color "#ffffff"
            text_outlines [(2, "#330000", 0, 0), (4, "#000000", 0, 0)]
            text_kerning 3

    # === INFORMATIONS EN BAS ===
    vbox:
        xalign 0.5
        yalign 0.92
        spacing 5
        
        text "⚠ CONTENU MATURE • 16+ ⚠":
            font "fonts/DMSerifText-Regular.ttf"
            size 14
            color "#ff0040B3"
            xalign 0.5
        
        text "Horreur psychologique • Jumpscares • Thèmes sombres":
            font "fonts/DMSerifText-Regular.ttf"
            size 12
            color "#444444"
            xalign 0.5
    
    # === VERSION ===
    text "v1.0":
        font "fonts/DMSerifText-Regular.ttf"
        xalign 0.98
        yalign 0.98
        size 12
        color "#333333"

# ═══════════════════════════════════════════════════════════════════════════════
#                         STYLES POUR DIALOGUES
# ═══════════════════════════════════════════════════════════════════════════════

style say_dialogue:
    color "#ffffff"
    outlines [(2, "#000000", 0, 0)]

style say_thought:
    color "#aaaaaa"
    italic True
    outlines [(2, "#000000", 0, 0)]

# Style pour les choix
style choice_button:
    xalign 0.5
    
style choice_button_text:
    color "#00ffff"
    hover_color "#ffffff"
    size 26
    outlines [(2, "#003333", 0, 0)]
