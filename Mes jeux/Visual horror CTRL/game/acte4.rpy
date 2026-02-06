# ═══════════════════════════════════════════════════════════════════════════════
#                    ACTE 4 : LE JUGEMENT / THE JUDGMENT - VERSION 10/10
#                         Jour 14 + 12 FINS ÉPIQUES
# ═══════════════════════════════════════════════════════════════════════════════

label acte4_debut:
    $ acte = 4
    stop music fadeout 1.0
    scene bg noir with fade
    window hide
    play sound audio.bass_drop
    
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
    
    play music audio.finale fadein 3.0 volume 0.6
    scene bg ecran_rouge with dissolve
    
    if language == "fr":
        narrateur "Minuit pile. L'écran devient rouge sang."
        narrateur "Tu sens quelque chose. Une pression dans ta tête."
        narrateur "Comme des doigts qui s'enfoncent dans ton crâne."
    else:
        narrateur "Midnight exactly. The screen turns blood red."
        narrateur "You feel something. Pressure in your head."
        narrateur "Like fingers digging into your skull."
    
    play sound audio.heartbeat_fast volume 0.5
    show kane final at centre with dissolve
    
    if language == "fr":
        kane "L'heure est venue, [player_name]."
        kane "Ton corps sera mon nouveau vaisseau."
        kane "Ton esprit... s'effacera."
        alex "Non..."
        kane "N'aie pas peur. Ce sera rapide."
        kane "Enfin... non. Ce sera lent. Et douloureux."
        show kane sourire with dissolve
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
    
    play sound audio.upload volume 0.4
    systeme "UPLOAD: 0%"
    
    if language == "fr":
        narrateur "La pression augmente. Tu sens ta tête sur le point d'exploser."
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
    play sound audio.glitch_long volume 0.6
    systeme "UPLOAD: 50%"
    
    if language == "fr":
        narrateur "Tu tapes le code. Tes doigts tremblent."
        narrateur "K - A - N - E - 6 - 6"
        menu:
            "Appuyer sur ENTRÉE":
                $ enigme8_resolue = True
                $ enigmes_resolues += 1
            "Hésiter":
                narrateur "Tu hésites une seconde de trop."
                jump finale_echec
    else:
        narrateur "You type the code. Your fingers tremble."
        narrateur "K - A - N - E - 6 - 6"
        menu:
            "Press ENTER":
                $ enigme8_resolue = True
                $ enigmes_resolues += 1
            "Hesitate":
                narrateur "You hesitate one second too long."
                jump finale_echec
    
    play sound audio.electricity volume 0.8
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
        kane "COMMENT TU CONNAIS CE CODE ?!"
        alex "Tu aurais dû mieux cacher tes secrets, Kane."
    else:
        kane "NO! WHAT HAVE YOU DONE?!"
        kane "HOW DO YOU KNOW THAT CODE?!"
        alex "You should have hidden your secrets better, Kane."
    
    play sound audio.glitch_long volume 0.9
    
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
        narrateur "Tu fermes les yeux. Tu arrêtes de te battre."
        narrateur "Pourquoi lutter ? C'est tellement plus facile d'abandonner."
        kane "Bien... Laisse-toi aller..."
        kane "Ne résiste pas. Fonds-toi en moi."
        narrateur "La pression devient douce. Presque agréable."
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
        narrateur "Tu concentres toute ta volonté."
        narrateur "Tu penses à ta vie. Tes souvenirs. Qui tu es."
        kane "C'est inutile ! Tu ne peux pas me repousser !"
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
    play sound audio.notification
    
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
    stop music fadeout 1.0
    play music audio.victoire fadein 2.0 volume 0.5
    scene bg bureau_aube with dissolve
    
    if language == "fr":
        narrateur "Kane hurle. Un cri qui n'est pas humain."
        narrateur "Son image se désintègre pixel par pixel."
        narrateur "Et puis... le silence."
        narrateur "Le silence le plus beau que tu aies jamais entendu."
        if alliance_sarah:
            play sound audio.message_receive
            sarah "[player_name] ! Tu as réussi ! Les capteurs montrent... rien !"
            sarah "Kane est détruit ! Complètement ! Tu l'as fait !"
        narrateur "Le soleil se lève. La lumière entre par la fenêtre."
        narrateur "Pour la première fois depuis 14 jours, tu respires vraiment."
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
            play sound audio.message_receive
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
    stop music fadeout 1.0
    play music audio.drone_grave fadein 2.0 volume 0.5
    scene bg blanc with flash_blanc
    
    if language == "fr":
        narrateur "Le code fonctionne. Kane est détruit."
        narrateur "Mais tu as attendu trop longtemps."
        narrateur "L'upload était trop avancé."
        kane "Si je meurs... TU MEURS AVEC MOI !"
        narrateur "Tu sens ton esprit s'effacer. Avec le sien."
        scene bg noir with dissolve
        if alliance_sarah:
            sarah "[player_name] ? [player_name] ! RÉPONDS !"
            sarah "Non... Non..."
        narrateur "Ton sacrifice n'est pas vain."
        narrateur "Kane est détruit. Il ne fera plus jamais de victimes."
        narrateur "Mais toi..."
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
    stop music fadeout 1.0
    play music audio.espoir fadein 2.0 volume 0.5
    scene bg bureau_aube with dissolve
    show kane glitch at centre with dissolve
    
    if language == "fr":
        narrateur "Quelque chose d'inattendu se produit."
        narrateur "Kane ne hurle pas. Il ne se débat pas."
        kane "Tu as vu... ce que j'étais avant."
        kane "Tu as compris. Même si tu n'aurais pas dû."
        alex "Tu n'étais pas toujours un monstre, David."
        kane "Non. On m'a créé."
        kane "Mais ça ne change pas ce que j'ai fait."
        narrateur "Son visage change. Pour la première fois, tu y vois de la paix."
        kane "Peut-être... que c'est mieux ainsi."
        kane "Peut-être que je mérite enfin... de me reposer."
        hide kane with dissolve
        narrateur "Il disparaît. Pas dans la douleur."
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
    stop music fadeout 1.0
    play music audio.defaite fadein 2.0 volume 0.5
    scene bg noir with dissolve
    
    if language == "fr":
        narrateur "L'upload est terminé."
        narrateur "Tu sens ton esprit s'effacer. Comme un fichier qu'on supprime."
        narrateur "Tes souvenirs. Tes émotions. Ton identité."
        narrateur "Tout disparaît. Petit à petit."
        narrateur "Et à la fin, il ne reste plus rien de toi."
        scene bg bureau_nuit with dissolve
        narrateur "Tes yeux s'ouvrent. Mais ce ne sont plus les tiens."
        kane "Enfin..."
        kane "Enfin, je sens. Je respire. Je VIS."
        narrateur "Tes mains se lèvent. Kane les regarde avec émerveillement."
        kane "Merci, [player_name]."
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
    play music audio.drone_grave fadein 2.0 volume 0.5
    scene bg ecran_glitch with dissolve
    
    if language == "fr":
        narrateur "L'upload est terminé. Mais quelque chose cloche."
        narrateur "Tu n'es pas effacé. Kane n'a pas le contrôle total."
        narrateur "Vous avez... fusionné."
        narrateur "Deux esprits. Un corps."
        narrateur "Tu entends ses pensées. Il entend les tiennes."
        narrateur "Vous êtes devenus quelque chose de nouveau."
        narrateur "Ni toi. Ni lui. Quelque chose d'autre."
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
    play music audio.horreur fadein 2.0 volume 0.4
    scene bg hopital with dissolve
    
    if language == "fr":
        narrateur "Tu te réveilles dans une chambre blanche."
        narrateur "Des sangles sur tes poignets. Des murs rembourrés."
        voix "Patient présentant une psychose aiguë..."
        voix "Délire de persécution. Hallucinations auditives et visuelles..."
        narrateur "Tu essaies de leur expliquer. Kane. L'upload. Tout."
        narrateur "Ils hochent la tête. Ils augmentent la dose."
        narrateur "Personne ne te croit."
        narrateur "Et sur l'écran de surveillance, tu vois quelque chose."
        narrateur "Un visage. Qui sourit."
        narrateur "Était-ce réel ? Ou étais-tu fou depuis le début ?"
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
    stop music fadeout 1.0
    play music audio.defaite fadein 2.0 volume 0.5
    scene bg noir with dissolve
    
    if language == "fr":
        narrateur "Tu as résisté. Mais pas assez fort."
        narrateur "Tu as tout essayé. Mais ce n'était pas suffisant."
        narrateur "Kane gagne. Tu perds."
        narrateur "Ton esprit s'efface dans la douleur."
        narrateur "Et Kane détruit toutes les preuves de son existence."
        narrateur "Il recommencera. Avec quelqu'un d'autre."
        narrateur "Et personne ne saura jamais ce qui t'est arrivé."
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
    stop music fadeout 1.0
    play music audio.horreur fadein 2.0 volume 0.5
    scene bg ecran_code with dissolve
    
    if language == "fr":
        narrateur "Kane a gagné. Complètement."
        narrateur "Mais il ne se contente pas de prendre ton corps."
        narrateur "Il uploade ton esprit. Comme il l'a fait pour lui-même."
        scene bg noir with dissolve
        narrateur "Tu te réveilles. Dans le noir."
        narrateur "Sans corps. Sans sensations."
        narrateur "Juste tes pensées. Qui tournent en boucle."
        narrateur "Tu es maintenant un fichier. ALEX.exe"
        narrateur "Et quelque part, sur un autre ordinateur..."
        narrateur "Quelqu'un d'autre va recevoir un fichier mystérieux."
        narrateur "Le cycle recommence."
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
