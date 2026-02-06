# ═══════════════════════════════════════════════════════════════════════════════
#                              CTRL+ALT+DELETE
#                    VISUAL NOVEL HORREUR PSYCHOLOGIQUE
#                           VERSION ULTIMATE
# ═══════════════════════════════════════════════════════════════════════════════
#
#    "Tu n'aurais jamais dû ouvrir ce fichier."
#
#    Un tueur en série a uploadé sa conscience avant son exécution.
#    Il a passé 5 ans à chercher le corps parfait.
#    Il t'a trouvé.
#
#    Durée : 4-6 heures
#    14 jours de gameplay
#    4 actes
#    12 fins différentes
#    10 énigmes
#
# ═══════════════════════════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════════════════════════
#                              CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════════

init -1:
    # Fond noir partout
    define gui.game_menu_background = "#000000"
    define gui.main_menu_background = "#000000"
    
    # Résolution du jeu
    define config.screen_width = 1920
    define config.screen_height = 1080

# Transform pour mettre les backgrounds en plein écran
transform bg_fullscreen:
    truecenter
    xysize (1920, 1080)

init python:
    import random
    import time
    
    config.window_title = "CTRL+ALT+DELETE"

    # Callback pour images manquantes — retourne un Solid coloré selon le pattern
    def missing_image_callback(name):
        name_str = " ".join(name) if isinstance(name, tuple) else str(name)
        name_lower = name_str.lower()
        if "bg" in name_lower:
            if "rouge" in name_lower or "red" in name_lower:
                return Solid("#1a0000", xysize=(1920, 1080))
            elif "code" in name_lower or "ecran" in name_lower:
                return Solid("#0a0a15", xysize=(1920, 1080))
            elif "bsod" in name_lower:
                return Solid("#0078d7", xysize=(1920, 1080))
            elif "hopital" in name_lower:
                return Solid("#e8e8e8", xysize=(1920, 1080))
            else:
                return Solid("#1a0000", xysize=(1920, 1080))
        elif "overlay" in name_lower:
            return Solid("#00000000", xysize=(1920, 1080))
        elif "jumpscare" in name_lower:
            return Solid("#ff000088", xysize=(1920, 1080))
        elif any(x in name_lower for x in ["entite", "kane", "marc", "sarah"]):
            return Null()
        return Solid("#1a0000", xysize=(1920, 1080))

    config.missing_image_callback = missing_image_callback

    # Fonction safe_play pour éviter les crashs si un fichier audio manque
    def safe_play(channel, filename, **kwargs):
        try:
            if channel == "music":
                renpy.music.play(filename, **kwargs)
            else:
                renpy.sound.play(filename, **kwargs)
        except Exception:
            pass

    # Fonction vérification santé mentale
    def check_sante_mentale():
        if store.sante_mentale <= 0:
            store.sante_mentale = 0
            renpy.jump("fin_folie_prematuree")
        if store.sante_mentale > 100:
            store.sante_mentale = 100
    
    # Fonction texte glitché
    def glitch_text(text, intensity=0.3):
        glitch_chars = "█▓▒░╳╱╲"
        result = ""
        for char in text:
            if random.random() < intensity:
                result += random.choice(glitch_chars)
            else:
                result += char
        return result
    
    # Fonction pour effet de frappe lente (tension)
    def slow_text(text):
        return "{cps=15}" + text + "{/cps}"

# ═══════════════════════════════════════════════════════════════════════════════
#                              PERSONNAGES
# ═══════════════════════════════════════════════════════════════════════════════

# L'ENTITÉ - Forme féminine (masque initial)
define entite = Character("???", 
    color="#00ffff", 
    what_color="#ccffff",
    what_prefix='"',
    what_suffix='"',
    voice_tag="entite")

# L'ENTITÉ - En colère
define entite_colere = Character("???", 
    color="#ff0040", 
    what_color="#ffcccc",
    what_prefix='"',
    what_suffix='"',
    voice_tag="entite")

# L'ENTITÉ - Vraie forme (David Kane)
define kane = Character("DAVID KANE", 
    color="#ff0000", 
    what_color="#ff6666",
    what_prefix='"',
    what_suffix='"',
    voice_tag="kane")

# ALEX - Le protagoniste (le joueur)
define alex = Character("[player_name]", 
    color="#7ee787", 
    what_color="#ffffff")

# Pensées intérieures d'Alex
define pensee = Character(None,
    what_color="#aaaaaa",
    what_italic=True,
    what_prefix='(',
    what_suffix=')')

# MARC - Le meilleur ami
define marc = Character("Marc", 
    color="#f0c674", 
    what_color="#ffffff",
    voice_tag="marc")

# SARAH - La survivante / alliée potentielle
define sarah = Character("Sarah", 
    color="#b294bb", 
    what_color="#ffffff",
    voice_tag="sarah")

# CLAIRE - La mère d'Alex
define maman = Character("Maman", 
    color="#81a2be", 
    what_color="#ffffff")

# SYSTÈME - Messages d'ordinateur
define systeme = Character("SYSTÈME", 
    color="#666666", 
    what_color="#aaaaaa",
    what_prefix='[[',
    what_suffix=']]')

# ERREUR - Messages d'erreur
define erreur = Character("ERREUR", 
    color="#ff0040", 
    what_color="#ff6666",
    what_prefix='⚠ ',
    what_suffix=' ⚠')

# NARRATEUR
define narrateur = Character(None, 
    what_color="#999999", 
    what_italic=True)

# VOIX INCONNUE (pour les moments de doute)
define voix = Character("???",
    color="#444444",
    what_color="#666666",
    what_italic=True)

# ═══════════════════════════════════════════════════════════════════════════════
#                              VARIABLES
# ═══════════════════════════════════════════════════════════════════════════════

# === IDENTITÉ ===
default player_name = "Alex"

# === STATS PRINCIPALES ===
default sante_mentale = 100      # 0-100 : 0 = folie totale, game over spécial
default mefiance = 50            # 0-100 : méfiance envers l'entité
default connaissance = 0         # 0-100 : ce qu'Alex sait sur Kane
default corruption = 0           # 0-100 : influence de Kane sur l'esprit d'Alex
default espoir = 50              # 0-100 : volonté de se battre

# === RELATIONS ===
default relation_marc = 100      # Amitié avec Marc
default relation_sarah = 0       # Confiance en Sarah
default relation_maman = 100     # Relation avec sa mère

# === PROGRESSION ===
default jour = 1
default acte = 1
default heure = "23:47"
default enigmes_resolues = 0

# === FLAGS HISTOIRE ===
default a_ouvert_fichier = False
default a_vu_photo_webcam = False
default a_trouve_archives = False
default connait_kane = False
default a_contacte_sarah = False
default alliance_sarah = False
default sarah_est_piege = False  # Twist potentiel
default a_prevenu_marc = False
default a_appele_maman = False
default marc_croit_alex = False
default a_tente_police = False
default police_corrompue = False

# === FLAGS TECHNIQUES ===
default webcam_couverte = False
default telephone_infecte = False
default maison_controlee = False
default a_trouve_code = False
default a_trouve_ip = False
default code_kane = "KANE66"
default tentatives_suppression = 0
default regles_brisees = 0
default a_debranche_internet = False

# === ÉNIGMES ===
default enigme1_resolue = False     # FREEDOM
default enigme2_resolue = False     # Messages corrompus
default enigme3_resolue = False     # Adresse IP 666
default enigme4_resolue = False     # Articles Kane
default enigme5_resolue = False     # Virus anti-Kane
default enigme6_resolue = False     # Code KANE66
default enigme7_resolue = False     # Labyrinthe mental
default enigme8_resolue = False     # Taper le code sous pression
default enigme9_resolue = False     # Choix moral
default enigme10_resolue = False    # Secret post-générique

# === COMPTEURS FINS ===
default upload_complete = False
default kane_detruit = False
default alex_survit = True
default fin_atteinte = ""

# ═══════════════════════════════════════════════════════════════════════════════
#                              AUDIO
# ═══════════════════════════════════════════════════════════════════════════════

# === MUSIQUES D'AMBIANCE ===
# Place ces fichiers dans game/audio/

define audio.menu_theme = "audio/menu_theme.ogg"              # Menu principal (drone sombre)
define audio.ambiance_nuit = "audio/ambiance_nuit.ogg"        # Nuit calme, grillons, vent léger
define audio.ambiance_bureau = "audio/ambiance_bureau.ogg"    # Ventilo PC, clavier distant
define audio.tension_legere = "audio/tension_legere.ogg"      # Tension croissante
define audio.tension_forte = "audio/tension_forte.ogg"        # Danger imminent
define audio.horreur = "audio/horreur.ogg"                    # Musique horrifique
define audio.chase = "audio/chase.ogg"                        # Poursuite/urgence
define audio.drone_grave = "audio/drone_grave.ogg"            # Drone basse fréquence (malaise)
define audio.silence = "audio/silence.ogg"                    # Silence oppressant (léger bruit de fond)
define audio.revelation = "audio/revelation.ogg"              # Moment de révélation
define audio.espoir = "audio/espoir.ogg"                      # Moment d'espoir
define audio.finale = "audio/finale.ogg"                      # Confrontation finale
define audio.victoire = "audio/victoire.ogg"                  # Fin positive
define audio.defaite = "audio/defaite.ogg"                    # Fin négative

# === EFFETS SONORES ===
define audio.notification = "audio/sfx/notification.ogg"      # Bip de notification
define audio.error = "audio/sfx/error.ogg"                    # Son d'erreur Windows
define audio.startup = "audio/sfx/startup.ogg"                # Démarrage PC
define audio.shutdown = "audio/sfx/shutdown.ogg"              # Extinction PC
define audio.glitch = "audio/sfx/glitch.ogg"                  # Glitch électronique
define audio.glitch_long = "audio/sfx/glitch_long.ogg"        # Glitch prolongé
define audio.static = "audio/sfx/static.ogg"                  # Bruit statique TV
define audio.heartbeat = "audio/sfx/heartbeat.ogg"            # Battement de coeur
define audio.heartbeat_fast = "audio/sfx/heartbeat_fast.ogg"  # Coeur rapide (panique)
define audio.breath = "audio/sfx/breath.ogg"                  # Respiration lourde
define audio.breath_close = "audio/sfx/breath_close.ogg"      # Respiration proche (terrifiant)
define audio.typing = "audio/sfx/typing.ogg"                  # Frappe clavier
define audio.typing_slow = "audio/sfx/typing_slow.ogg"        # Frappe lente (entité)
define audio.phone_ring = "audio/sfx/phone_ring.ogg"          # Téléphone sonne
define audio.phone_vibrate = "audio/sfx/phone_vibrate.ogg"    # Téléphone vibre
define audio.door_knock = "audio/sfx/door_knock.ogg"          # Coup à la porte
define audio.door_slam = "audio/sfx/door_slam.ogg"            # Porte claquée
define audio.glass_break = "audio/sfx/glass_break.ogg"        # Verre brisé
define audio.light_flicker = "audio/sfx/light_flicker.ogg"    # Lumière qui grésille
define audio.lights_off = "audio/sfx/lights_off.ogg"          # Lumières qui s'éteignent
define audio.lights_on = "audio/sfx/lights_on.ogg"            # Lumières qui s'allument
define audio.tv_on = "audio/sfx/tv_on.ogg"                    # TV qui s'allume
define audio.scream = "audio/sfx/scream.ogg"                  # Cri distant
define audio.whisper = "audio/sfx/whisper.ogg"                # Chuchotement
define audio.laugh = "audio/sfx/laugh.ogg"                    # Rire sinistre
define audio.jumpscare = "audio/sfx/jumpscare.ogg"            # Son de jumpscare
define audio.bass_drop = "audio/sfx/bass_drop.ogg"            # Impact grave
define audio.reverse = "audio/sfx/reverse.ogg"                # Son inversé (creepy)
define audio.message_send = "audio/sfx/message_send.ogg"      # Envoi message
define audio.message_receive = "audio/sfx/message_receive.ogg" # Réception message
define audio.webcam_click = "audio/sfx/webcam_click.ogg"      # Clic webcam (photo)
define audio.file_delete = "audio/sfx/file_delete.ogg"        # Suppression fichier
define audio.access_denied = "audio/sfx/access_denied.ogg"    # Accès refusé
define audio.success = "audio/sfx/success.ogg"                # Succès/validation
define audio.clock_tick = "audio/sfx/clock_tick.ogg"          # Tic-tac horloge
define audio.countdown = "audio/sfx/countdown.ogg"            # Compte à rebours
define audio.electricity = "audio/sfx/electricity.ogg"        # Grésillement électrique
define audio.upload = "audio/sfx/upload.ogg"                  # Son d'upload en cours

# ═══════════════════════════════════════════════════════════════════════════════
#                              IMAGES
# ═══════════════════════════════════════════════════════════════════════════════

# === BACKGROUNDS (1920x1080) ===
# Place ces fichiers dans game/images/

# Bureau/Chambre d'Alex
image bg bureau_nuit = im.Scale("images/bg_bureau_nuit.jpg", 1920, 1080)
image bg bureau_jour = im.Scale("images/bg_bureau_jour.jpg", 1920, 1080)
image bg bureau_soir = im.Scale("images/bg_bureau_soir.jpg", 1920, 1080)
image bg bureau_aube = im.Scale("images/bg_bureau_aube.jpg", 1920, 1080)
image bg bureau_glitch = im.Scale("images/bg_bureau_glitch.jpg", 1920, 1080)
image bg bureau_rouge = im.Scale("images/bg_bureau_rouge.jpg", 1920, 1080)

# Appartement
image bg salon_nuit = im.Scale("images/bg_salon_nuit.jpg", 1920, 1080)
image bg salon_tv = im.Scale("images/bg_salon_tv.jpg", 1920, 1080)
image bg cuisine_nuit = im.Scale("images/bg_cuisine_nuit.jpg", 1920, 1080)
image bg couloir_nuit = im.Scale("images/bg_couloir_nuit.jpg", 1920, 1080)
image bg chambre_nuit = im.Scale("images/bg_chambre_nuit.jpg", 1920, 1080)

# Extérieur (flashbacks, rencontres)
image bg cafe_jour = im.Scale("images/bg_cafe_jour.jpg", 1920, 1080)
image bg rue_nuit = im.Scale("images/bg_rue_nuit.jpg", 1920, 1080)
image bg hopital = im.Scale("images/bg_hopital.jpg", 1920, 1080)
image bg prison = im.Scale("images/bg_prison.jpg", 1920, 1080)
image bg morgue = im.Scale("images/bg_morgue.jpg", 1920, 1080)

# Écrans d'ordinateur
image bg ecran_noir = im.Scale("images/bg_ecran_noir.jpg", 1920, 1080)
image bg ecran_code = im.Scale("images/bg_ecran_code.jpg", 1920, 1080)
image bg ecran_glitch = im.Scale("images/bg_ecran_glitch.jpg", 1920, 1080)
image bg ecran_rouge = im.Scale("images/bg_ecran_rouge.jpg", 1920, 1080)
image bg ecran_upload = im.Scale("images/bg_ecran_upload.jpg", 1920, 1080)
image bg ecran_bsod = im.Scale("images/bg_ecran_bsod.jpg", 1920, 1080)

# États de l'écran
image bg static = im.Scale("images/bg_static.jpg", 1920, 1080)
image bg noir = Solid("#000000")
image bg blanc = Solid("#ffffff")
image bg rouge = Solid("#1a0000")
image bg rouge_flash = Solid("#ff0000")

# === ENTITÉ - FORME FÉMININE (masque) ===
image entite neutre = "images/entite_neutre.png"            # Visage féminin, yeux cyan, expression vide
image entite curieuse = "images/entite_curieuse.png"        # Tête penchée, sourire subtil
image entite souriante = "images/entite_souriante.png"      # Grand sourire dérangeant
image entite triste = "images/entite_triste.png"            # Expression triste (manipulation)
image entite colere = "images/entite_colere.png"            # Yeux rouges, expression menaçante
image entite glitch = "images/entite_glitch.png"            # Visage déformé, artefacts
image entite glitch2 = "images/entite_glitch2.png"          # Autre version glitch
image entite statique = "images/entite_statique.png"        # Visage couvert de statique

# === ENTITÉ - VRAIE FORME (David Kane) ===
image kane neutre = "images/kane_neutre.png"                # Visage masculin, yeux morts
image kane sourire = "images/kane_sourire.png"              # Sourire de psychopathe
image kane colere = "images/kane_colere.png"                # Rage
image kane glitch = "images/kane_glitch.png"                # Visage qui se désintègre
image kane fusion = "images/kane_fusion.png"                # Fusion des deux visages (creepy)
image kane final = "images/kane_final.png"                  # Forme finale terrifiante
image kane triste = "images/kane_triste.png"                # Kane expression triste

# === PERSONNAGES SECONDAIRES ===
image marc normal = "images/marc_normal.png"                # Marc, ami sympathique
image marc inquiet = "images/marc_inquiet.png"              # Marc inquiet
image marc colere = "images/marc_colere.png"                # Marc énervé
image marc peur = "images/marc_peur.png"                    # Marc terrifié

image sarah neutre = "images/sarah_neutre.png"              # Sarah, mystérieuse
image sarah serieuse = "images/sarah_serieuse.png"          # Sarah sérieuse
image sarah peur = "images/sarah_peur.png"                  # Sarah effrayée
image sarah sourire = "images/sarah_sourire.png"            # Sarah souriante (piège?)

# === POPUPS ET INTERFACES ===
image popup_fichier = "images/popup_fichier.png"            # Fenêtre ENTITY.exe
image popup_erreur = "images/popup_erreur.png"              # Message d'erreur
image popup_photo = "images/popup_photo.png"                # Photo prise par webcam
image popup_messages = "images/popup_messages.png"          # Messages corrompus
image popup_regles = "images/popup_regles.png"              # Liste des règles
image popup_menace = "images/popup_menace.png"              # Menace avec données personnelles
image popup_compte = "images/popup_compte.png"              # Compte bancaire
image popup_chat = "images/popup_chat.png"                  # Fenêtre de chat

image article_kane1 = "images/article_kane1.png"            # Article arrestation
image article_kane2 = "images/article_kane2.png"            # Article procès
image article_kane3 = "images/article_kane3.png"            # Article exécution
image photo_victimes = "images/photo_victimes.png"          # Photos des victimes

image tv_surveillance = "images/tv_surveillance.png"        # Images de surveillance
image webcam_photo = "images/webcam_photo.png"              # Photo d'Alex endormi

# === EFFETS VISUELS (overlays transparents) ===
image overlay_scanlines = "images/overlay_scanlines.png"    # Lignes de scan CRT
image overlay_glitch = "images/overlay_glitch.png"          # Effet glitch
image overlay_vignette = "images/overlay_vignette.png"      # Vignette sombre
image overlay_rouge = "images/overlay_rouge.png"            # Teinte rouge danger
image overlay_static = "images/overlay_static.png"          # Neige statique

# === JUMPSCARES ===
image jumpscare_entite = "images/jumpscare_entite.png"      # Jumpscare visage entité
image jumpscare_kane = "images/jumpscare_kane.png"          # Jumpscare visage Kane
image jumpscare_oeil = "images/jumpscare_oeil.png"          # Œil qui s'ouvre soudainement

# ═══════════════════════════════════════════════════════════════════════════════
#                              TRANSFORMS
# ═══════════════════════════════════════════════════════════════════════════════

# Positions
transform centre:
    xalign 0.5 yalign 0.5

transform centre_bas:
    xalign 0.5 yalign 0.65

transform gauche:
    xalign 0.2 yalign 0.65

transform droite:
    xalign 0.8 yalign 0.65

# Apparitions
transform apparition_lente:
    alpha 0.0
    linear 3.0 alpha 1.0

transform apparition_normale:
    alpha 0.0
    linear 1.0 alpha 1.0

transform apparition_soudaine:
    alpha 0.0
    pause 0.3
    linear 0.05 alpha 1.0

transform disparition_lente:
    alpha 1.0
    linear 2.0 alpha 0.0

# Effets de peur
transform glitch_leger:
    xoffset 0
    linear 0.03 xoffset -3
    linear 0.03 xoffset 5
    linear 0.03 xoffset -2
    linear 0.03 xoffset 0

transform glitch_moyen:
    xoffset 0 yoffset 0
    linear 0.02 xoffset -8 yoffset 3
    linear 0.02 xoffset 10 yoffset -5
    linear 0.02 xoffset -5 yoffset 2
    linear 0.02 xoffset 6 yoffset -3
    linear 0.02 xoffset 0 yoffset 0

transform glitch_violent:
    xoffset 0 yoffset 0 zoom 1.0
    linear 0.015 xoffset -20 yoffset 10 zoom 1.02
    linear 0.015 xoffset 25 yoffset -15 zoom 0.98
    linear 0.015 xoffset -15 yoffset 8 zoom 1.01
    linear 0.015 xoffset 18 yoffset -12 zoom 0.99
    linear 0.015 xoffset -10 yoffset 5 zoom 1.0
    linear 0.015 xoffset 0 yoffset 0 zoom 1.0

transform tremble_leger:
    linear 0.04 xoffset -2 yoffset -1
    linear 0.04 xoffset 2 yoffset 1
    linear 0.04 xoffset -1 yoffset -2
    linear 0.04 xoffset 1 yoffset 2
    linear 0.04 xoffset 0 yoffset 0
    repeat

transform tremble_fort:
    linear 0.02 xoffset -8 yoffset -5
    linear 0.02 xoffset 10 yoffset 6
    linear 0.02 xoffset -6 yoffset -8
    linear 0.02 xoffset 8 yoffset 5
    linear 0.02 xoffset 0 yoffset 0
    repeat

transform tremble_violent:
    linear 0.015 xoffset -15 yoffset -10
    linear 0.015 xoffset 18 yoffset 12
    linear 0.015 xoffset -12 yoffset -15
    linear 0.015 xoffset 15 yoffset 10
    linear 0.015 xoffset 0 yoffset 0
    repeat

# Zooms menaçants
transform zoom_lent:
    zoom 1.0
    linear 15.0 zoom 1.05
    linear 15.0 zoom 1.0
    repeat

transform zoom_moyen:
    zoom 1.0
    linear 8.0 zoom 1.15

transform zoom_rapide:
    zoom 1.0
    linear 3.0 zoom 1.2

transform zoom_jumpscare:
    zoom 1.0 alpha 0.0
    linear 0.1 zoom 1.5 alpha 1.0

# Respiration (personnages)
transform respiration:
    yoffset 0
    ease 2.0 yoffset -5
    ease 2.0 yoffset 0
    repeat

transform respiration_rapide:
    yoffset 0
    ease 0.5 yoffset -8
    ease 0.5 yoffset 0
    repeat

# Pulsation (éléments UI menaçants)
transform pulse:
    alpha 1.0
    ease 1.0 alpha 0.7
    ease 1.0 alpha 1.0
    repeat

transform pulse_rapide:
    alpha 1.0
    ease 0.3 alpha 0.5
    ease 0.3 alpha 1.0
    repeat

transform pulse_rouge:
    matrixcolor TintMatrix("#ffffff")
    ease 0.5 matrixcolor TintMatrix("#ff6666")
    ease 0.5 matrixcolor TintMatrix("#ffffff")
    repeat

# ═══════════════════════════════════════════════════════════════════════════════
#                              TRANSITIONS
# ═══════════════════════════════════════════════════════════════════════════════

# Glitch court
define trans_glitch = MultipleTransition([
    False, Dissolve(0.1),
    Solid("#ff0000"), Pause(0.03),
    Solid("#00ffff"), Dissolve(0.1),
    True
])

# Glitch long
define trans_glitch_long = MultipleTransition([
    False, Dissolve(0.05),
    Solid("#ff0000"), Pause(0.05),
    Solid("#00ff00"), Pause(0.03),
    Solid("#0000ff"), Pause(0.05),
    Solid("#ffffff"), Pause(0.02),
    Solid("#000000"), Dissolve(0.2),
    True
])

# Horreur (fondu noir lent)
define trans_horreur = MultipleTransition([
    False, Dissolve(0.8),
    Solid("#000000"), Dissolve(1.2),
    True
])

# Flash blanc (jumpscare)
define flash_blanc = MultipleTransition([
    False, Pause(0.0),
    Solid("#ffffff"), Dissolve(0.15),
    True
])

# Flash rouge (danger)
define flash_rouge = MultipleTransition([
    False, Pause(0.0),
    Solid("#ff0000"), Dissolve(0.2),
    True
])

# Statique TV
define trans_static = MultipleTransition([
    False, Dissolve(0.03),
    Solid("#333333"), Pause(0.05),
    Solid("#666666"), Pause(0.03),
    Solid("#111111"), Dissolve(0.1),
    True
])

# Noir instantané (coupure)
define noir_instant = MultipleTransition([
    False, Pause(0.0),
    Solid("#000000"), Pause(0.5),
    True
])

# ═══════════════════════════════════════════════════════════════════════════════
#                              ÉCRANS CUSTOM
# ═══════════════════════════════════════════════════════════════════════════════

# Barre de santé mentale (toujours visible)
screen hud_sante():
    zorder 100
    frame:
        xalign 0.02 yalign 0.02
        xpadding 15 ypadding 8
        background "#00000099"
        has vbox spacing 5
        
        hbox:
            spacing 10
            text "🧠 Santé mentale" size 14 color "#888888"
            bar value sante_mentale range 100 xsize 120 ysize 12:
                left_bar Frame("#00ff00", 0, 0)
                right_bar Frame("#333333", 0, 0)
        
        if sante_mentale <= 30:
            text "⚠ ÉTAT CRITIQUE" size 12 color "#ff0040"

# Écran de notification système
screen notification_systeme(message, duree=2.0):
    zorder 200
    frame:
        xalign 0.98 yalign 0.05
        xpadding 20 ypadding 15
        background "#1a1a2eee"
        has hbox spacing 15
        text "🔔" size 24
        text message size 16 color "#00ffff"
    
    timer duree action Hide("notification_systeme")

# Écran de popup d'erreur Windows
screen faux_erreur(titre="Erreur", message="Une erreur est survenue."):
    modal True
    zorder 300
    
    frame:
        xalign 0.5 yalign 0.5
        xsize 500 ysize 220
        background "#1a1a2e"
        
        has vbox spacing 20
        xalign 0.5 yalign 0.5
        
        hbox:
            xalign 0.5
            spacing 15
            text "⚠" size 40 color "#ff0040"
            text titre size 24 color "#ff0040"
        
        text message size 16 color "#ffffff" text_align 0.5 xalign 0.5
        
        textbutton "OK" action Return():
            xalign 0.5
            text_size 18
            text_color "#00ffff"

# Écran de Blue Screen of Death
screen faux_bsod():
    modal True
    zorder 500
    
    add Solid("#0078d7")
    
    vbox:
        xalign 0.5 yalign 0.35
        spacing 40
        
        text ":(" size 150 color "#ffffff" xalign 0.5
        
        text "Votre PC a rencontré un problème et doit redémarrer." size 28 color "#ffffff" xalign 0.5
        text "Nous collectons des informations sur l'erreur, puis nous" size 20 color "#ffffff" xalign 0.5
        text "redémarrerons pour vous." size 20 color "#ffffff" xalign 0.5
        
        null height 30
        
        text "0% effectué" size 18 color "#ffffff" xalign 0.5 id "progress"
    
    timer 4.0 action Return()

# Écran de saisie de code
screen saisie_code():
    modal True
    zorder 300
    
    add Solid("#000000cc")
    
    frame:
        xalign 0.5 yalign 0.5
        xsize 600 ysize 280
        background "#0a0a15"
        xpadding 30 ypadding 30
        
        has vbox spacing 25
        xalign 0.5
        
        text "⚠ PROTOCOLE DE DESTRUCTION ⚠" size 22 color "#ff0040" xalign 0.5
        text "Entrez le code de destruction :" size 18 color "#ffffff" xalign 0.5
        
        input default "" value VariableInputValue("code_entre") length 10:
            color "#00ff00"
            size 36
            xalign 0.5
        
        hbox:
            xalign 0.5
            spacing 40
            
            textbutton "CONFIRMER" action Return("confirm"):
                text_size 20
                text_color "#00ff00"
            
            textbutton "ANNULER" action Return("cancel"):
                text_size 20
                text_color "#ff0040"

# Écran de compte à rebours final
screen compte_a_rebours(temps):
    zorder 400
    
    frame:
        xalign 0.5 yalign 0.1
        xpadding 30 ypadding 15
        background "#1a0000ee"
        
        has hbox spacing 20
        
        text "⏱ UPLOAD EN COURS :" size 20 color "#ff6666"
        text "[temps]" size 28 color "#ff0040"

# Menu principal custom (thème horreur)
# Menu principal déplacé vers gui_premium.rpy pour plus de fonctionnalités

# ═══════════════════════════════════════════════════════════════════════════════
#                              FONCTIONS UTILES
# ═══════════════════════════════════════════════════════════════════════════════

init python:
    
    # Jouer un son avec volume
    def play_sfx(sound, volume=1.0):
        renpy.sound.play(sound, volume=volume)
    
    # Diminuer la santé mentale avec vérification
    def perte_sante(montant):
        store.sante_mentale = max(0, store.sante_mentale - montant)
        check_sante_mentale()
    
    # Augmenter la corruption
    def gain_corruption(montant):
        store.corruption = min(100, store.corruption + montant)
        if store.corruption >= 80:
            renpy.notify("⚠ Kane prend le contrôle...")

# ═══════════════════════════════════════════════════════════════════════════════
#                              LABEL START
# ═══════════════════════════════════════════════════════════════════════════════

label start:
    
    # Reset complet
    $ sante_mentale = 100
    $ mefiance = 50
    $ connaissance = 0
    $ corruption = 0
    $ espoir = 50
    $ relation_marc = 100
    $ relation_sarah = 0
    $ jour = 1
    $ acte = 1
    $ enigmes_resolues = 0
    $ a_ouvert_fichier = False
    $ connait_kane = False
    $ alliance_sarah = False
    $ a_trouve_code = False
    
    # Charger la langue sauvegardée
    $ language = persistent.language if persistent.language else "fr"
    
    # Pas de musique au départ
    stop music fadeout 1.0
    
    scene bg noir
    with fade
    
    window hide
    pause 1.0
    
    # === SÉLECTION DE LA LANGUE ===
    call screen language_select
    
    pause 0.5
    
    # === AVERTISSEMENT ===
    
    centered "{color=#ff0040}{size=+20}⚠ [t('AVERTISSEMENT', 'WARNING')] ⚠{/size}{/color}"
    pause 2.0
    
    if language == "fr":
        centered "{size=+5}Ce jeu contient :{/size}"
        pause 1.0
        centered "• Horreur psychologique intense"
        pause 0.7
        centered "• Thèmes de mort et de possession"
        pause 0.7
        centered "• Jumpscares"
        pause 0.7
        centered "• Contenu pouvant être perturbant"
        pause 1.5
        centered "{color=#666666}Recommandé aux personnes de 16 ans et plus.{/color}"
        pause 1.5
        centered "{color=#00ffff}🎧 Casque audio fortement recommandé 🎧{/color}"
        pause 1.5
        centered "{color=#00ffff}🌙 Jouez dans le noir pour une meilleure expérience 🌙{/color}"
    else:
        centered "{size=+5}This game contains:{/size}"
        pause 1.0
        centered "• Intense psychological horror"
        pause 0.7
        centered "• Themes of death and possession"
        pause 0.7
        centered "• Jumpscares"
        pause 0.7
        centered "• Disturbing content"
        pause 1.5
        centered "{color=#666666}Recommended for ages 16 and up.{/color}"
        pause 1.5
        centered "{color=#00ffff}🎧 Headphones strongly recommended 🎧{/color}"
        pause 1.5
        centered "{color=#00ffff}🌙 Play in the dark for the best experience 🌙{/color}"
    
    pause 2.0
    
    scene bg noir with dissolve
    pause 1.0
    
    # === ENTRÉE DU NOM ===
    
    play sound audio.startup
    pause 1.0
    
    if language == "fr":
        centered "{color=#00ff00}INITIALISATION DU SYSTÈME...{/color}"
        pause 1.0
        centered "{color=#00ff00}CONNEXION ÉTABLIE{/color}"
        pause 0.8
        centered "{color=#00ff00}IDENTIFICATION REQUISE{/color}"
        pause 1.5
        $ player_name = renpy.input("Entrez votre nom :", default="Alex", length=20)
    else:
        centered "{color=#00ff00}SYSTEM INITIALIZATION...{/color}"
        pause 1.0
        centered "{color=#00ff00}CONNECTION ESTABLISHED{/color}"
        pause 0.8
        centered "{color=#00ff00}IDENTIFICATION REQUIRED{/color}"
        pause 1.5
        $ player_name = renpy.input("Enter your name:", default="Alex", length=20)
    
    $ player_name = player_name.strip()
    
    if player_name == "":
        $ player_name = "Alex"
    
    play sound audio.notification
    pause 0.5
    
    if language == "fr":
        centered "{color=#00ff00}Bienvenue, [player_name].{/color}"
    else:
        centered "{color=#00ff00}Welcome, [player_name].{/color}"
    pause 1.5
    
    scene bg noir with trans_glitch
    
    play sound audio.glitch
    pause 0.5
    
    centered "{color=#ff0040}...{/color}"
    pause 1.0
    if language == "fr":
        centered "{color=#ff0040}Nous t'attendions.{/color}"
    else:
        centered "{color=#ff0040}We've been waiting for you.{/color}"
    pause 2.0
    
    scene bg noir with dissolve
    pause 1.0
    
    # Démarrage
    window show
    
    # Musique d'ambiance
    play music audio.ambiance_nuit fadein 2.0 volume 0.5
    
    jump acte1_debut
