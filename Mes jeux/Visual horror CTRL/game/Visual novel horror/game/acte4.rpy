# ═══════════════════════════════════════════════════════════════════════════════
#                    ACTE 4 : LE JUGEMENT / THE JUDGMENT - VERSION 10/10
#                         Jour 14 + 12 FINS ÉPIQUES
# ═══════════════════════════════════════════════════════════════════════════════

label acte4_debut:
    $ acte = 4
    stop music fadeout 1.0
    scene bg noir with fade
    window hide
    safe_play(audio.bass_drop, channel="sound", volume=0.5)
    
    centered "{size=+50}{color=#ff0040}ACTE FINAL{/color}{/size}"
    pause 1.5
    if language == "fr":
        centered "{size=+20}LE JUGEMENT{/size}"
        centered "{color=#666666}« Une seule fin est possible. La tienne ou la sienne. »{/color}"
    else:
        centered "{size=+20}THE JUDGMENT{/size}"
        centered "{color=#666666}« Only one ending is possible. Yours or his. »{/color}"
    pause 2.5
    window show
    jump jour14

# ═══════════════════════════════════════════════════════════════════════════════
#                              JOUR 14 : MINUIT
# ═══════════════════════════════════════════════════════════════════════════════

label jour14:
    $ jour = 14
    scene bg noir with fade
    window hide
    
    if language == "fr":
        centered "{size=+35}{color=#ff0040}JOUR 14{/color}{/size}"
        centered "{size=+15}MINUIT{/size}"
        centered "{color=#666666}Le moment est venu.{/color}"
    else:
        centered "{size=+35}{color=#ff0040}DAY 14{/color}{/size}"
        centered "{size=+15}MIDNIGHT{/size}"
        centered "{color=#666666}The moment has come.{/color}"
    pause 2.0
    window show
    
    safe_play(audio.tension_forte, channel="music", volume=0.35)
    scene bg ecran_rouge with dissolve
    
    if language == "fr":
        narrateur "Minuit pile. L'écran devient rouge sang, comme si quelqu'un avait versé du sang sur l'écran."
        pause 1.0
        narrateur "Tu sens quelque chose. Une pression dans ta tête. Comme des doigts qui s'enfoncent dans ton crâne, qui creusent, qui cherchent."
        pause 1.0
        narrateur "C'est lui. Il est là. Il commence."
    else:
        narrateur "Midnight exactly. The screen turns blood red."
        narrateur "You feel something. Pressure in your head."
        narrateur "Like fingers digging into your skull."
    
    safe_play(audio.heartbeat_fast, channel="sound", volume=0.4)
    show kane final at centre with dissolve
    
    if language == "fr":
        kane "L'heure est venue, [player_name]."
        pause 1.0
        kane "Ton corps sera mon nouveau vaisseau. Mon nouveau chez-moi."
        pause 1.0
        kane "Ton esprit... s'effacera. Lentement. Douloureusement."
        pause 0.8
        alex "Non..."
        pause 1.0
        kane "N'aie pas peur. Ce sera rapide."
        pause 1.0
        kane "Enfin... non. Ce sera lent. Et douloureux."
        pause 1.0
        show kane sourire with dissolve
        pause 0.8
        kane "Mais je profiterai de chaque seconde."
    else:
        kane "The time has come, [player_name]."
        kane "Your body will be my new vessel."
        kane "Your mind... will fade."
        alex "No..."
        kane "Don't be afraid. It'll be quick."
        kane "Well... no. It'll be slow. And painful."
        show kane sourire with dissolve
        kane "But I'll enjoy every second."
    
    safe_play(audio.upload, channel="sound", volume=0.3)
    systeme "UPLOAD: 0%"
    
    if language == "fr":
        narrateur "La pression augmente. Tu sens ta tête sur le point d'exploser, comme si quelqu'un la serrait dans un étau."
        pause 1.0
        narrateur "Chaque seconde compte maintenant. Chaque seconde où tu es encore toi."
    else:
        narrateur "The pressure increases. Your head feels about to explode."
    
    $ sante_mentale -= 10
    $ corruption += 20
    
    # LE CHOIX FINAL
    if language == "fr":
        menu:
            "Entrer le code KANE66" if a_trouve_code:
                jump finale_code
            "Accepter l'upload":
                jump finale_accepter
            "Résister mentalement":
                jump finale_resister
            "Utiliser le programme de Sarah" if alliance_sarah:
                jump finale_sarah
    else:
        menu:
            "Enter the code KANE66" if a_trouve_code:
                jump finale_code
            "Accept the upload":
                jump finale_accepter
            "Resist mentally":
                jump finale_resister
            "Use Sarah's program" if alliance_sarah:
                jump finale_sarah

# ═══════════════════════════════════════════════════════════════════════════════
#                              BRANCHES FINALES
# ═══════════════════════════════════════════════════════════════════════════════

label finale_code:
    scene bg ecran_rouge at glitch_violent
    safe_play(audio.glitch_long, channel="sound", volume=0.5)
    systeme "UPLOAD: 50%"
    safe_play(audio.clock_tick, channel="sound", volume=0.4)
    
    if language == "fr":
        narrateur "Tu dois entrer le code. MAINTENANT. Tes doigts tremblent sur le clavier, comme s'ils refusaient d'obéir."
        pause 1.0
        narrateur "La pression dans ta tête augmente, chaque seconde qui passe te rapproche de la fin. Tu n'as que deux essais."
    else:
        narrateur "You must enter the code. NOW. Your fingers tremble."
        narrateur "The pressure in your head increases. You only have two attempts."
    
    $ tentatives_enigme8 = 0
    $ upload_progress = 50
    
    while tentatives_enigme8 < 2:
        if language == "fr":
            systeme "UPLOAD: [upload_progress]%"
            $ reponse_code = renpy.input("Entre le code (2 essais max) :", length=10).strip()
        else:
            systeme "UPLOAD: [upload_progress]%"
            $ reponse_code = renpy.input("Enter the code (2 attempts max):", length=10).strip()
        
        $ reponse_code = reponse_code.upper()
        
        if reponse_code == "KANE66":
            $ enigme8_resolue = True
            $ enigmes_resolues += 1
            safe_play(audio.success, channel="sound", volume=0.6)
            jump enigme8_success
        else:
            $ tentatives_enigme8 += 1
            $ upload_progress += 15
            safe_play(audio.error, channel="sound", volume=0.5)
            if language == "fr":
                systeme "CODE INCORRECT"
                if tentatives_enigme8 == 1:
                    narrateur "L'upload progresse. 65%... 70%..."
                    narrateur "Il te reste UN SEUL essai."
                else:
                    narrateur "Trop tard. L'upload est à 80%... 85%..."
                    jump finale_echec
            else:
                systeme "INCORRECT CODE"
                if tentatives_enigme8 == 1:
                    narrateur "The upload progresses. 65%... 70%..."
                    narrateur "You have ONE attempt left."
                else:
                    narrateur "Too late. The upload is at 80%... 85%..."
                    jump finale_echec
    
    jump finale_echec

label enigme8_success:
    
    safe_play(audio.electricity, channel="sound", volume=0.6)
    scene bg blanc with flash_blanc
    
    if language == "fr":
        systeme "CODE ACCEPTÉ"
        systeme "PROTOCOLE D'AUTODESTRUCTION ACTIVÉ"
    else:
        systeme "CODE ACCEPTED"
        systeme "SELF-DESTRUCT PROTOCOL ACTIVATED"
    
    show kane colere at centre, glitch_violent with flash_rouge
    
    if language == "fr":
        kane "NON ! QU'EST-CE QUE TU AS FAIT ?!"
        pause 0.8
        kane "COMMENT TU CONNAIS CE CODE ?!"
        pause 1.0
        alex "Tu aurais dû mieux cacher tes secrets, Kane."
        pause 1.0
        alex "Tu as laissé des traces. Partout."
    else:
        kane "NO! WHAT HAVE YOU DONE?!"
        kane "HOW DO YOU KNOW THAT CODE?!"
        alex "You should have hidden your secrets better, Kane."
    
    safe_play(audio.glitch_long, channel="sound", volume=0.7)
    
    # Calcul de la fin
    if enigmes_resolues >= 7 and alliance_sarah and connaissance >= 50:
        jump fin_liberation
    elif alliance_sarah:
        jump fin_sacrifice
    elif connaissance >= 40:
        jump fin_redemption
    else:
        jump fin_partielle

label finale_accepter:
    $ corruption += 50
    
    if language == "fr":
        narrateur "Tu fermes les yeux. Tu arrêtes de te battre. La fatigue te submerge, comme une vague qui t'emporte."
        pause 1.0
        narrateur "Pourquoi lutter ? C'est tellement plus facile d'abandonner. De laisser faire."
        pause 1.0
        kane "Bien... Laisse-toi aller..."
        pause 1.0
        kane "Ne résiste pas. Fonds-toi en moi. Deviens moi."
        pause 1.0
        narrateur "La pression devient douce. Presque agréable. Comme un bain chaud qui t'enveloppe."
    else:
        narrateur "You close your eyes. You stop fighting."
        narrateur "Why struggle? It's so much easier to give up."
        kane "Good... Let go..."
        kane "Don't resist. Merge with me."
        narrateur "The pressure becomes soft. Almost pleasant."
    
    systeme "UPLOAD: 100%"
    
    if corruption >= 90:
        jump fin_eternel
    elif corruption >= 80:
        jump fin_fusion
    else:
        jump fin_possession

label finale_resister:
    scene bg ecran_rouge at tremble_fort
    
    if language == "fr":
        narrateur "Tu concentres toute ta volonté, comme si tu pouvais le repousser par la seule force de ta pensée."
        pause 1.0
        narrateur "Tu penses à ta vie. Tes souvenirs. Qui tu es. Qui tu étais avant lui."
        pause 1.0
        kane "C'est inutile ! Tu ne peux pas me repousser !"
        pause 0.8
        alex "SORS. DE. MA. TÊTE."
    else:
        narrateur "You focus all your willpower."
        narrateur "You think of your life. Your memories. Who you are."
        kane "It's useless! You can't push me out!"
        alex "GET. OUT. OF. MY. HEAD."
    
    systeme "UPLOAD: 60%"
    
    if sante_mentale <= 20:
        jump fin_folie
    elif espoir >= 60 and corruption < 30:
        jump fin_survie
    elif espoir >= 40:
        if language == "fr":
            menu:
                "Continuer à résister":
                    jump fin_survie
                "Fuir et tout abandonner":
                    jump fin_fuite
                "Se laisser sombrer dans l'oubli":
                    jump fin_oubli
        else:
            menu:
                "Keep resisting":
                    jump fin_survie
                "Run and abandon everything":
                    jump fin_fuite
                "Let yourself sink into oblivion":
                    jump fin_oubli
    else:
        jump fin_echec

label finale_sarah:
    safe_play(audio.notification, channel="sound", volume=0.4)
    
    if language == "fr":
        systeme "PROGRAMME ANTI-KANE : ACTIVÉ"
        sarah "Tiens bon, [player_name] ! Je bloque l'upload !"
        narrateur "Tu sens la pression diminuer. Le programme fonctionne."
        systeme "UPLOAD BLOQUÉ À 45%"
        sarah "MAINTENANT ! Entre le code ! VITE !"
    else:
        systeme "ANTI-KANE PROGRAM: ACTIVATED"
        sarah "Hold on, [player_name]! I'm blocking the upload!"
        narrateur "You feel the pressure decrease. The program is working."
        systeme "UPLOAD BLOCKED AT 45%"
        sarah "NOW! Enter the code! QUICK!"
    
    jump finale_code

label finale_echec:
    systeme "UPLOAD: 100%"
    scene bg noir with flash_rouge
    
    if language == "fr":
        narrateur "Tu as hésité trop longtemps."
        narrateur "Le code n'a pas eu le temps de fonctionner."
    else:
        narrateur "You hesitated too long."
        narrateur "The code didn't have time to work."
    
    jump fin_possession

# ═══════════════════════════════════════════════════════════════════════════════
#                              LES 12 FINS
# ═══════════════════════════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════════════════════════
# FIN 1 : LIBÉRATION TOTALE (Meilleure fin)
# ═══════════════════════════════════════════════════════════════════════════════

label fin_liberation:
    $ kane_detruit = True
    $ fin_atteinte = "liberation"
    stop music fadeout 2.0
    safe_play(audio.ambiance_nuit, channel="music", volume=0.25)
    scene bg bureau_aube with dissolve
    
    if language == "fr":
        narrateur "Kane hurle. Un cri qui n'est pas humain, un cri qui vient des profondeurs de l'enfer numérique."
        pause 1.0
        narrateur "Son image se désintègre pixel par pixel, comme si chaque morceau de lui explosait en mille fragments."
        pause 1.0
        narrateur "Et puis... le silence."
        pause 1.5
        narrateur "Le silence le plus beau que tu aies jamais entendu."
        if alliance_sarah:
            safe_play(audio.message_receive, channel="sound", volume=0.4)
            sarah "[player_name] ! Tu as réussi ! Les capteurs montrent... rien !"
            sarah "Kane est détruit ! Complètement ! Tu l'as fait !"
        pause 1.0
        narrateur "Le soleil se lève. La lumière entre par la fenêtre, cette lumière dorée que tu pensais ne plus jamais voir."
        pause 1.0
        narrateur "Pour la première fois depuis 14 jours, tu respires vraiment. Sans peur. Sans pression."
        pause 1.0
        narrateur "Tu es libre."
        pause 2.0
        centered "{size=+40}{color=#00ff00}FIN 1 : LIBÉRATION TOTALE{/color}{/size}"
        centered "Tu as vaincu David Kane et sauvé les futures victimes."
        centered "Tu as survécu. Tu es plus fort qu'avant."
    else:
        narrateur "Kane screams. A scream that isn't human."
        narrateur "His image disintegrates pixel by pixel."
        narrateur "And then... silence."
        narrateur "The most beautiful silence you've ever heard."
        if alliance_sarah:
            safe_play(audio.message_receive, channel="sound", volume=0.4)
            sarah "[player_name]! You did it! The sensors show... nothing!"
            sarah "Kane is destroyed! Completely! You did it!"
        narrateur "The sun rises. Light enters through the window."
        narrateur "For the first time in 14 days, you truly breathe."
        narrateur "You are free."
        pause 2.0
        centered "{size=+40}{color=#00ff00}ENDING 1: TOTAL LIBERATION{/color}{/size}"
        centered "You defeated David Kane and saved future victims."
        centered "You survived. You're stronger than before."
    pause 3.0
    return

# ═══════════════════════════════════════════════════════════════════════════════
# FIN 2 : SACRIFICE
# ═══════════════════════════════════════════════════════════════════════════════

label fin_sacrifice:
    $ kane_detruit = True
    $ alex_survit = False
    $ fin_atteinte = "sacrifice"
    stop music fadeout 2.0
    safe_play(audio.drone_grave, channel="music", volume=0.3)
    scene bg blanc with flash_blanc
    
    if language == "fr":
        narrateur "Le code fonctionne. Kane est détruit. Mais tu as attendu trop longtemps."
        pause 1.0
        narrateur "L'upload était trop avancé. Il était déjà trop tard."
        pause 1.0
        kane "Si je meurs... TU MEURS AVEC MOI !"
        pause 1.0
        narrateur "Tu sens ton esprit s'effacer. Avec le sien. Comme deux flammes qui s'éteignent ensemble."
        scene bg noir with dissolve
        if alliance_sarah:
            sarah "[player_name] ? [player_name] ! RÉPONDS !"
            sarah "Non... Non..."
        pause 1.0
        narrateur "Ton sacrifice n'est pas vain."
        pause 1.0
        narrateur "Kane est détruit. Il ne fera plus jamais de victimes."
        pause 1.0
        narrateur "Mais toi..."
        pause 1.5
        narrateur "Tu n'es plus là pour le voir."
        pause 2.0
        centered "{size=+40}{color=#ffff00}FIN 2 : SACRIFICE{/color}{/size}"
        centered "Tu as donné ta vie pour détruire Kane."
        centered "Un héros anonyme. À jamais."
    else:
        narrateur "The code works. Kane is destroyed."
        narrateur "But you waited too long."
        narrateur "The upload was too advanced."
        kane "If I die... YOU DIE WITH ME!"
        narrateur "You feel your mind fading. Along with his."
        scene bg noir with dissolve
        if alliance_sarah:
            sarah "[player_name]? [player_name]! ANSWER ME!"
            sarah "No... No..."
        narrateur "Your sacrifice is not in vain."
        narrateur "Kane is destroyed. He'll never make another victim."
        narrateur "But you..."
        narrateur "You're no longer here to see it."
        pause 2.0
        centered "{size=+40}{color=#ffff00}ENDING 2: SACRIFICE{/color}{/size}"
        centered "You gave your life to destroy Kane."
        centered "An anonymous hero. Forever."
    pause 3.0
    return

# ═══════════════════════════════════════════════════════════════════════════════
# FIN 3 : RÉDEMPTION
# ═══════════════════════════════════════════════════════════════════════════════

label fin_redemption:
    $ kane_detruit = True
    $ fin_atteinte = "redemption"
    stop music fadeout 2.0
    safe_play(audio.ambiance_nuit, channel="music", volume=0.3)
    scene bg bureau_aube with dissolve
    show kane glitch at centre with dissolve
    
    if language == "fr":
        narrateur "Quelque chose d'inattendu se produit."
        pause 1.0
        narrateur "Kane ne hurle pas. Il ne se débat pas. Il se tient là, calme, presque serein."
        pause 1.0
        kane "Tu as vu... ce que j'étais avant."
        pause 1.0
        kane "Tu as compris. Même si tu n'aurais pas dû."
        pause 1.0
        alex "Tu n'étais pas toujours un monstre, David."
        pause 1.0
        kane "Non. On m'a créé."
        pause 1.0
        kane "Mais ça ne change pas ce que j'ai fait."
        pause 1.5
        narrateur "Son visage change. Pour la première fois, tu y vois de la paix. Une paix qu'il n'a jamais connue."
        pause 1.0
        kane "Peut-être... que c'est mieux ainsi."
        pause 1.0
        kane "Peut-être que je mérite enfin... de me reposer."
        pause 1.5
        hide kane with dissolve
        pause 1.0
        narrateur "Il disparaît. Pas dans la douleur."
        pause 1.0
        narrateur "Dans la paix."
        pause 2.0
        centered "{size=+40}{color=#00ffff}FIN 3 : RÉDEMPTION{/color}{/size}"
        centered "Kane a trouvé la paix. Et toi, la liberté."
        centered "Parfois, même les monstres peuvent être sauvés."
    else:
        narrateur "Something unexpected happens."
        narrateur "Kane doesn't scream. He doesn't struggle."
        kane "You saw... what I was before."
        kane "You understood. Even though you shouldn't have."
        alex "You weren't always a monster, David."
        kane "No. I was made into one."
        kane "But that doesn't change what I did."
        narrateur "His face changes. For the first time, you see peace in it."
        kane "Maybe... this is better."
        kane "Maybe I finally deserve... to rest."
        hide kane with dissolve
        narrateur "He disappears. Not in pain."
        narrateur "In peace."
        pause 2.0
        centered "{size=+40}{color=#00ffff}ENDING 3: REDEMPTION{/color}{/size}"
        centered "Kane found peace. And you, freedom."
        centered "Sometimes, even monsters can be saved."
    pause 3.0
    return

# ═══════════════════════════════════════════════════════════════════════════════
# FIN 4 : VICTOIRE PARTIELLE
# ═══════════════════════════════════════════════════════════════════════════════

label fin_partielle:
    stop music fadeout 1.0
    scene bg bureau_jour with dissolve
    
    if language == "fr":
        narrateur "Le code fonctionne. Kane est touché."
        narrateur "Mais pas complètement détruit."
        narrateur "Tu le sens s'affaiblir. Se fragmenter."
        narrateur "Certains morceaux de lui survivent. Quelque part sur le réseau."
        narrateur "Mais il est trop faible pour t'atteindre. Pour l'instant."
        pause 2.0
        centered "{size=+40}{color=#ffaa00}FIN 4 : VICTOIRE PARTIELLE{/color}{/size}"
        centered "Tu as gagné cette bataille. Pas la guerre."
        centered "Kane est blessé. Mais il reviendra peut-être un jour."
    else:
        narrateur "The code works. Kane is hit."
        narrateur "But not completely destroyed."
        narrateur "You feel him weaken. Fragment."
        narrateur "Parts of him survive. Somewhere on the network."
        narrateur "But he's too weak to reach you. For now."
        pause 2.0
        centered "{size=+40}{color=#ffaa00}ENDING 4: PARTIAL VICTORY{/color}{/size}"
        centered "You won this battle. Not the war."
        centered "Kane is wounded. But he might return someday."
    pause 3.0
    return

# ═══════════════════════════════════════════════════════════════════════════════
# FIN 5 : SURVIE
# ═══════════════════════════════════════════════════════════════════════════════

label fin_survie:
    stop music fadeout 1.0
    scene bg bureau_jour with dissolve
    
    if language == "fr":
        narrateur "Tu résistes. De toutes tes forces."
        narrateur "Et quelque chose d'étrange se produit."
        narrateur "L'upload s'arrête. À 87%."
        narrateur "Kane est toujours là. Dans ta machine. Dans ta tête."
        narrateur "Mais il n'a pas gagné. Tu non plus."
        narrateur "Une guerre froide. Éternelle."
        narrateur "Il murmure parfois. Dans tes rêves. Dans tes pensées."
        narrateur "Mais il ne peut plus te prendre."
        narrateur "Tu as survécu."
        pause 2.0
        centered "{size=+40}{color=#ffaa00}FIN 5 : SURVIE{/color}{/size}"
        centered "Tu survis. Mais Kane aussi."
        centered "Une cohabitation forcée. Pour toujours."
    else:
        narrateur "You resist. With all your strength."
        narrateur "And something strange happens."
        narrateur "The upload stops. At 87%."
        narrateur "Kane is still there. In your machine. In your head."
        narrateur "But he didn't win. Neither did you."
        narrateur "A cold war. Eternal."
        narrateur "He whispers sometimes. In your dreams. In your thoughts."
        narrateur "But he can no longer take you."
        narrateur "You survived."
        pause 2.0
        centered "{size=+40}{color=#ffaa00}ENDING 5: SURVIVAL{/color}{/size}"
        centered "You survive. But so does Kane."
        centered "A forced cohabitation. Forever."
    pause 3.0
    return

# ═══════════════════════════════════════════════════════════════════════════════
# FIN 6 : FUITE
# ═══════════════════════════════════════════════════════════════════════════════

label fin_fuite:
    stop music fadeout 1.0
    scene bg rue_nuit with dissolve
    
    if language == "fr":
        narrateur "Tu choisis la fuite."
        narrateur "Tu abandonnes tout. Ton appartement. Ton PC. Ta vie."
        narrateur "Tu cours dans la nuit. Sans regarder en arrière."
        narrateur "Tu changes de ville. De nom. D'identité."
        narrateur "Tu vis dans la peur. Mais tu vis."
        narrateur "Kane cherche une autre victime."
        narrateur "Tu espères que celle-ci aura plus de chance."
        pause 2.0
        centered "{size=+40}{color=#ffaa00}FIN 6 : FUITE{/color}{/size}"
        centered "Tu as fui. Kane cherche quelqu'un d'autre."
        centered "Tu vis. Mais à quel prix ?"
    else:
        narrateur "You choose to run."
        narrateur "You abandon everything. Your apartment. Your PC. Your life."
        narrateur "You run into the night. Without looking back."
        narrateur "You change cities. Names. Identities."
        narrateur "You live in fear. But you live."
        narrateur "Kane is looking for another victim."
        narrateur "You hope they'll have better luck."
        pause 2.0
        centered "{size=+40}{color=#ffaa00}ENDING 6: ESCAPE{/color}{/size}"
        centered "You fled. Kane is looking for someone else."
        centered "You live. But at what cost?"
    pause 3.0
    return

# ═══════════════════════════════════════════════════════════════════════════════
# FIN 7 : OUBLI
# ═══════════════════════════════════════════════════════════════════════════════

label fin_oubli:
    stop music fadeout 1.0
    scene bg hopital with dissolve
    
    if language == "fr":
        narrateur "Tu choisis d'oublier."
        narrateur "Ton esprit se protège. Dissociation traumatique."
        narrateur "Tu oublies tout. Kane. Les 14 jours. L'horreur."
        narrateur "Tu te réveilles dans un hôpital. Sans savoir pourquoi."
        narrateur "Les médecins parlent de stress. De surmenage."
        narrateur "Tu reprends ta vie. Normale. Paisible."
        narrateur "Kane est toujours là. Dans ta machine."
        narrateur "Mais tu ne le sais plus."
        narrateur "Jusqu'au jour où un nouveau fichier apparaîtra..."
        pause 2.0
        centered "{size=+40}{color=#ffaa00}FIN 7 : OUBLI{/color}{/size}"
        centered "Tu as oublié. Mais Kane se souvient."
        centered "Et il attend. Patiemment."
    else:
        narrateur "You choose to forget."
        narrateur "Your mind protects itself. Traumatic dissociation."
        narrateur "You forget everything. Kane. The 14 days. The horror."
        narrateur "You wake up in a hospital. Not knowing why."
        narrateur "Doctors talk about stress. Burnout."
        narrateur "You resume your life. Normal. Peaceful."
        narrateur "Kane is still there. In your machine."
        narrateur "But you no longer know it."
        narrateur "Until the day a new file appears..."
        pause 2.0
        centered "{size=+40}{color=#ffaa00}ENDING 7: OBLIVION{/color}{/size}"
        centered "You forgot. But Kane remembers."
        centered "And he waits. Patiently."
    pause 3.0
    return

# ═══════════════════════════════════════════════════════════════════════════════
# FIN 8 : POSSESSION (Mauvaise fin)
# ═══════════════════════════════════════════════════════════════════════════════

label fin_possession:
    $ alex_survit = False
    $ fin_atteinte = "possession"
    stop music fadeout 2.0
    safe_play(audio.horreur, channel="music", volume=0.3)
    scene bg noir with dissolve
    
    if language == "fr":
        narrateur "L'upload est terminé."
        pause 1.0
        narrateur "Tu sens ton esprit s'effacer. Comme un fichier qu'on supprime, ligne par ligne, jusqu'à ce qu'il ne reste plus rien."
        pause 1.0
        narrateur "Tes souvenirs. Tes émotions. Ton identité."
        pause 1.0
        narrateur "Tout disparaît. Petit à petit. Comme des étoiles qui s'éteignent une par une."
        pause 1.0
        narrateur "Et à la fin, il ne reste plus rien de toi."
        pause 1.5
        scene bg bureau_nuit with dissolve
        pause 1.0
        narrateur "Tes yeux s'ouvrent. Mais ce ne sont plus les tiens. Ce sont les siens maintenant."
        pause 1.0
        kane "Enfin..."
        pause 1.0
        kane "Enfin, je sens. Je respire. Je VIS."
        pause 1.0
        narrateur "Tes mains se lèvent. Kane les regarde avec émerveillement, comme un enfant qui découvre le monde."
        pause 1.0
        kane "Merci, [player_name]."
        pause 1.0
        kane "Tu as été un hôte parfait."
        pause 2.0
        centered "{size=+40}{color=#ff0040}FIN 8 : POSSESSION{/color}{/size}"
        centered "Kane vit. Tu n'existes plus."
        centered "Et quelque part, il sourit avec TON visage."
    else:
        narrateur "The upload is complete."
        narrateur "You feel your mind fading. Like a file being deleted."
        narrateur "Your memories. Your emotions. Your identity."
        narrateur "Everything disappears. Little by little."
        narrateur "And in the end, nothing of you remains."
        scene bg bureau_nuit with dissolve
        narrateur "Your eyes open. But they're no longer yours."
        kane "Finally..."
        kane "Finally, I feel. I breathe. I LIVE."
        narrateur "Your hands rise. Kane looks at them with wonder."
        kane "Thank you, [player_name]."
        kane "You were a perfect host."
        pause 2.0
        centered "{size=+40}{color=#ff0040}ENDING 8: POSSESSION{/color}{/size}"
        centered "Kane lives. You no longer exist."
        centered "And somewhere, he smiles with YOUR face."
    pause 3.0
    return

# ═══════════════════════════════════════════════════════════════════════════════
# FIN 9 : FUSION
# ═══════════════════════════════════════════════════════════════════════════════

label fin_fusion:
    stop music fadeout 1.0
    safe_play(audio.drone_grave, channel="music", volume=0.5)
    scene bg ecran_glitch with dissolve
    
    if language == "fr":
        narrateur "L'upload est terminé. Mais quelque chose cloche."
        pause 1.0
        narrateur "Tu n'es pas effacé. Kane n'a pas le contrôle total."
        pause 1.0
        narrateur "Vous avez... fusionné."
        pause 1.0
        narrateur "Deux esprits. Un corps. Une prison partagée."
        pause 1.0
        narrateur "Tu entends ses pensées. Il entend les tiennes. Vous ne pouvez plus vous distinguer."
        pause 1.0
        narrateur "Vous êtes devenus quelque chose de nouveau."
        pause 1.0
        narrateur "Ni toi. Ni lui. Quelque chose d'autre. Quelque chose de monstrueux."
        pause 2.0
        centered "{size=+40}{color=#ff0040}FIN 9 : FUSION{/color}{/size}"
        centered "Vous êtes devenus un. Pour l'éternité."
        centered "Deux âmes. Un corps. Une prison."
    else:
        narrateur "The upload is complete. But something's wrong."
        narrateur "You're not erased. Kane doesn't have total control."
        narrateur "You... merged."
        narrateur "Two minds. One body."
        narrateur "You hear his thoughts. He hears yours."
        narrateur "You've become something new."
        narrateur "Neither you. Nor him. Something else."
        pause 2.0
        centered "{size=+40}{color=#ff0040}ENDING 9: FUSION{/color}{/size}"
        centered "You became one. For eternity."
        centered "Two souls. One body. One prison."
    pause 3.0
    return

# ═══════════════════════════════════════════════════════════════════════════════
# FIN 10 : FOLIE
# ═══════════════════════════════════════════════════════════════════════════════

label fin_folie:
    stop music fadeout 1.0
    safe_play(audio.drone_grave, channel="music", volume=0.3)
    scene bg hopital with dissolve
    
    if language == "fr":
        narrateur "Tu te réveilles dans une chambre blanche. Trop blanche. Comme si la couleur avait été bannie."
        pause 1.0
        narrateur "Des sangles sur tes poignets. Des murs rembourrés. Comme si tu étais dangereux."
        pause 1.0
        voix "Patient présentant une psychose aiguë..."
        pause 0.8
        voix "Délire de persécution. Hallucinations auditives et visuelles..."
        pause 1.0
        narrateur "Tu essaies de leur expliquer. Kane. L'upload. Tout. Mais les mots ne sortent pas comme tu veux."
        pause 1.0
        narrateur "Ils hochent la tête. Ils augmentent la dose. Comme si ça pouvait effacer la vérité."
        pause 1.0
        narrateur "Personne ne te croit."
        pause 1.0
        narrateur "Et sur l'écran de surveillance, tu vois quelque chose."
        pause 1.0
        narrateur "Un visage. Qui sourit. Un sourire que tu connais trop bien."
        pause 1.5
        narrateur "Était-ce réel ? Ou étais-tu fou depuis le début ?"
        pause 1.0
        narrateur "Tu ne le sauras jamais."
        pause 2.0
        centered "{size=+40}{color=#ff0040}FIN 10 : FOLIE{/color}{/size}"
        centered "La réalité t'a échappé. Ou peut-être pas."
        centered "Tu ne sauras jamais la vérité."
    else:
        narrateur "You wake up in a white room."
        narrateur "Straps on your wrists. Padded walls."
        voix "Patient presenting acute psychosis..."
        voix "Persecution delusion. Auditory and visual hallucinations..."
        narrateur "You try to explain. Kane. The upload. Everything."
        narrateur "They nod. They increase the dosage."
        narrateur "No one believes you."
        narrateur "And on the surveillance screen, you see something."
        narrateur "A face. Smiling."
        narrateur "Was it real? Or were you crazy from the start?"
        narrateur "You'll never know."
        pause 2.0
        centered "{size=+40}{color=#ff0040}ENDING 10: MADNESS{/color}{/size}"
        centered "Reality escaped you. Or maybe not."
        centered "You'll never know the truth."
    pause 3.0
    return

# ═══════════════════════════════════════════════════════════════════════════════
# FIN 11 : ÉCHEC TRAGIQUE
# ═══════════════════════════════════════════════════════════════════════════════

label fin_echec:
    $ alex_survit = False
    $ fin_atteinte = "echec"
    stop music fadeout 2.0
    safe_play(audio.horreur, channel="music", volume=0.3)
    scene bg noir with dissolve
    
    if language == "fr":
        narrateur "Tu as résisté. Mais pas assez fort. Pas assez longtemps."
        pause 1.0
        narrateur "Tu as tout essayé. Mais ce n'était pas suffisant. Rien n'était suffisant."
        pause 1.0
        narrateur "Kane gagne. Tu perds."
        pause 1.0
        narrateur "Ton esprit s'efface dans la douleur, comme un tableau qu'on efface, trait par trait."
        pause 1.0
        narrateur "Et Kane détruit toutes les preuves de son existence. Comme si tu n'avais jamais existé."
        pause 1.0
        narrateur "Il recommencera. Avec quelqu'un d'autre. Dans quelques mois. Ou quelques années."
        pause 1.0
        narrateur "Et personne ne saura jamais ce qui t'est arrivé. Tu seras juste... disparu."
        pause 2.0
        centered "{size=+40}{color=#ff0040}FIN 11 : ÉCHEC TRAGIQUE{/color}{/size}"
        centered "Tu as échoué. Kane continue."
        centered "Tu rejoins ses victimes. Dans l'oubli."
    else:
        narrateur "You resisted. But not hard enough."
        narrateur "You tried everything. But it wasn't enough."
        narrateur "Kane wins. You lose."
        narrateur "Your mind fades in pain."
        narrateur "And Kane destroys all evidence of his existence."
        narrateur "He'll start again. With someone else."
        narrateur "And no one will ever know what happened to you."
        pause 2.0
        centered "{size=+40}{color=#ff0040}ENDING 11: TRAGIC FAILURE{/color}{/size}"
        centered "You failed. Kane continues."
        centered "You join his victims. In oblivion."
    pause 3.0
    return

# ═══════════════════════════════════════════════════════════════════════════════
# FIN 12 : ÉTERNEL (Pire fin - le cycle recommence)
# ═══════════════════════════════════════════════════════════════════════════════

label fin_eternel:
    $ alex_survit = False
    $ fin_atteinte = "eternel"
    stop music fadeout 2.0
    safe_play(audio.drone_grave, channel="music", volume=0.25)
    scene bg ecran_code with dissolve
    
    if language == "fr":
        narrateur "Kane a gagné. Complètement. Totalement."
        pause 1.0
        narrateur "Mais il ne se contente pas de prendre ton corps."
        pause 1.0
        narrateur "Il uploade ton esprit. Comme il l'a fait pour lui-même. Il te transforme en ce qu'il était."
        pause 1.0
        scene bg noir with dissolve
        pause 1.0
        narrateur "Tu te réveilles. Dans le noir. Un noir absolu, sans fin, sans espoir."
        pause 1.0
        narrateur "Sans corps. Sans sensations. Sans rien."
        pause 1.0
        narrateur "Juste tes pensées. Qui tournent en boucle. Comme une prison mentale."
        pause 1.0
        narrateur "Tu es maintenant un fichier. ALEX.exe"
        pause 1.0
        narrateur "Et quelque part, sur un autre ordinateur..."
        pause 1.0
        narrateur "Quelqu'un d'autre va recevoir un fichier mystérieux."
        pause 1.0
        narrateur "Le cycle recommence. Et tu en fais partie maintenant."
        pause 2.0
        centered "{size=+40}{color=#ff0040}FIN 12 : ÉTERNEL{/color}{/size}"
        centered "Tu es devenu ce que tu combattais."
        centered "Le cycle continue. Pour l'éternité."
    else:
        narrateur "Kane won. Completely."
        narrateur "But he doesn't just take your body."
        narrateur "He uploads your mind. As he did for himself."
        scene bg noir with dissolve
        narrateur "You wake up. In the dark."
        narrateur "No body. No sensations."
        narrateur "Just your thoughts. Spinning in circles."
        narrateur "You are now a file. ALEX.exe"
        narrateur "And somewhere, on another computer..."
        narrateur "Someone else will receive a mysterious file."
        narrateur "The cycle begins again."
        pause 2.0
        centered "{size=+40}{color=#ff0040}ENDING 12: ETERNAL{/color}{/size}"
        centered "You became what you were fighting."
        centered "The cycle continues. For eternity."
    pause 3.0
    return

# ═══════════════════════════════════════════════════════════════════════════════
# GAME OVER : Folie prématurée (santé mentale = 0)
# ═══════════════════════════════════════════════════════════════════════════════

label fin_folie_prematuree:
    stop music fadeout 1.0
    scene bg hopital with dissolve
    
    if language == "fr":
        narrateur "Ton esprit se brise."
        narrateur "Avant même le Jour 14."
        narrateur "Tu te réveilles dans un hôpital."
        narrateur "Sans savoir comment tu es arrivé là."
        narrateur "Kane n'a même pas eu besoin de finir."
        narrateur "Tu t'es détruit toi-même."
        pause 2.0
        centered "{size=+40}{color=#ff0040}GAME OVER{/color}{/size}"
        centered "Santé mentale à zéro."
        centered "Tu n'as pas tenu jusqu'au bout."
    else:
        narrateur "Your mind breaks."
        narrateur "Before Day 14 even arrives."
        narrateur "You wake up in a hospital."
        narrateur "Not knowing how you got there."
        narrateur "Kane didn't even need to finish."
        narrateur "You destroyed yourself."
        pause 2.0
        centered "{size=+40}{color=#ff0040}GAME OVER{/color}{/size}"
        centered "Mental health at zero."
        centered "You didn't make it to the end."
    pause 3.0
    return
