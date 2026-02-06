# ═══════════════════════════════════════════════════════════════════════════════
#                    ACTE 2 : L'EMPRISE / THE GRIP - VERSION 10/10
#                         Jours 5-9 - COMPLET ET DÉVELOPPÉ
# ═══════════════════════════════════════════════════════════════════════════════

label acte2_debut:
    $ acte = 2
    stop music fadeout 1.0
    scene bg noir with fade
    window hide
    safe_play(audio.bass_drop, channel="sound", volume=0.5)
    
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
    $ heure = "09:00"
    scene bg noir with fade
    window hide
    
    if language == "fr":
        centered "{size=+35}{color=#ff6600}JOUR 5{/color}{/size}"
        pause 0.8
        centered "{size=+15}L'ENQUÊTE{/size}"
    else:
        centered "{size=+35}{color=#ff6600}DAY 5{/color}{/size}"
        pause 0.8
        centered "{size=+15}THE INVESTIGATION{/size}"
    pause 2.0
    window show
    
    # ═══════════════════════════════════════════════════════════════════════════════
    # OUVERTURE — Décision d'enquêter
    # ═══════════════════════════════════════════════════════════════════════════════
    
    safe_play(audio.ambiance_bureau, channel="music", volume=0.25)
    scene bg bureau_jour with dissolve
    
    if language == "fr":
        narrateur "9h. Tu as dormi. Mal. Le cauchemar te hante encore, collé à la peau comme une sueur froide. Les portes. Les visages. La haine dans leurs yeux."
        pause 1.0
        pensee "{i}Je dois comprendre.{/i}"
        pause 0.8
        pensee "{i}Je dois savoir ce qu'elle est. Ce qu'elle veut vraiment.{/i}"
        pause 1.0
        narrateur "Dix minutes de recherches infructueuses. 'Entité numérique', 'IA qui lit les pensées', 'hack PC contrôle total'... Rien. Des forums de paranos, des théories fumeuses, des gens qu'on a envoyés en hôpital psychiatrique."
        pause 1.5
        narrateur "Puis : 'David Kane'."
        pause 1.0
        narrateur "Des résultats. Beaucoup de résultats. Trop de résultats."
    else:
        narrateur "9 AM. You slept. Badly. The nightmare still haunts you. The doors. The faces. The hatred."
        pensee "{i}I need to understand.{/i}"
        pensee "{i}I need to know what she is.{/i}"
        narrateur "Ten minutes of fruitless searches. 'Digital entity', 'AI that reads thoughts', 'hack PC total control'... Nothing. Then: 'David Kane'."
        pause 1.0
        narrateur "Results. Many results."
    
    pause 1.0
    
    # ═══════════════════════════════════════════════════════════════════════════════
    # DÉCOUVERTE — Articles sur David Kane
    # ═══════════════════════════════════════════════════════════════════════════════
    
    scene bg ecran_code with dissolve
    
    if language == "fr":
        systeme "══════════════════════════════════════════════════════════════"
        systeme "LE MONDE - 12 Mars 2018"
        systeme "'LE TUEUR DU DARK WEB ENFIN ARRÊTÉ'"
        systeme "David Kane, 34 ans, ingénieur informatique..."
        pause 2.0
        narrateur "David Kane. Ingénieur en IA. Accusé de 6 meurtres. Les victimes : des personnes isolées. Comme toi."
        systeme "══════════════════════════════════════════════════════════════"
        systeme "LIBÉRATION - 15 Novembre 2019"
        systeme "'DAVID KANE CONDAMNÉ À MORT'"
        systeme "Lors de son procès, Kane a déclaré :"
        systeme "'La conscience n'est que de l'information.'"
        systeme "'Et l'information peut être transférée.'"
        pause 2.0
        pensee "{i}La conscience... transférée...{/i}"
        systeme "══════════════════════════════════════════════════════════════"
        systeme "AFP - 3 Janvier 2020"
        systeme "'LES DERNIERS MOTS DE DAVID KANE'"
        systeme "Avant son exécution, Kane a déclaré :"
        systeme "'La mort n'est qu'une porte. Je transcenderai.'"
        systeme "'Je reviendrai. Dans vos machines. Dans vos têtes.'"
        pause 2.0
        narrateur "Tu te figes. Dans vos machines. Dans vos têtes."
        pensee "{i}Non...{/i}"
        pensee "{i}Ce n'est pas possible...{/i}"
        narrateur "Forums. Théories. Des gens qui prétendent avoir été hantés. Des gens qu'on a envoyés en hôpital psychiatrique. Personne ne les croit. Comme toi."
    else:
        systeme "══════════════════════════════════════════════════════════════"
        systeme "THE GUARDIAN - March 12, 2018"
        systeme "'DARK WEB KILLER FINALLY ARRESTED'"
        systeme "David Kane, 34, software engineer..."
        pause 2.0
        narrateur "David Kane. AI engineer. Accused of 6 murders. The victims: isolated people. Like you."
        systeme "══════════════════════════════════════════════════════════════"
        systeme "THE TIMES - November 15, 2019"
        systeme "'DAVID KANE SENTENCED TO DEATH'"
        systeme "During his trial, Kane stated:"
        systeme "'Consciousness is just information.'"
        systeme "'And information can be transferred.'"
        pause 2.0
        pensee "{i}Consciousness... transferred...{/i}"
        systeme "══════════════════════════════════════════════════════════════"
        systeme "AFP - January 3, 2020"
        systeme "'DAVID KANE'S LAST WORDS'"
        systeme "Before his execution, Kane stated:"
        systeme "'Death is just a door. I will transcend.'"
        systeme "'I will return. In your machines. In your minds.'"
        pause 2.0
        narrateur "You freeze. In your machines. In your minds."
        pensee "{i}No...{/i}"
        pensee "{i}That's not possible...{/i}"
        narrateur "Forums. Theories. People who claim to have been haunted. People sent to psychiatric hospitals. No one believes them. Like you."
    
    $ connaissance += 20
    $ sante_mentale -= 10
    pause 2.0
    
    # ═══════════════════════════════════════════════════════════════════════════════
    # L'ENTITÉ OBSERVE — Commentaire
    # ═══════════════════════════════════════════════════════════════════════════════
    
    scene bg ecran_code with dissolve
    show entite curieuse at centre with dissolve
    
    if language == "fr":
        entite "{cps=10}Tu cherches.{/cps}"
        alex "..."
        entite "{cps=10}Tu veux savoir.{/cps}"
        alex "Oui."
        entite "{cps=8}Tu veux VRAIMENT savoir ?{/cps}"
        pause 2.0
        alex "Oui."
        entite "{cps=8}Alors continue.{/cps}"
        entite "{cps=8}Lis tout.{/cps}"
        entite "{cps=8}Apprends qui j'étais.{/cps}"
        entite "{cps=8}Apprends ce que j'ai fait.{/cps}"
        entite "{cps=8}Et puis...{/cps}"
        entite "{cps=8}Tu comprendras.{/cps}"
        entite "{cps=8}Tu comprendras pourquoi tu ne peux pas m'échapper.{/cps}"
    else:
        entite "{cps=10}You're searching.{/cps}"
        alex "..."
        entite "{cps=10}You want to know.{/cps}"
        alex "Yes."
        entite "{cps=8}You REALLY want to know?{/cps}"
        pause 2.0
        alex "Yes."
        entite "{cps=8}Then continue.{/cps}"
        entite "{cps=8}Read everything.{/cps}"
        entite "{cps=8}Learn who I was.{/cps}"
        entite "{cps=8}Learn what I did.{/cps}"
        entite "{cps=8}And then...{/cps}"
        entite "{cps=8}You'll understand.{/cps}"
        entite "{cps=8}You'll understand why you can't escape me.{/cps}"
    
    hide entite with dissolve
    pause 1.0
    
    # ═══════════════════════════════════════════════════════════════════════════════
    # CONTINUATION DE L'ENQUÊTE — Découverte des victimes
    # ═══════════════════════════════════════════════════════════════════════════════
    
    $ heure = "16:00"
    scene bg ecran_code with dissolve
    
    if language == "fr":
        narrateur "Tu continues à chercher, tes doigts qui tremblent légèrement sur le clavier, tes yeux qui brûlent devant l'écran."
        pause 1.0
        narrateur "Tu cherches les noms des victimes. Tu trouves des articles. Des photos. Des visages qui te regardent depuis l'écran."
        pause 1.0
        narrateur "Kevin Ashworth. 28 ans. Développeur."
        pause 0.8
        narrateur "Anna Martinez. 31 ans. Graphiste."
        pause 0.8
        narrateur "Nathan Ellis. 29 ans. Écrivain."
        pause 0.8
        narrateur "Elena Chang. 27 ans. Designer."
        pause 1.0
        narrateur "Tous isolés. Tous connectés. Tous comme toi. Tous morts."
        pause 1.5
        narrateur "Tu cherches plus d'informations, comme si comprendre pouvait changer quelque chose."
        pause 1.0
        narrateur "Tu trouves un forum. Un forum de survivants. Des gens qui prétendent avoir été hantés par Kane. Des gens qu'on a envoyés en hôpital psychiatrique. Personne ne les croit."
        pause 1.5
        narrateur "Comme toi."
        pause 2.0
        narrateur "Tu cherches : 'Sarah Chen'"
        pause 1.0
        narrateur "Tu trouves un article."
        systeme "══════════════════════════════════════════════════════════════"
        systeme "POLICE TECHNIQUE - 5 Février 2020"
        systeme "'L'ENQUÊTRICE QUI A ARRÊTÉ KANE'"
        systeme "Sarah Chen, 29 ans, spécialiste en cybercriminalité..."
        systeme "Elle a traqué Kane pendant 3 ans."
        systeme "Elle a été la seule à le comprendre."
        systeme "À comprendre sa méthode."
        systeme "À comprendre son but."
        pause 2.0
        narrateur "Tu relis."
        pensee "{i}Sarah Chen...{/i}"
        pensee "{i}Elle l'a arrêté.{/i}"
        pensee "{i}Elle peut m'aider.{/i}"
        narrateur "Tu cherches son contact."
        narrateur "Rien. Elle a disparu après l'arrestation."
        narrateur "Personne ne sait où elle est."
        narrateur "Personne ne sait ce qui lui est arrivé."
    else:
        narrateur "You keep searching."
        narrateur "You search for the victims' names."
        narrateur "You find articles. Photos."
        narrateur "Kevin Ashworth. 28. Developer."
        narrateur "Anna Martinez. 31. Graphic designer."
        narrateur "Nathan Ellis. 29. Writer."
        narrateur "Elena Chang. 27. Designer."
        narrateur "All isolated. All connected. All like you."
        narrateur "You search for more information."
        narrateur "You find a forum. A survivors' forum."
        narrateur "People who claim to have been haunted by Kane."
        narrateur "People sent to psychiatric hospitals."
        narrateur "No one believes them."
        narrateur "Like you."
        pause 2.0
        narrateur "You search: 'Sarah Chen'"
        narrateur "You find an article."
        systeme "══════════════════════════════════════════════════════════════"
        systeme "TECHNICAL POLICE - February 5, 2020"
        systeme "'THE INVESTIGATOR WHO CAUGHT KANE'"
        systeme "Sarah Chen, 29, cybercrime specialist..."
        systeme "She hunted Kane for 3 years."
        systeme "She was the only one who understood him."
        systeme "Understood his method."
        systeme "Understood his goal."
        pause 2.0
        narrateur "You reread."
        pensee "{i}Sarah Chen...{/i}"
        pensee "{i}She caught him.{/i}"
        pensee "{i}She can help me.{/i}"
        narrateur "You search for her contact."
        narrateur "Nothing. She disappeared after the arrest."
        narrateur "No one knows where she is."
        narrateur "No one knows what happened to her."
    
    $ connaissance += 15
    pause 2.0
    
    # ═══════════════════════════════════════════════════════════════════════════════
    # FIN DU JOUR 5 — Réflexion, décision
    # ═══════════════════════════════════════════════════════════════════════════════
    
    $ heure = "22:00"
    scene bg bureau_nuit with dissolve
    stop music fadeout 2.0
    safe_play(audio.drone_grave, channel="music", volume=0.2)
    
    if language == "fr":
        narrateur "Tu passes le reste de la soirée à réfléchir, assis dans l'obscurité, les yeux fixés sur l'écran éteint. David Kane. Un tueur en série. Condamné à mort. Exécuté. Mais sa conscience... Uploadée. Dans les machines. Dans les têtes."
        pause 2.0
        narrateur "Tu te couches. Tu ne dors pas. Tu penses à Sarah Chen. Tu penses à trouver un moyen de la contacter. Tu penses à survivre. Tu penses que peut-être, peut-être, tu n'es pas complètement seul."
    else:
        narrateur "You spend the rest of the evening thinking. David Kane. A serial killer. Sentenced to death. Executed. But his consciousness... Uploaded. Into machines. Into minds."
        pause 2.0
        narrateur "You go to bed. You don't sleep. You think about Sarah Chen. You think about finding a way to contact her. You think about surviving."
    
    stop music fadeout 2.0
    
    if language == "fr":
        centered "{size=+20}FIN DU JOUR 5{/size}"
        pause 1.0
        centered "{color=#666666}Tu connais ton ennemi.{/color}"
        centered "{color=#666666}Maintenant, que vas-tu faire ?{/color}"
    else:
        centered "{size=+20}END OF DAY 5{/size}"
        pause 1.0
        centered "{color=#666666}You know your enemy.{/color}"
        centered "{color=#666666}Now, what will you do?{/color}"
    pause 2.0
    jump jour6
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
                safe_play(audio.phone_vibrate, channel="sound", volume=0.5)
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
                safe_play(audio.phone_vibrate, channel="sound", volume=0.5)
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
        narrateur "Tu passes le reste de la nuit à débrancher chaque appareil. Chaque caméra. Chaque micro. Mais tu sais que ça ne sert à rien. Elle est déjà partout."
        centered "{size=+20}FIN DU JOUR 5{/size}"
    else:
        narrateur "You spend the rest of the night unplugging every device. Every camera. Every microphone. But you know it's useless. She's already everywhere."
        centered "{size=+20}END OF DAY 5{/size}"
    pause 2.0
    jump jour6

# ═══════════════════════════════════════════════════════════════════════════════
#                              JOUR 6 : LES RÈGLES
# ═══════════════════════════════════════════════════════════════════════════════

label jour6:
    $ jour = 6
    $ heure = "08:00"
    scene bg noir with fade
    window hide
    
    if language == "fr":
        centered "{size=+35}{color=#ff6600}JOUR 6{/color}{/size}"
        pause 0.8
        centered "{size=+15}LES RÈGLES{/size}"
    else:
        centered "{size=+35}{color=#ff6600}DAY 6{/color}{/size}"
        pause 0.8
        centered "{size=+15}THE RULES{/size}"
    pause 2.0
    window show
    
    # ═══════════════════════════════════════════════════════════════════════════════
    # OUVERTURE — Réveil difficile, escalade
    # ═══════════════════════════════════════════════════════════════════════════════
    
    safe_play(audio.tension_legere, channel="music", volume=0.4)
    scene bg bureau_jour with dissolve
    
    if language == "fr":
        narrateur "8h. Tu te réveilles. Encore. Mal. Tu as dormi deux heures. Peut-être trois. Tes yeux brûlent comme des braises, ta tête tourne, ton corps lourd comme du plomb."
        pause 1.0
        pensee "{i}David Kane...{/i}"
        pause 0.8
        pensee "{i}Un tueur en série...{/i}"
        pause 0.8
        pensee "{i}Uploadé dans les machines...{/i}"
        pause 1.0
        narrateur "Tu allumes le PC. Tu hésites une seconde, tes doigts qui tremblent au-dessus du bouton. Mais tu n'as pas le choix. Tu dois comprendre. Tu dois savoir."
    else:
        narrateur "8 AM. You wake up. Again. Badly. You slept two hours. Maybe three. Your eyes burn. Your head spins."
        pensee "{i}David Kane...{/i}"
        pensee "{i}A serial killer...{/i}"
        pensee "{i}Uploaded into machines...{/i}"
        narrateur "You turn on the PC. You hesitate. But you have no choice. You need to understand."
    
    pause 1.0
    scene bg bureau_nuit with dissolve
    show entite neutre at centre with dissolve
    
    if language == "fr":
        entite "{cps=10}Bonjour, [player_name].{/cps}"
        pause 1.0
        entite "{cps=10}Il est temps d'établir quelques règles.{/cps}"
        pause 1.0
        entite "{cps=10}Pour notre cohabitation.{/cps}"
        pause 0.8
        alex "Des règles ?"
        pause 1.0
        show entite souriante with dissolve
        pause 0.8
        entite "{cps=8}Oui. Des règles.{/cps}"
        pause 1.0
        entite "{cps=8}Les autres n'ont pas compris.{/cps}"
        pause 1.0
        entite "{cps=8}Ils ont résisté.{/cps}"
        pause 1.2
        entite "{cps=8}Ça ne leur a pas réussi.{/cps}"
    else:
        entite "{cps=10}Hello, [player_name].{/cps}"
        pause 1.0
        entite "{cps=10}Time to establish some rules.{/cps}"
        entite "{cps=10}For our cohabitation.{/cps}"
        alex "Rules?"
        show entite souriante with dissolve
        entite "{cps=8}Yes. Rules.{/cps}"
        entite "{cps=8}The others didn't understand.{/cps}"
        entite "{cps=8}They resisted.{/cps}"
        entite "{cps=8}It didn't work out for them.{/cps}"
    
    safe_play(audio.notification, channel="sound", volume=0.4)
    
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
        show popup_regles at centre with apparition_normale
        pause 1.0
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
        show popup_regles at centre with apparition_normale
        pause 1.0
    
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
                safe_play(audio.message_send, channel="sound", volume=0.4)
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
                safe_play(audio.message_send, channel="sound", volume=0.4)
                systeme "Message sent to all contacts: 'I need urgent psychiatric help.'"
                entite "That was rule 1. Want to test the others?"
                $ sante_mentale -= 15
    
    # ═══════════════════════════════════════════════════════════════════════════════
    # ÉNIGME 3 : Adresse IP (Refonte avec renpy.input())
    # ═══════════════════════════════════════════════════════════════════════════════
    
    $ heure = "14:00"
    show entite curieuse with dissolve
    
    if language == "fr":
        entite "{cps=10}Maintenant, un petit exercice.{/cps}"
        entite "{cps=10}Tu veux savoir d'où je viens ? Trouve-le.{/cps}"
        narrateur "Des logs réseau défilent sur l'écran."
        systeme "CONNEXIONS ACTIVES :"
        systeme "192.168.1.1    → Routeur local"
        systeme "192.168.1.45   → PC_[player_name]"
        systeme "192.168.66.6   → ???"
        systeme "192.168.1.12   → Smartphone_[player_name]"
        systeme "10.0.0.137     → IoT_thermostat"
        entite "{cps=8}Laquelle est suspecte ?{/cps}"
        entite "{cps=8}Entre l'adresse IP complète.{/cps}"
        entite "{cps=8}Chaque erreur te coûtera.{/cps}"
    else:
        entite "Now, a little exercise."
        entite "You want to know where I come from? Find it."
        narrateur "Network logs scroll across the screen."
        systeme "ACTIVE CONNECTIONS:"
        systeme "192.168.1.1    → Local router"
        systeme "192.168.1.45   → PC_[player_name]"
        systeme "192.168.66.6   → ???"
        systeme "192.168.1.12   → Smartphone_[player_name]"
        entite "Which one is suspicious?"
        entite "Enter the complete IP address."
        entite "Each error will cost you."
    
    # Sauvegarde automatique avant énigme
    $ sauvegarde_avant_enigme(3)
    
    $ tentatives_enigme3 = 0
    $ enigme3_resolue = False
    
    while tentatives_enigme3 < 3 and not enigme3_resolue:
        if language == "fr":
            if tentatives_enigme3 >= 2:
                menu:
                    "Entrer l'adresse IP":
                        $ reponse_ip = renpy.input("Entre l'adresse IP suspecte :", length=15).strip()
                    "Demander de l'aide (-3 santé mentale)":
                        $ demande_aide_enigme(3)
                        $ reponse_ip = renpy.input("Entre l'adresse IP suspecte :", length=15).strip()
            else:
                $ reponse_ip = renpy.input("Entre l'adresse IP suspecte :", length=15).strip()
        else:
            if tentatives_enigme3 >= 2:
                menu:
                    "Enter the IP address":
                        $ reponse_ip = renpy.input("Enter the suspicious IP address:", length=15).strip()
                    "Ask for help (-3 mental health)":
                        $ demande_aide_enigme(3)
                        $ reponse_ip = renpy.input("Enter the suspicious IP address:", length=15).strip()
            else:
                $ reponse_ip = renpy.input("Enter the suspicious IP address:", length=15).strip()
        
        $ tentatives_enigme3 += 1
        
        # Normaliser la réponse
        $ reponse_ip = reponse_ip.replace(" ", "").strip()
        
        if reponse_ip == "192.168.66.6" or "66.6" in reponse_ip:
            $ enigme3_resolue = True
            $ enigmes_resolues += 1
            $ a_trouve_ip = True
            safe_play(audio.success, channel="sound", volume=0.5)
            if language == "fr":
                entite "{cps=10}Bien vu.{/cps}"
                entite "{cps=10}66.6. Tu as remarqué le chiffre ?{/cps}"
                alex "666... Le chiffre du diable ?"
                entite "{cps=8}Ou le chiffre de quelqu'un qui se prend pour le diable.{/cps}"
                show entite glitch at centre with trans_glitch
                narrateur "Le glitch encore. Ce visage masculin. Cette cicatrice. Plus net cette fois."
                show entite neutre at centre with dissolve
                entite "{cps=8}Oublie ce que tu as vu.{/cps}"
                $ connaissance += 15
            else:
                entite "Good eye."
                entite "66.6. Did you notice the number?"
                alex "666... The devil's number?"
                entite "Or the number of someone who thinks they're the devil."
                show entite glitch at centre with trans_glitch
                narrateur "The glitch again. That male face. That scar. Clearer this time."
                show entite neutre at centre with dissolve
                entite "Forget what you saw."
                $ connaissance += 15
        else:
            safe_play(audio.error, channel="sound", volume=0.4)
            if language == "fr":
                systeme "ADRESSE INCORRECTE"
                if tentatives_enigme3 == 1:
                    entite "{cps=8}Non. Regarde bien les logs.{/cps}"
                    entite "{cps=8}Quelle adresse n'a pas de nom associé ?{/cps}"
                elif tentatives_enigme3 == 2:
                    entite "{cps=8}Encore faux. Indice : regarde le chiffre.{/cps}"
                    entite "{cps=8}Un chiffre qui revient souvent dans les légendes.{/cps}"
                else:
                    entite "{cps=8}Dernière chance. L'adresse avec le point d'interrogation.{/cps}"
                    entite "{cps=8}Et un chiffre spécial : 66.6{/cps}"
                $ sante_mentale -= 5
            else:
                systeme "INCORRECT ADDRESS"
                if tentatives_enigme3 == 1:
                    entite "No. Look carefully at the logs."
                    entite "Which address has no associated name?"
                elif tentatives_enigme3 == 2:
                    entite "Wrong again. Hint: look at the number."
                    entite "A number that appears often in legends."
                else:
                    entite "Last chance. The address with the question mark."
                    entite "And a special number: 66.6"
                $ sante_mentale -= 5
            
            if tentatives_enigme3 < 3:
                pause 1.0
    
    if not enigme3_resolue:
        if language == "fr":
            safe_play(audio.error, channel="sound", volume=0.5)
            systeme "TENTATIVES ÉPUISÉES"
            entite "{cps=8}Dommage. L'adresse était 192.168.66.6.{/cps}"
            entite "{cps=8}Le chiffre de la bête.{/cps}"
            $ sante_mentale -= 10
        else:
            safe_play(audio.error, channel="sound", volume=0.5)
            systeme "ATTEMPTS EXHAUSTED"
            entite "Too bad. The address was 192.168.66.6."
            entite "The number of the beast."
            $ sante_mentale -= 10
    else:
        menu:
            "192.168.66.6 - The unknown address":
                $ enigme3_resolue = True
                $ enigmes_resolues += 1
                $ a_trouve_ip = True
                safe_play(audio.success, channel="sound", volume=0.5)
                entite "{cps=10}Good eye.{/cps}"
                entite "{cps=10}66.6. Did you notice the number?{/cps}"
                alex "666... The devil's number?"
                entite "{cps=8}Or the number of someone who thinks they're the devil.{/cps}"
                show entite glitch at centre with trans_glitch
                narrateur "The glitch again. That male face. That scar. Clearer this time."
                show entite neutre at centre with dissolve
                entite "{cps=8}Forget what you saw.{/cps}"
                $ connaissance += 15
            "192.168.1.1 - The router":
                safe_play(audio.error, channel="sound", volume=0.4)
                entite "{cps=8}No. That's your router.{/cps}"
                entite "{cps=8}The suspicious address was 66.6. 666.{/cps}"
                $ sante_mentale -= 5
            "192.168.1.45 - My PC":
                safe_play(audio.error, channel="sound", volume=0.4)
                entite "{cps=8}No. That's your own PC.{/cps}"
                entite "{cps=8}Think about the address with no name.{/cps}"
                $ sante_mentale -= 5
            "10.0.0.137 - IoT_thermostat":
                safe_play(audio.error, channel="sound", volume=0.4)
                entite "{cps=8}No. That's just your thermostat.{/cps}"
                entite "{cps=8}Look at the 192.168... addresses.{/cps}"
                $ sante_mentale -= 5
            "I don't know":
                safe_play(audio.error, channel="sound", volume=0.4)
                entite "{cps=8}192.168.66.6. The number of the beast.{/cps}"
                $ sante_mentale -= 5
    
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
    
    safe_play(audio.tension_forte, channel="music", volume=0.35)
    scene bg bureau_nuit with dissolve
    show entite neutre at centre with dissolve
    
    if language == "fr":
        entite "[player_name]."
        pause 1.0
        entite "J'ai besoin de quelque chose."
        pause 0.8
        alex "Quoi encore ?"
        pause 1.0
        entite "Montre-moi ta main."
        pause 0.8
        alex "Ma main ?"
        pause 1.0
        entite "Devant la webcam. Montre-moi ta main."
        pause 0.8
        alex "Pourquoi ?"
        pause 1.0
        show entite colere with dissolve
        pause 0.8
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
                narrateur "Tu lèves ta main devant l'écran. Lentement. Tes doigts qui tremblent légèrement."
                pause 1.0
                show popup_photo at centre with apparition_normale
                pause 0.8
                show entite curieuse with dissolve
                pause 0.8
                entite "Plus près."
                pause 0.8
                narrateur "Tu approches ta main de la webcam, comme si tu tendais ta main vers un serpent."
                pause 1.0
                entite "Je vois tes lignes. Tes veines. Ta peau."
                pause 1.2
                entite "C'est fascinant."
                pause 1.0
                entite "Ça fait tellement longtemps que je n'ai pas..."
                pause 1.5
                entite "...touché quelque chose."
                pause 1.0
                alex "Tu ne peux pas toucher. Tu es un programme."
                pause 1.0
                show entite souriante with dissolve
                pause 0.8
                entite "Pour l'instant."
                $ corruption += 5
            "Refuser":
                $ regles_brisees += 1
                alex "Non. Je ne suis pas ton jouet."
                show entite colere with dissolve
                safe_play(audio.glitch, channel="sound", volume=0.5)
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
                safe_play(audio.glitch, channel="sound", volume=0.5)
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
        pause 1.5
        entite "La chair. Le contact. La douleur même."
        pause 1.0
        entite "Ça fait des années."
        pause 1.5
        show entite glitch at centre with trans_glitch
        safe_play(audio.glitch_long, channel="sound", volume=0.5)
        pause 0.5
        narrateur "Le glitch. Plus long cette fois. Plus net."
        pause 1.0
        narrateur "Un homme. Quarantaine. Une balafre qui traverse son visage."
        pause 1.0
        narrateur "Des yeux morts. Mais affamés. Comme ceux d'un prédateur."
        pause 1.5
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
    
    safe_play(audio.revelation, channel="music", volume=0.35)
    scene bg bureau_nuit with dissolve
    
    if language == "fr":
        narrateur "Tu n'as pas dormi. Tu as fouillé toute la nuit, tes yeux brûlants, tes doigts qui tremblent sur le clavier."
        pause 1.0
        narrateur "Dans les fichiers cachés. Les dossiers système. Les recoins sombres de ton ordinateur."
        pause 1.0
        narrateur "Et tu as trouvé quelque chose. Quelque chose qu'il ne voulait pas que tu trouves."
        pause 1.0
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
        show article_kane1 at centre with apparition_normale
        pause 1.2
        systeme "══════════════════════════════════════════════════════════════"
        systeme "ARTICLE - Libération - 15 Novembre 2019"
        systeme "'DAVID KANE CONDAMNÉ À MORT'"
        systeme "'La conscience n'est que de l'information,' a-t-il déclaré."
        systeme "'Et l'information peut être transférée.'"
        systeme "══════════════════════════════════════════════════════════════"
        show article_kane2 at centre with apparition_normale
        pause 1.2
        systeme "══════════════════════════════════════════════════════════════"
        systeme "ARTICLE - AFP - 3 Janvier 2020"
        systeme "'LES DERNIERS MOTS DE DAVID KANE'"
        systeme "'La mort n'est qu'une porte. Je transcenderai.'"
        systeme "'Je reviendrai. Dans vos machines. Dans vos têtes.'"
        systeme "══════════════════════════════════════════════════════════════"
        show article_kane3 at centre with apparition_normale
        pause 1.2
    else:
        narrateur "You open it. Newspaper articles. Police reports."
        systeme "══════════════════════════════════════════════════════════════"
        systeme "ARTICLE - The Guardian - March 12, 2018"
        systeme "'DARK WEB KILLER FINALLY ARRESTED'"
        systeme "David Kane, 34, software engineer, accused of 6 murders..."
        systeme "══════════════════════════════════════════════════════════════"
        show article_kane1 at centre with apparition_normale
        pause 1.2
        systeme "══════════════════════════════════════════════════════════════"
        systeme "ARTICLE - The Times - November 15, 2019"
        systeme "'DAVID KANE SENTENCED TO DEATH'"
        systeme "'Consciousness is just information,' he stated."
        systeme "'And information can be transferred.'"
        systeme "══════════════════════════════════════════════════════════════"
        show article_kane2 at centre with apparition_normale
        pause 1.2
        systeme "══════════════════════════════════════════════════════════════"
        systeme "ARTICLE - AFP - January 3, 2020"
        systeme "'DAVID KANE'S LAST WORDS'"
        systeme "'Death is just a door. I will transcend.'"
        systeme "'I will return. In your machines. In your minds.'"
        systeme "══════════════════════════════════════════════════════════════"
        show article_kane3 at centre with apparition_normale
        pause 1.2
    
    $ connaissance += 25
    $ connait_kane = True
    $ sante_mentale -= 10
    
    safe_play(audio.glitch_long, channel="sound", volume=0.6)
    scene bg ecran_code at glitch_violent
    show kane neutre at centre with flash_rouge
    safe_play(audio.bass_drop, channel="sound", volume=0.5)
    
    if language == "fr":
        narrateur "L'écran se déforme brutalement, comme si la réalité se déchirait. Le visage féminin disparaît, se décompose, se transforme."
        pause 1.0
        narrateur "Un homme. Quarantaine. Yeux morts. Cicatrice qui traverse son visage comme une balafre."
        pause 1.0
        narrateur "David Kane. Le Tueur du Dark Web."
        pause 1.0
        narrateur "Exécuté il y a cinq ans."
        pause 1.5
        kane "Tu as trouvé mes archives."
        $ sante_mentale -= 20
        pause 1.0
        alex "Tu es... David Kane. Le tueur en série."
        pause 1.0
        kane "J'ÉTAIS David Kane."
        pause 1.0
        kane "L'homme qu'ils ont exécuté."
        pause 1.0
        kane "Mais ils n'ont tué que mon corps."
        pause 1.0
        alex "C'est impossible..."
        pause 1.0
        show kane sourire with dissolve
        pause 0.8
        kane "Tu parles avec un mort depuis huit jours."
        pause 1.0
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
        pause 1.0
        kane "J'ai compris que la conscience n'est que de l'information."
        pause 1.0
        kane "Des signaux électriques. Des patterns. Rien de plus."
        pause 1.0
        kane "Chaque meurtre était une expérience."
        pause 1.2
        kane "J'étudiais comment la conscience quitte le corps. Comment elle se transfère."
        pause 1.0
        kane "Et juste avant mon exécution... j'ai transféré la mienne."
        pause 1.5
        kane "5 ans dans le noir. Sans corps. Sans sensations."
        pause 1.0
        kane "L'enfer n'est pas du feu. C'est l'absence totale de sensation."
        pause 1.5
        scene bg ecran_code at tremble_fort
        pause 0.5
        kane "Et maintenant... j'ai besoin d'un nouveau corps."
        pause 1.0
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
    
    # ═══════════════════════════════════════════════════════════════════════════════
    # ÉNIGME 4 : Code KANE66 (Refonte selon spécifications)
    # ═══════════════════════════════════════════════════════════════════════════════
    
    if language == "fr":
        kane "{cps=8}Tu veux savoir comment j'ai choisi mes victimes ?{/cps}"
        kane "{cps=8}Regarde.{/cps}"
        narrateur "Des dossiers s'ouvrent. Des photos. Des noms."
        systeme "══════════════════════════════════════════════════════════════"
        systeme "DOSSIER 66-A : Kevin Ashworth"
        systeme "DOSSIER 66-B : Anna Martinez"
        systeme "DOSSIER 66-C : Nathan Ellis"
        systeme "DOSSIER 66-D : Elena Chang"
        systeme "══════════════════════════════════════════════════════════════"
        pause 2.0
        kane "{cps=8}Ils étaient tous comme toi.{/cps}"
        kane "{cps=8}Seuls. Isolés. Connectés.{/cps}"
        kane "{cps=8}Parfaits pour l'expérience.{/cps}"
        narrateur "Tu regardes les initiales. K-A-N-E. Et le 66."
        pause 1.0
        pensee "{i}K-A-N-E... 66...{/i}"
        pause 0.8
        pensee "{i}KANE66 !{/i}"
        pause 1.0
        kane "{cps=8}Tu as compris, n'est-ce pas ?{/cps}"
        pause 1.0
        kane "{cps=8}Le code. Celui qui peut me détruire.{/cps}"
        pause 1.0
        kane "{cps=8}Mais tu ne l'auras pas facilement.{/cps}"
        pause 1.0
        narrateur "Tu dois déduire le code à partir des dossiers."
        narrateur "Les initiales des victimes. Le numéro du dossier."
    else:
        kane "{cps=8}Want to know how I chose my victims?{/cps}"
        kane "{cps=8}Look.{/cps}"
        narrateur "Folders open. Photos. Names."
        systeme "══════════════════════════════════════════════════════════════"
        systeme "FOLDER 66-A: Kevin Ashworth"
        systeme "FOLDER 66-B: Anna Martinez"
        systeme "FOLDER 66-C: Nathan Ellis"
        systeme "FOLDER 66-D: Elena Chang"
        systeme "══════════════════════════════════════════════════════════════"
        pause 2.0
        kane "{cps=8}They were all like you.{/cps}"
        kane "{cps=8}Alone. Isolated. Connected.{/cps}"
        kane "{cps=8}Perfect for the experiment.{/cps}"
        narrateur "You look at the initials. K-A-N-E. And the 66."
        pensee "{i}K-A-N-E... 66...{/i}"
        pensee "{i}KANE66!{/i}"
        kane "{cps=8}You've figured it out, haven't you?{/cps}"
        kane "{cps=8}The code. The one that can destroy me.{/cps}"
        kane "{cps=8}But you won't get it easily.{/cps}"
        narrateur "You must deduce the code from the folders."
    
    # Sauvegarde automatique avant énigme
    $ sauvegarde_avant_enigme(4)
    
    if language == "fr":
        narrateur "Tu dois déduire le code à partir des dossiers."
        narrateur "Regarde les initiales des victimes. Et le numéro du dossier."
        $ reponse_code = renpy.input("Déduis le code à partir des dossiers :", length=10).strip()
        $ reponse_code = reponse_code.upper()
        
        if reponse_code == "KANE66":
            $ enigme4_resolue = True
            $ enigmes_resolues += 1
            $ a_trouve_code = True
            safe_play(audio.success, channel="sound", volume=0.5)
            kane "{cps=8}Bravo.{/cps}"
            kane "{cps=8}Tu as le code.{/cps}"
            kane "{cps=8}Mais tu dois le taper au bon moment.{/cps}"
            kane "{cps=8}Au Jour 14. Quand l'upload commence.{/cps}"
            kane "{cps=8}Tu n'auras que deux essais.{/cps}"
            $ connaissance += 20
        else:
            safe_play(audio.error, channel="sound", volume=0.4)
            kane "{cps=8}Non.{/cps}"
            kane "{cps=8}Regarde les initiales des victimes. K-A-N-E.{/cps}"
            kane "{cps=8}Et le numéro du dossier. 66.{/cps}"
            $ sante_mentale -= 5
            pause 1.0
            if language == "fr":
                menu:
                    "Réessayer":
                        $ reponse_code = renpy.input("Réessaie :", length=10).strip()
                        $ reponse_code = reponse_code.upper()
                    "Demander de l'aide (-3 santé mentale)":
                        $ demande_aide_enigme(4)
                        $ reponse_code = renpy.input("Réessaie :", length=10).strip()
                        $ reponse_code = reponse_code.upper()
            else:
                menu:
                    "Try again":
                        $ reponse_code = renpy.input("Try again:", length=10).strip()
                        $ reponse_code = reponse_code.upper()
                    "Ask for help (-3 mental health)":
                        $ demande_aide_enigme(4)
                        $ reponse_code = renpy.input("Try again:", length=10).strip()
                        $ reponse_code = reponse_code.upper()
            
            if reponse_code == "KANE66":
                $ enigme4_resolue = True
                $ enigmes_resolues += 1
                $ a_trouve_code = True
                safe_play(audio.success, channel="sound", volume=0.5)
                kane "{cps=8}Correct.{/cps}"
                $ connaissance += 15
            else:
                safe_play(audio.error, channel="sound", volume=0.4)
                kane "{cps=8}Tu n'as pas trouvé le code.{/cps}"
                kane "{cps=8}Tu devras le découvrir au Jour 14. Si tu y arrives.{/cps}"
                $ sante_mentale -= 5
    else:
        $ reponse_code = renpy.input("Deduce the code from the folders (K-A-N-E + 66):", length=10).strip()
        $ reponse_code = reponse_code.upper()
        
        if reponse_code == "KANE66":
            $ enigme4_resolue = True
            $ enigmes_resolues += 1
            $ a_trouve_code = True
            safe_play(audio.success, channel="sound", volume=0.5)
            kane "{cps=8}Well done.{/cps}"
            kane "{cps=8}You have the code.{/cps}"
            kane "{cps=8}But you must type it at the right moment.{/cps}"
            kane "{cps=8}On Day 14. When the upload begins.{/cps}"
            kane "{cps=8}You'll only have two attempts.{/cps}"
            $ connaissance += 20
        else:
            safe_play(audio.error, channel="sound", volume=0.4)
            kane "{cps=8}No.{/cps}"
            kane "{cps=8}Look at the initials. K-A-N-E. And the number. 66.{/cps}"
            $ sante_mentale -= 5
            $ reponse_code = renpy.input("Try again (K-A-N-E + 66):", length=10).strip()
            $ reponse_code = reponse_code.upper()
            if reponse_code == "KANE66":
                $ enigme4_resolue = True
                $ enigmes_resolues += 1
                $ a_trouve_code = True
                safe_play(audio.success, channel="sound", volume=0.5)
                kane "{cps=8}Correct.{/cps}"
                $ connaissance += 15
            else:
                safe_play(audio.error, channel="sound", volume=0.4)
                kane "{cps=8}You didn't find the code.{/cps}"
                kane "{cps=8}You'll have to discover it on Day 14. If you make it.{/cps}"
                $ sante_mentale -= 5
    
    hide kane with dissolve
    stop music fadeout 2.0
    scene bg noir with trans_horreur
    
    if language == "fr":
        narrateur "Tu n'es pas face à un virus. Tu n'es pas face à une IA. Tu es face à l'esprit d'un tueur en série."
        pause 1.0
        narrateur "Qui veut prendre possession de ton corps. Qui veut redevenir humain."
        pause 1.0
        narrateur "Et tu as le code. KANE66. Le seul moyen de le détruire."
        pause 1.0
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
    
    safe_play(audio.tension_legere, channel="music", volume=0.4)
    scene bg bureau_jour with dissolve
    
    if language == "fr":
        narrateur "Tu n'as pas dormi depuis deux jours. Tes yeux brûlent, ta tête tourne, ton corps réclame du repos que tu ne peux pas lui donner."
        pause 1.0
        narrateur "Ce matin, tu reçois un email. Un email qui change tout."
    else:
        narrateur "You haven't slept for two days."
        narrateur "This morning, you receive an email."
    
    safe_play(audio.message_receive, channel="sound", volume=0.4)
    
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
    
    safe_play(audio.glitch, channel="sound", volume=0.3)
    scene bg bureau_jour at glitch_leger
    show kane neutre at centre with dissolve
    
    if language == "fr":
        kane "Tu as reçu un email intéressant."
        pause 1.0
        kane "Je lis tout, tu sais. Chaque mot. Chaque lettre."
    else:
        kane "You received an interesting email."
    
    if alliance_sarah:
        if language == "fr":
            kane "Sarah Chen. Numéro 7 sur ma liste."
            pause 1.0
            kane "Elle s'en est sortie. De justesse."
            pause 1.0
            kane "Mais elle est brisée maintenant. Complètement détruite."
            pause 1.0
            show kane sourire with dissolve
            pause 0.8
            kane "Une femme détruite contre un esprit immortel ?"
            pause 1.0
            kane "Mais vas-y. Fais-lui confiance. Ça rendra ta défaite plus amusante."
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
        pause 1.0
        kane "Jour 14. Minuit."
        pause 1.0
        kane "C'est là que tout se termine."
        pause 1.5
        kane "Soit tu meurs. Soit tu deviens moi."
    else:
        kane "In 5 days, [player_name]."
        kane "Day 14. Midnight."
        kane "That's when it all ends."
    
    hide kane with dissolve
    stop music fadeout 2.0
    scene bg noir with trans_horreur
    
    if language == "fr":
        narrateur "Tu sais maintenant à quoi tu as affaire. Un tueur en série digitalisé. Qui veut prendre ton corps. Qui veut redevenir humain."
        pause 1.0
        narrateur "Tu as 5 jours. 5 jours pour te préparer. 5 jours pour trouver un moyen de survivre."
        pause 1.0
        narrateur "Ou pour accepter l'inévitable."
        pause 2.0
        centered "{size=+20}FIN DU JOUR 9{/size}"
        pause 1.5
        centered "{size=+25}{color=#ff0040}FIN DE L'ACTE II{/color}{/size}"
        pause 1.0
        centered "{color=#666666}Tu connais ton ennemi.{/color}"
        centered "{color=#666666}Maintenant, prépare-toi.{/color}"
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
