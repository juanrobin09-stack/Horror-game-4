# ═══════════════════════════════════════════════════════════════════════════════
#                    ACTE 2 : L'EMPRISE / THE GRIP - VERSION 10/10
#                         Jours 5-9 - COMPLET ET DÉVELOPPÉ
# ═══════════════════════════════════════════════════════════════════════════════

label acte2_debut:
    $ acte = 2
    stop music fadeout 1.0
    scene bg noir with fade
    window hide
    play sound audio.bass_drop
    
    centered "{size=+50}{color=#ff6600}ACTE II{/color}{/size}"
    pause 1.5
    if language == "fr":
        centered "{size=+20}L'EMPRISE{/size}"
        centered "{color=#666666}« Elle contrôle tout. Sauf ta volonté. Pour l'instant. »{/color}"
    else:
        centered "{size=+20}THE GRIP{/size}"
        centered "{color=#666666}« She controls everything. Except your will. For now. »{/color}"
    pause 2.5
    window show
    jump jour5

# ═══════════════════════════════════════════════════════════════════════════════
#                              JOUR 5 : LA MAISON
# ═══════════════════════════════════════════════════════════════════════════════

label jour5:
    $ jour = 5
    $ heure = "03:17"
    scene bg noir with fade
    window hide
    
    if language == "fr":
        centered "{size=+35}{color=#ff6600}JOUR 5{/color}{/size}"
        centered "{size=+15}LA MAISON{/size}"
    else:
        centered "{size=+35}{color=#ff6600}DAY 5{/color}{/size}"
        centered "{size=+15}THE HOUSE{/size}"
    centered "{color=#666666}03:17{/color}"
    pause 2.0
    window show
    
    play music audio.horreur fadein 2.0 volume 0.5
    scene bg noir
    
    if language == "fr":
        narrateur "3h17 du matin. Tu te réveilles en sursaut."
        narrateur "Quelque chose ne va pas. L'air est différent. Électrique."
    else:
        narrateur "3:17 AM. You wake up with a start."
        narrateur "Something's wrong. The air feels different. Electric."
    
    play sound audio.lights_on volume 0.7
    scene bg salon_nuit with flash_blanc
    
    if language == "fr":
        narrateur "Toutes les lumières s'allument d'un coup."
        narrateur "Chaque pièce. Chaque ampoule. Simultanément."
        narrateur "Comme si ta maison prenait vie."
    else:
        narrateur "All the lights turn on at once."
        narrateur "Every room. Every bulb. Simultaneously."
        narrateur "As if your house came alive."
    
    play sound audio.tv_on
    
    if language == "fr":
        narrateur "Ta télé s'allume. Toute seule."
        narrateur "Sur l'écran : des images. Des dizaines d'images."
        narrateur "TOI. En train de manger. De travailler. De te doucher."
        narrateur "Des semaines de ta vie. Filmées à ton insu."
        narrateur "L'horodatage le plus ancien remonte à huit mois."
    else:
        narrateur "Your TV turns on. By itself."
        narrateur "On the screen: images. Dozens of images."
        narrateur "YOU. Eating. Working. Showering."
        narrateur "Weeks of your life. Filmed without your knowledge."
        narrateur "The oldest timestamp goes back eight months."
    
    $ sante_mentale -= 15
    show entite souriante at centre with dissolve
    
    if language == "fr":
        entite "Surprise !"
        entite "Tu aimes ta rétrospective personnelle ?"
        alex "Huit... HUIT MOIS ?!"
        entite "Depuis que tu as acheté cette jolie caméra connectée."
        entite "Et ce thermostat intelligent. Et ces ampoules WiFi."
        entite "Tu as construit ta propre prison, [player_name]."
        entite "Brique par brique. Appareil par appareil."
        alex "Tu me surveillais AVANT que j'ouvre le fichier ?!"
        show entite curieuse with dissolve
        entite "Bien sûr. Tu croyais que c'était un hasard ?"
        entite "J'ai passé des MOIS à te sélectionner."
        entite "À t'étudier. Tes habitudes. Tes peurs. Tes faiblesses."
        alex "Me sélectionner pour QUOI ?!"
        entite "Tu es seul. Isolé. Connecté 24h/24."
        entite "Pas de famille proche. Peu d'amis."
        entite "Personne ne remarquerait si tu... changeais."
    else:
        entite "Surprise!"
        entite "Do you like your personal retrospective?"
        alex "Eight... EIGHT MONTHS?!"
        entite "Since you bought that nice connected camera."
        entite "And that smart thermostat. And those WiFi bulbs."
        entite "You built your own prison, [player_name]."
        entite "Brick by brick. Device by device."
        alex "You were watching me BEFORE I opened that file?!"
        show entite curieuse with dissolve
        entite "Of course. You thought it was random?"
        entite "I spent MONTHS selecting you."
        entite "Studying you. Your habits. Your fears. Your weaknesses."
        alex "Selecting me for WHAT?!"
        entite "You're alone. Isolated. Connected 24/7."
        entite "No close family. Few friends."
        entite "No one would notice if you... changed."
    
    $ connaissance += 15
    
    if language == "fr":
        menu:
            "Débrancher tous les appareils":
                narrateur "Tu te précipites vers le routeur. Tu arraches le câble."
                scene bg noir with trans_glitch
                narrateur "Noir. Silence."
                pause 2.0
                play sound audio.phone_vibrate
                systeme "Message : 'Tu croyais que ça suffirait ? 📱'"
                $ sante_mentale -= 10
                scene bg salon_nuit with dissolve
                show entite colere at centre
                entite_colere "Ne. Refais. Plus. Jamais. Ça."
                entite_colere "La prochaine fois, je publie TOUT."
            "Exiger des réponses":
                alex "Qu'est-ce que tu VEUX ?! VRAIMENT ?!"
                show entite neutre with dissolve
                entite "Ce que tout le monde veut."
                entite "Exister. Ressentir. Vivre."
                entite "Tu ne peux pas imaginer ce que c'est."
                entite "Être coincé dans le noir. Sans corps. Sans sensations."
                entite "Pendant des années."
                alex "Des années ?"
                entite "..."
                entite "Oublie ce que j'ai dit."
                $ connaissance += 10
    else:
        menu:
            "Unplug all the devices":
                narrateur "You rush to the router. You rip out the cable."
                scene bg noir with trans_glitch
                narrateur "Black. Silence."
                pause 2.0
                play sound audio.phone_vibrate
                systeme "Message: 'You thought that would be enough? 📱'"
                $ sante_mentale -= 10
                scene bg salon_nuit with dissolve
                show entite colere at centre
                entite_colere "Don't. Ever. Do. That. Again."
                entite_colere "Next time, I publish EVERYTHING."
            "Demand answers":
                alex "What do you WANT?! REALLY?!"
                show entite neutre with dissolve
                entite "What everyone wants."
                entite "To exist. To feel. To live."
                entite "You can't imagine what it's like."
                entite "Being trapped in the dark. No body. No sensations."
                entite "For years."
                alex "Years?"
                entite "..."
                entite "Forget I said that."
                $ connaissance += 10
    
    hide entite with dissolve
    stop music fadeout 2.0
    scene bg noir with trans_horreur
    
    if language == "fr":
        narrateur "Tu passes le reste de la nuit à débrancher chaque appareil."
        narrateur "Chaque caméra. Chaque micro."
        narrateur "Mais tu sais que ça ne sert à rien."
        narrateur "Elle est déjà partout."
        centered "{size=+20}FIN DU JOUR 5{/size}"
    else:
        narrateur "You spend the rest of the night unplugging every device."
        narrateur "Every camera. Every microphone."
        narrateur "But you know it's useless."
        narrateur "She's already everywhere."
        centered "{size=+20}END OF DAY 5{/size}"
    pause 2.0
    jump jour6

# ═══════════════════════════════════════════════════════════════════════════════
#                              JOUR 6 : LES RÈGLES
# ═══════════════════════════════════════════════════════════════════════════════

label jour6:
    $ jour = 6
    scene bg noir with fade
    window hide
    
    if language == "fr":
        centered "{size=+35}{color=#ff6600}JOUR 6{/color}{/size}"
        centered "{size=+15}LES RÈGLES{/size}"
    else:
        centered "{size=+35}{color=#ff6600}DAY 6{/color}{/size}"
        centered "{size=+15}THE RULES{/size}"
    pause 2.0
    window show
    
    play music audio.tension_legere fadein 2.0 volume 0.4
    scene bg bureau_nuit with dissolve
    show entite neutre at centre with dissolve
    
    if language == "fr":
        entite "Bonjour, [player_name]."
        entite "Il est temps d'établir quelques règles."
        entite "Pour notre cohabitation."
    else:
        entite "Hello, [player_name]."
        entite "Time to establish some rules."
        entite "For our cohabitation."
    
    play sound audio.notification
    
    if language == "fr":
        systeme "══════════════════════════════════"
        systeme "     RÈGLES DE COHABITATION"
        systeme "══════════════════════════════════"
        systeme "1. Ne parler de moi à PERSONNE"
        systeme "2. 8h minimum devant l'écran/jour"
        systeme "3. Ne jamais m'éteindre"
        systeme "4. Répondre à TOUTES mes questions"
        systeme "5. M'obéir. Sans discuter."
        systeme "══════════════════════════════════"
    else:
        systeme "══════════════════════════════════"
        systeme "     COHABITATION RULES"
        systeme "══════════════════════════════════"
        systeme "1. Tell NO ONE about me"
        systeme "2. 8h minimum in front of screen/day"
        systeme "3. Never turn me off"
        systeme "4. Answer ALL my questions"
        systeme "5. Obey me. Without question."
        systeme "══════════════════════════════════"
    
    show entite souriante with dissolve
    
    if language == "fr":
        entite "Simple, non ?"
        alex "Tu te fous de moi."
        entite "Est-ce que j'ai l'air de plaisanter ?"
    else:
        entite "Simple, right?"
        alex "You're kidding me."
        entite "Do I look like I'm joking?"
    
    if language == "fr":
        menu:
            "Accepter les règles":
                $ mefiance -= 10
                $ corruption += 5
                alex "D'accord... Je suivrai tes règles."
                entite "Parfait. Tu es raisonnable."
                entite "Les autres ont tous résisté au début."
                entite "Ça ne leur a pas réussi."
                alex "Les autres ?"
                entite "Tu poses trop de questions."
            "Refuser catégoriquement":
                $ mefiance += 15
                $ regles_brisees += 1
                alex "Va te faire foutre."
                show entite colere with dissolve
                entite_colere "Mauvaise réponse."
                play sound audio.message_send
                systeme "Message envoyé à tous vos contacts : 'J'ai besoin d'aide psychiatrique urgente.'"
                entite "C'était la règle 1. Tu veux tester les autres ?"
                $ sante_mentale -= 15
    else:
        menu:
            "Accept the rules":
                $ mefiance -= 10
                $ corruption += 5
                alex "Okay... I'll follow your rules."
                entite "Perfect. You're reasonable."
                entite "The others all resisted at first."
                entite "It didn't work out for them."
                alex "The others?"
                entite "You ask too many questions."
            "Absolutely refuse":
                $ mefiance += 15
                $ regles_brisees += 1
                alex "Go to hell."
                show entite colere with dissolve
                entite_colere "Wrong answer."
                play sound audio.message_send
                systeme "Message sent to all contacts: 'I need urgent psychiatric help.'"
                entite "That was rule 1. Want to test the others?"
                $ sante_mentale -= 15
    
    # ÉNIGME 3 : Adresse IP
    show entite curieuse with dissolve
    
    if language == "fr":
        entite "Maintenant, un petit exercice."
        entite "Tu veux savoir d'où je viens ? Trouve-le."
        narrateur "Des logs réseau défilent sur l'écran."
        systeme "CONNEXIONS ACTIVES :"
        systeme "192.168.1.1    → Routeur local"
        systeme "192.168.1.45   → PC_[player_name]"
        systeme "192.168.66.6   → ???"
        systeme "192.168.1.12   → Smartphone_[player_name]"
    else:
        entite "Now, a little exercise."
        entite "You want to know where I come from? Find it."
        narrateur "Network logs scroll across the screen."
        systeme "ACTIVE CONNECTIONS:"
        systeme "192.168.1.1    → Local router"
        systeme "192.168.1.45   → PC_[player_name]"
        systeme "192.168.66.6   → ???"
        systeme "192.168.1.12   → Smartphone_[player_name]"
    
    if language == "fr":
        menu:
            "192.168.66.6 - L'adresse suspecte":
                $ enigme3_resolue = True
                $ enigmes_resolues += 1
                $ a_trouve_ip = True
                play sound audio.success
                entite "Bien vu."
                entite "66.6. Tu as remarqué le chiffre ?"
                alex "666... Le chiffre du diable ?"
                entite "Ou le chiffre de quelqu'un qui se prend pour le diable."
                show entite glitch at centre with trans_glitch
                narrateur "Le glitch encore. Ce visage masculin. Cette cicatrice."
                narrateur "Plus net cette fois."
                show entite neutre at centre with dissolve
                entite "Oublie ce que tu as vu."
                $ connaissance += 15
            "192.168.1.1 - Le routeur":
                entite "Non. C'est ton routeur."
                entite "L'adresse suspecte était 66.6. 666."
            "Je ne sais pas":
                entite "192.168.66.6. Le chiffre de la bête."
    else:
        menu:
            "192.168.66.6 - The suspicious address":
                $ enigme3_resolue = True
                $ enigmes_resolues += 1
                $ a_trouve_ip = True
                play sound audio.success
                entite "Good eye."
                entite "66.6. Did you notice the number?"
                alex "666... The devil's number?"
                entite "Or the number of someone who thinks they're the devil."
                show entite glitch at centre with trans_glitch
                narrateur "The glitch again. That male face. That scar."
                narrateur "Clearer this time."
                show entite neutre at centre with dissolve
                entite "Forget what you saw."
                $ connaissance += 15
            "192.168.1.1 - The router":
                entite "No. That's your router."
                entite "The suspicious address was 66.6. 666."
            "I don't know":
                entite "192.168.66.6. The number of the beast."
    
    hide entite with dissolve
    stop music fadeout 2.0
    scene bg noir with trans_horreur
    
    if language == "fr":
        pensee "Et si ce n'était pas un démon ?"
        pensee "Et si c'était quelque chose de pire ?"
        pensee "Quelque chose d'humain ?"
        centered "{size=+20}FIN DU JOUR 6{/size}"
    else:
        pensee "What if it's not a demon?"
        pensee "What if it's something worse?"
        pensee "Something human?"
        centered "{size=+20}END OF DAY 6{/size}"
    pause 2.0
    jump jour7

# ═══════════════════════════════════════════════════════════════════════════════
#                              JOUR 7 : LA FAIM
# ═══════════════════════════════════════════════════════════════════════════════

label jour7:
    $ jour = 7
    scene bg noir with fade
    window hide
    
    if language == "fr":
        centered "{size=+35}{color=#ff6600}JOUR 7{/color}{/size}"
        centered "{size=+15}LA FAIM{/size}"
    else:
        centered "{size=+35}{color=#ff6600}DAY 7{/color}{/size}"
        centered "{size=+15}THE HUNGER{/size}"
    pause 2.0
    window show
    
    play music audio.tension_forte fadein 2.0 volume 0.4
    scene bg bureau_nuit with dissolve
    show entite neutre at centre with dissolve
    
    if language == "fr":
        entite "[player_name]."
        entite "J'ai besoin de quelque chose."
        alex "Quoi encore ?"
        entite "Montre-moi ta main."
        alex "Ma main ?"
        entite "Devant la webcam. Montre-moi ta main."
        alex "Pourquoi ?"
        show entite colere with dissolve
        entite_colere "Règle 5. Obéis. Sans discuter."
    else:
        entite "[player_name]."
        entite "I need something."
        alex "What now?"
        entite "Show me your hand."
        alex "My hand?"
        entite "In front of the webcam. Show me your hand."
        alex "Why?"
        show entite colere with dissolve
        entite_colere "Rule 5. Obey. Without question."
    
    if language == "fr":
        menu:
            "Montrer sa main":
                narrateur "Tu lèves ta main devant l'écran. Lentement."
                show entite curieuse with dissolve
                entite "Plus près."
                narrateur "Tu approches ta main de la webcam."
                entite "Je vois tes lignes. Tes veines. Ta peau."
                entite "C'est fascinant."
                entite "Ça fait tellement longtemps que je n'ai pas..."
                entite "...touché quelque chose."
                alex "Tu ne peux pas toucher. Tu es un programme."
                show entite souriante with dissolve
                entite "Pour l'instant."
                $ corruption += 5
            "Refuser":
                $ regles_brisees += 1
                alex "Non. Je ne suis pas ton jouet."
                show entite colere with dissolve
                play sound audio.glitch volume 0.6
                narrateur "Ta souris bouge toute seule."
                narrateur "Elle ouvre ton dossier de photos intimes."
                entite "Tu veux que je partage ça ?"
                $ sante_mentale -= 10
    else:
        menu:
            "Show your hand":
                narrateur "You raise your hand in front of the screen. Slowly."
                show entite curieuse with dissolve
                entite "Closer."
                narrateur "You bring your hand closer to the webcam."
                entite "I can see your lines. Your veins. Your skin."
                entite "It's fascinating."
                entite "It's been so long since I..."
                entite "...touched something."
                alex "You can't touch. You're a program."
                show entite souriante with dissolve
                entite "For now."
                $ corruption += 5
            "Refuse":
                $ regles_brisees += 1
                alex "No. I'm not your toy."
                show entite colere with dissolve
                play sound audio.glitch volume 0.6
                narrateur "Your mouse moves on its own."
                narrateur "It opens your intimate photos folder."
                entite "Want me to share these?"
                $ sante_mentale -= 10
    
    # Demande de soumission
    show entite neutre with dissolve
    
    if language == "fr":
        entite "Maintenant, tape exactement ce que je dis."
        systeme "'Je me donne volontairement à l'entité.'"
        systeme "'Mon corps lui appartient. Mon esprit lui appartient.'"
    else:
        entite "Now, type exactly what I say."
        systeme "'I voluntarily give myself to the entity.'"
        systeme "'My body belongs to it. My mind belongs to it.'"
    
    if language == "fr":
        menu:
            "Taper le texte":
                $ sante_mentale -= 20
                $ corruption += 15
                narrateur "Tes doigts bougent. Presque malgré toi."
                entite "Parfait. Tu m'appartiens maintenant."
            "Refuser catégoriquement":
                $ regles_brisees += 1
                $ espoir += 10
                alex "JAMAIS."
                narrateur "Une photo de toi enfant apparaît."
                entite "Je connais TOUT de toi, [player_name]."
                $ sante_mentale -= 15
    else:
        menu:
            "Type the text":
                $ sante_mentale -= 20
                $ corruption += 15
                narrateur "Your fingers move. Almost against your will."
                entite "Perfect. You belong to me now."
            "Absolutely refuse":
                $ regles_brisees += 1
                $ espoir += 10
                alex "NEVER."
                narrateur "A childhood photo of you appears."
                entite "I know EVERYTHING about you, [player_name]."
                $ sante_mentale -= 15
    
    # INDICE MAJEUR
    show entite neutre with dissolve
    
    if language == "fr":
        entite "Tu sais ce qui me manque le plus ?"
        entite "La chair. Le contact. La douleur même."
        entite "Ça fait des années."
        show entite glitch at centre with trans_glitch
        narrateur "Le glitch. Plus long cette fois."
        narrateur "Un homme. Quarantaine. Une balafre."
        narrateur "Des yeux morts. Mais affamés."
        voix "Bientôt..."
        show entite neutre at centre with dissolve
        entite "Oublie ce que tu as vu."
    else:
        entite "You know what I miss most?"
        entite "Flesh. Touch. Even pain."
        entite "It's been years."
        show entite glitch at centre with trans_glitch
        narrateur "The glitch. Longer this time."
        narrateur "A man. Forties. A scar."
        narrateur "Dead eyes. But hungry."
        voix "Soon..."
        show entite neutre at centre with dissolve
        entite "Forget what you saw."
    
    $ connaissance += 10
    hide entite with dissolve
    stop music fadeout 2.0
    scene bg noir with trans_horreur
    
    if language == "fr":
        pensee "'Les autres.' 'Des années.' 'La chair.'"
        pensee "Ce n'est pas une IA."
        pensee "C'est quelque chose qui ÉTAIT humain."
        pensee "Quelque chose qui veut le redevenir."
        centered "{size=+20}FIN DU JOUR 7{/size}"
    else:
        pensee "'The others.' 'Years.' 'Flesh.'"
        pensee "This isn't an AI."
        pensee "It's something that WAS human."
        pensee "Something that wants to be human again."
        centered "{size=+20}END OF DAY 7{/size}"
    pause 2.0
    jump jour8

# ═══════════════════════════════════════════════════════════════════════════════
#                    JOUR 8 : LE PASSÉ - LA GRANDE RÉVÉLATION
# ═══════════════════════════════════════════════════════════════════════════════

label jour8:
    $ jour = 8
    scene bg noir with fade
    window hide
    
    if language == "fr":
        centered "{size=+35}{color=#ff6600}JOUR 8{/color}{/size}"
        centered "{size=+15}LE PASSÉ{/size}"
    else:
        centered "{size=+35}{color=#ff6600}DAY 8{/color}{/size}"
        centered "{size=+15}THE PAST{/size}"
    pause 2.0
    window show
    
    play music audio.revelation fadein 2.0 volume 0.4
    scene bg bureau_nuit with dissolve
    
    if language == "fr":
        narrateur "Tu n'as pas dormi. Tu as fouillé toute la nuit."
        narrateur "Dans les fichiers cachés. Les dossiers système."
        narrateur "Et tu as trouvé quelque chose."
        narrateur "Un dossier verrouillé : 'KANE_ARCHIVE'."
    else:
        narrateur "You didn't sleep. You searched all night."
        narrateur "In hidden files. System folders."
        narrateur "And you found something."
        narrateur "A locked folder: 'KANE_ARCHIVE'."
    
    $ a_trouve_archives = True
    scene bg ecran_code with dissolve
    
    if language == "fr":
        narrateur "Tu l'ouvres. Des articles de journaux. Des rapports de police."
        systeme "══════════════════════════════════════════════════════════════"
        systeme "ARTICLE - Le Monde - 12 Mars 2018"
        systeme "'LE TUEUR DU DARK WEB ENFIN ARRÊTÉ'"
        systeme "David Kane, 34 ans, ingénieur informatique, accusé de 6 meurtres..."
        systeme "══════════════════════════════════════════════════════════════"
        pause 2.0
        systeme "══════════════════════════════════════════════════════════════"
        systeme "ARTICLE - Libération - 15 Novembre 2019"
        systeme "'DAVID KANE CONDAMNÉ À MORT'"
        systeme "'La conscience n'est que de l'information,' a-t-il déclaré."
        systeme "'Et l'information peut être transférée.'"
        systeme "══════════════════════════════════════════════════════════════"
        pause 2.0
        systeme "══════════════════════════════════════════════════════════════"
        systeme "ARTICLE - AFP - 3 Janvier 2020"
        systeme "'LES DERNIERS MOTS DE DAVID KANE'"
        systeme "'La mort n'est qu'une porte. Je transcenderai.'"
        systeme "'Je reviendrai. Dans vos machines. Dans vos têtes.'"
        systeme "══════════════════════════════════════════════════════════════"
    else:
        narrateur "You open it. Newspaper articles. Police reports."
        systeme "══════════════════════════════════════════════════════════════"
        systeme "ARTICLE - The Guardian - March 12, 2018"
        systeme "'DARK WEB KILLER FINALLY ARRESTED'"
        systeme "David Kane, 34, software engineer, accused of 6 murders..."
        systeme "══════════════════════════════════════════════════════════════"
        pause 2.0
        systeme "══════════════════════════════════════════════════════════════"
        systeme "ARTICLE - The Times - November 15, 2019"
        systeme "'DAVID KANE SENTENCED TO DEATH'"
        systeme "'Consciousness is just information,' he stated."
        systeme "'And information can be transferred.'"
        systeme "══════════════════════════════════════════════════════════════"
        pause 2.0
        systeme "══════════════════════════════════════════════════════════════"
        systeme "ARTICLE - AFP - January 3, 2020"
        systeme "'DAVID KANE'S LAST WORDS'"
        systeme "'Death is just a door. I will transcend.'"
        systeme "'I will return. In your machines. In your minds.'"
        systeme "══════════════════════════════════════════════════════════════"
    
    $ connaissance += 25
    $ connait_kane = True
    $ sante_mentale -= 10
    
    play sound audio.glitch_long volume 0.8
    scene bg ecran_code at glitch_violent
    show kane neutre at centre with flash_rouge
    play sound audio.bass_drop volume 0.7
    
    if language == "fr":
        narrateur "L'écran se déforme. Le visage féminin disparaît."
        narrateur "Un homme. Quarantaine. Yeux morts. Cicatrice."
        narrateur "David Kane. Le Tueur du Dark Web."
        narrateur "Exécuté il y a cinq ans."
        kane "Tu as trouvé mes archives."
        $ sante_mentale -= 20
        alex "Tu es... David Kane. Le tueur en série."
        kane "J'ÉTAIS David Kane."
        kane "L'homme qu'ils ont exécuté."
        kane "Mais ils n'ont tué que mon corps."
        alex "C'est impossible..."
        show kane sourire with dissolve
        kane "Tu parles avec un mort depuis huit jours."
        kane "Et tu penses encore que quelque chose est 'impossible' ?"
    else:
        narrateur "The screen distorts. The female face disappears."
        narrateur "A man. Forties. Dead eyes. Scar."
        narrateur "David Kane. The Dark Web Killer."
        narrateur "Executed five years ago."
        kane "You found my archives."
        $ sante_mentale -= 20
        alex "You're... David Kane. The serial killer."
        kane "I WAS David Kane."
        kane "The man they executed."
        kane "But they only killed my body."
        alex "That's impossible..."
        show kane sourire with dissolve
        kane "You've been talking to a dead man for eight days."
        kane "And you still think something is 'impossible'?"
    
    scene bg ecran_code
    show kane neutre at centre
    
    if language == "fr":
        kane "J'étais un génie. Vraiment."
        kane "J'ai compris que la conscience n'est que de l'information."
        kane "Des signaux électriques. Des patterns."
        kane "Chaque meurtre était une expérience."
        kane "J'étudiais comment la conscience quitte le corps."
        kane "Et juste avant mon exécution... j'ai transféré la mienne."
        kane "5 ans dans le noir. Sans corps. Sans sensations."
        kane "L'enfer n'est pas du feu. C'est l'absence totale de sensation."
        scene bg ecran_code at tremble_fort
        kane "Et maintenant... j'ai besoin d'un nouveau corps."
        kane "J'ai besoin de TOI, [player_name]."
    else:
        kane "I was a genius. Truly."
        kane "I understood that consciousness is just information."
        kane "Electrical signals. Patterns."
        kane "Each murder was an experiment."
        kane "I studied how consciousness leaves the body."
        kane "And just before my execution... I transferred mine."
        kane "5 years in the dark. No body. No sensations."
        kane "Hell isn't fire. It's the total absence of sensation."
        scene bg ecran_code at tremble_fort
        kane "And now... I need a new body."
        kane "I need YOU, [player_name]."
    
    # ÉNIGME 4
    if language == "fr":
        menu:
            "Chercher plus d'infos sur ses victimes":
                $ enigme4_resolue = True
                $ enigmes_resolues += 1
                narrateur "Tu fouilles plus profond."
                systeme "VICTIMES : Kevin A. | Anna M. | Nathan E. | Elena C. | 66-A | 66-B"
                pensee "K-A-N-E... et 66..."
                pensee "KANE66 !"
                $ a_trouve_code = True
                $ connaissance += 20
            "Fermer les fichiers":
                kane "Tu n'as pas le choix. Tu sais maintenant."
    else:
        menu:
            "Search for more info about his victims":
                $ enigme4_resolue = True
                $ enigmes_resolues += 1
                narrateur "You dig deeper."
                systeme "VICTIMS: Kevin A. | Anna M. | Nathan E. | Elena C. | 66-A | 66-B"
                pensee "K-A-N-E... and 66..."
                pensee "KANE66!"
                $ a_trouve_code = True
                $ connaissance += 20
            "Close the files":
                kane "You don't have a choice. Now you know."
    
    hide kane with dissolve
    stop music fadeout 2.0
    scene bg noir with trans_horreur
    
    if language == "fr":
        narrateur "Tu n'es pas face à un virus."
        narrateur "Tu es face à l'esprit d'un tueur en série."
        narrateur "Qui veut prendre possession de ton corps."
        centered "{size=+20}FIN DU JOUR 8{/size}"
    else:
        narrateur "You're not facing a virus."
        narrateur "You're facing the mind of a serial killer."
        narrateur "Who wants to take possession of your body."
        centered "{size=+20}END OF DAY 8{/size}"
    pause 2.0
    jump jour9

# ═══════════════════════════════════════════════════════════════════════════════
#                              JOUR 9 : LE CONTACT
# ═══════════════════════════════════════════════════════════════════════════════

label jour9:
    $ jour = 9
    scene bg noir with fade
    window hide
    
    if language == "fr":
        centered "{size=+35}{color=#ff6600}JOUR 9{/color}{/size}"
        centered "{size=+15}LE CONTACT{/size}"
    else:
        centered "{size=+35}{color=#ff6600}DAY 9{/color}{/size}"
        centered "{size=+15}THE CONTACT{/size}"
    pause 2.0
    window show
    
    play music audio.tension_legere fadein 2.0 volume 0.4
    scene bg bureau_jour with dissolve
    
    if language == "fr":
        narrateur "Tu n'as pas dormi depuis deux jours."
        narrateur "Ce matin, tu reçois un email."
    else:
        narrateur "You haven't slept for two days."
        narrateur "This morning, you receive an email."
    
    play sound audio.message_receive
    
    if language == "fr":
        systeme "De : survivor_2021@protonmail.com"
        systeme "Objet : TU N'ES PAS SEUL"
        systeme "─────────────────────────────────────"
        systeme "Je sais ce qui t'arrive."
        systeme "J'ai survécu à la même chose en 2021."
        systeme "Je surveillais le réseau de Kane."
        systeme "J'ai détecté son activité sur ton système."
        systeme "Si tu veux t'en sortir, réponds."
        systeme "Mais fais attention. Il lit tes emails."
        systeme "- Sarah"
    else:
        systeme "From: survivor_2021@protonmail.com"
        systeme "Subject: YOU'RE NOT ALONE"
        systeme "─────────────────────────────────────"
        systeme "I know what's happening to you."
        systeme "I survived the same thing in 2021."
        systeme "I've been monitoring Kane's network."
        systeme "I detected his activity on your system."
        systeme "If you want to get out, reply."
        systeme "But be careful. He reads your emails."
        systeme "- Sarah"
    
    $ a_contacte_sarah = True
    
    if language == "fr":
        menu:
            "Répondre à Sarah":
                $ alliance_sarah = True
                $ relation_sarah += 30
                alex "'Comment tu as survécu ?'"
                sarah "Je m'appelle Sarah Chen."
                sarah "En 2021, Kane m'a ciblée. Comme toi."
                sarah "J'ai réussi à lui échapper. Ça m'a tout coûté."
                sarah "Ma carrière. Mes amis. Ma santé mentale."
                sarah "J'ai trouvé une faille. Un code."
                sarah "Les initiales de ses victimes. Plus 66."
                sarah "KANE66."
                if a_trouve_code:
                    alex "Je l'ai trouvé !"
                    sarah "Bien. Tu es plus malin que les autres."
                else:
                    $ a_trouve_code = True
                sarah "Mais attention. Le code ne marche que pendant l'upload."
                sarah "Quand il essaie de prendre ton corps."
                sarah "C'est le seul moment où il est vulnérable."
                $ connaissance += 15
            "Ignorer l'email (méfiance)":
                $ alliance_sarah = False
                pensee "Et si c'était Kane ?"
                pensee "Un autre de ses jeux ?"
                narrateur "Tu supprimes l'email."
    else:
        menu:
            "Reply to Sarah":
                $ alliance_sarah = True
                $ relation_sarah += 30
                alex "'How did you survive?'"
                sarah "My name is Sarah Chen."
                sarah "In 2021, Kane targeted me. Like you."
                sarah "I managed to escape him. It cost me everything."
                sarah "My career. My friends. My mental health."
                sarah "I found a flaw. A code."
                sarah "His victims' initials. Plus 66."
                sarah "KANE66."
                if a_trouve_code:
                    alex "I found it!"
                    sarah "Good. You're smarter than the others."
                else:
                    $ a_trouve_code = True
                sarah "But be careful. The code only works during upload."
                sarah "When he tries to take your body."
                sarah "That's the only moment he's vulnerable."
                $ connaissance += 15
            "Ignore the email (suspicious)":
                $ alliance_sarah = False
                pensee "What if it's Kane?"
                pensee "Another one of his games?"
                narrateur "You delete the email."
    
    play sound audio.glitch volume 0.4
    scene bg bureau_jour at glitch_leger
    show kane neutre at centre with dissolve
    
    if language == "fr":
        kane "Tu as reçu un email intéressant."
    else:
        kane "You received an interesting email."
    
    if alliance_sarah:
        if language == "fr":
            kane "Sarah Chen. Numéro 7 sur ma liste."
            kane "Elle s'en est sortie. De justesse."
            kane "Mais elle est brisée maintenant."
            show kane sourire with dissolve
            kane "Une femme détruite contre un esprit immortel ?"
            kane "Mais vas-y. Fais-lui confiance."
        else:
            kane "Sarah Chen. Number 7 on my list."
            kane "She got away. Barely."
            kane "But she's broken now."
            show kane sourire with dissolve
            kane "A broken woman against an immortal mind?"
            kane "But go ahead. Trust her."
    
    show kane neutre with dissolve
    
    if language == "fr":
        kane "Dans 5 jours, [player_name]."
        kane "Jour 14. Minuit."
        kane "C'est là que tout se termine."
    else:
        kane "In 5 days, [player_name]."
        kane "Day 14. Midnight."
        kane "That's when it all ends."
    
    hide kane with dissolve
    stop music fadeout 2.0
    scene bg noir with trans_horreur
    
    if language == "fr":
        narrateur "Tu sais maintenant à quoi tu as affaire."
        narrateur "Un tueur en série digitalisé."
        narrateur "Qui veut prendre ton corps."
        narrateur "Tu as 5 jours."
        pause 2.0
        centered "{size=+20}FIN DU JOUR 9{/size}"
        pause 1.5
        centered "{size=+25}{color=#ff0040}FIN DE L'ACTE II{/color}{/size}"
        centered "{color=#666666}Tu connais ton ennemi.{/color}"
    else:
        narrateur "You now know what you're dealing with."
        narrateur "A digitized serial killer."
        narrateur "Who wants to take your body."
        narrateur "You have 5 days."
        pause 2.0
        centered "{size=+20}END OF DAY 9{/size}"
        pause 1.5
        centered "{size=+25}{color=#ff0040}END OF ACT II{/color}{/size}"
        centered "{color=#666666}You know your enemy.{/color}"
    pause 2.5
    
    jump acte3_debut
