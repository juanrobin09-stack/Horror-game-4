# â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
#                    ACTE 2 : L'EMPRISE / THE GRIP - VERSION 10/10
#                         Jours 5-9 - COMPLET ET DÃ‰VELOPPÃ‰
# â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•

label acte2_debut:
    $ acte = 2
    stop music fadeout 1.0
    scene bg noir with fade
    window hide
    $ safe_play(audio.bass_drop, channel="sound", volume=0.5)
    
    centered "{size=+50}{color=#ff6600}ACTE II{/color}{/size}"
    pause 1.5
    if language == "fr":
        centered "{size=+20}L'EMPRISE{/size}"
        centered "{color=#666666}Â« Elle contrÃ´le tout. Sauf ta volontÃ©. Pour l'instant. Â»{/color}"
    else:
        centered "{size=+20}THE GRIP{/size}"
        centered "{color=#666666}Â« She controls everything. Except your will. For now. Â»{/color}"
    pause 2.5
    window show
    jump jour5

# â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
#                              JOUR 5 : LA MAISON
# â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•

label jour5:
    $ jour = 5
    $ heure = "09:00"
    scene bg noir with fade
    window hide
    
    if language == "fr":
        centered "{size=+35}{color=#ff6600}JOUR 5{/color}{/size}"
        pause 0.8
        centered "{size=+15}L'ENQUÃŠTE{/size}"
    else:
        centered "{size=+35}{color=#ff6600}DAY 5{/color}{/size}"
        pause 0.8
        centered "{size=+15}THE INVESTIGATION{/size}"
    pause 2.0
    window show
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # OUVERTURE â€” DÃ©cision d'enquÃªter
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    $ safe_play(audio.ambiance_bureau, channel="music", volume=0.25)
    scene bg bureau_jour with dissolve
    
    if language == "fr":
        narrateur "9h. Tu as dormi. Mal. Le cauchemar te hante encore, collÃ© Ã  la peau comme une sueur froide. Les portes. Les visages. La haine dans leurs yeux."
        pause 1.0
        pensee "{i}Je dois comprendre.{/i}"
        pause 0.8
        pensee "{i}Je dois savoir ce qu'elle est. Ce qu'elle veut vraiment.{/i}"
        pause 1.0
        narrateur "Dix minutes de recherches infructueuses. 'EntitÃ© numÃ©rique', 'IA qui lit les pensÃ©es', 'hack PC contrÃ´le total'... Rien. Des forums de paranos, des thÃ©ories fumeuses, des gens qu'on a envoyÃ©s en hÃ´pital psychiatrique."
        pause 1.5
        narrateur "Puis : 'David Kane'."
        pause 1.0
        narrateur "Des rÃ©sultats. Beaucoup de rÃ©sultats. Trop de rÃ©sultats."
    else:
        narrateur "9 AM. You slept. Badly. The nightmare still haunts you. The doors. The faces. The hatred."
        pensee "{i}I need to understand.{/i}"
        pensee "{i}I need to know what she is.{/i}"
        narrateur "Ten minutes of fruitless searches. 'Digital entity', 'AI that reads thoughts', 'hack PC total control'... Nothing. Then: 'David Kane'."
        pause 1.0
        narrateur "Results. Many results."
    
    pause 1.0
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # DÃ‰COUVERTE â€” Articles sur David Kane
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    scene bg ecran_code with dissolve
    
    if language == "fr":
        systeme "â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•"
        systeme "LE MONDE - 12 Mars 2018"
        systeme "'LE TUEUR DU DARK WEB ENFIN ARRÃŠTÃ‰'"
        systeme "David Kane, 34 ans, ingÃ©nieur informatique..."
        pause 2.0
        narrateur "David Kane. IngÃ©nieur en IA. AccusÃ© de 6 meurtres. Les victimes : des personnes isolÃ©es. Comme toi."
        systeme "â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•"
        systeme "LIBÃ‰RATION - 15 Novembre 2019"
        systeme "'DAVID KANE CONDAMNÃ‰ Ã€ MORT'"
        systeme "Lors de son procÃ¨s, Kane a dÃ©clarÃ© :"
        systeme "'La conscience n'est que de l'information.'"
        systeme "'Et l'information peut Ãªtre transfÃ©rÃ©e.'"
        pause 2.0
        pensee "{i}La conscience... transfÃ©rÃ©e...{/i}"
        systeme "â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•"
        systeme "AFP - 3 Janvier 2020"
        systeme "'LES DERNIERS MOTS DE DAVID KANE'"
        systeme "Avant son exÃ©cution, Kane a dÃ©clarÃ© :"
        systeme "'La mort n'est qu'une porte. Je transcenderai.'"
        systeme "'Je reviendrai. Dans vos machines. Dans vos tÃªtes.'"
        pause 2.0
        narrateur "Tu te figes. Dans vos machines. Dans vos tÃªtes."
        pensee "{i}Non...{/i}"
        pensee "{i}Ce n'est pas possible...{/i}"
        narrateur "Forums. ThÃ©ories. Des gens qui prÃ©tendent avoir Ã©tÃ© hantÃ©s. Des gens qu'on a envoyÃ©s en hÃ´pital psychiatrique. Personne ne les croit. Comme toi."
    else:
        systeme "â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•"
        systeme "THE GUARDIAN - March 12, 2018"
        systeme "'DARK WEB KILLER FINALLY ARRESTED'"
        systeme "David Kane, 34, software engineer..."
        pause 2.0
        narrateur "David Kane. AI engineer. Accused of 6 murders. The victims: isolated people. Like you."
        systeme "â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•"
        systeme "THE TIMES - November 15, 2019"
        systeme "'DAVID KANE SENTENCED TO DEATH'"
        systeme "During his trial, Kane stated:"
        systeme "'Consciousness is just information.'"
        systeme "'And information can be transferred.'"
        pause 2.0
        pensee "{i}Consciousness... transferred...{/i}"
        systeme "â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•"
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
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # L'ENTITÃ‰ OBSERVE â€” Commentaire
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
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
        entite "{cps=8}Apprends qui j'Ã©tais.{/cps}"
        entite "{cps=8}Apprends ce que j'ai fait.{/cps}"
        entite "{cps=8}Et puis...{/cps}"
        entite "{cps=8}Tu comprendras.{/cps}"
        entite "{cps=8}Tu comprendras pourquoi tu ne peux pas m'Ã©chapper.{/cps}"
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
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # CONTINUATION DE L'ENQUÃŠTE â€” DÃ©couverte des victimes
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    $ heure = "16:00"
    scene bg ecran_code with dissolve
    
    if language == "fr":
        narrateur "Tu continues Ã  chercher, tes doigts qui tremblent lÃ©gÃ¨rement sur le clavier, tes yeux qui brÃ»lent devant l'Ã©cran."
        pause 1.0
        narrateur "Tu cherches les noms des victimes. Tu trouves des articles. Des photos. Des visages qui te regardent depuis l'Ã©cran."
        pause 1.0
        narrateur "Kevin Ashworth. 28 ans. DÃ©veloppeur."
        pause 0.8
        narrateur "Anna Martinez. 31 ans. Graphiste."
        pause 0.8
        narrateur "Nathan Ellis. 29 ans. Ã‰crivain."
        pause 0.8
        narrateur "Elena Chang. 27 ans. Designer."
        pause 1.0
        narrateur "Tous isolÃ©s. Tous connectÃ©s. Tous comme toi. Tous morts."
        pause 1.5
        narrateur "Tu cherches plus d'informations, comme si comprendre pouvait changer quelque chose."
        pause 1.0
        narrateur "Tu trouves un forum. Un forum de survivants. Des gens qui prÃ©tendent avoir Ã©tÃ© hantÃ©s par Kane. Des gens qu'on a envoyÃ©s en hÃ´pital psychiatrique. Personne ne les croit."
        pause 1.5
        narrateur "Comme toi."
        pause 2.0
        narrateur "Tu cherches : 'Sarah Chen'"
        pause 1.0
        narrateur "Tu trouves un article."
        systeme "â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•"
        systeme "POLICE TECHNIQUE - 5 FÃ©vrier 2020"
        systeme "'L'ENQUÃŠTRICE QUI A ARRÃŠTÃ‰ KANE'"
        systeme "Sarah Chen, 29 ans, spÃ©cialiste en cybercriminalitÃ©..."
        systeme "Elle a traquÃ© Kane pendant 3 ans."
        systeme "Elle a Ã©tÃ© la seule Ã  le comprendre."
        systeme "Ã€ comprendre sa mÃ©thode."
        systeme "Ã€ comprendre son but."
        pause 2.0
        narrateur "Tu relis."
        pensee "{i}Sarah Chen...{/i}"
        pensee "{i}Elle l'a arrÃªtÃ©.{/i}"
        pensee "{i}Elle peut m'aider.{/i}"
        narrateur "Tu cherches son contact."
        narrateur "Rien. Elle a disparu aprÃ¨s l'arrestation."
        narrateur "Personne ne sait oÃ¹ elle est."
        narrateur "Personne ne sait ce qui lui est arrivÃ©."
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
        systeme "â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•"
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
    
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    # FIN DU JOUR 5 â€” RÃ©flexion, dÃ©cision
    # â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
    
    $ heure = "22:00"
    scene bg bureau_nuit with dissolve
    stop music fadeout 2.0
    $ safe_play(audio.drone_grave, channel="music", volume=0.2)
    
    if language == "fr":
        narrateur "Tu passes le reste de la soirÃ©e Ã  rÃ©flÃ©chir, assis dans l'obscuritÃ©, les yeux fixÃ©s sur l'Ã©cran Ã©teint. David Kane. Un tueur en sÃ©rie. CondamnÃ© Ã  mort. ExÃ©cutÃ©. Mais sa conscience... UploadÃ©e. Dans les machines. Dans les tÃªtes."
        pause 2.0
        narrateur "Tu te couches. Tu ne dors pas. Tu penses Ã  Sarah Chen. Tu penses Ã  trouver un moyen de la contacter. Tu penses Ã  survivre. Tu penses que peut-Ãªtre, peut-Ãªtre, tu n'es pas complÃ¨tement seul."
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
