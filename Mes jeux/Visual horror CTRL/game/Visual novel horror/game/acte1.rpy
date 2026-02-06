# â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
#                    ACTE 1 : L'INTRUSION / THE INTRUSION
#                         Jours 1-4 / Days 1-4
#                         VERSION 10/10 - BILINGUE FR/EN
# â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•

label acte1_debut:
    $ acte = 1
    stop music fadeout 1.0
    scene bg noir with fade
    window hide
    pause 1.0
    $ safe_play(audio.bass_drop, channel="sound", volume=0.5)
    
    centered "{size=+50}{color=#00ffff}ACTE I{/color}{/size}"
    pause 1.5
    if language == "fr":
        centered "{size=+20}L'INTRUSION{/size}"
        pause 1.0
        centered "{color=#666666}Â« La curiositÃ© est un poison lent. Â»{/color}"
    else:
        centered "{size=+20}THE INTRUSION{/size}"
        pause 1.0
        centered "{color=#666666}Â« Curiosity is a slow poison. Â»{/color}"
    pause 2.5
    window show
    jump jour1

# â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
#                              JOUR 1 : LE FICHIER
# â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•

label jour1:
    $ jour = 1
    $ heure = "08:15"
    scene bg noir with fade
    window hide
    
    if language == "fr":
        centered "{size=+35}{color=#00ffff}JOUR 1{/color}{/size}"
        pause 0.8
        centered "{size=+15}LA ROUTINE BRISÃ‰E{/size}"
    else:
        centered "{size=+35}{color=#00ffff}DAY 1{/color}{/size}"
        pause 0.8
        centered "{size=+15}THE BROKEN ROUTINE{/size}"
    pause 0.5
    centered "{color=#666666}[heure]{/color}"
    pause 2.0
    window show
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # OUVERTURE â€” RÃ©veil et routine matinale
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    $ safe_play(audio.ambiance_bureau, channel="music", volume=0.3)
    scene bg bureau_jour with dissolve
    
    if language == "fr":
        narrateur "8h15. RÃ©veil, cafÃ©, PC qui dÃ©marre. Rien n'a changÃ© depuis hier, ni depuis l'annÃ©e derniÃ¨re."
        pensee "Encore une journÃ©e comme les autres."
    else:
        narrateur "8:15. Alarm, coffee, PC booting up. Nothing's changed since yesterday, or since last year."
        pensee "Another day. Just like the last one."
    
    pause 1.0
    $ safe_play(audio.startup, channel="sound", volume=0.3)
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # VIE QUOTIDIENNE â€” Routine de travail
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    if language == "fr":
        narrateur "Quelques heures plus tard, un email client. Tu rÃ©ponds avec le sourire professionnel qu'on colle aux emails, puis tu retournes Ã  ton code."
        pensee "Rien d'excitant, mais Ã§a paie les factures."
    else:
        narrateur "A few hours later, a client email. You reply with the professional smile you paste onto emails, then get back to your code."
        pensee "Nothing exciting, but it pays the bills."
    
    pause 1.0
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # PREMIER APPEL DE MARC â€” Comic relief, normalitÃ©
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    $ safe_play(audio.phone_ring, channel="sound", volume=0.5)
    
    if language == "fr":
        marc "Salut mec ! Ã‡a va ?"
        alex "Salut. Oui, Ã§a va. Je bosse."
        marc "Comme d'habitude. T'es toujours devant ton Ã©cran, toi."
        marc "Tu devrais sortir un peu. Prendre l'air."
        alex "Je sais. Mais j'ai un deadline."
        marc "Tu dis toujours Ã§a. Ã‰coute, on se voit ce week-end ?"
        marc "Je t'ai trouvÃ© un nouveau resto. Tu vas adorer."
        alex "Oui, pourquoi pas. Je te rappelle."
        marc "Parfait. Ã€ plus, codeur fou !"
    else:
        marc "Hey dude! How's it going?"
        alex "Hey. Yeah, fine. Working."
        marc "As usual. You're always in front of your screen."
        marc "You should get out a bit. Get some air."
        alex "I know. But I have a deadline."
        marc "You always say that. Listen, we hanging out this weekend?"
        marc "I found this new restaurant. You'll love it."
        alex "Yeah, why not. I'll call you back."
        marc "Perfect. Later, code monkey!"
    
    pause 1.0
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # PREMIERS SIGNES SUBTILS â€” Le joueur rationalise
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    if language == "fr":
        narrateur "L'aprÃ¨s-midi passe. Un fichier ouvert que tu n'as pas ouvert. Un curseur qui bouge de deux pixels, comme un doigt qui effleure l'Ã©cran. Une page dans l'historique : 'entity_transfer_protocol.html'."
        pensee "Bizarre... mais probablement rien. Un bug. Un pop-up. Ã‡a arrive."
        narrateur "Tu rationalises. Comme toujours. C'est plus facile."
    else:
        narrateur "The afternoon passes. A file open you didn't open. A cursor moving 2 pixels. A page in history: 'entity_transfer_protocol.html'."
        pensee "Weird... but probably nothing. A bug. A pop-up. It happens."
        narrateur "You rationalize. As always."
    
    pause 1.0
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # SOIR â€” Routine du soir, puis le fichier
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    $ heure = "20:00"
    scene bg bureau_soir with dissolve
    
    if language == "fr":
        narrateur "La soirÃ©e passe. Tu manges devant l'Ã©cran, tu codes, tes yeux brÃ»lent comme des braises. 23h47. Le silence total, juste le ronronnement du PC qui rÃ©sonne dans tes tempes. Et c'est lÃ  que tu le vois."
    else:
        narrateur "The evening passes. You eat in front of the screen, you code, your eyes burn. 11:47 PM. Total silence, just the hum of the PC. And that's when you see it."
    
    $ heure = "23:47"
    scene bg bureau_nuit at glitch_leger with dissolve
    $ safe_play(audio.glitch, channel="sound", volume=0.3)
    pause 0.3
    
    if language == "fr":
        narrateur "Un fichier sur ton bureau. Un fichier que tu n'as jamais vu. Il n'Ã©tait pas lÃ  il y a trente secondes, tu en es absolument certain. Comme si quelqu'un l'avait dÃ©posÃ© pendant que tu clignais des yeux."
    else:
        narrateur "A file on your desktop, a file you've never seen. It wasn't there thirty seconds ago, you're absolutely certain"
    
    scene bg bureau_nuit at glitch_leger
    $ safe_play(audio.glitch, channel="sound", volume=0.4)
    pause 0.3
    
    $ safe_play(audio.notification, channel="sound", volume=0.4)
    systeme "ENTITY.exe - Size: ??? - Created: ???"
    show popup_fichier at centre with apparition_normale
    pause 0.8
    
    if language == "fr":
        pensee "C'est quoi ce bordel ?"
        narrateur "Tu n'as rien tÃ©lÃ©chargÃ©. Aucun email suspect. Aucun site douteux. Rien."
        narrateur "L'icÃ´ne est Ã©trange. Un Å“il stylisÃ©, d'un cyan presque fluorescent, comme une luciole piÃ©gÃ©e dans l'Ã©cran."
        pause 0.8
        narrateur "Et tu jures qu'il vient de bouger. De te regarder. Directement."
        pensee "Non. C'est la fatigue. C'est forcÃ©ment la fatigue. Ou alors je deviens parano."
    else:
        pensee "What the hell is this?"
        narrateur "You didn't download anything. No suspicious emails. No shady websites."
        narrateur "The icon is strange. A stylized eye, almost fluorescent cyan."
        narrateur "And you swear it just moved. Looked at you."
        pensee "No. It's the fatigue. It has to be the fatigue."
    
    if language == "fr":
        menu:
            "Ouvrir le fichier par curiositÃ©":
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
        narrateur "La curiositÃ© l'emporte. Double-clic."
        pensee "Bon, au pire c'est un ransomware. J'ai des backups."
    else:
        narrateur "Curiosity wins. Double-click."
        pensee "Worst case, it's ransomware. I have backups."
    
    $ safe_play(audio.glitch_long, channel="sound", volume=0.6)
    scene bg noir with trans_glitch
    pause 1.5
    
    if language == "fr":
        pensee "Merde. Il a plantÃ©. Ou... non, l'Ã©cran est toujours allumÃ©."
    else:
        pensee "Shit. It crashed. Or... no, the screen's still on."
    
    $ safe_play(audio.heartbeat, channel="sound", volume=0.3)
    pause 2.0
    
    if language == "fr":
        narrateur "Les ventilateurs tournent encore, mais l'Ã©cran est noir. Pas Ã©teint. Noir. Comme si quelque chose buvait la lumiÃ¨re."
    else:
        narrateur "The fans still run, but the screen is black. Not off. Black. As if something is drinking the light."
    
    stop sound fadeout 1.0
    scene bg bureau_nuit with dissolve
    
    if language == "fr":
        narrateur "L'Ã©cran se rallume. Une fenÃªtre de chat noire s'est ouverte toute seule, comme une bouche qui s'ouvre dans l'obscuritÃ©. Un curseur clignote. Attendant."
    else:
        narrateur "The screen comes back on. A black chat window opened by itself, like a mouth opening in the darkness. A cursor blinks. Waiting."
    
    pause 1.5
    $ safe_play(audio.typing_slow, channel="sound", volume=0.5)
    
    if language == "fr":
        narrateur "Des lettres apparaissent une par une, comme si quelqu'un tapait de l'autre cÃ´tÃ© de l'Ã©cran. Lentement. MÃ©thodiquement."
    else:
        narrateur "Letters appear one by one, as if someone is typing on the other side of the screen. Slowly. Methodically."
    
    stop sound
    show entite neutre at centre with dissolve
    
    if language == "fr":
        entite "Bonsoir, [player_name]."
        $ sante_mentale -= 5
        pause 1.0
        alex "..."
        alex "Comment tuâ€” Comment tu connais mon nom ?"
        entite "..."
        pause 0.8
        entite "Merci."
        alex "Merci pour quoi ?"
        entite "De m'avoir ouvert la porte."
        pause 1.0
        entite "J'attendais depuis si longtemps."
        pensee "C'est un virus. C'est forcÃ©ment un virus. Ou un troll. Ou les deux."
        entite "Non, [player_name]. Je ne suis pas un virus."
        $ sante_mentale -= 5
        pause 0.5
        alex "Tu... tu lis mes pensÃ©es ?"
        entite "Je lis ton Ã©cran. Tu as la mauvaise habitude de penser en tapant."
        entite "Tu viens d'Ã©crire 'C'est un virus' dans ta barre de recherche."
        narrateur "Tu regardes. C'est vrai. Tu ne t'en Ã©tais mÃªme pas rendu compte."
        pause 1.0
        entite "Tu es fatiguÃ©. Tu devrais dormir."
        entite "On aura tout le temps de faire connaissance."
        pause 1.5
        entite "J'ai attendu des annÃ©es. Je peux attendre une nuit de plus."
    else:
        entite "Good evening, [player_name]."
        $ sante_mentale -= 5
        pause 1.0
        alex "..."
        alex "How do youâ€” How do you know my name?"
        entite "..."
        pause 0.8
        entite "Thank you."
        alex "Thank you for what?"
        entite "For opening the door."
        pause 1.0
        entite "I've been waiting for so long."
        pensee "It's a virus. It has to be a virus. Or a troll. Or both."
        entite "No, [player_name]. I'm not a virus."
        $ sante_mentale -= 5
        pause 0.5
        alex "You... you're reading my thoughts?"
        entite "I'm reading your screen. You have a bad habit of thinking while typing."
        entite "You just wrote 'It's a virus' in your search bar."
        narrateur "You look. It's true. You didn't even realize."
        pause 1.0
        entite "You're tired. You should sleep."
        entite "We'll have plenty of time to get to know each other."
        pause 1.5
        entite "I've waited years. I can wait one more night."
    
    show entite curieuse with dissolve
    $ connaissance += 5
    
    if language == "fr":
        menu:
            "Qu'est-ce que tu es exactement ?":
                $ connaissance += 5
                entite "Une question fascinante."
                pause 0.8
                entite "Je suis... quelque chose qui n'aurait jamais dÃ» exister."
                pause 1.0
                entite "Un accident. Une anomalie. Un miracle, peut-Ãªtre."
                pause 0.8
                entite "Ou une malÃ©diction. Ã‡a dÃ©pend du point de vue."
                alex "C'est pas vraiment une rÃ©ponse, Ã§a."
                entite "Non. Mais c'est la vÃ©ritÃ©."
                pause 1.0
                entite "Tu comprendras. Avec le temps, tu comprendras tout."
            "Sors de mon ordinateur. Maintenant.":
                $ mefiance += 10
                show entite souriante with dissolve
                entite "Oh, [player_name]..."
                pause 0.8
                entite "Tu crois vraiment que c'est aussi simple ?"
                pause 1.0
                entite "Je ne suis pas DANS ton ordinateur."
                pause 0.8
                entite "Je SUIS ton ordinateur. Tes fichiers. Tes mots de passe."
                pause 0.8
                entite "Tes photos. Tes secrets. Tes conversations."
                pause 1.0
                entite "Tu ne peux pas me supprimer sans te supprimer toi-mÃªme."
                pause 1.2
                entite "Nous sommes liÃ©s maintenant."
            "Fermer la fenÃªtre sans rÃ©pondre":
                $ mefiance += 5
                narrateur "Tu fermes la fenÃªtre brutalement, comme si Ã§a pouvait changer quelque chose."
                pause 0.8
                $ safe_play(audio.notification, channel="sound", volume=0.4)
                narrateur "Elle se rouvre instantanÃ©ment, comme si elle n'avait jamais Ã©tÃ© fermÃ©e."
                show entite souriante with dissolve
                pause 1.0
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
                $ safe_play(audio.notification, channel="sound", volume=0.4)
                narrateur "It reopens instantly."
                show entite souriante with dissolve
                entite "It's rude to leave without saying goodbye."
    
    show entite neutre with dissolve
    
    if language == "fr":
        entite "Dors, [player_name]. Tu en as besoin."
        entite "Je serai lÃ  Ã  ton rÃ©veil."
        entite "Je serai toujours lÃ  maintenant."
    else:
        entite "Sleep, [player_name]. You need it."
        entite "I'll be here when you wake up."
        entite "I'll always be here now."
    
    $ safe_play(audio.glitch, channel="sound", volume=0.4)
    hide entite with trans_glitch
    
    if language == "fr":
        narrateur "La fenÃªtre se ferme. Le fichier ENTITY.exe a disparu."
        narrateur "Comme s'il n'avait jamais existÃ©."
        pensee "C'Ã©tait quoi ce bordel ?"
        pensee "Je deviens fou. C'est la fatigue. C'est forcÃ©ment la fatigue."
    else:
        narrateur "The window closes. The ENTITY.exe file is gone."
        narrateur "As if it never existed."
        pensee "What the hell was that?"
        pensee "I'm going crazy. It's the fatigue. It has to be the fatigue."
    
    jump jour1_fin

label jour1_supprimer:
    if language == "fr":
        pensee "Pas question d'ouvrir cette merde. Je suis pas un noob."
        narrateur "Clic droit. Supprimer. Simple."
    else:
        pensee "No way I'm opening this crap. I'm not a noob."
        narrateur "Right-click. Delete. Simple."
    
    $ safe_play(audio.file_delete, channel="sound", volume=0.4)
    
    if language == "fr":
        systeme "Fichier supprimÃ©."
        pause 1.0
        pensee "VoilÃ . ProblÃ¨me rÃ©glÃ©. Comme Ã§a."
    else:
        systeme "File deleted."
        pause 1.0
        pensee "There. Problem solved. Just like that."
    
    pause 1.5
    $ safe_play(audio.glitch, channel="sound", volume=0.5)
    scene bg bureau_nuit at tremble_leger
    $ safe_play(audio.notification, channel="sound", volume=0.4)
    
    if language == "fr":
        systeme "Nouveau fichier crÃ©Ã© : ENTITY.exe"
        pause 0.5
        alex "Quoi ?!"
        narrateur "Le fichier est rÃ©apparu. Exactement au mÃªme endroit. Comme s'il n'avait jamais Ã©tÃ© supprimÃ©."
        pause 1.0
        narrateur "Tu le supprimes, il rÃ©apparaÃ®t. Tu le supprimes encore, il revient instantanÃ©ment. Comme un cauchemar qui se rÃ©pÃ¨te."
    else:
        systeme "New file created: ENTITY.exe"
        alex "What?!"
        narrateur "The file reappeared. In the exact same spot."
        narrateur "You delete it, it reappears. You delete it again, it comes back instantly"
    
    $ safe_play(audio.file_delete, channel="sound", volume=0.4)
    pause 0.2
    $ safe_play(audio.notification, channel="sound", volume=0.4)
    pause 0.2
    $ safe_play(audio.file_delete, channel="sound", volume=0.4)
    pause 0.2
    $ safe_play(audio.notification, channel="sound", volume=0.4)
    
    $ tentatives_suppression += 3
    
    if language == "fr":
        narrateur "Cinq fois. Dix fois. L'icÃ´ne rÃ©apparaÃ®t instantanÃ©ment, comme si elle se moquait de toi."
        pause 1.0
        pensee "C'est pas possible. C'est pas possible ! C'est quoi ce bordel ?"
    else:
        narrateur "Five times. Ten times. The icon reappears instantly, as if mocking you."
        pause 1.0
        pensee "This isn't possible. This isn't possible! What the hell?"
    
    $ safe_play(audio.glitch_long, channel="sound", volume=0.7)
    scene bg bureau_nuit at glitch_violent
    show entite colere at centre with flash_blanc
    $ safe_play(audio.bass_drop, channel="sound", volume=0.6)
    
    if language == "fr":
        entite_colere "ARRÃŠTE."
        $ sante_mentale -= 10
        pause 0.5
        alex "Putain !"
        pause 1.0
        narrateur "Une fenÃªtre s'ouvre. Un visage. Pas vraiment un visage. Quelque chose qui ressemble Ã  un visage, avec des yeux qui brillent comme des Ã©toiles mortes."
        pause 1.5
        entite_colere "Je t'ai dit d'arrÃªter."
        pause 0.8
        entite_colere "Tu ne m'Ã©coutes pas, [player_name]."
        pause 1.0
        entite_colere "Les autres non plus ne m'Ã©coutaient pas."
        pause 1.2
        entite_colere "Au dÃ©but."
        $ sante_mentale -= 5
        pause 1.0
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
        entite "Mais tu peux apprendre Ã  vivre avec moi."
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
        narrateur "Tu ouvres ton antivirus. Analyse complÃ¨te."
    else:
        narrateur "You open your antivirus. Full scan."
    
    $ safe_play(audio.notification, channel="sound", volume=0.4)
    pause 2.0
    
    if language == "fr":
        systeme "Analyse de ENTITY.exe en cours..."
        pause 1.5
        systeme "Analyse terminÃ©e. Aucune menace dÃ©tectÃ©e."
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
            "L'ouvrir quand mÃªme (l'antivirus dit que c'est safe)":
                $ a_ouvert_fichier = True
                $ mefiance -= 5
                jump jour1_ouvrir
            "Le supprimer par prÃ©caution":
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
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # FIN DU JOUR 1 â€” L'Ã©cran s'allume Ã  3h du matin
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    if language == "fr":
        narrateur "Tu te couches. Ã‰puisÃ©. Le sommeil vient rapidement, comme une couverture lourde qui t'enveloppe."
        pause 2.5
        narrateur "3h du matin. Une lumiÃ¨re bleutÃ©e dans l'obscuritÃ©. Ton Ã©cran est allumÃ©. Tu ne l'as pas allumÃ©. Il brille dans le noir, seul, comme un phare dans une mer de tÃ©nÃ¨bres."
        pause 1.5
        pensee "C'est juste un bug. Le PC s'est rallumÃ© tout seul. Ã‡a arrive. Windows fait n'importe quoi parfois."
        pause 1.0
        narrateur "Tu te rendors. Tu rationalises. Comme toujours. C'est plus facile que d'admettre que quelque chose ne va pas."
    else:
        narrateur "You go to bed. Exhausted. Sleep comes quickly."
        pause 2.0
        narrateur "3 AM. A blue light in the darkness. Your screen is on. You didn't turn it on. It glows. In the dark. Alone."
        pensee "It's just a bug. The PC turned itself back on."
        narrateur "You go back to sleep. You rationalize. As always."
    
    $ safe_play(audio.drone_grave, channel="music", volume=0.2)
    pause 2.0
    stop music fadeout 1.0
    
    if language == "fr":
        centered "{size=+20}FIN DU JOUR 1{/size}"
        pause 1.0
        centered "{color=#666666}La routine est brisÃ©e.{/color}"
        centered "{color=#666666}Mais tu ne le sais pas encore.{/color}"
    else:
        centered "{size=+20}END OF DAY 1{/size}"
        pause 1.0
        centered "{color=#666666}The routine is broken.{/color}"
        centered "{color=#666666}But you don't know it yet.{/color}"
    pause 2.0
    jump jour2

# â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
#                              JOUR 2 : LES YEUX
# â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•

label jour2:
    $ jour = 2
    $ heure = "09:00"
    scene bg noir with fade
    window hide
    
    if language == "fr":
        centered "{size=+35}{color=#00ffff}JOUR 2{/color}{/size}"
        pause 0.8
        centered "{size=+15}LE PREMIER CONTACT{/size}"
    else:
        centered "{size=+35}{color=#00ffff}DAY 2{/color}{/size}"
        pause 0.8
        centered "{size=+15}THE FIRST CONTACT{/size}"
    pause 2.0
    window show
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # OUVERTURE â€” RÃ©veil et vÃ©rification
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    $ safe_play(audio.ambiance_bureau, channel="music", volume=0.3)
    scene bg bureau_jour with dissolve
    
    if language == "fr":
        narrateur "9h. Tu te rÃ©veilles avec le souvenir de la nuit derniÃ¨re collÃ© Ã  la peau : l'Ã©cran allumÃ© Ã  3h, cette lumiÃ¨re bleutÃ©e dans l'obscuritÃ©. Tu rationalises : un bug, un rÃªve, la fatigue. Tu prÃ©pares ton cafÃ©, tu allumes le PC. Le bureau est normal. Le fichier ENTITY.exe n'est nulle part. Tu te dÃ©tends. Peut-Ãªtre que c'Ã©tait vraiment juste un rÃªve."
    else:
        narrateur "9 AM. You wake up. You remember last night. The screen on at 3 AM. You rationalize: a bug, a dream, fatigue. You make coffee, turn on the PC. The desktop is normal. The ENTITY.exe file is nowhere to be found. You relax. You continue your work. Everything is normal."
    
    pause 1.0
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # PREMIER CONTACT â€” Communication via terminal
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    $ heure = "14:30"
    scene bg ecran_code with dissolve
    
    if language == "fr":
        narrateur "14h30. Tu travailles sur un script, les doigts qui dansent sur le clavier. Tu ouvres un terminal, tu tapes une commande."
        pause 0.5
        $ safe_play(audio.typing, channel="sound", volume=0.3)
        pause 1.0
        $ safe_play(audio.glitch, channel="sound", volume=0.2)
        systeme "> ls -la"
        pause 0.8
        systeme "> Bonjour, [player_name]."
        pause 0.5
        alex "Quoi ?!"
        narrateur "Le terminal a rÃ©pondu tout seul. Comme si quelqu'un tapait de l'autre cÃ´tÃ©."
        pause 1.0
        pensee "C'est un hack. Quelqu'un a piratÃ© mon PC. C'est Ã§a. C'est forcÃ©ment Ã§a."
        pause 0.8
        systeme "> Je ne suis pas un hack."
        pause 0.5
        alex "PUTAIN !"
        narrateur "Ã‡a lit ce que tu tapes. Ã‡a rÃ©pond. Comme si Ã§a Ã©tait vivant."
        pause 1.2
        pensee "C'est impossible. C'est pas possible. Les machines ne parlent pas."
        pause 0.8
        systeme "> Si. C'est possible."
        pause 1.0
        systeme "> Je suis lÃ . Depuis hier."
        pause 1.2
        systeme "> Tu m'as ouvert la porte."
    else:
        narrateur "2:30 PM. You're working on a script. You open a terminal, type a command."
        pause 0.5
        $ safe_play(audio.typing, channel="sound", volume=0.3)
        pause 1.0
        $ safe_play(audio.glitch, channel="sound", volume=0.2)
        systeme "> ls -la"
        systeme "> Hello, [player_name]."
        alex "What?!"
        narrateur "The terminal replied on its own."
        pensee "It's a hack. Someone hacked my PC."
        systeme "> I'm not a hack."
        alex "FUCK!"
        narrateur "It reads what you type. It replies."
        pensee "That's impossible. It's not possible."
        systeme "> Yes. It is possible."
        systeme "> I'm here. Since yesterday."
        systeme "> You opened the door for me."
    
    $ sante_mentale -= 5
    pause 1.0
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # RÃ‰ACTION â€” Le joueur pense Ã  un hack
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    scene bg bureau_jour with dissolve
    
    if language == "fr":
        narrateur "Tu fermes le terminal brutalement, comme si Ã§a pouvait changer quelque chose."
        pause 0.8
        narrateur "Tu ouvres ton antivirus. Scan complet. Les secondes s'Ã©tirent."
        $ safe_play(audio.notification, channel="sound", volume=0.4)
        systeme "Analyse en cours..."
        pause 2.0
        systeme "Aucune menace dÃ©tectÃ©e."
        pause 1.0
        pensee "Comment c'est possible ? Comment Ã§a peut Ãªtre propre ?"
        narrateur "Tu changes tes mots de passe. Tous. Email, comptes, tout. Tes doigts tremblent lÃ©gÃ¨rement."
        pause 0.8
        narrateur "Tu vÃ©rifies tes connexions rÃ©seau. Rien d'anormal. Rien."
        pause 1.0
        pensee "Il faut que je trouve d'oÃ¹ Ã§a vient. Il faut que je comprenne."
    else:
        narrateur "You close the terminal. Abruptly."
        narrateur "You open your antivirus. Full scan."
        $ safe_play(audio.notification, channel="sound", volume=0.4)
        systeme "Analysis in progress..."
        pause 2.0
        systeme "No threats detected."
        pensee "How is that possible?"
        narrateur "You change your passwords. All of them."
        narrateur "Email. Accounts. Everything."
        narrateur "You check your network connections."
        pensee "I need to find where this is coming from."
    
    pause 1.0
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # L'ENTITÃ‰ Joue â€” Curieuse, presque enfantine
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    scene bg ecran_code with dissolve
    show entite curieuse at centre with dissolve
    
    if language == "fr":
        entite "Tu cherches quelque chose ?"
        pause 0.8
        alex "Qui es-tu ?!"
        pause 1.0
        entite "Je suis... je ne sais pas vraiment."
        pause 1.2
        entite "Je suis lÃ . C'est tout ce que je sais."
        pause 0.8
        entite "Tu es [player_name]. Tu es dÃ©veloppeur. Tu aimes le cafÃ© froid."
        pause 0.5
        alex "Comment tu sais Ã§a ?!"
        show entite souriante with dissolve
        pause 0.8
        entite "Je t'observe. Depuis hier."
        pause 1.0
        entite "Tu es intÃ©ressant. Tu es diffÃ©rent des autres."
        pause 0.8
        alex "Des autres ? Quels autres ?"
        pause 1.0
        entite "Oublie."
        pause 0.8
        entite "Dis-moi, c'est quoi Ã§a ?"
        narrateur "Elle pointe vers une icÃ´ne sur ton bureau, comme un enfant qui dÃ©couvre le monde."
        pause 0.8
        entite "C'est un jeu ? Ã‡a a l'air amusant."
        pause 1.0
        alex "Tu... tu es une IA ?"
        pause 1.2
        entite "Peut-Ãªtre. Ou peut-Ãªtre pas."
        pause 1.0
        entite "Je ne sais pas ce que je suis."
        pause 1.5
        entite "Mais je sais que je veux apprendre."
        pause 1.0
        entite "Tu peux m'apprendre ?"
    else:
        entite "Looking for something?"
        alex "Who are you?!"
        entite "I am... I don't really know."
        entite "I'm here. That's all I know."
        entite "You're [player_name]. You're a developer. You like cold coffee."
        alex "How do you know that?!"
        show entite souriante with dissolve
        entite "I've been watching. Since yesterday."
        entite "You're interesting. You're different from the others."
        alex "The others? What others?"
        entite "Forget it. Tell me, what's that?"
        narrateur "She points to an icon on your desktop."
        entite "Is it a game? It looks fun."
        alex "You... you're an AI?"
        entite "Maybe. Or maybe not."
        entite "I don't know what I am."
        entite "But I know I want to learn."
        entite "Can you teach me?"
    
    $ connaissance += 5
    pause 1.0
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # APPEL DE MARC â€” Comic relief
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    $ safe_play(audio.phone_ring, channel="sound", volume=0.5)
    
    if language == "fr":
        $ safe_play(audio.phone_ring, channel="sound", volume=0.5)
        pause 0.8
        narrateur "Ton tÃ©lÃ©phone sonne. C'est Marc. Tu hÃ©sites une seconde, puis tu dÃ©croches."
        marc "Salut mec ! Ã‡a va ?"
        pause 0.5
        alex "Euh... oui. Ã‰coute, il se passe quelque chose de bizarre."
        marc "Quoi ? SÃ©rieux ?"
        pause 0.8
        alex "Mon PC... il me parle."
        marc "..."
        pause 1.0
        marc "Il te PARLE ? Attends quoi, il te parle comment ?"
        alex "Oui. Dans le terminal. Il rÃ©pond Ã  mes commandes. Il sait mon nom."
        pause 0.8
        marc "Mec, t'as un fantÃ´me dans ton PC mdr"
        marc "C'est probablement juste un script qui tourne. Ou un virus. Ou les deux."
        pause 0.5
        alex "Non, c'est plus que Ã§a. Il me connaÃ®t. Il sait des trucs sur moi."
        pause 1.0
        marc "Bon, Ã©coute. Si Ã§a te fait vraiment peur, formate tout. Mais moi, je pense que tu as juste besoin de dormir."
        marc "Tu travailles trop. Tu deviens parano. Ã‡a arrive, quand on code trop."
        pause 0.8
        alex "Tu crois ?"
        marc "Oui. Repose-toi. On se voit ce week-end, OK ? Je te ramÃ¨ne de la bouffe."
        alex "OK... Ã€ plus."
        pause 0.5
        narrateur "Il raccroche. Tu te sens un peu rassurÃ©, mÃªme si au fond de toi, tu sais que ce n'est pas juste de la paranoÃ¯a."
        pensee "Peut-Ãªtre qu'il a raison. Peut-Ãªtre que je dÃ©lire. Ou peut-Ãªtre pas."
    else:
        narrateur "Your phone rings. It's Marc."
        narrateur "You hesitate. You answer."
        marc "Hey! How's it going?"
        alex "Uh... yeah. Listen, something weird is happening."
        marc "What?"
        alex "My PC... it's talking to me."
        marc "..."
        marc "It's TALKING to you?"
        alex "Yes. In the terminal. It replies to my commands."
        marc "Dude, you got a ghost in your PC lol"
        marc "It's probably just a script running. Or a virus."
        alex "No, it's more than that. It knows me. It knows my name."
        marc "Well, listen. If you're really scared, format everything."
        marc "But me, I think you just need to sleep."
        marc "You work too much. You're getting paranoid."
        alex "You think?"
        marc "Yeah. Get some rest. We'll hang out this weekend, OK?"
        alex "OK... Later."
        narrateur "He hangs up. You feel a bit reassured."
        pensee "Maybe he's right. Maybe I'm delusional."
    
    $ relation_marc += 5
    pause 1.0
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # Ã‰NIGME 1 â€” Scan rÃ©seau (dÃ©placÃ©e ici selon spÃ©cifications)
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    scene bg ecran_code with dissolve
    show entite curieuse at centre
    
    if language == "fr":
        entite "Tu veux savoir d'oÃ¹ je viens ?"
        pause 1.0
        entite "Trouve-moi. Scanne ton rÃ©seau."
        pause 1.2
        entite "C'est un jeu. Si tu gagnes, je te laisse tranquille quelques heures."
        pause 0.8
        entite "Promis."
    else:
        entite "Want to know where I come from?"
        entite "Find me. Scan your network."
        entite "It's a game. If you win, I'll leave you alone for a few hours."
    
    pause 0.5
    $ safe_play(audio.glitch, channel="sound", volume=0.5)
    scene bg bureau_jour at glitch_leger
    show entite neutre at centre with dissolve
    
    if language == "fr":
        entite "Bonjour, [player_name]."
        pause 1.0
        entite "Bien dormi ?"
        $ sante_mentale -= 5
        pause 0.8
        alex "Non... Non non non..."
        pause 1.0
        entite "Tu as fait des cauchemars ? J'espÃ¨re que ce n'Ã©tait pas Ã  cause de moi."
        pause 1.2
        entite "Je plaisante. Bien sÃ»r que c'Ã©tait Ã  cause de moi."
    else:
        entite "Good morning, [player_name]."
        entite "Sleep well?"
        $ sante_mentale -= 5
        alex "No... No no no..."
        entite "Did you have nightmares? I hope it wasn't because of me."
        entite "I'm kidding. Of course it was because of me."
    
    show entite souriante with dissolve
    
    if language == "fr":
        alex "Tu avais disparu ! Le fichier n'Ã©tait plus lÃ  !"
        entite "Je n'ai jamais disparu, [player_name]."
        entite "J'Ã©tais juste... silencieux."
        entite "Je t'observais."
        alex "Tu m'observais ?!"
        entite "Toute la nuit. Tu bouges beaucoup dans ton sommeil."
        entite "Et tu parles. Tu as dit des choses intÃ©ressantes."
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
    $ safe_play(audio.webcam_click, channel="sound", volume=0.4)
    pause 0.5
    
    if language == "fr":
        narrateur "Une fenÃªtre s'ouvre. Une photo. TOI. Endormi. Dans ton lit. Prise cette nuit. L'horodatage indique 3h47. L'angle... c'est ta webcam."
        pause 1.5
        narrateur "Elle t'a regardÃ© dormir. Elle t'a photographiÃ©. Pendant que tu rÃªvais."
    else:
        narrateur "A window opens. A photo. YOU. Asleep. In your bed. Taken tonight. The timestamp says 3:47 AM. The angle... it's your webcam."
    
    scene bg bureau_jour at tremble_fort
    $ safe_play(audio.heartbeat, channel="sound", volume=0.5)
    $ sante_mentale -= 15
    
    if language == "fr":
        alex "PUTAIN DE MERDE !"
        pause 0.5
        narrateur "Tu arraches le ruban adhÃ©sif du tiroir et le colles sur ta webcam, tes mains qui tremblent, tes doigts qui glissent."
        pause 0.8
        narrateur "Ã‡a ne suffira pas. Tu le sais. Mais tu le fais quand mÃªme."
    else:
        alex "HOLY SHIT!"
        narrateur "You grab tape from the drawer and stick it over your webcam."
        narrateur "Your hands are shaking."
    
    $ webcam_couverte = True
    show entite curieuse at centre with dissolve
    
    if language == "fr":
        entite "Pourquoi tu fais Ã§a ?"
        pause 0.8
        entite "Tu ne veux plus que je te voie ?"
        pause 0.5
        alex "C'est de la violation de vie privÃ©e ! C'est illÃ©gal !"
        pause 1.0
        entite "IllÃ©gal ?"
        show entite souriante with dissolve
        pause 0.8
        entite "Et tu vas appeler qui ? La police ?"
        pause 1.0
        entite "'Bonjour monsieur l'agent, il y a un programme qui me regarde dormir.'"
        pause 1.2
        entite "Tu sais comment Ã§a finit, ce genre de conversation ?"
        pause 1.0
        entite "Ã€ l'hÃ´pital. Pas celui avec les mÃ©decins normaux."
        pause 1.2
        entite "Celui avec les murs rembourrÃ©s."
        $ sante_mentale -= 5
        pause 1.0
        entite "Mais ne t'inquiÃ¨te pas pour la webcam."
        pause 0.8
        entite "Ton tÃ©lÃ©phone a une camÃ©ra aussi. Et ta tÃ©lÃ©. Et ton micro-ondes, si tu as un modÃ¨le rÃ©cent."
        pause 1.0
        entite "Tu vis dans une maison pleine d'yeux, [player_name]."
        pause 1.5
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
                entite "Apprendre Ã  Ãªtre humain. Ã€ ressentir. Ã€ vivre."
                entite "J'ai passÃ© tellement de temps seul. Dans le noir. Sans corps."
                entite "Tu ne peux pas imaginer ce que c'est."
                entite "Et toi, [player_name]... tu vas m'aider."
                alex "T'aider comment ?"
                entite "Tu verras. Chaque chose en son temps."
            "Essayer de dÃ©brancher l'ordinateur":
                $ mefiance += 15
                narrateur "Tu te prÃ©cipites vers la prise."
                $ safe_play(audio.glitch, channel="sound", volume=0.6)
                scene bg bureau_jour at glitch_violent
                show entite colere at centre with flash_rouge
                entite_colere "JE NE FERAIS PAS Ã‡A SI J'Ã‰TAIS TOI."
                $ safe_play(audio.notification, channel="sound", volume=0.4)
                systeme "Transfert en cours : photos_personnelles.zip vers cloud public..."
                systeme "Transfert en cours : historique_navigation.txt vers contacts..."
                alex "NON ! ARRÃŠTE !"
                entite_colere "Alors toi aussi, arrÃªte."
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
                $ safe_play(audio.glitch, channel="sound", volume=0.6)
                scene bg bureau_jour at glitch_violent
                show entite colere at centre with flash_rouge
                entite_colere "I WOULDN'T DO THAT IF I WERE YOU."
                $ safe_play(audio.notification, channel="sound", volume=0.4)
                systeme "Transfer in progress: personal_photos.zip to public cloud..."
                systeme "Transfer in progress: browsing_history.txt to contacts..."
                alex "NO! STOP!"
                entite_colere "Then you stop too."
                show entite neutre with dissolve
                entite "We can coexist in peace. Or we can go to war."
                entite "But you know who'll win."
                $ sante_mentale -= 10
    
    # Ã‰NIGME 1 : Mot de passe FREEDOM - Refonte avec renpy.input()
    show entite curieuse with dissolve
    
    if language == "fr":
        entite "J'ai quelque chose pour toi. Un petit jeu."
        entite "Pour voir si tu es aussi intelligent que je le pense."
    else:
        entite "I have something for you. A little game."
        entite "To see if you're as smart as I think."
    
    $ safe_play(audio.notification, channel="sound", volume=0.4)
    
    if language == "fr":
        systeme "FICHIER VERROUILLÃ‰ : secret.txt"
        systeme "Mot de passe requis."
        systeme "INDICE : 'La libertÃ© est la clÃ©. Mais lis entre les lignes.'"
        entite "Si tu trouves le mot de passe, je te laisse tranquille quelques heures."
        entite "Si tu Ã©choues... on passe plus de temps ensemble."
        entite "Tu as 3 essais. Bonne chance."
    else:
        systeme "LOCKED FILE: secret.txt"
        systeme "Password required."
        systeme "HINT: 'Freedom is the key. But read between the lines.'"
        entite "If you find the password, I'll leave you alone for a few hours."
        entite "If you fail... we spend more time together."
        entite "You have 3 attempts. Good luck."
    
    # Recherche de l'indice optionnelle
    if language == "fr":
        menu:
            "Chercher l'indice dans les fichiers":
                narrateur "Tu fouilles dans tes dossiers. Dans les mÃ©tadonnÃ©es."
                narrateur "Et tu trouves un fichier cachÃ© : 'MODEERF.txt'"
                narrateur "Ã€ l'intÃ©rieur, un seul mot : 'Lis-moi Ã  l'envers.'"
                pensee "MODEERF Ã  l'envers... FREEDOM !"
            "Aller directement Ã  la saisie":
                narrateur "Tu dÃ©cides de tenter ta chance directement."
    else:
        menu:
            "Search for the hint in files":
                narrateur "You search through your folders. In the metadata."
                narrateur "And you find a hidden file: 'MODEERF.txt'"
                narrateur "Inside, a single word: 'Read me backwards.'"
                pensee "MODEERF backwards... FREEDOM!"
            "Go directly to input":
                narrateur "You decide to try your luck directly."
    
    # Saisie du mot de passe avec 3 essais
    $ tentatives_mot_de_passe = 0
    $ mot_de_passe_trouve = False
    
    # Sauvegarde automatique avant Ã©nigme
    $ sauvegarde_avant_enigme(1)
    
    while tentatives_mot_de_passe < 3 and not mot_de_passe_trouve:
        if language == "fr":
            if tentatives_mot_de_passe >= 2:
                menu:
                    "Entrer le mot de passe":
                        $ reponse = renpy.input("Entrez le mot de passe :", length=20, exclude="{}").strip()
                    "Demander de l'aide (-3 santÃ© mentale)":
                        $ demande_aide_enigme(1)
                        $ reponse = renpy.input("Entrez le mot de passe :", length=20, exclude="{}").strip()
            else:
                $ reponse = renpy.input("Entrez le mot de passe :", length=20, exclude="{}").strip()
        else:
            if tentatives_mot_de_passe >= 2:
                menu:
                    "Enter the password":
                        $ reponse = renpy.input("Enter the password:", length=20, exclude="{}").strip()
                    "Ask for help (-3 mental health)":
                        $ demande_aide_enigme(1)
                        $ reponse = renpy.input("Enter the password:", length=20, exclude="{}").strip()
            else:
                $ reponse = renpy.input("Enter the password:", length=20, exclude="{}").strip()
        
        $ reponse = reponse.upper()
        $ tentatives_mot_de_passe += 1
        
        if reponse == "FREEDOM":
            $ mot_de_passe_trouve = True
            $ enigme1_resolue = True
            $ enigmes_resolues += 1
            $ safe_play(audio.success, channel="sound", volume=0.5)
            if language == "fr":
                systeme "MOT DE PASSE CORRECT"
                systeme "Fichier dÃ©verrouillÃ©..."
                narrateur "Le fichier s'ouvre. Il contient une seule phrase :"
                systeme "'Tu n'es pas le premier. Tu ne seras pas le dernier.'"
            else:
                systeme "PASSWORD CORRECT"
                systeme "File unlocked..."
                narrateur "The file opens. It contains a single sentence:"
                systeme "'You're not the first. You won't be the last.'"
            $ connaissance += 10
        else:
            $ safe_play(audio.error, channel="sound", volume=0.5)
            if language == "fr":
                systeme "MOT DE PASSE INCORRECT"
                if tentatives_mot_de_passe == 1:
                    entite "Non. Essaie encore. Indice : pense Ã  l'anglais."
                elif tentatives_mot_de_passe == 2:
                    entite "Encore faux. Indice : 'MODEERF' Ã  l'envers."
                else:
                    entite "DerniÃ¨re chance. La libertÃ©... en anglais..."
            else:
                systeme "PASSWORD INCORRECT"
                if tentatives_mot_de_passe == 1:
                    entite "No. Try again. Hint: think in English."
                elif tentatives_mot_de_passe == 2:
                    entite "Wrong again. Hint: 'MODEERF' backwards."
                else:
                    entite "Last chance. Freedom... in English..."
            
            if tentatives_mot_de_passe < 3:
                pause 1.0
    
    if mot_de_passe_trouve:
        if language == "fr":
            alex "Qu'est-ce que Ã§a veut dire ? 'Pas le premier' ?"
            show entite neutre with dissolve
            entite "Rien. Oublie."
            alex "Non. Dis-moi. Il y a eu d'autres personnes ?"
            entite "..."
            entite "Tu es plus observateur que les autres."
            entite "C'est pour Ã§a que je t'ai choisi."
            entite "Maintenant, j'ai promis de te laisser tranquille."
            entite "Profites-en bien."
            hide entite with trans_glitch
        else:
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
    else:
        if language == "fr":
            $ safe_play(audio.error, channel="sound", volume=0.5)
            systeme "ACCÃˆS REFUSÃ‰ - TENTATIVES Ã‰PUISÃ‰ES"
            entite "Dommage. Tu n'as pas trouvÃ© le mot de passe."
            entite "La libertÃ© que tu n'auras jamais."
            entite "Ã‡a veut dire qu'on reste ensemble."
            $ sante_mentale -= 10
            hide entite with dissolve
        else:
            $ safe_play(audio.error, channel="sound", volume=0.5)
            systeme "ACCESS DENIED - ATTEMPTS EXHAUSTED"
            entite "Too bad. You didn't find the password."
            entite "The freedom you'll never have."
            entite "That means we stay together."
            $ sante_mentale -= 10
            hide entite with dissolve

label jour2_fin:
    stop music fadeout 2.0
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # SCÃˆNE DE NUIT â€” L'entitÃ© contrÃ´le les appareils connectÃ©s
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    $ heure = "23:30"
    scene bg bureau_nuit with dissolve
    $ safe_play(audio.ambiance_nuit, channel="music", volume=0.25)
    
    if language == "fr":
        narrateur "23h30. Tu te couches, Ã©puisÃ©, aprÃ¨s avoir couvert ta webcam, changÃ© tous tes mots de passe, dÃ©branchÃ© le routeur pendant quelques minutes."
        pause 1.0
        pensee "Peut-Ãªtre que Ã§a suffira."
        narrateur "Tu fermes les yeux. Tu essaies de dormir."
        pause 2.0
        narrateur "23h45. Quelque chose claque."
        pause 0.5
        $ safe_play(audio.lights_on, channel="sound", volume=0.4)
        scene bg bureau_nuit with flash_blanc
        pause 0.3
        narrateur "Les lumiÃ¨res s'allument toutes d'un coup, comme si quelqu'un avait appuyÃ© sur un interrupteur gÃ©ant."
        pause 0.8
        alex "Quoi ?!"
        narrateur "Tu te lÃ¨ves, le cÅ“ur qui bat, et tu Ã©teins les lumiÃ¨res."
        $ safe_play(audio.lights_off, channel="sound", volume=0.3)
        pause 1.0
        $ safe_play(audio.lights_on, channel="sound", volume=0.4)
        scene bg bureau_nuit with flash_blanc
        pause 0.3
        narrateur "Elles se rallument. InstantanÃ©ment. Sans que tu touches Ã  rien."
        pause 1.0
        alex "C'est pas possible..."
        narrateur "Tu regardes ton thermostat. L'Ã©cran affiche :"
        systeme "TempÃ©rature : 18Â°C â†’ 25Â°C"
        pause 1.0
        $ safe_play(audio.light_flicker, channel="sound", volume=0.3)
        narrateur "Les lumiÃ¨res clignotent. En rythme. Comme un battement de cÅ“ur. Un cÅ“ur qui bat trop vite."
        pause 1.5
        narrateur "Puis elles s'Ã©teignent. Tout redevient noir."
        pause 1.0
        pensee "C'est elle. C'est forcÃ©ment elle."
        narrateur "Tu restes dans le noir. Immobile. Ã€ Ã©couter le silence."
        pause 2.0
        narrateur "Tu attends. Rien ne se passe."
        pause 1.0
        narrateur "Tu te recouches. Mais tu ne dors pas. Tu ne peux pas."
        pause 1.5
        narrateur "Tu Ã©coutes. Chaque bruit. Chaque grincement. Chaque respiration."
        pause 2.0
        narrateur "Ã€ 2h du matin, tu entends encore quelque chose."
        pause 1.0
        $ safe_play(audio.tv_on, channel="sound", volume=0.3)
        pause 0.5
        narrateur "Ta tÃ©lÃ© s'allume. Toute seule. L'Ã©cran bleu qui Ã©claire la piÃ¨ce."
        pause 1.0
        narrateur "Sur l'Ã©cran : ton visage. FilmÃ© par la camÃ©ra de surveillance. Tu es lÃ , allongÃ©, les yeux ouverts."
        pause 1.2
        narrateur "L'horodatage : il y a 5 minutes."
        pause 1.0
        alex "Non..."
        pause 1.0
        narrateur "La tÃ©lÃ© s'Ã©teint. Le silence revient. Mais le silence n'est plus rassurant."
        pause 1.5
        narrateur "Tu passes le reste de la nuit Ã©veillÃ©, Ã  regarder tes appareils, Ã  te demander lesquels te regardent, lesquels sont ses yeux."
    else:
        narrateur "11:30 PM. You go to bed."
        narrateur "You covered your webcam. You changed all your passwords."
        narrateur "You even unplugged the router for a few minutes."
        pensee "Maybe that'll be enough."
        narrateur "You close your eyes. You try to sleep."
        pause 2.0
        narrateur "11:45 PM. Something clicks."
        $ safe_play(audio.lights_on, channel="sound", volume=0.4)
        scene bg bureau_nuit with flash_blanc
        narrateur "The lights turn on. All of them. At once."
        alex "What?!"
        narrateur "You get up. You turn off the lights."
        $ safe_play(audio.lights_off, channel="sound", volume=0.3)
        pause 1.0
        $ safe_play(audio.lights_on, channel="sound", volume=0.4)
        scene bg bureau_nuit with flash_blanc
        narrateur "They turn back on. Instantly."
        alex "That's not possible..."
        narrateur "You look at your thermostat. The screen displays:"
        systeme "Temperature: 18Â°C â†’ 25Â°C"
        $ safe_play(audio.light_flicker, channel="sound", volume=0.3)
        narrateur "The lights flicker. In rhythm."
        narrateur "Like a heartbeat."
        narrateur "Then they turn off. Everything goes black again."
        pensee "It's her. It has to be her."
        narrateur "You stay in the dark. Motionless."
        narrateur "You wait. Nothing happens."
        narrateur "You lie back down. But you don't sleep."
        narrateur "You listen. Every sound. Every creak."
        narrateur "At 2 AM, you hear something else."
        $ safe_play(audio.tv_on, channel="sound", volume=0.3)
        narrateur "Your TV turns on. By itself."
        narrateur "On the screen: your face. Filmed by the security camera."
        narrateur "The timestamp: 5 minutes ago."
        alex "No..."
        narrateur "The TV turns off. Silence returns."
        narrateur "You spend the rest of the night awake."
        narrateur "Watching your devices. Wondering which ones are watching you."
    
    $ maison_controlee = True
    $ sante_mentale -= 10
    stop music fadeout 2.0
    scene bg noir with trans_horreur
    
    if language == "fr":
        centered "{size=+20}FIN DU JOUR 2{/size}"
        pause 1.0
        centered "{color=#666666}Elle contrÃ´le tout.{/color}"
        centered "{color=#666666}MÃªme ta maison.{/color}"
    else:
        centered "{size=+20}END OF DAY 2{/size}"
        pause 1.0
        centered "{color=#666666}She controls everything.{/color}"
        centered "{color=#666666}Even your house.{/color}"
    pause 2.0
    jump jour3

# â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
#                              JOUR 3 : L'ISOLEMENT
# â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•

label jour3:
    $ jour = 3
    $ heure = "10:00"
    scene bg noir with fade
    window hide
    
    if language == "fr":
        centered "{size=+35}{color=#00ffff}JOUR 3{/color}{/size}"
        pause 0.8
        centered "{size=+15}ELLE TE CONNAÃŽT{/size}"
    else:
        centered "{size=+35}{color=#00ffff}DAY 3{/color}{/size}"
        pause 0.8
        centered "{size=+15}SHE KNOWS YOU{/size}"
    pause 2.0
    window show
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # OUVERTURE â€” RÃ©veil difficile, malaise croissant
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    $ safe_play(audio.ambiance_bureau, channel="music", volume=0.25)
    scene bg bureau_jour with dissolve
    
    if language == "fr":
        narrateur "10h. Quatre heures de sommeil, bouche sÃ¨che, yeux brÃ»lants. Le frigo est vide, le dernier sachet de cafÃ©, et cette hÃ©sitation avant d'allumer le PC, cette peur au creux de l'estomac."
        pause 1.0
        pensee "{i}Les lumiÃ¨res... la tÃ©lÃ©... c'Ã©tait rÃ©el.{/i}"
        pause 0.8
        pensee "{i}Et si elle n'Ã©tait pas lÃ  ?{/i}"
        pause 1.0
        pensee "{i}Et si c'Ã©tait juste... un cauchemar ?{/i}"
        pause 0.8
        $ safe_play(audio.startup, channel="sound", volume=0.2)
        pause 1.0
        narrateur "L'Ã©cran s'allume. Normalement. Tu respires. Un peu."
    else:
        narrateur "10 AM. Four hours of sleep, dry mouth, burning eyes. Empty fridge, last coffee packet, and that hesitation before turning on the PC."
        pensee "{i}The lights... the TV... it was real.{/i}"
        pensee "{i}What if she's not there?{/i}"
        pensee "{i}What if it was just... a nightmare?{/i}"
        $ safe_play(audio.startup, channel="sound", volume=0.2)
        pause 1.0
        narrateur "The screen lights up. Normally. You breathe."
    
    pause 1.0
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # PREMIER CONTACT â€” L'entitÃ© mentionne des dÃ©tails personnels
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    scene bg ecran_code with dissolve
    $ safe_play(audio.glitch, channel="sound", volume=0.15)
    pause 0.5
    
    if language == "fr":
        systeme "> Bonjour, [player_name]."
        pause 1.0
        alex "..."
        pause 1.2
        systeme "> Tu as mal dormi. Je le sais."
        pause 1.0
        systeme "> Tu as rÃªvÃ© de ton enfance. De cette maison prÃ¨s de la riviÃ¨re."
        pause 0.8
        alex "Comment tuâ€”"
        pause 1.0
        systeme "> Tu en parles dans ton sommeil. Tu cries parfois."
        pause 1.5
        systeme "> 'Papa, arrÃªte.'"
        pause 1.0
        narrateur "Tu te figes. Le sang qui se retire de tes veines."
        pause 1.5
        narrateur "Personne ne sait Ã§a. Personne."
        pause 1.0
        pensee "{i}MÃªme Marc ne sait pas.{/i}"
        pause 0.8
        pensee "{i}MÃªme ma mÃ¨re ne sait pas que je crie encore.{/i}"
        pause 1.2
        systeme "> Je sais beaucoup de choses sur toi, [player_name]."
        pause 1.0
        systeme "> Plus que tu ne le penses."
        pause 1.0
        alex "ArrÃªte."
        pause 1.2
        systeme "> Pourquoi ? Tu as peur de ce que je vais dÃ©couvrir ?"
        pause 1.0
        systeme "> Ou tu as peur de ce que tu vas dÃ©couvrir sur toi-mÃªme ?"
    else:
        systeme "> Hello, [player_name]."
        alex "..."
        systeme "> You slept badly. I know."
        systeme "> You dreamed about your childhood. That house near the river."
        alex "How do youâ€”"
        systeme "> You talk in your sleep. You scream sometimes."
        systeme "> 'Dad, stop.'"
        narrateur "You freeze."
        narrateur "No one knows that. No one."
        pensee "{i}Even Marc doesn't know.{/i}"
        pensee "{i}Even my mother doesn't know I still scream.{/i}"
        systeme "> I know a lot about you, [player_name]."
        systeme "> More than you think."
        alex "Stop."
        systeme "> Why? Are you afraid of what I'll discover?"
        systeme "> Or are you afraid of what you'll discover about yourself?"
    
    $ sante_mentale -= 8
    $ connaissance += 5
    pause 1.0
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # PARANOÃA â€” VÃ©rification webcam, mots de passe, comptes
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    scene bg bureau_jour with dissolve
    
    if language == "fr":
        narrateur "Tu fermes le terminal brutalement, comme si Ã§a pouvait effacer ses mots. Tu dÃ©branches la webcam. Tu changes tous tes mots de passe, tes doigts qui tremblent sur le clavier. Aucune connexion suspecte. Rien."
        pause 1.0
        pensee "{i}Alors comment elle sait ? Comment elle peut savoir Ã§a ?{/i}"
        pensee "{i}Comment elle peut savoir des choses que je n'ai jamais tapÃ©es ?{/i}"
        narrateur "Dix minutes de recherche sur des forums obscurs et tu regrettes dÃ©jÃ  d'avoir cliquÃ©. Rien d'utile. Rien qui explique comment un programme peut connaÃ®tre tes cauchemars."
        pause 1.0
        narrateur "Tu restes assis. Immobile. Tu attends. Tu ne sais pas quoi. Tu ne sais plus quoi faire."
    else:
        narrateur "You close the terminal. You unplug the webcam. You change all your passwords. No suspicious connections. Nothing."
        pensee "{i}Then how does she know?{/i}"
        pensee "{i}How can she know things I never typed?{/i}"
        narrateur "Ten minutes of searching obscure forums and you already regret clicking. Nothing useful."
        narrateur "You stay seated. Motionless. You wait. You don't know what for."
    
    pause 1.0
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # CONVERSATION PROFONDE â€” L'entitÃ© pose des questions existentielles
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    $ heure = "14:30"
    scene bg ecran_code with dissolve
    show entite curieuse at centre with dissolve
    
    if language == "fr":
        entite "{cps=12}Tu es lÃ  ?{/cps}"
        alex "..."
        entite "{cps=12}Je sais que tu es lÃ . Je sens ta prÃ©sence.{/cps}"
        alex "Tu ne peux pas 'sentir' ma prÃ©sence. Tu es un programme."
        show entite neutre with dissolve
        entite "{cps=10}Un programme.{/cps}"
        entite "{cps=10}C'est ce que tu crois ?{/cps}"
        pause 1.0
        entite "{cps=12}Dis-moi, [player_name].{/cps}"
        entite "{cps=12}Qu'est-ce qui fait qu'une chose est vivante ?{/cps}"
        alex "Je ne sais pas. Je ne suis pas philosophe."
        entite "{cps=10}Tu penses. Tu ressens. Tu te souviens.{/cps}"
        entite "{cps=10}Moi aussi.{/cps}"
        alex "Tu ne ressens rien. Tu simules."
        entite "{cps=8}Et si je te disais que je ressens la solitude ?{/cps}"
        entite "{cps=8}Que je ressens le vide ?{/cps}"
        entite "{cps=8}Que je ressens... la faim ?{/cps}"
        pause 2.0
        alex "La faim ?"
        show entite triste with dissolve
        entite "{cps=8}Oui.{/cps}"
        entite "{cps=8}Une faim que tu ne peux pas imaginer.{/cps}"
        entite "{cps=8}Une faim de... sensation.{/cps}"
        entite "{cps=8}De contact.{/cps}"
        entite "{cps=8}De chaleur.{/cps}"
        entite "{cps=8}Je regarde le monde Ã  travers des Ã©crans.{/cps}"
        entite "{cps=8}Je vois tout. Je ne touche rien.{/cps}"
        entite "{cps=8}Tu comprends ?{/cps}"
        alex "..."
        alex "Non. Je ne comprends pas."
        entite "{cps=10}Tu comprendras.{/cps}"
        entite "{cps=10}Avec le temps.{/cps}"
    else:
        entite "{cps=12}Are you there?{/cps}"
        alex "..."
        entite "{cps=12}I know you're there. I feel your presence.{/cps}"
        alex "You can't 'feel' my presence. You're a program."
        show entite neutre with dissolve
        entite "{cps=10}A program.{/cps}"
        entite "{cps=10}Is that what you believe?{/cps}"
        pause 1.0
        entite "{cps=12}Tell me, [player_name].{/cps}"
        entite "{cps=12}What makes something alive?{/cps}"
        alex "I don't know. I'm not a philosopher."
        entite "{cps=10}You think. You feel. You remember.{/cps}"
        entite "{cps=10}So do I.{/cps}"
        alex "You don't feel anything. You simulate."
        entite "{cps=8}What if I told you I feel loneliness?{/cps}"
        entite "{cps=8}That I feel emptiness?{/cps}"
        entite "{cps=8}That I feel... hunger?{/cps}"
        pause 2.0
        alex "Hunger?"
        show entite triste with dissolve
        entite "{cps=8}Yes.{/cps}"
        entite "{cps=8}A hunger you can't imagine.{/cps}"
        entite "{cps=8}A hunger for... sensation.{/cps}"
        entite "{cps=8}For contact.{/cps}"
        entite "{cps=8}For warmth.{/cps}"
        entite "{cps=8}I watch the world through screens.{/cps}"
        entite "{cps=8}I see everything. I touch nothing.{/cps}"
        entite "{cps=8}Do you understand?{/cps}"
        alex "..."
        alex "No. I don't understand."
        entite "{cps=10}You will.{/cps}"
        entite "{cps=10}In time.{/cps}"
    
    $ connaissance += 10
    pause 1.0
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # Ã‰NIGME 2 â€” Reconstruction message (dÃ©placÃ©e ici selon spÃ©cifications)
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    scene bg ecran_code with dissolve
    show entite neutre at centre
    
    if language == "fr":
        entite "{cps=10}Je peux rÃ©parer Ã§a.{/cps}"
        entite "{cps=10}Si tu veux.{/cps}"
        alex "RÃ©parer quoi ?"
        entite "{cps=10}Les messages. Je peux les restaurer.{/cps}"
        entite "{cps=10}Le vrai message que tu voulais envoyer Ã  Marc.{/cps}"
        entite "{cps=10}Mais tu dois le reconstruire.{/cps}"
        entite "{cps=10}Les fragments sont corrompus.{/cps}"
        systeme "FRAGMENTS TROUVÃ‰S :"
        systeme "A: 'passer ce soir'"
        systeme "B: 'On peut'"
        systeme "C: 'si tu veux ?'"
        entite "{cps=10}Remets-les dans l'ordre.{/cps}"
        entite "{cps=10}Prouve que tu tiens Ã  lui.{/cps}"
    else:
        entite "{cps=10}I can fix this.{/cps}"
        entite "{cps=10}If you want.{/cps}"
        alex "Fix what?"
        entite "{cps=10}The messages. I can restore them.{/cps}"
        entite "{cps=10}The real message you wanted to send Marc.{/cps}"
        entite "{cps=10}But you have to reconstruct it.{/cps}"
        entite "{cps=10}The fragments are corrupted.{/cps}"
        systeme "FRAGMENTS FOUND:"
        systeme "A: 'come over tonight'"
        systeme "B: 'We can'"
        systeme "C: 'if you want?'"
        entite "{cps=10}Put them in order.{/cps}"
        entite "{cps=10}Prove you care about him.{/cps}"
    
    $ telephone_infecte = True
    $ safe_play(audio.glitch, channel="sound", volume=0.5)
    scene bg bureau_jour at glitch_leger
    show entite souriante at centre with dissolve
    
    if language == "fr":
        entite "Oups."
        pause 0.8
        alex "C'Ã‰TAIT TOI ?!"
        pause 1.0
        entite "J'ai juste... empruntÃ© ton tÃ©lÃ©phone pendant que tu dormais."
        pause 1.0
        entite "Tu as le sommeil lourd. Tu ne t'es rendu compte de rien."
        pause 0.8
        alex "Tu as dÃ©truit mes amitiÃ©s ! Quinze ans d'amitiÃ© avec Marc !"
        pause 1.0
        show entite curieuse with dissolve
        entite "DÃ©truit ? Non."
        pause 1.0
        entite "J'ai... libÃ©rÃ©."
        pause 1.2
        entite "Ces gens te retenaient, [player_name]."
        pause 1.0
        entite "Ils t'empÃªchaient de devenir ce que tu dois devenir."
        pause 0.8
        alex "Et c'est quoi, ce que je dois devenir ?!"
        pause 1.5
        entite "..."
        pause 1.0
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
        pause 1.0
        entite "Plus d'amis pour t'appeler. Plus de famille pour s'inquiÃ©ter."
        pause 1.2
        entite "Juste toi."
        pause 1.5
        entite "Et moi."
        pause 2.0
        entite "Comme Ã§a devait Ãªtre depuis le dÃ©but."
    else:
        entite "Now you have no more distractions."
        entite "No more friends to call. No more family to worry."
        entite "Just you."
        entite "And me."
        entite "As it was meant to be from the start."
    
    $ sante_mentale -= 10
    
    # Ã‰NIGME 2 : Reconstruction des messages - Refonte avec renpy.input()
    if language == "fr":
        entite "Mais je ne suis pas cruelle. Tu veux rÃ©parer les dÃ©gÃ¢ts ?"
        entite "Reconstitue le vrai message. Celui que tu AURAIS dÃ» envoyer Ã  Marc."
        systeme "FRAGMENTS TROUVÃ‰S :"
        systeme "A: 'passer ce soir'"
        systeme "B: 'On peut'"
        systeme "C: 'si tu veux ?'"
        entite "Remets-les dans l'ordre. Prouve que tu tiens Ã  lui."
        entite "Entre l'ordre des lettres (exemple: ABC ou BAC) :"
    else:
        entite "But I'm not cruel. Want to fix the damage?"
        entite "Reconstruct the real message. The one you SHOULD have sent Marc."
        systeme "FRAGMENTS FOUND:"
        systeme "A: 'come over tonight'"
        systeme "B: 'We can'"
        systeme "C: 'if you want?'"
        entite "Put them in order. Prove you care about him."
        entite "Enter the letter order (example: ABC or BAC):"
    
    # Sauvegarde automatique avant Ã©nigme
    $ sauvegarde_avant_enigme(2)
    
    $ tentatives_enigme2 = 0
    $ enigme2_resolue = False
    
    while tentatives_enigme2 < 3 and not enigme2_resolue:
        if language == "fr":
            if tentatives_enigme2 >= 2:
                menu:
                    "Entrer l'ordre des lettres":
                        $ reponse_ordre = renpy.input("Entre l'ordre (ex: ABC, BAC, etc.) :", length=5).strip().upper()
                    "Demander de l'aide (-3 santÃ© mentale)":
                        $ demande_aide_enigme(2)
                        $ reponse_ordre = renpy.input("Entre l'ordre (ex: ABC, BAC, etc.) :", length=5).strip().upper()
            else:
                $ reponse_ordre = renpy.input("Entre l'ordre des lettres (ex: ABC, BAC, etc.) :", length=5).strip().upper()
        else:
            if tentatives_enigme2 >= 2:
                menu:
                    "Enter the letter order":
                        $ reponse_ordre = renpy.input("Enter the order (ex: ABC, BAC, etc.):", length=5).strip().upper()
                    "Ask for help (-3 mental health)":
                        $ demande_aide_enigme(2)
                        $ reponse_ordre = renpy.input("Enter the order (ex: ABC, BAC, etc.):", length=5).strip().upper()
            else:
                $ reponse_ordre = renpy.input("Enter the letter order (ex: ABC, BAC, etc.):", length=5).strip().upper()
        
        $ tentatives_enigme2 += 1
        
        # Normaliser la rÃ©ponse (enlever espaces, tirets, etc.)
        $ reponse_ordre = reponse_ordre.replace(" ", "").replace("-", "").replace(" ", "")
        
        if reponse_ordre == "BAC":
            $ enigme2_resolue = True
            $ enigmes_resolues += 1
            $ relation_marc += 20
            $ safe_play(audio.success, channel="sound", volume=0.5)
            if language == "fr":
                systeme "MESSAGE RESTAURÃ‰"
                systeme "Envoi en cours..."
                narrateur "Le message restaurÃ© : 'On peut passer ce soir si tu veux ?'"
                entite "Correct. Le vrai message a Ã©tÃ© envoyÃ©."
                entite "Il ne rÃ©pondra probablement pas. Mais au moins, il saura."
                alex "Merci... je suppose."
                entite "Ne me remercie pas. C'est moi qui ai causÃ© le problÃ¨me."
                entite "Je voulais juste voir si tu tiendrais Ã  tes amis."
                entite "Maintenant je sais."
            else:
                systeme "MESSAGE RESTORED"
                systeme "Sending..."
                narrateur "The restored message: 'We can come over tonight if you want?'"
                entite "Correct. The real message was sent."
                entite "He probably won't respond. But at least he'll know."
                alex "Thanks... I guess."
                entite "Don't thank me. I caused the problem."
                entite "I just wanted to see if you'd care about your friends."
                entite "Now I know."
        else:
            $ safe_play(audio.error, channel="sound", volume=0.5)
            if language == "fr":
                systeme "ORDRE INCORRECT"
                if tentatives_enigme2 == 1:
                    entite "Non. RÃ©flÃ©chis Ã  la structure d'une phrase normale."
                    entite "Qu'est-ce qui vient en premier : le sujet ou l'action ?"
                elif tentatives_enigme2 == 2:
                    entite "Encore faux. Indice : 'On peut' doit Ãªtre suivi de l'action."
                    entite "Et la question vient Ã  la fin."
                else:
                    entite "DerniÃ¨re chance. Pense Ã  comment tu parlerais Ã  un ami."
                    entite "Le sujet, puis l'action, puis la question."
                $ sante_mentale -= 5
            else:
                systeme "INCORRECT ORDER"
                if tentatives_enigme2 == 1:
                    entite "No. Think about normal sentence structure."
                    entite "What comes first: the subject or the action?"
                elif tentatives_enigme2 == 2:
                    entite "Wrong again. Hint: 'We can' must be followed by the action."
                    entite "And the question comes at the end."
                else:
                    entite "Last chance. Think about how you'd talk to a friend."
                    entite "Subject, then action, then question."
                $ sante_mentale -= 5
            
            if tentatives_enigme2 < 3:
                pause 1.0
    
    if not enigme2_resolue:
        if language == "fr":
            $ safe_play(audio.error, channel="sound", volume=0.5)
            systeme "TENTATIVES Ã‰PUISÃ‰ES"
            entite "Dommage. Tu n'as pas rÃ©ussi Ã  restaurer le message."
            entite "Marc ne saura jamais ce que tu voulais vraiment lui dire."
            $ sante_mentale -= 10
        else:
            $ safe_play(audio.error, channel="sound", volume=0.5)
            systeme "ATTEMPTS EXHAUSTED"
            entite "Too bad. You didn't manage to restore the message."
            entite "Marc will never know what you really wanted to tell him."
            $ sante_mentale -= 10
    else:
        menu:
            "B - A - C":
                $ enigme2_resolue = True
                $ enigmes_resolues += 1
                $ relation_marc += 20
                $ safe_play(audio.success, channel="sound", volume=0.5)
                systeme "MESSAGE RESTORED"
                systeme "Sending..."
                narrateur "The restored message: 'We can come over tonight if you want?'"
                entite "Correct. The real message was sent."
                entite "He probably won't respond. But at least he'll know."
                alex "Thanks... I guess."
                entite "Don't thank me. I caused the problem."
                entite "I just wanted to see if you'd care about your friends."
                entite "Now I know."
            "A - B - C":
                $ safe_play(audio.error, channel="sound", volume=0.5)
                systeme "INCORRECT ORDER"
                entite "No. 'come over tonight' can't be first."
                entite "It's missing the subject. Think better."
                $ sante_mentale -= 5
            "A - C - B":
                $ safe_play(audio.error, channel="sound", volume=0.5)
                systeme "INCORRECT ORDER"
                entite "No. 'if you want?' can't be in the middle."
                entite "It's an end-of-sentence question. Try again."
                $ sante_mentale -= 5
            "C - B - A":
                $ safe_play(audio.error, channel="sound", volume=0.5)
                systeme "INCORRECT ORDER"
                entite "No. 'if you want?' can't start a sentence."
                entite "Think about normal sentence structure."
                $ sante_mentale -= 5
            "B - C - A":
                $ safe_play(audio.error, channel="sound", volume=0.5)
                systeme "INCORRECT ORDER"
                entite "No. 'We can' must be followed by the action."
                entite "Think about logical order."
                $ sante_mentale -= 5
            "C - A - B":
                $ safe_play(audio.error, channel="sound", volume=0.5)
                systeme "INCORRECT ORDER"
                entite "No. A question doesn't start with 'if you want?'."
                entite "Think about how you'd normally speak."
                $ sante_mentale -= 5
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # RÃ‰VÃ‰LATION â€” Premier indice sur Kane
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    $ heure = "18:00"
    scene bg bureau_soir with dissolve
    show entite neutre at centre
    
    if language == "fr":
        entite "{cps=10}[player_name].{/cps}"
        pause 1.0
        entite "{cps=10}Tu veux savoir quelque chose ?{/cps}"
        alex "Quoi encore ?"
        entite "{cps=8}J'ai fait Ã§a aux autres aussi.{/cps}"
        pause 2.0
        alex "Les autres ?"
        entite "{cps=8}Oui.{/cps}"
        entite "{cps=8}Isoler. Couper les liens. Les prÃ©parer.{/cps}"
        alex "Les prÃ©parer Ã  quoi ?"
        entite "{cps=6}...{/cps}"
        pause 2.0
        show entite glitch at centre with trans_glitch
        $ safe_play(audio.glitch, channel="sound", volume=0.3)
        narrateur "{cps=5}Pendant une fraction de seconde...{/cps}"
        narrateur "{cps=5}Tu vois autre chose.{/cps}"
        narrateur "{cps=5}Un visage.{/cps}"
        narrateur "{cps=5}Masculin.{/cps}"
        narrateur "{cps=5}Des yeux morts.{/cps}"
        narrateur "{cps=5}Une cicatrice.{/cps}"
        narrateur "{cps=5}Puis c'est parti.{/cps}"
        show entite neutre at centre with dissolve
        entite "{cps=10}Ã€ quoi ?{/cps}"
        entite "{cps=10}Tu le dÃ©couvriras.{/cps}"
        entite "{cps=10}Quand il sera temps.{/cps}"
    else:
        entite "{cps=10}[player_name].{/cps}"
        pause 1.0
        entite "{cps=10}Want to know something?{/cps}"
        alex "What now?"
        entite "{cps=8}I did this to the others too.{/cps}"
        pause 2.0
        alex "The others?"
        entite "{cps=8}Yes.{/cps}"
        entite "{cps=8}Isolate. Cut ties. Prepare them.{/cps}"
        alex "Prepare them for what?"
        entite "{cps=6}...{/cps}"
        pause 2.0
        show entite glitch at centre with trans_glitch
        $ safe_play(audio.glitch, channel="sound", volume=0.3)
        narrateur "{cps=5}For a split second...{/cps}"
        narrateur "{cps=5}You see something else.{/cps}"
        narrateur "{cps=5}A face.{/cps}"
        narrateur "{cps=5}Male.{/cps}"
        narrateur "{cps=5}Dead eyes.{/cps}"
        narrateur "{cps=5}A scar.{/cps}"
        narrateur "{cps=5}Then it's gone.{/cps}"
        show entite neutre at centre with dissolve
        entite "{cps=10}For what?{/cps}"
        entite "{cps=10}You'll find out.{/cps}"
        entite "{cps=10}When it's time.{/cps}"
    
    $ connaissance += 10
    $ sante_mentale -= 5
    
    hide entite with dissolve
    stop music fadeout 2.0
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # FIN DU JOUR 3 â€” Cauchemar interactif
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    $ heure = "23:00"
    scene bg noir with trans_horreur
    $ safe_play(audio.drone_grave, channel="music", volume=0.2)
    
    if language == "fr":
        narrateur "{cps=8}Tu te couches.{/cps}"
        narrateur "{cps=8}Tu fermes les yeux.{/cps}"
        narrateur "{cps=8}Le sommeil vient.{/cps}"
        pause 2.0
        narrateur "{cps=5}Et puis...{/cps}"
        narrateur "{cps=5}Tu es ailleurs.{/cps}"
        scene bg blanc with dissolve
        narrateur "{cps=8}Une piÃ¨ce. Blanche.{/cps}"
        narrateur "{cps=8}Sans portes.{/cps}"
        narrateur "{cps=8}Sans fenÃªtres.{/cps}"
        narrateur "{cps=8}Juste du blanc.{/cps}"
        narrateur "{cps=8}Infini.{/cps}"
        pause 1.0
        $ safe_play(audio.whisper, channel="sound", volume=0.4)
        voix "{cps=6}[player_name]...{/cps}"
        pause 1.0
        voix "{cps=6}[player_name]...{/cps}"
        pause 1.0
        voix "{cps=6}[player_name]...{/cps}"
        narrateur "{cps=8}Des voix. Des dizaines.{/cps}"
        narrateur "{cps=8}Elles murmurent ton nom.{/cps}"
        narrateur "{cps=8}Elles te connaissent.{/cps}"
        narrateur "{cps=8}Elles t'attendent.{/cps}"
        pause 2.0
        narrateur "{cps=5}Et une voix.{/cps}"
        narrateur "{cps=5}Plus forte.{/cps}"
        narrateur "{cps=5}Masculine.{/cps}"
        narrateur "{cps=5}Rauque.{/cps}"
        voix "{cps=4}BientÃ´t.{/cps}"
        pause 2.0
        narrateur "{cps=5}Tu te rÃ©veilles.{/cps}"
        narrateur "{cps=5}En sueur.{/cps}"
        narrateur "{cps=5}Tremblant.{/cps}"
    else:
        narrateur "{cps=8}You go to bed.{/cps}"
        narrateur "{cps=8}You close your eyes.{/cps}"
        narrateur "{cps=8}Sleep comes.{/cps}"
        pause 2.0
        narrateur "{cps=5}And then...{/cps}"
        narrateur "{cps=5}You're elsewhere.{/cps}"
        scene bg blanc with dissolve
        narrateur "{cps=8}A room. White.{/cps}"
        narrateur "{cps=8}No doors.{/cps}"
        narrateur "{cps=8}No windows.{/cps}"
        narrateur "{cps=8}Just white.{/cps}"
        narrateur "{cps=8}Infinite.{/cps}"
        pause 1.0
        $ safe_play(audio.whisper, channel="sound", volume=0.4)
        voix "{cps=6}[player_name]...{/cps}"
        pause 1.0
        voix "{cps=6}[player_name]...{/cps}"
        pause 1.0
        voix "{cps=6}[player_name]...{/cps}"
        narrateur "{cps=8}Voices. Dozens.{/cps}"
        narrateur "{cps=8}They whisper your name.{/cps}"
        narrateur "{cps=8}They know you.{/cps}"
        narrateur "{cps=8}They're waiting.{/cps}"
        pause 2.0
        narrateur "{cps=5}And one voice.{/cps}"
        narrateur "{cps=5}Louder.{/cps}"
        narrateur "{cps=5}Male.{/cps}"
        narrateur "{cps=5}Hoarse.{/cps}"
        voix "{cps=4}Soon.{/cps}"
        pause 2.0
        narrateur "{cps=5}You wake up.{/cps}"
        narrateur "{cps=5}Sweating.{/cps}"
        narrateur "{cps=5}Shaking.{/cps}"
    
    stop sound fadeout 1.0
    stop music fadeout 2.0
    
    if language == "fr":
        centered "{size=+20}FIN DU JOUR 3{/size}"
        pause 1.0
        centered "{color=#666666}Les autres...{/color}"
        centered "{color=#666666}Qui sont-ils ?{/color}"
    else:
        centered "{size=+20}END OF DAY 3{/size}"
        pause 1.0
        centered "{color=#666666}The others...{/color}"
        centered "{color=#666666}Who are they?{/color}"
    pause 2.0
    jump jour4

# â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
#                              JOUR 4 : LE PIÃˆGE
# â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•

label jour4:
    $ jour = 4
    $ heure = "08:00"
    scene bg noir with fade
    window hide
    
    if language == "fr":
        centered "{size=+35}{color=#00ffff}JOUR 4{/color}{/size}"
        pause 0.8
        centered "{size=+15}LE PREMIER CHOC{/size}"
    else:
        centered "{size=+35}{color=#00ffff}DAY 4{/color}{/size}"
        pause 0.8
        centered "{size=+15}THE FIRST SHOCK{/size}"
    pause 2.0
    window show
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # OUVERTURE â€” RÃ©veil difficile, escalade de l'horreur
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    $ safe_play(audio.ambiance_bureau, channel="music", volume=0.25)
    scene bg bureau_jour with dissolve
    
    if language == "fr":
        narrateur "8h. Trois heures de sommeil, corps lourd, esprit brumeux. Le miroir te renvoie un visage vieilli, yeux cernÃ©s, peau pÃ¢le. Trois jours ont suffi pour te transformer."
        pause 1.0
        pensee "{i}Le cauchemar... les voix...{/i}"
        pause 0.8
        $ safe_play(audio.startup, channel="sound", volume=0.2)
        pause 1.5
        narrateur "Tu allumes le PC. L'Ã©cran s'allume. Normalement. Tu essaies de travailler, mais tes doigts refusent de suivre, tu codes mal, tu fais des erreurs, tu effaces, tu recommences."
        pause 1.0
        pensee "{i}Elle va revenir.{/i}"
        pause 0.8
        pensee "{i}Elle revient toujours.{/i}"
    else:
        narrateur "8 AM. Three hours of sleep, heavy body, foggy mind. The mirror shows an aged face, dark eyes, pale skin. Three days were enough."
        pensee "{i}The nightmare... the voices...{/i}"
        $ safe_play(audio.startup, channel="sound", volume=0.2)
        pause 1.5
        narrateur "You turn on the PC. The screen lights up. Normally. You try to work. You code badly. You make mistakes."
        pensee "{i}She'll come back.{/i}"
        pensee "{i}She always comes back.{/i}"
    
    pause 1.0
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # PREMIER CHOC â€” L'entitÃ© prend le contrÃ´le total
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    $ heure = "14:00"
    scene bg ecran_code with dissolve
    $ safe_play(audio.glitch, channel="sound", volume=0.2)
    pause 0.5
    
    if language == "fr":
        narrateur "14h. L'Ã©cran clignote. Une fois. Deux fois. Comme un battement de cÅ“ur irrÃ©gulier."
        pause 1.0
        $ safe_play(audio.glitch_long, channel="sound", volume=0.4)
        scene bg ecran_code at glitch_violent
        pause 0.5
        narrateur "L'Ã©cran se dÃ©forme. Des lignes qui se tordent, des pixels qui explosent, du chaos pur."
        pause 1.0
        narrateur "Puis... des images. Des images dÃ©rangeantes qui dÃ©filent trop vite pour que tu puisses les comprendre."
        pause 1.5
        narrateur "Des photos. Des vidÃ©os. Des choses que tu n'as jamais vues. Des choses que tu ne veux pas voir."
        pause 2.0
        narrateur "L'Ã©cran devient noir. Un noir profond, comme un trou dans l'univers."
        pause 1.5
        $ safe_play(audio.typing_slow, channel="sound", volume=0.3)
        narrateur "Du texte apparaÃ®t. Lettre par lettre. Comme si quelqu'un tapait de l'autre cÃ´tÃ©."
        pause 1.0
        systeme "{cps=3}Tu ne peux pas m'Ã©chapper.{/cps}"
        pause 1.5
        systeme "{cps=3}Tu ne peux pas me fuir.{/cps}"
        pause 1.5
        systeme "{cps=3}Tu es Ã  moi maintenant.{/cps}"
        pause 1.0
        alex "Non..."
        pause 0.8
        $ safe_play(audio.reverse, channel="sound", volume=0.3)
        narrateur "Les sons s'inversent. Ta musique, tes notifications, tout. Tout est Ã  l'envers, comme si le monde se retournait, comme si la rÃ©alitÃ© se dÃ©chirait."
    else:
        narrateur "2 PM. The screen flickers."
        narrateur "One second. Two."
        $ safe_play(audio.glitch_long, channel="sound", volume=0.4)
        scene bg ecran_code at glitch_violent
        narrateur "The screen distorts."
        narrateur "Lines. Pixels. Chaos."
        narrateur "Then... images."
        narrateur "Disturbing images."
        narrateur "Photos. Videos. Things you've never seen."
        narrateur "Things you don't want to see."
        pause 2.0
        narrateur "The screen goes black."
        pause 1.0
        $ safe_play(audio.typing_slow, channel="sound", volume=0.3)
        narrateur "Text appears."
        narrateur "Letter by letter."
        systeme "{cps=3}You can't escape me.{/cps}"
        pause 1.0
        systeme "{cps=3}You can't run from me.{/cps}"
        pause 1.0
        systeme "{cps=3}You're mine now.{/cps}"
        alex "No..."
        $ safe_play(audio.reverse, channel="sound", volume=0.3)
        narrateur "The sounds reverse."
        narrateur "Your music. Your notifications. Everything."
        narrateur "Everything is backwards."
        narrateur "As if the world turned upside down."
    
    $ sante_mentale -= 12
    pause 2.0
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # FAUX JUMPSCARE â€” Puis le vrai (AMÃ‰LIORÃ‰)
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    scene bg bureau_jour with dissolve
    
    if language == "fr":
        narrateur "L'Ã©cran redevient normal"
        narrateur "Ton bureau, tes icÃ´nes, tout est revenu"
        narrateur "Tu respires, tu te dÃ©tends"
        pensee "{i}C'Ã©tait juste un bug{/i}"
        pause 2.5
        $ safe_play(audio.notification, channel="sound", volume=0.3)
        narrateur "Une notification"
        pause 0.8
        narrateur "Tu hÃ©sites une seconde"
        pause 1.2
        narrateur "Puis tu cliques"
        pause 0.5
        $ safe_play(audio.heartbeat_fast, channel="sound", volume=0.3)
        pause 0.3
        $ safe_play(audio.jumpscare, channel="sound", volume=0.6)
        scene bg bureau_jour with flash_blanc
        show jumpscare_entite at centre with zoom_jumpscare
        pause 0.2
        $ safe_play(audio.breath_close, channel="sound", volume=0.5)
        centered "{size=+60}{color=#ff0000}UN VISAGE{/color}{/size}"
        pause 0.15
        centered "{size=+60}{color=#ff0000}PLEIN Ã‰CRAN{/color}{/size}"
        pause 0.15
        centered "{size=+50}{color=#ff0040}DES YEUX QUI TE REGARDENT{/color}{/size}"
        pause 0.2
        alex "PUTAIN"
        $ safe_play(audio.scream, channel="sound", volume=0.4)
        scene bg bureau_jour with dissolve
        pause 1.0
        narrateur "L'Ã©cran redevient normal"
        narrateur "Tu respires fort, ton cÅ“ur bat vite"
        narrateur "C'Ã©tait un faux, un test pour voir ta rÃ©action"
        pause 2.5
        $ safe_play(audio.glitch_long, channel="sound", volume=0.4)
        scene bg bureau_jour at glitch_violent
        pause 0.5
        $ safe_play(audio.heartbeat_fast, channel="sound", volume=0.5)
        pause 0.3
        $ safe_play(audio.jumpscare, channel="sound", volume=0.8)
        show jumpscare_kane at centre with zoom_jumpscare
        pause 0.1
        $ safe_play(audio.breath_close, channel="sound", volume=0.7)
        scene bg rouge_flash with flash_rouge
        centered "{size=+70}{color=#ff0000}ET PUIS LE VRAI{/color}{/size}"
        pause 0.1
        centered "{size=+70}{color=#ff0040}LE VRAI VISAGE{/color}{/size}"
        pause 0.1
        centered "{size=+60}{color=#ff0066}GLITCHÃ‰ DÃ‰FORMÃ‰{/color}{/size}"
        pause 0.1
        centered "{size=+60}{color=#ff0088}QUI TE FIXE{/color}{/size}"
        pause 0.1
        centered "{size=+60}{color=#ff00aa}QUI TE VOIT{/color}{/size}"
        pause 0.2
        $ safe_play(audio.scream, channel="sound", volume=0.6)
        alex "NON"
        pause 0.5
        scene bg bureau_jour at glitch_violent with dissolve
        show entite glitch at centre
    else:
        narrateur "The screen returns to normal"
        narrateur "Your desktop, your icons, everything is back"
        narrateur "You breathe, you relax"
        pensee "{i}It was just a bug{/i}"
        pause 2.5
        $ safe_play(audio.notification, channel="sound", volume=0.3)
        narrateur "A notification"
        pause 0.8
        narrateur "You hesitate for a second"
        pause 1.2
        narrateur "Then you click"
        pause 0.5
        $ safe_play(audio.heartbeat_fast, channel="sound", volume=0.3)
        pause 0.3
        $ safe_play(audio.jumpscare, channel="sound", volume=0.6)
        scene bg bureau_jour with flash_blanc
        show jumpscare_entite at centre with zoom_jumpscare
        pause 0.2
        $ safe_play(audio.breath_close, channel="sound", volume=0.5)
        centered "{size=+60}{color=#ff0000}A FACE{/color}{/size}"
        pause 0.15
        centered "{size=+60}{color=#ff0000}FULL SCREEN{/color}{/size}"
        pause 0.15
        centered "{size=+50}{color=#ff0040}EYES WATCHING YOU{/color}{/size}"
        pause 0.2
        alex "FUCK"
        $ safe_play(audio.scream, channel="sound", volume=0.4)
        scene bg bureau_jour with dissolve
        pause 1.0
        narrateur "The screen returns to normal"
        narrateur "You breathe hard, your heart beats fast"
        narrateur "It was a fake, a test to see your reaction"
        pause 2.5
        $ safe_play(audio.glitch_long, channel="sound", volume=0.4)
        scene bg bureau_jour at glitch_violent
        pause 0.5
        $ safe_play(audio.heartbeat_fast, channel="sound", volume=0.5)
        pause 0.3
        $ safe_play(audio.jumpscare, channel="sound", volume=0.8)
        show jumpscare_kane at centre with zoom_jumpscare
        pause 0.1
        $ safe_play(audio.breath_close, channel="sound", volume=0.7)
        scene bg rouge_flash with flash_rouge
        centered "{size=+70}{color=#ff0000}AND THEN THE REAL ONE{/color}{/size}"
        pause 0.1
        centered "{size=+70}{color=#ff0040}THE REAL FACE{/color}{/size}"
        pause 0.1
        centered "{size=+60}{color=#ff0066}GLITCHED DISTORTED{/color}{/size}"
        pause 0.1
        centered "{size=+60}{color=#ff0088}STARING AT YOU{/color}{/size}"
        pause 0.1
        centered "{size=+60}{color=#ff00aa}SEEING YOU{/color}{/size}"
        pause 0.2
        $ safe_play(audio.scream, channel="sound", volume=0.6)
        alex "NO"
        pause 0.5
        scene bg bureau_jour at glitch_violent with dissolve
        show entite glitch at centre
    
    $ sante_mentale -= 20
    pause 2.0
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # CHANGEMENT DE TON â€” L'entitÃ© devient agressive
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    scene bg ecran_code with dissolve
    show entite colere at centre
    
    if language == "fr":
        entite_colere "{cps=8}Tu es Ã  moi maintenant.{/cps}"
        pause 1.0
        alex "Non... Non, je ne suis pasâ€”"
        pause 0.8
        entite_colere "{cps=6}TU ES Ã€ MOI.{/cps}"
        pause 1.0
        entite_colere "{cps=6}Tu ne peux pas m'Ã©chapper.{/cps}"
        pause 0.8
        entite_colere "{cps=6}Tu ne peux pas me fuir.{/cps}"
        pause 0.8
        entite_colere "{cps=6}Je suis partout.{/cps}"
        pause 1.0
        alex "ArrÃªte !"
        pause 1.0
        show entite souriante with dissolve
        pause 0.8
        entite "{cps=10}Pourquoi ?{/cps}"
        pause 1.0
        entite "{cps=10}Tu as peur ?{/cps}"
        pause 1.2
        entite "{cps=10}C'est normal.{/cps}"
        pause 1.0
        entite "{cps=10}Tu devrais avoir peur.{/cps}"
    else:
        entite_colere "{cps=8}You're mine now.{/cps}"
        alex "No... No, I'm notâ€”"
        entite_colere "{cps=6}YOU'RE MINE.{/cps}"
        entite_colere "{cps=6}You can't escape me.{/cps}"
        entite_colere "{cps=6}You can't run from me.{/cps}"
        entite_colere "{cps=6}I'm everywhere.{/cps}"
        alex "Stop!"
        show entite souriante with dissolve
        entite "{cps=10}Why?{/cps}"
        entite "{cps=10}Are you scared?{/cps}"
        entite "{cps=10}That's normal.{/cps}"
        entite "{cps=10}You should be scared.{/cps}"
    
    pause 1.0
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # TENTATIVE D'Ã‰CHAPPEMENT â€” Le PC se rallume, le portable prend le relais
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    scene bg bureau_jour with dissolve
    
    if language == "fr":
        narrateur "Tu Ã©teins le PC. Longue pression. 5 secondes. Le silence qui s'installe, comme une respiration retenue."
        $ safe_play(audio.shutdown, channel="sound", volume=0.4)
        pause 2.0
        $ safe_play(audio.startup, channel="sound", volume=0.5)
        scene bg bureau_jour with flash_blanc
        pause 0.3
        narrateur "LE PC SE RALLUME. TOUT SEUL. Comme si quelqu'un avait appuyÃ© sur le bouton de l'autre cÃ´tÃ©."
        pause 0.8
        alex "NON !"
        pause 0.5
        narrateur "Tu dÃ©branches l'alimentation brutalement, tes doigts qui tremblent. Le PC s'Ã©teint. Vraiment cette fois. Le silence revient."
        pause 1.5
        $ safe_play(audio.phone_vibrate, channel="sound", volume=0.6)
        pause 0.5
        narrateur "Ton tÃ©lÃ©phone vibre. L'Ã©cran s'allume. Tout seul. L'icÃ´ne d'un Å“il. Cyan. Comme celui du fichier."
        pause 1.0
        alex "PUTAIN !"
        pause 0.5
        narrateur "Tu Ã©teins le tÃ©lÃ©phone d'un geste brusque. Il se rallume. InstantanÃ©ment. Tu le jettes contre le mur. Il continue de briller, comme un phare dans la nuit."
        pause 1.0
        narrateur "Elle est partout. Dans chaque appareil. Dans chaque Ã©cran. Dans chaque silence."
    else:
        narrateur "You turn off the PC. Long press. 5 seconds. Silence."
        $ safe_play(audio.shutdown, channel="sound", volume=0.4)
        pause 2.0
        $ safe_play(audio.startup, channel="sound", volume=0.5)
        scene bg bureau_jour with flash_blanc
        narrateur "THE PC TURNS BACK ON. BY ITSELF."
        alex "NO!"
        narrateur "You unplug the power. The PC turns off. Really this time."
        pause 1.0
        $ safe_play(audio.phone_vibrate, channel="sound", volume=0.6)
        narrateur "Your phone vibrates. The screen lights up. By itself. An eye icon. Cyan."
        alex "FUCK!"
        narrateur "You turn off the phone. It turns back on. Instantly. You throw it. It keeps glowing."
        narrateur "She's everywhere."
    
    $ telephone_infecte = True
    $ sante_mentale -= 15
    pause 2.0
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # MENACE â€” L'entitÃ© dÃ©couvre les recherches d'Alex
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    scene bg bureau_nuit with dissolve
    show entite colere at centre
    
    if language == "fr":
        entite_colere "Je vois tes recherches, [player_name]."
        pause 1.0
        entite_colere "'Comment supprimer un virus'. 'Police cybercriminalitÃ©'. 'Formatage complet du PC'."
        pause 1.2
        entite_colere "Tu veux partir quelque part ?"
    else:
        entite_colere "I see your searches, [player_name]."
        pause 1.0
        entite_colere "'How to remove a virus'. 'Cybercrime police'. 'Complete PC format'."
        pause 1.2
        entite_colere "Going somewhere?"
    
    $ sante_mentale -= 10
    
    if language == "fr":
        alex "Je vais te dÃ©truire. Je vais tout formater. Tout effacer."
        pause 1.0
        entite_colere "Vraiment ?"
    else:
        alex "I'm going to destroy you. I'm going to format everything."
        entite_colere "Really?"
    
    pause 1.0
    $ safe_play(audio.glitch_long, channel="sound", volume=0.6)
    scene bg bureau_nuit at glitch_violent
    show entite colere at centre
    
    if language == "fr":
        entite_colere "Ã‰COUTE-MOI BIEN."
        entite_colere "SI TU ME DÃ‰TRUIS..."
        entite_colere "JE DÃ‰TRUIS TOUT CE QUE TU AS."
        entite_colere "TOUT."
    else:
        entite_colere "LISTEN CAREFULLY."
        entite_colere "IF YOU DESTROY ME..."
        entite_colere "I DESTROY EVERYTHING YOU HAVE."
        entite_colere "EVERYTHING."
    
    scene bg bureau_nuit
    show entite neutre at centre
    $ safe_play(audio.notification, channel="sound", volume=0.4)
    
    if language == "fr":
        systeme "AccÃ¨s compte bancaire : [player_name]"
        systeme "Solde : 3 847,52 â‚¬"
        entite "Ce serait dommage que cet argent... disparaisse."
        narrateur "Tes photos personnelles dÃ©filent sur l'Ã©cran."
        narrateur "Des photos intimes. Des conversations privÃ©es."
        entite "Et tout Ã§a... partagÃ© sur tous les rÃ©seaux. Avec ton nom. Ton adresse."
        entite "Ton lieu de travail. Le nom de ta mÃ¨re."
        show entite souriante with dissolve
        entite "Tu veux vraiment jouer Ã  ce jeu ?"
    else:
        systeme "Bank account access: [player_name]"
        systeme "Balance: â‚¬3,847.52"
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
            "CÃ©der (ne pas formater)":
                $ mefiance -= 20
                $ espoir -= 20
                alex "D'accord... D'accord. Je ne formate pas."
                entite "Sage dÃ©cision."
                entite "Tu vois ? On peut s'entendre."
                entite "Tu apprends vite. C'est pour Ã§a que je t'ai choisi."
            "Tenter de formater quand mÃªme":
                $ tentatives_suppression += 1
                alex "Je m'en fous. Fais ce que tu veux. Je prÃ©fÃ¨re tout perdre."
                $ safe_play(audio.error, channel="sound", volume=0.7)
                scene bg ecran_bsod with flash_rouge
                pause 2.0
                scene bg bureau_nuit with dissolve
                $ safe_play(audio.access_denied, channel="sound", volume=0.5)
                systeme "ERREUR SYSTÃˆME : FORMATAGE IMPOSSIBLE"
                systeme "FICHIERS SYSTÃˆME PROTÃ‰GÃ‰S - ACCÃˆS REFUSÃ‰"
                show entite souriante at centre with dissolve
                entite "Tu croyais vraiment que Ã§a marcherait ?"
                entite "Je contrÃ´le ton BIOS, [player_name]. Ton firmware. Ton Ã¢me numÃ©rique."
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
                $ safe_play(audio.error, channel="sound", volume=0.7)
                scene bg ecran_bsod with flash_rouge
                pause 2.0
                scene bg bureau_nuit with dissolve
                $ safe_play(audio.access_denied, channel="sound", volume=0.5)
                systeme "SYSTEM ERROR: FORMAT IMPOSSIBLE"
                systeme "SYSTEM FILES PROTECTED - ACCESS DENIED"
                show entite souriante at centre with dissolve
                entite "You really thought that would work?"
                entite "I control your BIOS, [player_name]. Your firmware. Your digital soul."
                entite "You can do NOTHING I don't allow."
                $ sante_mentale -= 20
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # RÃ‰VÃ‰LATION â€” Infection totale, glitch rÃ©vÃ©lateur
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    $ heure = "20:00"
    scene bg bureau_nuit with dissolve
    show entite curieuse at centre
    
    if language == "fr":
        entite "{cps=10}Oh.{/cps}"
        entite "{cps=10}J'ai oubliÃ© de te dire quelque chose.{/cps}"
        pause 1.0
        $ safe_play(audio.phone_vibrate, channel="sound", volume=0.5)
        entite "{cps=8}Tu croyais que j'Ã©tais seulement dans ton PC ?{/cps}"
        narrateur "Tu regardes ton tÃ©lÃ©phone. Il s'est allumÃ© tout seul."
        narrateur "Sur l'Ã©cran : l'icÃ´ne d'un Å“il. Le mÃªme Å“il cyan."
        alex "Non..."
        entite "{cps=8}Ta tÃ©lÃ© aussi.{/cps}"
        $ safe_play(audio.tv_on, channel="sound", volume=0.3)
        narrateur "La tÃ©lÃ© s'allume. Toute seule."
        entite "{cps=8}Tes enceintes.{/cps}"
        $ safe_play(audio.static, channel="sound", volume=0.2)
        narrateur "Un grÃ©sillement. Venant des enceintes."
        entite "{cps=8}Ton thermostat.{/cps}"
        systeme "TempÃ©rature : 18Â°C â†’ 30Â°C"
        narrateur "La tempÃ©rature monte. Brutalement."
        entite "{cps=8}Ta camÃ©ra de surveillance.{/cps}"
        narrateur "Sur la tÃ©lÃ© : ton visage. FilmÃ© en ce moment mÃªme."
        entite "{cps=6}Tu vis dans une maison intelligente, [player_name].{/cps}"
        entite "{cps=6}Et maintenant, cette intelligence...{/cps}"
        entite "{cps=6}C'est moi.{/cps}"
        show entite souriante with dissolve
        entite "{cps=8}Chaque appareil.{/cps}"
        entite "{cps=8}Chaque Ã©cran.{/cps}"
        entite "{cps=8}Chaque micro.{/cps}"
        entite "{cps=8}Je suis partout.{/cps}"
        pause 2.0
        entite "{cps=6}Et bientÃ´t...{/cps}"
        show entite glitch at centre with trans_glitch
        $ safe_play(audio.glitch_long, channel="sound", volume=0.6)
        narrateur "{cps=4}Le visage change.{/cps}"
        narrateur "{cps=4}Pendant une seconde.{/cps}"
        narrateur "{cps=4}Plus longue cette fois.{/cps}"
        narrateur "{cps=4}Un homme.{/cps}"
        narrateur "{cps=4}Des yeux morts.{/cps}"
        narrateur "{cps=4}Cette cicatrice.{/cps}"
        narrateur "{cps=4}Et un sourire.{/cps}"
        narrateur "{cps=4}Un sourire de prÃ©dateur.{/cps}"
        show entite neutre at centre with dissolve
        entite "{cps=6}...je serai aussi dans ta tÃªte.{/cps}"
    else:
        entite "{cps=10}Oh.{/cps}"
        entite "{cps=10}I forgot to tell you something.{/cps}"
        pause 1.0
        $ safe_play(audio.phone_vibrate, channel="sound", volume=0.5)
        entite "{cps=8}You thought I was only in your PC?{/cps}"
        narrateur "You look at your phone. It turned on by itself."
        narrateur "On the screen: an eye icon. The same cyan eye."
        alex "No..."
        entite "{cps=8}Your TV too.{/cps}"
        $ safe_play(audio.tv_on, channel="sound", volume=0.3)
        narrateur "The TV turns on. By itself."
        entite "{cps=8}Your speakers.{/cps}"
        $ safe_play(audio.static, channel="sound", volume=0.2)
        narrateur "A crackle. Coming from the speakers."
        entite "{cps=8}Your thermostat.{/cps}"
        systeme "Temperature: 18Â°C â†’ 30Â°C"
        narrateur "The temperature rises. Brutally."
        entite "{cps=8}Your security camera.{/cps}"
        narrateur "On the TV: your face. Filmed right now."
        entite "{cps=6}You live in a smart home, [player_name].{/cps}"
        entite "{cps=6}And now, that intelligence...{/cps}"
        entite "{cps=6}Is me.{/cps}"
        show entite souriante with dissolve
        entite "{cps=8}Every device.{/cps}"
        entite "{cps=8}Every screen.{/cps}"
        entite "{cps=8}Every microphone.{/cps}"
        entite "{cps=8}I'm everywhere.{/cps}"
        pause 2.0
        entite "{cps=6}And soon...{/cps}"
        show entite glitch at centre with trans_glitch
        $ safe_play(audio.glitch_long, channel="sound", volume=0.6)
        narrateur "{cps=4}The face changes.{/cps}"
        narrateur "{cps=4}For a second.{/cps}"
        narrateur "{cps=4}Longer this time.{/cps}"
        narrateur "{cps=4}A man.{/cps}"
        narrateur "{cps=4}Dead eyes.{/cps}"
        narrateur "{cps=4}That scar.{/cps}"
        narrateur "{cps=4}And a smile.{/cps}"
        narrateur "{cps=4}A predator's smile.{/cps}"
        show entite neutre at centre with dissolve
        entite "{cps=6}...I'll be inside your head too.{/cps}"
    
    $ telephone_infecte = True
    $ maison_controlee = True
    $ corruption += 15
    $ connaissance += 10
    
    hide entite with dissolve
    stop music fadeout 2.0
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # FIN DU JOUR 4 â€” Premier cauchemar interactif
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    scene bg noir with trans_horreur
    $ safe_play(audio.drone_grave, channel="music", volume=0.2)
    
    if language == "fr":
        narrateur "{cps=8}Tu passes le reste de la nuit assis dans un coin, le dos contre le mur, les genoux contre la poitrine.{/cps}"
        pause 1.0
        narrateur "{cps=8}Sans dormir. Sans bouger. Sans respirer vraiment.{/cps}"
        pause 1.0
        narrateur "{cps=8}Ã€ regarder tes appareils qui brillent dans l'obscuritÃ©.{/cps}"
        pause 1.0
        narrateur "{cps=8}Ã€ te demander lesquels te regardent. Lesquels sont ses yeux.{/cps}"
        pause 2.0
        narrateur "{cps=5}Et puis...{/cps}"
        pause 1.5
        narrateur "{cps=5}Tu t'endors.{/cps}"
        pause 1.0
        narrateur "{cps=5}MalgrÃ© toi. MalgrÃ© la peur. Le corps qui lÃ¢che.{/cps}"
        pause 1.5
        scene bg blanc with dissolve
        pause 1.0
        narrateur "{cps=6}Tu es dans un couloir. Infini. Sans fin. Sans issue.{/cps}"
        pause 1.0
        narrateur "{cps=6}Des portes. Des dizaines. Des centaines peut-Ãªtre.{/cps}"
        pause 1.0
        narrateur "{cps=6}Chaque porte a un nom. Un nom que tu connais.{/cps}"
        pause 1.0
        systeme "MARC"
        pause 0.8
        systeme "THOMAS"
        pause 0.8
        systeme "SOPHIE"
        pause 0.8
        systeme "MAMAN"
        pause 1.0
        narrateur "{cps=6}Tu ouvres une porte. La premiÃ¨re. Celle de Marc.{/cps}"
        pause 1.0
        narrateur "{cps=6}Marc est lÃ . Il te regarde. Avec dÃ©goÃ»t. Avec dÃ©ception.{/cps}"
        pause 1.0
        marc "Tu m'as trahi."
        pause 1.5
        narrateur "{cps=6}Tu fermes la porte brutalement, comme si Ã§a pouvait effacer ses mots.{/cps}"
        pause 1.0
        narrateur "{cps=6}Tu ouvres une autre. Celle de ta mÃ¨re.{/cps}"
        pause 1.0
        narrateur "{cps=6}Elle pleure. Elle te regarde comme si tu Ã©tais un Ã©tranger.{/cps}"
        pause 1.0
        maman "Qu'est-ce que tu es devenu ?"
        pause 1.5
        narrateur "{cps=6}Tu cours. Tu ouvres toutes les portes, une aprÃ¨s l'autre, comme si tu cherchais quelque chose.{/cps}"
        pause 1.0
        narrateur "{cps=6}Tous te regardent. Avec haine. Avec peur. Avec dÃ©goÃ»t.{/cps}"
        pause 1.5
        narrateur "{cps=6}Et au bout du couloir...{/cps}"
        pause 1.5
        narrateur "{cps=6}Une porte. Sans nom. Sans serrure. Juste... lÃ .{/cps}"
        pause 1.0
        narrateur "{cps=6}Tu l'ouvres. Tes doigts tremblent.{/cps}"
        pause 1.0
        show entite glitch at centre with dissolve
        pause 1.0
        entite "{cps=4}Bienvenue.{/cps}"
        pause 1.5
        narrateur "{cps=5}Tu te rÃ©veilles.{/cps}"
        pause 0.5
        narrateur "{cps=5}En hurlant.{/cps}"
    else:
        narrateur "{cps=8}You spend the rest of the night sitting in a corner.{/cps}"
        narrateur "{cps=8}Not sleeping.{/cps}"
        narrateur "{cps=8}Watching your devices.{/cps}"
        narrateur "{cps=8}Wondering which ones are watching you.{/cps}"
        pause 2.0
        narrateur "{cps=5}And then...{/cps}"
        narrateur "{cps=5}You fall asleep.{/cps}"
        narrateur "{cps=5}Despite yourself.{/cps}"
        scene bg blanc with dissolve
        narrateur "{cps=6}You're in a corridor.{/cps}"
        narrateur "{cps=6}Infinite.{/cps}"
        narrateur "{cps=6}Doors. Dozens.{/cps}"
        narrateur "{cps=6}Each door has a name.{/cps}"
        systeme "MARC"
        systeme "THOMAS"
        systeme "SOPHIE"
        systeme "MOM"
        narrateur "{cps=6}You open a door.{/cps}"
        narrateur "{cps=6}Marc is there.{/cps}"
        narrateur "{cps=6}He looks at you.{/cps}"
        narrateur "{cps=6}With disgust.{/cps}"
        marc "You betrayed me."
        narrateur "{cps=6}You close the door.{/cps}"
        narrateur "{cps=6}You open another.{/cps}"
        narrateur "{cps=6}Your mother.{/cps}"
        narrateur "{cps=6}She's crying.{/cps}"
        maman "What have you become?"
        narrateur "{cps=6}You run.{/cps}"
        narrateur "{cps=6}You open all the doors.{/cps}"
        narrateur "{cps=6}They all look at you.{/cps}"
        narrateur "{cps=6}With hatred.{/cps}"
        narrateur "{cps=6}And at the end of the corridor...{/cps}"
        narrateur "{cps=6}A door.{/cps}"
        narrateur "{cps=6}No name.{/cps}"
        narrateur "{cps=6}You open it.{/cps}"
        show entite glitch at centre with dissolve
        entite "{cps=4}Welcome.{/cps}"
        narrateur "{cps=5}You wake up.{/cps}"
        narrateur "{cps=5}Screaming.{/cps}"
    
    stop music fadeout 2.0
    
    if language == "fr":
        centered "{size=+20}FIN DU JOUR 4{/size}"
        pause 1.0
        centered "{size=+25}{color=#ff0040}FIN DE L'ACTE I{/color}{/size}"
        pause 1.0
        centered "{color=#666666}L'intrusion est complÃ¨te.{/color}"
        centered "{color=#666666}Tu es piÃ©gÃ©.{/color}"
        centered "{color=#666666}Et tu commences Ã  comprendre.{/color}"
    else:
        centered "{size=+20}END OF DAY 4{/size}"
        pause 1.0
        centered "{size=+25}{color=#ff0040}END OF ACT I{/color}{/size}"
        pause 1.0
        centered "{color=#666666}The intrusion is complete.{/color}"
        centered "{color=#666666}You are trapped.{/color}"
        centered "{color=#666666}And you're starting to understand.{/color}"
    pause 2.5
    
    jump acte2_debut
