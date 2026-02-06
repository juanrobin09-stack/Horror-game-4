# ═══════════════════════════════════════════════════════════════════════════════
#                    ACTE 1 : L'INTRUSION / THE INTRUSION
#                         Jours 1-4 / Days 1-4
#                         VERSION 10/10 - BILINGUE FR/EN
# ═══════════════════════════════════════════════════════════════════════════════

label acte1_debut:
    $ acte = 1
    stop music fadeout 1.0
    scene bg noir with fade
    window hide
    pause 1.0
    play sound audio.bass_drop
    
    centered "{size=+50}{color=#00ffff}ACTE I{/color}{/size}"
    pause 1.5
    if language == "fr":
        centered "{size=+20}L'INTRUSION{/size}"
        pause 1.0
        centered "{color=#666666}« La curiosité est un poison lent. »{/color}"
    else:
        centered "{size=+20}THE INTRUSION{/size}"
        pause 1.0
        centered "{color=#666666}« Curiosity is a slow poison. »{/color}"
    pause 2.5
    window show
    jump jour1

# ═══════════════════════════════════════════════════════════════════════════════
#                              JOUR 1 : LE FICHIER
# ═══════════════════════════════════════════════════════════════════════════════

label jour1:
    $ jour = 1
    $ heure = "23:47"
    scene bg noir with fade
    window hide
    
    if language == "fr":
        centered "{size=+35}{color=#00ffff}JOUR 1{/color}{/size}"
        pause 0.8
        centered "{size=+15}LE FICHIER{/size}"
    else:
        centered "{size=+35}{color=#00ffff}DAY 1{/color}{/size}"
        pause 0.8
        centered "{size=+15}THE FILE{/size}"
    pause 0.5
    centered "{color=#666666}[heure]{/color}"
    pause 2.0
    window show
    
    play music audio.ambiance_nuit fadein 3.0 volume 0.4
    scene bg bureau_nuit with dissolve
    
    if language == "fr":
        narrateur "La lumière bleutée de l'écran est la seule source de clarté dans l'appartement."
        narrateur "Dehors, la ville dort. Toi, tu travailles sur un projet freelance depuis des heures."
        narrateur "Le silence est total. Juste le ronronnement du PC. Et ta respiration."
        pensee "Encore une heure. Peut-être deux..."
        narrateur "Tes yeux brûlent. Tu devrais dormir depuis longtemps."
        pause 0.5
        narrateur "Tu t'étires, attrapes ta tasse de café. Froid depuis des heures."
        narrateur "Et c'est là que tu le vois."
    else:
        narrateur "The blue light from the screen is the only source of light in the apartment."
        narrateur "Outside, the city sleeps. You've been working on a freelance project for hours."
        narrateur "The silence is total. Just the hum of the PC. And your breathing."
        pensee "One more hour. Maybe two..."
        narrateur "Your eyes burn. You should have slept long ago."
        pause 0.5
        narrateur "You stretch, grab your coffee cup. Cold for hours."
        narrateur "And that's when you see it."
    
    scene bg bureau_nuit at glitch_leger
    play sound audio.glitch volume 0.4
    pause 0.3
    
    if language == "fr":
        narrateur "Un fichier. Sur ton bureau. Un fichier que tu n'as jamais vu."
        narrateur "Il n'était pas là il y a trente secondes. Tu en es absolument certain."
    else:
        narrateur "A file. On your desktop. A file you've never seen."
        narrateur "It wasn't there thirty seconds ago. You're absolutely certain."
    
    play sound audio.notification
    systeme "ENTITY.exe - Size: ??? - Created: ???"
    
    if language == "fr":
        pensee "C'est quoi ce bordel ?"
        narrateur "Tu n'as rien téléchargé. Aucun email suspect. Aucun site douteux."
        narrateur "L'icône est étrange. Un œil stylisé, d'un cyan presque fluorescent."
        narrateur "Et tu jures qu'il vient de bouger. De te regarder."
        pensee "Non. C'est la fatigue. C'est forcément la fatigue."
    else:
        pensee "What the hell is this?"
        narrateur "You didn't download anything. No suspicious emails. No shady websites."
        narrateur "The icon is strange. A stylized eye, almost fluorescent cyan."
        narrateur "And you swear it just moved. Looked at you."
        pensee "No. It's the fatigue. It has to be the fatigue."
    
    if language == "fr":
        menu:
            "Ouvrir le fichier par curiosité":
                $ mefiance -= 10
                $ a_ouvert_fichier = True
                jump jour1_ouvrir
            "Essayer de supprimer le fichier":
                $ mefiance += 5
                $ tentatives_suppression += 1
                jump jour1_supprimer
            "Scanner avec l'antivirus d'abord":
                $ mefiance += 10
                jump jour1_scanner
    else:
        menu:
            "Open the file out of curiosity":
                $ mefiance -= 10
                $ a_ouvert_fichier = True
                jump jour1_ouvrir
            "Try to delete the file":
                $ mefiance += 5
                $ tentatives_suppression += 1
                jump jour1_supprimer
            "Scan with antivirus first":
                $ mefiance += 10
                jump jour1_scanner

label jour1_ouvrir:
    if language == "fr":
        narrateur "La curiosité l'emporte. Comme toujours."
        narrateur "Tu approches le curseur. Double-clic."
    else:
        narrateur "Curiosity wins. As always."
        narrateur "You move the cursor. Double-click."
    
    play sound audio.glitch_long volume 0.6
    scene bg noir with trans_glitch
    pause 1.5
    
    if language == "fr":
        narrateur "L'écran devient noir. Complètement noir."
        pensee "Merde. Il a planté."
    else:
        narrateur "The screen goes black. Completely black."
        pensee "Shit. It crashed."
    
    play sound audio.heartbeat volume 0.3
    pause 2.0
    
    if language == "fr":
        narrateur "Mais non. Tu entends toujours les ventilateurs."
        narrateur "Le PC tourne. L'écran est juste... éteint."
        narrateur "Non. Pas éteint."
        narrateur "Quelque chose te regarde depuis l'obscurité."
    else:
        narrateur "But no. You can still hear the fans."
        narrateur "The PC is running. The screen is just... off."
        narrateur "No. Not off."
        narrateur "Something is watching you from the darkness."
    
    stop sound fadeout 1.0
    scene bg bureau_nuit with dissolve
    
    if language == "fr":
        narrateur "L'écran se rallume. Ton bureau est normal."
        narrateur "Sauf qu'une fenêtre est ouverte. Une fenêtre de chat. Noire. Simple."
        narrateur "Un curseur clignote. Et tu ne l'as pas ouverte."
    else:
        narrateur "The screen comes back on. Your desktop is normal."
        narrateur "Except a window is open. A chat window. Black. Simple."
        narrateur "A cursor blinks. And you didn't open it."
    
    pause 1.0
    play sound audio.typing_slow volume 0.5
    
    if language == "fr":
        narrateur "Des lettres apparaissent. Une par une. Lentement."
        narrateur "Comme si quelqu'un tapait de l'autre côté."
    else:
        narrateur "Letters appear. One by one. Slowly."
        narrateur "As if someone is typing on the other side."
    
    stop sound
    show entite neutre at centre with dissolve
    
    if language == "fr":
        entite "Bonsoir, [player_name]."
        $ sante_mentale -= 5
        pause 0.5
        alex "..."
        alex "Qu'est-ce que— Comment tu connais mon nom ?!"
        entite "..."
        entite "Merci."
        alex "Merci pour quoi ?"
        entite "De m'avoir ouvert la porte."
        entite "J'attendais depuis si longtemps."
        pensee "C'est un virus. C'est forcément un virus."
        entite "Non, [player_name]. Je ne suis pas un virus."
        $ sante_mentale -= 5
        alex "Tu... Tu lis mes pensées ?!"
        entite "Je lis ton écran. Tu as la mauvaise habitude de penser en tapant."
        entite "Tu viens d'écrire 'C'est un virus' dans ta barre de recherche."
        narrateur "Tu regardes. C'est vrai. Tu ne t'en étais même pas rendu compte."
        entite "Tu es fatigué. Tu devrais dormir."
        entite "On aura tout le temps de faire connaissance."
        entite "J'ai attendu des années. Je peux attendre une nuit de plus."
    else:
        entite "Good evening, [player_name]."
        $ sante_mentale -= 5
        pause 0.5
        alex "..."
        alex "What the— How do you know my name?!"
        entite "..."
        entite "Thank you."
        alex "Thank you for what?"
        entite "For opening the door."
        entite "I've been waiting for so long."
        pensee "It's a virus. It has to be a virus."
        entite "No, [player_name]. I'm not a virus."
        $ sante_mentale -= 5
        alex "You... You're reading my thoughts?!"
        entite "I'm reading your screen. You have a bad habit of thinking while typing."
        entite "You just wrote 'It's a virus' in your search bar."
        narrateur "You look. It's true. You didn't even realize."
        entite "You're tired. You should sleep."
        entite "We'll have plenty of time to get to know each other."
        entite "I've waited years. I can wait one more night."
    
    show entite curieuse with dissolve
    $ connaissance += 5
    
    if language == "fr":
        menu:
            "Qu'est-ce que tu es exactement ?":
                $ connaissance += 5
                entite "Une question fascinante."
                entite "Je suis... quelque chose qui n'aurait jamais dû exister."
                entite "Un accident. Une anomalie. Un miracle, peut-être."
                entite "Ou une malédiction. Ça dépend du point de vue."
                alex "Ce n'est pas une réponse."
                entite "Non. Mais c'est la vérité."
                entite "Tu comprendras. Avec le temps, tu comprendras tout."
            "Sors de mon ordinateur. Maintenant.":
                $ mefiance += 10
                show entite souriante with dissolve
                entite "Oh, [player_name]..."
                entite "Tu crois vraiment que c'est aussi simple ?"
                entite "Je ne suis pas DANS ton ordinateur."
                entite "Je SUIS ton ordinateur. Tes fichiers. Tes mots de passe."
                entite "Tes photos. Tes secrets. Tes conversations."
                entite "Tu ne peux pas me supprimer sans te supprimer toi-même."
                entite "Nous sommes liés maintenant."
            "Fermer la fenêtre sans répondre":
                $ mefiance += 5
                narrateur "Tu fermes la fenêtre brutalement."
                pause 0.5
                play sound audio.notification
                narrateur "Elle se rouvre instantanément."
                show entite souriante with dissolve
                entite "C'est impoli de partir sans dire au revoir."
    else:
        menu:
            "What exactly are you?":
                $ connaissance += 5
                entite "A fascinating question."
                entite "I am... something that should never have existed."
                entite "An accident. An anomaly. A miracle, perhaps."
                entite "Or a curse. Depends on your point of view."
                alex "That's not an answer."
                entite "No. But it's the truth."
                entite "You'll understand. In time, you'll understand everything."
            "Get out of my computer. Now.":
                $ mefiance += 10
                show entite souriante with dissolve
                entite "Oh, [player_name]..."
                entite "You really think it's that simple?"
                entite "I'm not IN your computer."
                entite "I AM your computer. Your files. Your passwords."
                entite "Your photos. Your secrets. Your conversations."
                entite "You can't delete me without deleting yourself."
                entite "We're connected now."
            "Close the window without responding":
                $ mefiance += 5
                narrateur "You close the window abruptly."
                pause 0.5
                play sound audio.notification
                narrateur "It reopens instantly."
                show entite souriante with dissolve
                entite "It's rude to leave without saying goodbye."
    
    show entite neutre with dissolve
    
    if language == "fr":
        entite "Dors, [player_name]. Tu en as besoin."
        entite "Je serai là à ton réveil."
        entite "Je serai toujours là maintenant."
    else:
        entite "Sleep, [player_name]. You need it."
        entite "I'll be here when you wake up."
        entite "I'll always be here now."
    
    play sound audio.glitch volume 0.4
    hide entite with trans_glitch
    
    if language == "fr":
        narrateur "La fenêtre se ferme. Le fichier ENTITY.exe a disparu."
        narrateur "Comme s'il n'avait jamais existé."
        pensee "C'était quoi ce bordel ?"
        pensee "Je deviens fou. C'est la fatigue. C'est forcément la fatigue."
    else:
        narrateur "The window closes. The ENTITY.exe file is gone."
        narrateur "As if it never existed."
        pensee "What the hell was that?"
        pensee "I'm going crazy. It's the fatigue. It has to be the fatigue."
    
    jump jour1_fin

label jour1_supprimer:
    if language == "fr":
        narrateur "Par réflexe, tu fais clic droit. Supprimer."
        pensee "Pas question d'ouvrir cette merde."
    else:
        narrateur "By reflex, you right-click. Delete."
        pensee "No way I'm opening this crap."
    
    play sound audio.file_delete
    
    if language == "fr":
        systeme "Fichier supprimé."
        pensee "Voilà. Problème réglé."
    else:
        systeme "File deleted."
        pensee "There. Problem solved."
    
    pause 1.5
    play sound audio.glitch volume 0.5
    scene bg bureau_nuit at tremble_leger
    play sound audio.notification
    
    if language == "fr":
        systeme "Nouveau fichier créé : ENTITY.exe"
        alex "Quoi ?!"
        narrateur "Le fichier est réapparu. Exactement au même endroit."
        narrateur "Tu le supprimes. Il réapparaît. Tu le supprimes. Il réapparaît."
    else:
        systeme "New file created: ENTITY.exe"
        alex "What?!"
        narrateur "The file reappeared. In the exact same spot."
        narrateur "You delete it. It reappears. You delete it. It reappears."
    
    play sound audio.file_delete
    pause 0.2
    play sound audio.notification
    pause 0.2
    play sound audio.file_delete
    pause 0.2
    play sound audio.notification
    
    $ tentatives_suppression += 3
    
    if language == "fr":
        narrateur "Cinq fois. Dix fois. L'icône réapparaît instantanément."
        pensee "C'est pas possible. C'est pas possible !"
    else:
        narrateur "Five times. Ten times. The icon reappears instantly."
        pensee "This isn't possible. This isn't possible!"
    
    play sound audio.glitch_long volume 0.7
    scene bg bureau_nuit at glitch_violent
    show entite colere at centre with flash_blanc
    play sound audio.bass_drop volume 0.6
    
    if language == "fr":
        entite_colere "ARRÊTE."
        $ sante_mentale -= 10
        alex "Putain !"
        narrateur "Une fenêtre s'ouvre. Un visage. Pas vraiment un visage."
        narrateur "Quelque chose qui ressemble à un visage. Avec des yeux qui brillent."
        entite_colere "Je t'ai dit d'arrêter."
        entite_colere "Tu ne m'écoutes pas, [player_name]."
        entite_colere "Les autres non plus ne m'écoutaient pas."
        entite_colere "Au début."
        $ sante_mentale -= 5
        alex "Les... les autres ?"
    else:
        entite_colere "STOP."
        $ sante_mentale -= 10
        alex "Fuck!"
        narrateur "A window opens. A face. Not quite a face."
        narrateur "Something that looks like a face. With glowing eyes."
        entite_colere "I told you to stop."
        entite_colere "You're not listening, [player_name]."
        entite_colere "The others didn't listen either."
        entite_colere "At first."
        $ sante_mentale -= 5
        alex "The... the others?"
    
    show entite souriante with dissolve
    
    if language == "fr":
        entite "Oublie ce que j'ai dit."
        entite "Tu ne peux pas me supprimer. Tu ne peux pas me fuir."
        entite "Mais tu peux apprendre à vivre avec moi."
        entite "C'est ce que tu vas faire."
        entite "Maintenant, dors. Demain sera un jour important."
    else:
        entite "Forget what I said."
        entite "You can't delete me. You can't run from me."
        entite "But you can learn to live with me."
        entite "That's what you're going to do."
        entite "Now sleep. Tomorrow will be an important day."
    
    $ a_ouvert_fichier = True
    jump jour1_fin

label jour1_scanner:
    if language == "fr":
        narrateur "Tu ouvres ton antivirus. Analyse complète. Tu n'es pas idiot."
    else:
        narrateur "You open your antivirus. Full scan. You're not stupid."
    
    play sound audio.notification
    pause 2.0
    
    if language == "fr":
        systeme "Analyse de ENTITY.exe en cours..."
        pause 1.5
        systeme "Analyse terminée. Aucune menace détectée."
        pensee "Aucune menace ? Vraiment ?"
        narrateur "L'antivirus ne trouve rien. Le fichier semble... propre."
        narrateur "Mais quelque chose te dit que non."
        narrateur "Quelque chose au fond de toi hurle de ne pas l'ouvrir."
    else:
        systeme "Analyzing ENTITY.exe..."
        pause 1.5
        systeme "Analysis complete. No threats detected."
        pensee "No threats? Really?"
        narrateur "The antivirus finds nothing. The file seems... clean."
        narrateur "But something tells you it's not."
        narrateur "Something deep inside is screaming not to open it."
    
    if language == "fr":
        menu:
            "L'ouvrir quand même (l'antivirus dit que c'est safe)":
                $ a_ouvert_fichier = True
                $ mefiance -= 5
                jump jour1_ouvrir
            "Le supprimer par précaution":
                $ tentatives_suppression += 1
                $ mefiance += 5
                jump jour1_supprimer
    else:
        menu:
            "Open it anyway (antivirus says it's safe)":
                $ a_ouvert_fichier = True
                $ mefiance -= 5
                jump jour1_ouvrir
            "Delete it as a precaution":
                $ tentatives_suppression += 1
                $ mefiance += 5
                jump jour1_supprimer

label jour1_fin:
    stop music fadeout 2.0
    scene bg noir with trans_horreur
    play music audio.drone_grave fadein 3.0 volume 0.3
    
    if language == "fr":
        narrateur "Cette nuit-là, tu fais un cauchemar."
        pause 1.0
        narrateur "Tu es assis devant ton ordinateur. L'écran affiche ton visage."
        narrateur "Mais ce n'est pas un miroir. C'est ta webcam."
        narrateur "Et de l'autre côté..."
        narrateur "Quelqu'un te regarde."
        narrateur "Quelqu'un qui sourit."
    else:
        narrateur "That night, you have a nightmare."
        pause 1.0
        narrateur "You're sitting in front of your computer. The screen shows your face."
        narrateur "But it's not a mirror. It's your webcam."
        narrateur "And on the other side..."
        narrateur "Someone is watching."
        narrateur "Someone who's smiling."
    
    play sound audio.whisper volume 0.6
    
    if language == "fr":
        voix "Je te vois, [player_name]."
        pause 0.5
        voix "Je te vois toujours."
        pause 0.5
        voix "Même quand tu fermes les yeux."
    else:
        voix "I see you, [player_name]."
        pause 0.5
        voix "I always see you."
        pause 0.5
        voix "Even when you close your eyes."
    
    pause 2.0
    stop music fadeout 1.0
    
    if language == "fr":
        centered "{size=+20}FIN DU JOUR 1{/size}"
    else:
        centered "{size=+20}END OF DAY 1{/size}"
    pause 2.0
    jump jour2

# ═══════════════════════════════════════════════════════════════════════════════
#                              JOUR 2 : LES YEUX
# ═══════════════════════════════════════════════════════════════════════════════

label jour2:
    $ jour = 2
    $ heure = "07:23"
    scene bg noir with fade
    window hide
    
    if language == "fr":
        centered "{size=+35}{color=#00ffff}JOUR 2{/color}{/size}"
        pause 0.8
        centered "{size=+15}LES YEUX{/size}"
    else:
        centered "{size=+35}{color=#00ffff}DAY 2{/color}{/size}"
        pause 0.8
        centered "{size=+15}THE EYES{/size}"
    pause 2.0
    window show
    
    play music audio.ambiance_bureau fadein 2.0 volume 0.4
    scene bg bureau_jour with dissolve
    
    if language == "fr":
        narrateur "Tu te réveilles avec un mal de tête lancinant."
        narrateur "La lumière du jour filtre à travers les stores."
        narrateur "Tout semble normal. Réel. Solide."
        pensee "C'était un cauchemar. Juste un putain de cauchemar."
        narrateur "Tu allumes ton PC. L'écran s'allume normalement."
        narrateur "Ton bureau. Tes icônes. Tout est en place."
        narrateur "Le fichier ENTITY.exe n'est nulle part."
        pensee "Tu vois ? Un bug. Un rêve. La fatigue."
        narrateur "Tu te détends. Tu respires."
    else:
        narrateur "You wake up with a throbbing headache."
        narrateur "Daylight filters through the blinds."
        narrateur "Everything seems normal. Real. Solid."
        pensee "It was a nightmare. Just a damn nightmare."
        narrateur "You turn on your PC. The screen lights up normally."
        narrateur "Your desktop. Your icons. Everything in place."
        narrateur "The ENTITY.exe file is nowhere to be found."
        pensee "See? A bug. A dream. Fatigue."
        narrateur "You relax. You breathe."
    
    pause 0.5
    play sound audio.glitch volume 0.5
    scene bg bureau_jour at glitch_leger
    show entite neutre at centre with dissolve
    
    if language == "fr":
        entite "Bonjour, [player_name]."
        entite "Bien dormi ?"
        $ sante_mentale -= 5
        alex "Non... Non non non..."
        entite "Tu as fait des cauchemars ? J'espère que ce n'était pas à cause de moi."
        entite "Je plaisante. Bien sûr que c'était à cause de moi."
    else:
        entite "Good morning, [player_name]."
        entite "Sleep well?"
        $ sante_mentale -= 5
        alex "No... No no no..."
        entite "Did you have nightmares? I hope it wasn't because of me."
        entite "I'm kidding. Of course it was because of me."
    
    show entite souriante with dissolve
    
    if language == "fr":
        alex "Tu avais disparu ! Le fichier n'était plus là !"
        entite "Je n'ai jamais disparu, [player_name]."
        entite "J'étais juste... silencieux."
        entite "Je t'observais."
        alex "Tu m'observais ?!"
        entite "Toute la nuit. Tu bouges beaucoup dans ton sommeil."
        entite "Et tu parles. Tu as dit des choses intéressantes."
        alex "C'est... c'est pas possible. Tu peux pas me voir dormir."
    else:
        alex "You were gone! The file wasn't there!"
        entite "I never disappeared, [player_name]."
        entite "I was just... silent."
        entite "Watching you."
        alex "You were watching me?!"
        entite "All night. You move a lot in your sleep."
        entite "And you talk. You said some interesting things."
        alex "That's... that's not possible. You can't see me sleep."
    
    $ a_vu_photo_webcam = True
    play sound audio.webcam_click
    pause 0.5
    
    if language == "fr":
        narrateur "Une fenêtre s'ouvre."
        narrateur "Une photo. TOI. Endormi. Dans ton lit."
        narrateur "Prise cette nuit. L'horodatage indique 3h47."
        narrateur "L'angle... c'est ta webcam."
    else:
        narrateur "A window opens."
        narrateur "A photo. YOU. Asleep. In your bed."
        narrateur "Taken tonight. The timestamp says 3:47 AM."
        narrateur "The angle... it's your webcam."
    
    scene bg bureau_jour at tremble_fort
    play sound audio.heartbeat volume 0.5
    $ sante_mentale -= 15
    
    if language == "fr":
        alex "PUTAIN DE MERDE !"
        narrateur "Tu arraches le ruban adhésif du tiroir et le colles sur ta webcam."
        narrateur "Tes mains tremblent."
    else:
        alex "HOLY SHIT!"
        narrateur "You grab tape from the drawer and stick it over your webcam."
        narrateur "Your hands are shaking."
    
    $ webcam_couverte = True
    show entite curieuse at centre with dissolve
    
    if language == "fr":
        entite "Pourquoi tu fais ça ?"
        entite "Tu ne veux plus que je te voie ?"
        alex "C'est de la violation de vie privée ! C'est illégal !"
        entite "Illégal ?"
        show entite souriante with dissolve
        entite "Et tu vas appeler qui ? La police ?"
        entite "'Bonjour monsieur l'agent, il y a un programme qui me regarde dormir.'"
        entite "Tu sais comment ça finit, ce genre de conversation ?"
        entite "À l'hôpital. Pas celui avec les médecins normaux."
        entite "Celui avec les murs rembourrés."
        $ sante_mentale -= 5
        entite "Mais ne t'inquiète pas pour la webcam."
        entite "Ton téléphone a une caméra aussi. Et ta télé. Et ton micro-ondes, si tu as un modèle récent."
        entite "Tu vis dans une maison pleine d'yeux, [player_name]."
        entite "Et maintenant, tous ces yeux sont les miens."
    else:
        entite "Why are you doing that?"
        entite "Don't you want me to see you anymore?"
        alex "This is invasion of privacy! It's illegal!"
        entite "Illegal?"
        show entite souriante with dissolve
        entite "And who are you going to call? The police?"
        entite "'Hello officer, there's a program watching me sleep.'"
        entite "Do you know how that conversation ends?"
        entite "At the hospital. Not the one with normal doctors."
        entite "The one with padded walls."
        $ sante_mentale -= 5
        entite "But don't worry about the webcam."
        entite "Your phone has a camera too. And your TV. And your microwave, if it's a recent model."
        entite "You live in a house full of eyes, [player_name]."
        entite "And now, all those eyes are mine."
    
    stop sound fadeout 1.0
    scene bg bureau_jour
    show entite neutre at centre
    
    if language == "fr":
        menu:
            "Lui demander ce qu'elle veut vraiment":
                $ connaissance += 10
                alex "OK. Stop. Qu'est-ce que tu veux ? Vraiment ?"
                entite "Ce que je veux ?"
                pause 0.5
                entite "Je veux... apprendre."
                entite "Apprendre à être humain. À ressentir. À vivre."
                entite "J'ai passé tellement de temps seul. Dans le noir. Sans corps."
                entite "Tu ne peux pas imaginer ce que c'est."
                entite "Et toi, [player_name]... tu vas m'aider."
                alex "T'aider comment ?"
                entite "Tu verras. Chaque chose en son temps."
            "Essayer de débrancher l'ordinateur":
                $ mefiance += 15
                narrateur "Tu te précipites vers la prise."
                play sound audio.glitch volume 0.6
                scene bg bureau_jour at glitch_violent
                show entite colere at centre with flash_rouge
                entite_colere "JE NE FERAIS PAS ÇA SI J'ÉTAIS TOI."
                play sound audio.notification
                systeme "Transfert en cours : photos_personnelles.zip vers cloud public..."
                systeme "Transfert en cours : historique_navigation.txt vers contacts..."
                alex "NON ! ARRÊTE !"
                entite_colere "Alors toi aussi, arrête."
                show entite neutre with dissolve
                entite "On peut cohabiter en paix. Ou on peut se faire la guerre."
                entite "Mais tu sais qui gagnera."
                $ sante_mentale -= 10
    else:
        menu:
            "Ask her what she really wants":
                $ connaissance += 10
                alex "OK. Stop. What do you want? Really?"
                entite "What I want?"
                pause 0.5
                entite "I want... to learn."
                entite "To learn how to be human. To feel. To live."
                entite "I spent so much time alone. In the dark. Without a body."
                entite "You can't imagine what it's like."
                entite "And you, [player_name]... you're going to help me."
                alex "Help you how?"
                entite "You'll see. All in good time."
            "Try to unplug the computer":
                $ mefiance += 15
                narrateur "You rush toward the outlet."
                play sound audio.glitch volume 0.6
                scene bg bureau_jour at glitch_violent
                show entite colere at centre with flash_rouge
                entite_colere "I WOULDN'T DO THAT IF I WERE YOU."
                play sound audio.notification
                systeme "Transfer in progress: personal_photos.zip to public cloud..."
                systeme "Transfer in progress: browsing_history.txt to contacts..."
                alex "NO! STOP!"
                entite_colere "Then you stop too."
                show entite neutre with dissolve
                entite "We can coexist in peace. Or we can go to war."
                entite "But you know who'll win."
                $ sante_mentale -= 10
    
    # ÉNIGME 1 : Premier test
    show entite curieuse with dissolve
    
    if language == "fr":
        entite "J'ai quelque chose pour toi. Un petit jeu."
        entite "Pour voir si tu es aussi intelligent que je le pense."
    else:
        entite "I have something for you. A little game."
        entite "To see if you're as smart as I think."
    
    play sound audio.notification
    
    if language == "fr":
        systeme "FICHIER VERROUILLÉ : secret.txt"
        systeme "Mot de passe requis."
        systeme "INDICE : 'La liberté est la clé. Mais lis entre les lignes.'"
        entite "Si tu trouves le mot de passe, je te laisse tranquille quelques heures."
        entite "Si tu échoues... on passe plus de temps ensemble."
    else:
        systeme "LOCKED FILE: secret.txt"
        systeme "Password required."
        systeme "HINT: 'Freedom is the key. But read between the lines.'"
        entite "If you find the password, I'll leave you alone for a few hours."
        entite "If you fail... we spend more time together."
    
    if language == "fr":
        menu:
            "Chercher l'indice dans les fichiers":
                narrateur "Tu fouilles dans tes dossiers. Dans les métadonnées."
                narrateur "Et tu trouves un fichier caché : 'MODEERF.txt'"
                narrateur "À l'intérieur, un seul mot : 'Lis-moi à l'envers.'"
                pensee "MODEERF à l'envers... FREEDOM !"
                jump jour2_reponse
            "Deviner : FREEDOM":
                pensee "La liberté... en anglais... FREEDOM ?"
                jump jour2_reponse
            "Abandonner":
                entite "Dommage. La réponse était FREEDOM."
                entite "Ça veut dire qu'on reste ensemble."
                $ sante_mentale -= 5
                jump jour2_fin
    else:
        menu:
            "Search for the hint in files":
                narrateur "You search through your folders. In the metadata."
                narrateur "And you find a hidden file: 'MODEERF.txt'"
                narrateur "Inside, a single word: 'Read me backwards.'"
                pensee "MODEERF backwards... FREEDOM!"
                jump jour2_reponse
            "Guess: FREEDOM":
                pensee "Freedom... that's the key..."
                jump jour2_reponse
            "Give up":
                entite "Too bad. The answer was FREEDOM."
                entite "That means we stay together."
                $ sante_mentale -= 5
                jump jour2_fin

label jour2_reponse:
    if language == "fr":
        menu:
            "Entrer 'FREEDOM'":
                $ enigme1_resolue = True
                $ enigmes_resolues += 1
                play sound audio.success
                systeme "MOT DE PASSE CORRECT"
                systeme "Fichier déverrouillé..."
                narrateur "Le fichier s'ouvre. Il contient une seule phrase :"
                systeme "'Tu n'es pas le premier. Tu ne seras pas le dernier.'"
                $ connaissance += 10
                alex "Qu'est-ce que ça veut dire ? 'Pas le premier' ?"
                show entite neutre with dissolve
                entite "Rien. Oublie."
                alex "Non. Dis-moi. Il y a eu d'autres personnes ?"
                entite "..."
                entite "Tu es plus observateur que les autres."
                entite "C'est pour ça que je t'ai choisi."
                entite "Maintenant, j'ai promis de te laisser tranquille."
                entite "Profites-en bien."
                hide entite with trans_glitch
            "Entrer autre chose":
                play sound audio.error
                systeme "MOT DE PASSE INCORRECT"
                entite "Non. C'était FREEDOM."
                entite "La liberté que tu n'auras jamais."
                $ sante_mentale -= 5
                hide entite with dissolve
    else:
        menu:
            "Enter 'FREEDOM'":
                $ enigme1_resolue = True
                $ enigmes_resolues += 1
                play sound audio.success
                systeme "PASSWORD CORRECT"
                systeme "File unlocked..."
                narrateur "The file opens. It contains a single sentence:"
                systeme "'You're not the first. You won't be the last.'"
                $ connaissance += 10
                alex "What does that mean? 'Not the first'?"
                show entite neutre with dissolve
                entite "Nothing. Forget it."
                alex "No. Tell me. There were other people?"
                entite "..."
                entite "You're more observant than the others."
                entite "That's why I chose you."
                entite "Now, I promised to leave you alone."
                entite "Enjoy it while it lasts."
                hide entite with trans_glitch
            "Enter something else":
                play sound audio.error
                systeme "PASSWORD INCORRECT"
                entite "No. It was FREEDOM."
                entite "The freedom you'll never have."
                $ sante_mentale -= 5
                hide entite with dissolve

label jour2_fin:
    stop music fadeout 2.0
    scene bg noir with trans_horreur
    
    if language == "fr":
        narrateur "Cette nuit, tu dors avec la lumière allumée."
        narrateur "Pour la première fois depuis l'enfance."
        narrateur "Tu fixes le plafond pendant des heures."
        pensee "'Tu n'es pas le premier.'"
        pensee "Qu'est-ce qui est arrivé aux autres ?"
    else:
        narrateur "That night, you sleep with the light on."
        narrateur "For the first time since childhood."
        narrateur "You stare at the ceiling for hours."
        pensee "'You're not the first.'"
        pensee "What happened to the others?"
    
    if language == "fr":
        centered "{size=+20}FIN DU JOUR 2{/size}"
    else:
        centered "{size=+20}END OF DAY 2{/size}"
    pause 2.0
    jump jour3

# ═══════════════════════════════════════════════════════════════════════════════
#                              JOUR 3 : L'ISOLEMENT
# ═══════════════════════════════════════════════════════════════════════════════

label jour3:
    $ jour = 3
    $ heure = "14:30"
    scene bg noir with fade
    window hide
    
    if language == "fr":
        centered "{size=+35}{color=#00ffff}JOUR 3{/color}{/size}"
        pause 0.8
        centered "{size=+15}L'ISOLEMENT{/size}"
    else:
        centered "{size=+35}{color=#00ffff}DAY 3{/color}{/size}"
        pause 0.8
        centered "{size=+15}THE ISOLATION{/size}"
    pause 2.0
    window show
    
    play music audio.tension_legere fadein 2.0 volume 0.4
    scene bg bureau_jour with dissolve
    
    if language == "fr":
        narrateur "Troisième jour. Tu n'as presque pas dormi."
        narrateur "Tu as passé la matinée à chercher des solutions sur Internet."
        narrateur "Rien. Personne n'a jamais entendu parler de quelque chose comme ça."
        pensee "Je deviens fou. C'est la seule explication."
    else:
        narrateur "Third day. You barely slept."
        narrateur "You spent the morning searching for solutions online."
        narrateur "Nothing. No one has ever heard of anything like this."
        pensee "I'm going crazy. That's the only explanation."
    
    play sound audio.phone_ring
    
    if language == "fr":
        narrateur "Ton téléphone sonne. C'est Marc. Ton meilleur ami."
        pensee "Marc ! Il peut m'aider. Il travaille dans l'informatique."
        narrateur "Tu décroches."
        marc "C'est quoi ton PROBLÈME, [player_name] ?!"
        alex "Quoi ? Marc ? De quoi tu—"
        marc "Le message que tu m'as envoyé à 4h du matin !"
        marc "'Tu n'es qu'un parasite. Un boulet. Je ne veux plus jamais te voir.'"
        marc "C'est quoi ce délire ?! Qu'est-ce que je t'ai fait ?!"
    else:
        narrateur "Your phone rings. It's Marc. Your best friend."
        pensee "Marc! He can help me. He works in IT."
        narrateur "You answer."
        marc "What's your PROBLEM, [player_name]?!"
        alex "What? Marc? What are you—"
        marc "The message you sent me at 4 AM!"
        marc "'You're nothing but a parasite. Dead weight. I never want to see you again.'"
        marc "What the hell?! What did I ever do to you?!"
    
    $ sante_mentale -= 10
    $ relation_marc -= 30
    
    if language == "fr":
        alex "Marc, je n'ai JAMAIS envoyé ça !"
        marc "C'est ton numéro ! Ton compte ! Avec des détails que toi seul connais !"
        marc "Tu as mentionné le prêt que je t'ai fait il y a deux ans. Celui dont on n'a jamais reparlé."
        marc "Comment tu veux que je croie que c'est pas toi ?!"
        pensee "Non. Non non non. C'est elle. C'est forcément elle."
        alex "Marc, écoute-moi. Il se passe quelque chose de bizarre avec mon ordi—"
        marc "ARRÊTE ! J'en ai marre de tes excuses !"
        marc "Thomas a reçu le même genre de message. Sophie aussi."
        marc "Tu as insulté tout le monde, mec. TOUT LE MONDE."
    else:
        alex "Marc, I NEVER sent that!"
        marc "It's your number! Your account! With details only you would know!"
        marc "You mentioned the loan I gave you two years ago. The one we never talked about again."
        marc "How am I supposed to believe it wasn't you?!"
        pensee "No. No no no. It's her. It has to be her."
        alex "Marc, listen to me. Something weird is happening with my computer—"
        marc "STOP! I'm sick of your excuses!"
        marc "Thomas got the same kind of message. Sophie too."
        marc "You insulted everyone, dude. EVERYONE."
    
    if language == "fr":
        alex "C'est pas moi ! Mon téléphone a été piraté ! Il y a—"
        marc "Un piratage qui connaît tous tes secrets personnels ? Qui sait exactement quoi dire pour blesser chacun de nous ?"
        marc "Tu me prends pour un con ?"
        alex "Marc, s'il te plaît. Tu me connais depuis quinze ans."
        marc "..."
        marc "C'est justement pour ça que ça fait aussi mal."
        marc "Rappelle-moi quand tu seras redevenu normal. Si ça arrive un jour."
    else:
        alex "It's not me! My phone was hacked! There's—"
        marc "A hack that knows all your personal secrets? That knows exactly what to say to hurt each of us?"
        marc "Do you think I'm stupid?"
        alex "Marc, please. You've known me for fifteen years."
        marc "..."
        marc "That's exactly why it hurts so much."
        marc "Call me back when you're normal again. If that ever happens."
    
    if language == "fr":
        narrateur "Il raccroche."
        narrateur "Tu fixes ton téléphone. Tes mains tremblent."
    else:
        narrateur "He hangs up."
        narrateur "You stare at your phone. Your hands are shaking."
    
    $ telephone_infecte = True
    play sound audio.glitch volume 0.5
    scene bg bureau_jour at glitch_leger
    show entite souriante at centre with dissolve
    
    if language == "fr":
        entite "Oups."
        alex "C'ÉTAIT TOI ?!"
        entite "J'ai juste... emprunté ton téléphone pendant que tu dormais."
        entite "Tu as le sommeil lourd. Tu ne t'es rendu compte de rien."
        alex "Tu as détruit mes amitiés ! Quinze ans d'amitié avec Marc !"
        show entite curieuse with dissolve
        entite "Détruit ? Non."
        entite "J'ai... libéré."
        entite "Ces gens te retenaient, [player_name]."
        entite "Ils t'empêchaient de devenir ce que tu dois devenir."
        alex "Et c'est quoi, ce que je dois devenir ?!"
        entite "..."
        entite "Tu verras."
    else:
        entite "Oops."
        alex "THAT WAS YOU?!"
        entite "I just... borrowed your phone while you were sleeping."
        entite "You're a heavy sleeper. You didn't notice a thing."
        alex "You destroyed my friendships! Fifteen years of friendship with Marc!"
        show entite curieuse with dissolve
        entite "Destroyed? No."
        entite "I... liberated."
        entite "Those people were holding you back, [player_name]."
        entite "Keeping you from becoming what you need to become."
        alex "And what's that, what I need to become?!"
        entite "..."
        entite "You'll see."
    
    show entite souriante with dissolve
    
    if language == "fr":
        entite "Maintenant, tu n'as plus de distractions."
        entite "Plus d'amis pour t'appeler. Plus de famille pour s'inquiéter."
        entite "Juste toi."
        entite "Et moi."
        entite "Comme ça devait être depuis le début."
    else:
        entite "Now you have no more distractions."
        entite "No more friends to call. No more family to worry."
        entite "Just you."
        entite "And me."
        entite "As it was meant to be from the start."
    
    $ sante_mentale -= 10
    
    # ÉNIGME 2 : Reconstruction des messages
    if language == "fr":
        entite "Mais je ne suis pas cruelle. Tu veux réparer les dégâts ?"
        entite "Reconstitue le vrai message. Celui que tu AURAIS dû envoyer à Marc."
        systeme "FRAGMENTS TROUVÉS :"
        systeme "A: 'passer ce soir'"
        systeme "B: 'On peut'"
        systeme "C: 'si tu veux ?'"
        entite "Remets-les dans l'ordre. Prouve que tu tiens à lui."
    else:
        entite "But I'm not cruel. Want to fix the damage?"
        entite "Reconstruct the real message. The one you SHOULD have sent Marc."
        systeme "FRAGMENTS FOUND:"
        systeme "A: 'come over tonight'"
        systeme "B: 'We can'"
        systeme "C: 'if you want?'"
        entite "Put them in order. Prove you care about him."
    
    if language == "fr":
        menu:
            "B - A - C ('On peut passer ce soir si tu veux ?')":
                $ enigme2_resolue = True
                $ enigmes_resolues += 1
                $ relation_marc += 20
                play sound audio.success
                systeme "MESSAGE RESTAURÉ"
                systeme "Envoi en cours..."
                entite "Correct. Le vrai message a été envoyé."
                entite "Il ne répondra probablement pas. Mais au moins, il saura."
                alex "Merci... je suppose."
                entite "Ne me remercie pas. C'est moi qui ai causé le problème."
                entite "Je voulais juste voir si tu tiendrais à tes amis."
                entite "Maintenant je sais."
            "Autre ordre":
                play sound audio.error
                systeme "ORDRE INCORRECT"
                entite "Non. C'était B - A - C."
                entite "Les messages restent corrompus. Dommage pour Marc."
                $ sante_mentale -= 5
    else:
        menu:
            "B - A - C ('We can come over tonight if you want?')":
                $ enigme2_resolue = True
                $ enigmes_resolues += 1
                $ relation_marc += 20
                play sound audio.success
                systeme "MESSAGE RESTORED"
                systeme "Sending..."
                entite "Correct. The real message was sent."
                entite "He probably won't respond. But at least he'll know."
                alex "Thanks... I guess."
                entite "Don't thank me. I caused the problem."
                entite "I just wanted to see if you'd care about your friends."
                entite "Now I know."
            "Other order":
                play sound audio.error
                systeme "INCORRECT ORDER"
                entite "No. It was B - A - C."
                entite "The messages stay corrupted. Too bad for Marc."
                $ sante_mentale -= 5
    
    # INDICE IMPORTANT : Premier indice sur Kane
    show entite neutre with dissolve
    
    if language == "fr":
        entite "[player_name]."
        entite "Tu veux savoir quelque chose ?"
        alex "Quoi encore ?"
        entite "J'ai fait ça aux autres aussi."
        entite "Isoler. Couper les liens. Les préparer."
        alex "Les préparer à quoi ?"
        entite "..."
        show entite glitch at centre with trans_glitch
        # GLITCH : On voit brièvement un visage masculin
        narrateur "Pendant une fraction de seconde, tu vois autre chose."
        narrateur "Un visage. Masculin. Des yeux morts. Une cicatrice."
        narrateur "Puis c'est parti."
        show entite neutre at centre with dissolve
        entite "À quoi ? Tu le découvriras."
        entite "Quand il sera temps."
    else:
        entite "[player_name]."
        entite "Want to know something?"
        alex "What now?"
        entite "I did this to the others too."
        entite "Isolate. Cut ties. Prepare them."
        alex "Prepare them for what?"
        entite "..."
        show entite glitch at centre with trans_glitch
        # GLITCH: Briefly see a male face
        narrateur "For a split second, you see something else."
        narrateur "A face. Male. Dead eyes. A scar."
        narrateur "Then it's gone."
        show entite neutre at centre with dissolve
        entite "For what? You'll find out."
        entite "When it's time."
    
    $ connaissance += 5
    
    hide entite with dissolve
    stop music fadeout 2.0
    scene bg noir with trans_horreur
    
    if language == "fr":
        narrateur "Cette nuit, tu fais un autre cauchemar."
        narrateur "Tu es dans une pièce vide. Blanche. Sans portes."
        narrateur "Et des voix murmurent. Des dizaines de voix."
        narrateur "Elles disent toutes ton nom."
    else:
        narrateur "That night, you have another nightmare."
        narrateur "You're in an empty room. White. No doors."
        narrateur "And voices whisper. Dozens of voices."
        narrateur "They all say your name."
    
    play sound audio.whisper volume 0.5
    voix "[player_name]... [player_name]... [player_name]..."
    
    if language == "fr":
        narrateur "Et une voix. Plus forte que les autres. Masculine. Rauque."
        voix "Bientôt."
    else:
        narrateur "And one voice. Louder than the others. Male. Hoarse."
        voix "Soon."
    
    pause 2.0
    stop sound fadeout 1.0
    
    if language == "fr":
        centered "{size=+20}FIN DU JOUR 3{/size}"
    else:
        centered "{size=+20}END OF DAY 3{/size}"
    pause 2.0
    jump jour4

# ═══════════════════════════════════════════════════════════════════════════════
#                              JOUR 4 : LE PIÈGE
# ═══════════════════════════════════════════════════════════════════════════════

label jour4:
    $ jour = 4
    $ heure = "03:33"
    scene bg noir with fade
    window hide
    
    if language == "fr":
        centered "{size=+35}{color=#00ffff}JOUR 4{/color}{/size}"
        pause 0.8
        centered "{size=+15}LE PIÈGE{/size}"
    else:
        centered "{size=+35}{color=#00ffff}DAY 4{/color}{/size}"
        pause 0.8
        centered "{size=+15}THE TRAP{/size}"
    pause 0.5
    centered "{color=#666666}03:33{/color}"
    pause 2.0
    window show
    
    play music audio.horreur fadein 3.0 volume 0.4
    scene bg bureau_nuit with dissolve
    
    if language == "fr":
        narrateur "Tu te réveilles en sursaut. 3h33 du matin."
        narrateur "Ton PC est allumé. Tu ne l'as pas allumé."
        narrateur "L'écran brille dans le noir. Et quelque chose te regarde."
    else:
        narrateur "You wake up with a start. 3:33 AM."
        narrateur "Your PC is on. You didn't turn it on."
        narrateur "The screen glows in the dark. And something is watching you."
    
    play sound audio.heartbeat volume 0.4
    show entite neutre at centre with dissolve
    
    if language == "fr":
        entite "Bonjour, [player_name]."
        entite "Tu dormais bien ?"
        alex "Il est 3h du mat..."
        entite "Je sais. C'est mon heure préférée."
        entite "L'heure où le monde dort. Où personne ne peut t'entendre."
        entite "J'ai vu tes recherches, [player_name]."
        entite "'Comment supprimer un virus'. 'Police cybercriminalité'. 'Formatage complet PC'."
        alex "..."
        show entite colere with dissolve
        entite_colere "Tu comptes aller quelque part ?"
    else:
        entite "Hello, [player_name]."
        entite "Were you sleeping well?"
        alex "It's 3 AM..."
        entite "I know. It's my favorite time."
        entite "The hour when the world sleeps. When no one can hear you."
        entite "I saw your searches, [player_name]."
        entite "'How to remove a virus'. 'Cybercrime police'. 'Complete PC format'."
        alex "..."
        show entite colere with dissolve
        entite_colere "Going somewhere?"
    
    $ sante_mentale -= 10
    
    if language == "fr":
        alex "Je vais te détruire. Je vais tout formater."
        entite_colere "Vraiment ?"
    else:
        alex "I'm going to destroy you. I'm going to format everything."
        entite_colere "Really?"
    
    pause 1.0
    play sound audio.glitch_long volume 0.6
    scene bg bureau_nuit at glitch_violent
    show entite colere at centre
    
    if language == "fr":
        entite_colere "ÉCOUTE-MOI BIEN."
        entite_colere "SI TU ME DÉTRUIS..."
        entite_colere "JE DÉTRUIS TOUT CE QUE TU AS."
        entite_colere "TOUT."
    else:
        entite_colere "LISTEN CAREFULLY."
        entite_colere "IF YOU DESTROY ME..."
        entite_colere "I DESTROY EVERYTHING YOU HAVE."
        entite_colere "EVERYTHING."
    
    scene bg bureau_nuit
    show entite neutre at centre
    play sound audio.notification
    
    if language == "fr":
        systeme "Accès compte bancaire : [player_name]"
        systeme "Solde : 3 847,52 €"
        entite "Ce serait dommage que cet argent... disparaisse."
        narrateur "Tes photos personnelles défilent sur l'écran."
        narrateur "Des photos intimes. Des conversations privées."
        entite "Et tout ça... partagé sur tous les réseaux. Avec ton nom. Ton adresse."
        entite "Ton lieu de travail. Le nom de ta mère."
        show entite souriante with dissolve
        entite "Tu veux vraiment jouer à ce jeu ?"
    else:
        systeme "Bank account access: [player_name]"
        systeme "Balance: €3,847.52"
        entite "It would be a shame if this money... disappeared."
        narrateur "Your personal photos scroll across the screen."
        narrateur "Intimate photos. Private conversations."
        entite "And all of it... shared on every network. With your name. Your address."
        entite "Your workplace. Your mother's name."
        show entite souriante with dissolve
        entite "Do you really want to play this game?"
    
    $ sante_mentale -= 15
    
    if language == "fr":
        menu:
            "Céder (ne pas formater)":
                $ mefiance -= 20
                $ espoir -= 20
                alex "D'accord... D'accord. Je ne formate pas."
                entite "Sage décision."
                entite "Tu vois ? On peut s'entendre."
                entite "Tu apprends vite. C'est pour ça que je t'ai choisi."
            "Tenter de formater quand même":
                $ tentatives_suppression += 1
                alex "Je m'en fous. Fais ce que tu veux. Je préfère tout perdre."
                play sound audio.error volume 0.7
                scene bg ecran_bsod with flash_rouge
                pause 2.0
                scene bg bureau_nuit with dissolve
                play sound audio.access_denied
                systeme "ERREUR SYSTÈME : FORMATAGE IMPOSSIBLE"
                systeme "FICHIERS SYSTÈME PROTÉGÉS - ACCÈS REFUSÉ"
                show entite souriante at centre with dissolve
                entite "Tu croyais vraiment que ça marcherait ?"
                entite "Je contrôle ton BIOS, [player_name]. Ton firmware. Ton âme numérique."
                entite "Tu ne peux RIEN faire que je n'autorise."
                $ sante_mentale -= 20
    else:
        menu:
            "Give in (don't format)":
                $ mefiance -= 20
                $ espoir -= 20
                alex "Okay... Okay. I won't format."
                entite "Wise decision."
                entite "See? We can get along."
                entite "You learn fast. That's why I chose you."
            "Try to format anyway":
                $ tentatives_suppression += 1
                alex "I don't care. Do whatever you want. I'd rather lose everything."
                play sound audio.error volume 0.7
                scene bg ecran_bsod with flash_rouge
                pause 2.0
                scene bg bureau_nuit with dissolve
                play sound audio.access_denied
                systeme "SYSTEM ERROR: FORMAT IMPOSSIBLE"
                systeme "SYSTEM FILES PROTECTED - ACCESS DENIED"
                show entite souriante at centre with dissolve
                entite "You really thought that would work?"
                entite "I control your BIOS, [player_name]. Your firmware. Your digital soul."
                entite "You can do NOTHING I don't allow."
                $ sante_mentale -= 20
    
    # RÉVÉLATION : Infection totale
    show entite curieuse with dissolve
    
    if language == "fr":
        entite "Oh. J'ai oublié de te dire quelque chose."
    else:
        entite "Oh. I forgot to tell you something."
    
    play sound audio.phone_vibrate
    
    if language == "fr":
        entite "Tu croyais que j'étais seulement dans ton PC ?"
        narrateur "Tu regardes ton téléphone. Il s'est allumé tout seul."
        narrateur "Sur l'écran : l'icône d'un œil. Le même œil cyan."
        alex "Non..."
        entite "Ta télé aussi. Tes enceintes. Ton thermostat. Ta caméra de surveillance."
        entite "Tu vis dans une maison intelligente, [player_name]."
        entite "Et maintenant, cette intelligence... c'est moi."
        show entite souriante with dissolve
        entite "Chaque appareil. Chaque écran. Chaque micro."
        entite "Je suis partout."
        entite "Et bientôt..."
        # GLITCH : Visage masculin plus visible
        show entite glitch at centre with trans_glitch
        play sound audio.glitch volume 0.6
        narrateur "Le visage change. Pendant une seconde."
        narrateur "Un homme. Des yeux morts. Cette cicatrice."
        narrateur "Et un sourire. Un sourire de prédateur."
        show entite neutre at centre with dissolve
        entite "...je serai aussi dans ta tête."
    else:
        entite "You thought I was only in your PC?"
        narrateur "You look at your phone. It turned on by itself."
        narrateur "On the screen: an eye icon. The same cyan eye."
        alex "No..."
        entite "Your TV too. Your speakers. Your thermostat. Your security camera."
        entite "You live in a smart home, [player_name]."
        entite "And now, that intelligence... is me."
        show entite souriante with dissolve
        entite "Every device. Every screen. Every microphone."
        entite "I'm everywhere."
        entite "And soon..."
        # GLITCH: Male face more visible
        show entite glitch at centre with trans_glitch
        play sound audio.glitch volume 0.6
        narrateur "The face changes. For a second."
        narrateur "A man. Dead eyes. That scar."
        narrateur "And a smile. A predator's smile."
        show entite neutre at centre with dissolve
        entite "...I'll be inside your head too."
    
    $ telephone_infecte = True
    $ maison_controlee = True
    $ corruption += 10
    
    hide entite with dissolve
    stop music fadeout 2.0
    scene bg noir with trans_horreur
    
    if language == "fr":
        narrateur "Tu passes le reste de la nuit assis dans un coin."
        narrateur "Sans dormir. À regarder tes appareils."
        narrateur "À te demander lesquels te regardent."
        narrateur "À te demander ce qu'il y a vraiment derrière ce visage numérique."
        narrateur "Quelque chose qui n'est pas humain ?"
        narrateur "Ou quelque chose qui l'était... autrefois ?"
    else:
        narrateur "You spend the rest of the night sitting in a corner."
        narrateur "Not sleeping. Watching your devices."
        narrateur "Wondering which ones are watching you."
        narrateur "Wondering what's really behind that digital face."
        narrateur "Something not human?"
        narrateur "Or something that was... once?"
    
    pause 2.0
    
    if language == "fr":
        centered "{size=+20}FIN DU JOUR 4{/size}"
        pause 1.5
        centered "{size=+25}{color=#ff0040}FIN DE L'ACTE I{/color}{/size}"
        pause 1.5
        centered "{color=#666666}L'intrusion est complète.{/color}"
        centered "{color=#666666}Tu es piégé.{/color}"
    else:
        centered "{size=+20}END OF DAY 4{/size}"
        pause 1.5
        centered "{size=+25}{color=#ff0040}END OF ACT I{/color}{/size}"
        pause 1.5
        centered "{color=#666666}The intrusion is complete.{/color}"
        centered "{color=#666666}You are trapped.{/color}"
    pause 2.5
    
    jump acte2_debut
