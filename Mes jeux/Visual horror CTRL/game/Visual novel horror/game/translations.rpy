# ═══════════════════════════════════════════════════════════════════════════════
#                    SYSTÈME DE TRADUCTION FR/EN
#                         CTRL+ALT+DELETE
# ═══════════════════════════════════════════════════════════════════════════════

init python:
    # Langue par défaut = Français
    if not persistent.language:
        persistent.language = "fr"

# Variable pour accéder facilement
default language = "fr"

init python:
    def set_language(lang):
        persistent.language = lang
        store.language = lang
        renpy.restart_interaction()
    
    def t(fr_text, en_text):
        """Fonction de traduction simple"""
        if store.language == "en":
            return en_text
        return fr_text

# ═══════════════════════════════════════════════════════════════════════════════
#                         ÉCRAN SÉLECTION LANGUE
# ═══════════════════════════════════════════════════════════════════════════════

screen language_select():
    modal True
    add Solid("#000000")
    
    vbox:
        xalign 0.5 yalign 0.5
        spacing 30
        
        text "🌍 LANGUE / LANGUAGE" size 40 color "#ffffff" xalign 0.5
        
        null height 20
        
        hbox:
            xalign 0.5
            spacing 50
            
            textbutton "🇫🇷 FRANÇAIS":
                action [SetVariable("language", "fr"), SetField(persistent, "language", "fr"), Return()]
                text_size 32
                text_color "#00ffff"
                text_hover_color "#ffffff"
            
            textbutton "🇬🇧 ENGLISH":
                action [SetVariable("language", "en"), SetField(persistent, "language", "en"), Return()]
                text_size 32
                text_color "#00ffff"
                text_hover_color "#ffffff"

# ═══════════════════════════════════════════════════════════════════════════════
#                         BOUTON LANGUE DANS OPTIONS
# ═══════════════════════════════════════════════════════════════════════════════

# Ajoute ça dans ton écran de préférences/options :
# textbutton "🌍 Langue / Language" action Show("language_select")
