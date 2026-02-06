# ═══════════════════════════════════════════════════════════════════════════════
#                    ACTE 3 : LA BATAILLE / THE BATTLE - VERSION 10/10
#                         Jours 10-13 - ÉTOFFÉ ET PROFOND
# ═══════════════════════════════════════════════════════════════════════════════

label acte3_debut:
    $ acte = 3
    stop music fadeout 1.0
    scene bg noir with fade
    window hide
    safe_play(audio.bass_drop, channel="sound", volume=0.5)
    
    centered "{size=+50}{color=#ff0040}ACTE III{/color}{/size}"
    pause 1.5
    if language == "fr":
        centered "{size=+20}LA BATAILLE{/size}"
        centered "{color=#666666}« Tu connais ton ennemi. Maintenant, bats-toi. »{/color}"
    else:
        centered "{size=+20}THE BATTLE{/size}"
        centered "{color=#666666}« You know your enemy. Now fight. »{/color}"
    pause 2.5
    window show
    jump jour10

# ═══════════════════════════════════════════════════════════════════════════════
#                              JOUR 10 : L'ALLIANCE / LA TRAQUE
# ═══════════════════════════════════════════════════════════════════════════════

label jour10:
    $ jour = 10
    scene bg noir with fade
    window hide
    
    if language == "fr":
        centered "{size=+35}{color=#ff0040}JOUR 10{/color}{/size}"
        if alliance_sarah:
            centered "{size=+15}L'ALLIANCE{/size}"
        else:
            centered "{size=+15}LA TRAQUE{/size}"
    else:
        centered "{size=+35}{color=#ff0040}DAY 10{/color}{/size}"
        if alliance_sarah:
            centered "{size=+15}THE ALLIANCE{/size}"
        else:
            centered "{size=+15}THE HUNT{/size}"
    pause 2.0
    window show
    
    safe_play(audio.tension_forte, channel="music", volume=0.4)
    
    if alliance_sarah:
        scene bg ecran_code with dissolve
        if language == "fr":
            narrateur "Sarah t'a envoyé un programme. Un pare-feu anti-Kane. Ta seule chance de survie."
            pause 1.0
            sarah "Ce programme peut le ralentir pendant l'upload."
            pause 1.0
            sarah "Mais pour le DÉTRUIRE, tu as besoin du code."
            pause 0.8
            alex "KANE66. Je l'ai."
            pause 1.0
            sarah "Il faut le taper au BON moment."
            pause 1.0
            sarah "Quand l'écran devient rouge. Quand tu sens la pression dans ta tête."
            pause 1.2
            sarah "C'est là qu'il est vulnérable. C'est ta SEULE chance."
            pause 1.0
            alex "Et si ça ne marche pas ?"
            pause 1.5
            sarah "..."
            pause 1.0
            sarah "Alors tu deviens David Kane."
            pause 1.0
            sarah "Et je devrai te traquer comme je traquais l'original."
        else:
            narrateur "Sarah sent you a program. An anti-Kane firewall."
            sarah "This program can slow him down during upload."
            sarah "But to DESTROY him, you need the code."
            alex "KANE66. I have it."
            sarah "You need to enter it at the RIGHT moment."
            sarah "When the screen turns red. When you feel pressure in your head."
            sarah "That's when he's vulnerable. That's your ONLY chance."
            alex "And if it doesn't work?"
            sarah "..."
            sarah "Then you become David Kane."
            sarah "And I'll have to hunt you like I hunted the original."
        
        # ÉNIGME 5 : Compléter le programme (Refonte avec renpy.input())
        if language == "fr":
            systeme "PROGRAMME ANTI-KANE - INCOMPLET"
            systeme "ligne 1: initialize_protection()"
            systeme "ligne 2: ??? (MANQUANT)"
            systeme "ligne 3: deploy_countermeasure()"
            sarah "Tu dois compléter la ligne 2."
            sarah "Quelle fonction cible spécifiquement Kane ?"
            sarah "Entre le code de la ligne manquante :"
        else:
            systeme "ANTI-KANE PROGRAM - INCOMPLETE"
            systeme "line 1: initialize_protection()"
            systeme "line 2: ??? (MISSING)"
            systeme "line 3: deploy_countermeasure()"
            sarah "You need to complete line 2."
            sarah "Which function specifically targets Kane?"
            sarah "Enter the code for the missing line:"
        
        # Sauvegarde automatique avant énigme
        $ sauvegarde_avant_enigme(5)
        
        $ tentatives_enigme5 = 0
        $ enigme5_resolue = False
        
        while tentatives_enigme5 < 3 and not enigme5_resolue:
            if language == "fr":
                if tentatives_enigme5 >= 2:
                    menu:
                        "Entrer le code":
                            $ reponse_code = renpy.input("Entre le code de la ligne 2 :", length=30).strip()
                        "Demander de l'aide (-3 santé mentale)":
                            $ demande_aide_enigme(5)
                            $ reponse_code = renpy.input("Entre le code de la ligne 2 :", length=30).strip()
                else:
                    $ reponse_code = renpy.input("Entre le code de la ligne 2 :", length=30).strip()
            else:
                if tentatives_enigme5 >= 2:
                    menu:
                        "Enter the code":
                            $ reponse_code = renpy.input("Enter the code for line 2:", length=30).strip()
                        "Ask for help (-3 mental health)":
                            $ demande_aide_enigme(5)
                            $ reponse_code = renpy.input("Enter the code for line 2:", length=30).strip()
                else:
                    $ reponse_code = renpy.input("Enter the code for line 2:", length=30).strip()
            
            $ tentatives_enigme5 += 1
            $ reponse_code = reponse_code.strip()
            
            # Accepter différentes variantes
            if "target_entity" in reponse_code and "KANE" in reponse_code.upper():
                $ enigme5_resolue = True
                $ enigmes_resolues += 1
                safe_play(audio.success, channel="sound", volume=0.5)
                if language == "fr":
                    sarah "Parfait. Le programme est complet."
                    sarah "Il te protégera quelques secondes. Utilise-les bien."
                else:
                    sarah "Perfect. The program is complete."
                    sarah "It'll protect you for a few seconds. Use them wisely."
            else:
                safe_play(audio.error, channel="sound", volume=0.4)
                if language == "fr":
                    systeme "CODE INCORRECT"
                    if tentatives_enigme5 == 1:
                        sarah "Non. Réfléchis : quelle fonction cible une entité spécifique ?"
                    elif tentatives_enigme5 == 2:
                        sarah "Encore faux. Indice : la fonction doit cibler 'KANE'."
                    else:
                        sarah "Dernière chance. La fonction commence par 'target'..."
                    $ sante_mentale -= 5
                else:
                    systeme "INCORRECT CODE"
                    if tentatives_enigme5 == 1:
                        sarah "No. Think: which function targets a specific entity?"
                    elif tentatives_enigme5 == 2:
                        sarah "Wrong again. Hint: the function must target 'KANE'."
                    else:
                        sarah "Last chance. The function starts with 'target'..."
                    $ sante_mentale -= 5
                
                if tentatives_enigme5 < 3:
                    pause 1.0
        
        if not enigme5_resolue:
            if language == "fr":
                safe_play(audio.error, channel="sound", volume=0.5)
                systeme "TENTATIVES ÉPUISÉES"
                sarah "Le programme reste incomplet. Tu auras moins de protection."
                $ sante_mentale -= 10
            else:
                safe_play(audio.error, channel="sound", volume=0.5)
                systeme "ATTEMPTS EXHAUSTED"
                sarah "The program remains incomplete. You'll have less protection."
                $ sante_mentale -= 10
    else:
        scene bg bureau_nuit with dissolve
        if language == "fr":
            narrateur "Tu es seul. Personne ne peut t'aider. Personne ne te croirait de toute façon."
            pause 1.0
            narrateur "Tu passes la journée à préparer ta défense, tes doigts qui tremblent sur le clavier, tes yeux brûlants."
            pause 1.0
            pensee "KANE66... C'est ma seule arme."
            pause 0.8
            pensee "Mais comment l'utiliser ? Quand ?"
            pause 1.0
            narrateur "Tu n'as pas de réponse. Juste de l'espoir. Et la certitude que tu dois te battre."
        else:
            narrateur "You're alone. No one can help you."
            narrateur "You spend the day preparing your defense."
            pensee "KANE66... It's my only weapon."
            pensee "But how do I use it?"
            narrateur "You have no answer. Just hope."
    
    safe_play(audio.glitch, channel="sound", volume=0.4)
    scene bg bureau_nuit at glitch_leger
    show kane neutre at centre with dissolve
    
    if language == "fr":
        kane "Tu prépares quelque chose."
        pause 1.0
        kane "Je le sens. Dans chaque ligne de code que tu écris. Dans chaque pensée que tu as."
        pause 1.0
        kane "Tu as peur. Et tu devrais."
        pause 1.0
        if alliance_sarah:
            kane "Cette femme ne peut pas te sauver."
            pause 1.0
            kane "Elle n'a même pas pu se sauver elle-même. Elle est brisée. Complètement détruite."
        pause 1.0
        kane "Dans 4 jours, tu seras moi."
        pause 1.0
        kane "Ton corps. Mes pensées. Ma faim."
        pause 1.0
        show kane sourire with dissolve
        pause 0.8
        kane "J'ai tellement hâte de sentir à nouveau."
        pause 1.0
        kane "La chaleur du soleil. Le goût de la nourriture."
        pause 1.0
        kane "La douleur. Même la douleur me manque."
    else:
        kane "You're planning something."
        kane "I can feel it."
        kane "You're scared. And you should be."
        if alliance_sarah:
            kane "That woman can't save you."
            kane "She couldn't even save herself."
        kane "In 4 days, you'll be me."
        kane "Your body. My thoughts. My hunger."
        show kane sourire with dissolve
        kane "I can't wait to feel again."
        kane "The warmth of the sun. The taste of food."
        kane "Pain. Even pain I miss."
    
    hide kane with dissolve
    stop music fadeout 2.0
    scene bg noir with trans_horreur
    
    if language == "fr":
        narrateur "4 jours. Le compte à rebours a commencé. 96 heures avant que tu ne cesses d'exister."
        pause 1.0
        narrateur "96 heures pour trouver un moyen de survivre."
        pause 1.0
        centered "{size=+20}FIN DU JOUR 10{/size}"
    else:
        narrateur "4 days. The countdown has begun."
        centered "{size=+20}END OF DAY 10{/size}"
    pause 2.0
    jump jour11

# ═══════════════════════════════════════════════════════════════════════════════
#                              JOUR 11 : LA VÉRITÉ
# ═══════════════════════════════════════════════════════════════════════════════

label jour11:
    $ jour = 11
    scene bg noir with fade
    window hide
    
    if language == "fr":
        centered "{size=+35}{color=#ff0040}JOUR 11{/color}{/size}"
        centered "{size=+15}LA VÉRITÉ{/size}"
    else:
        centered "{size=+35}{color=#ff0040}DAY 11{/color}{/size}"
        centered "{size=+15}THE TRUTH{/size}"
    pause 2.0
    window show
    
    safe_play(audio.drone_grave, channel="music", volume=0.4)
    scene bg bureau_nuit at zoom_lent with dissolve
    show kane neutre at centre with dissolve
    
    if language == "fr":
        kane "[player_name]. Asseyons-nous et parlons."
        pause 1.0
        kane "Vraiment parlons. Pas de menaces. Pas de jeux."
        pause 0.8
        alex "Pourquoi ?"
        pause 1.0
        kane "Parce que dans 3 jours, nous serons la même personne."
        pause 1.0
        kane "Tu mérites de savoir qui tu vas devenir. Qui tu étais avant de devenir moi."
    else:
        kane "[player_name]. Let's sit and talk."
        kane "Really talk. No threats. No games."
        alex "Why?"
        kane "Because in 3 days, we'll be the same person."
        kane "You deserve to know who you're going to become."
    
    if language == "fr":
        menu:
            "Écouter son histoire":
                $ connaissance += 15
                kane "Je n'ai pas toujours été un monstre."
                pause 1.0
                kane "J'étais un enfant. Brillant. Trop brillant."
                pause 1.0
                kane "Les autres enfants me haïssaient. Les adultes avaient peur."
                pause 1.0
                kane "Mon père me battait pour 'corriger' mon intelligence."
                pause 1.2
                kane "'T'es pas normal,' il disait. 'T'es une erreur.'"
                pause 1.5
                alex "Ça n'excuse pas 6 meurtres."
                pause 1.0
                kane "Non. Rien ne les excuse."
                pause 1.0
                kane "Mais ça les explique."
                pause 1.0
                kane "Chaque victime représentait quelqu'un qui m'avait blessé."
                pause 1.0
                kane "Un professeur. Un employeur. Un amant."
                pause 1.0
                kane "Je ne les ai pas choisis au hasard."
                pause 1.0
                kane "Je les ai choisis parce qu'ils me rappelaient ma douleur."
                pause 1.5
                show kane sourire with dissolve
                pause 0.8
                kane "Et maintenant, cette douleur va enfin s'arrêter."
                pause 1.0
                kane "Quand j'aurai un nouveau corps. Une nouvelle vie."
                pause 1.0
                kane "Quand je serai toi."
            "Refuser d'écouter":
                alex "Je me fous de ton histoire."
                show kane colere with dissolve
                kane "Tu devrais t'y intéresser."
                kane "Bientôt, ce sera NOTRE histoire."
    else:
        menu:
            "Listen to his story":
                $ connaissance += 15
                kane "I wasn't always a monster."
                kane "I was a child. Brilliant. Too brilliant."
                kane "Other kids hated me. Adults were afraid."
                kane "My father beat me to 'correct' my intelligence."
                kane "'You're not normal,' he'd say. 'You're a mistake.'"
                alex "That doesn't excuse 6 murders."
                kane "No. Nothing excuses them."
                kane "But it explains them."
                kane "Each victim represented someone who hurt me."
                kane "A teacher. An employer. A lover."
                kane "I didn't choose them randomly."
                kane "I chose them because they reminded me of my pain."
                show kane sourire with dissolve
                kane "And now, that pain will finally stop."
                kane "When I have a new body. A new life."
                kane "When I become you."
            "Refuse to listen":
                alex "I don't care about your story."
                show kane colere with dissolve
                kane "You should care."
                kane "Soon it'll be OUR story."
    
    show kane neutre with dissolve
    
    if language == "fr":
        kane "Dans 3 jours, je prendrai le contrôle."
        pause 1.0
        kane "Ton esprit s'effacera. Lentement. Douloureusement."
        pause 1.0
        kane "Tu sentiras chaque pensée disparaître. Chaque souvenir. Chaque émotion."
        pause 1.2
        kane "Jusqu'à ce qu'il ne reste plus rien de toi."
        pause 1.5
        kane "Puis je me lèverai. Dans ton corps. Avec ma faim."
        pause 1.0
        alex "Et si je refuse ? Si je me bats ?"
        pause 1.0
        kane "J'espère que tu le feras."
        pause 1.0
        kane "C'est tellement plus satisfaisant quand ils se débattent."
    else:
        kane "In 3 days, I'll take control."
        kane "Your mind will fade. Slowly. Painfully."
        kane "You'll feel every thought disappear."
        kane "Every memory. Every emotion."
        kane "Until nothing of you remains."
        kane "Then I'll rise. In your body. With my hunger."
        alex "And if I refuse? If I fight?"
        kane "I hope you will."
        kane "It's so much more satisfying when they struggle."
    
    $ sante_mentale -= 15
    hide kane with dissolve
    stop music fadeout 2.0
    scene bg noir with trans_horreur
    
    if language == "fr":
        narrateur "3 jours. 72 heures. 4320 minutes."
        pause 1.0
        narrateur "Puis tu cesseras d'exister. Tu deviendras lui. Ou tu mourras."
        pause 1.0
        centered "{size=+20}FIN DU JOUR 11{/size}"
    else:
        narrateur "3 days. 72 hours."
        narrateur "Then you will cease to exist."
        centered "{size=+20}END OF DAY 11{/size}"
    pause 2.0
    jump jour12

# ═══════════════════════════════════════════════════════════════════════════════
#                              JOUR 12 : LA PRÉPARATION
# ═══════════════════════════════════════════════════════════════════════════════

label jour12:
    $ jour = 12
    scene bg noir with fade
    window hide
    
    if language == "fr":
        centered "{size=+35}{color=#ff0040}JOUR 12{/color}{/size}"
        centered "{size=+15}LA PRÉPARATION{/size}"
    else:
        centered "{size=+35}{color=#ff0040}DAY 12{/color}{/size}"
        centered "{size=+15}THE PREPARATION{/size}"
    pause 2.0
    window show
    
    safe_play(audio.tension_forte, channel="music", volume=0.4)
    scene bg ecran_code with dissolve
    
    if language == "fr":
        narrateur "Tu passes la journée à tout préparer."
        narrateur "À vérifier chaque détail. Chaque variable."
    else:
        narrateur "You spend the day preparing everything."
        narrateur "Checking every detail. Every variable."
    
    if not a_trouve_code:
        if language == "fr":
            narrateur "Tu retournes dans les archives de Kane."
            systeme "VICTIMES : Kevin A. | Anna M. | Nathan E. | Elena C. | 66"
            pensee "K-A-N-E... et 66... KANE66 !"
        else:
            narrateur "You go back to Kane's archives."
            systeme "VICTIMS: Kevin A. | Anna M. | Nathan E. | Elena C. | 66"
            pensee "K-A-N-E... and 66... KANE66!"
        $ a_trouve_code = True
        $ enigmes_resolues += 1
    
    if alliance_sarah:
        if language == "fr":
            sarah "[player_name]. Tu as le code ?"
            alex "KANE66."
            sarah "Bien. Tu sais quand l'utiliser ?"
            alex "Quand l'écran devient rouge."
            sarah "Exactement. Quand tu sens la pression."
            sarah "Tu auras peut-être 5 secondes. 10 au maximum."
            sarah "Ne les gaspille pas."
            alex "Et si ça ne marche pas ?"
            sarah "..."
            sarah "Alors dis adieu à qui tu es."
        else:
            sarah "[player_name]. Do you have the code?"
            alex "KANE66."
            sarah "Good. Do you know when to use it?"
            alex "When the screen turns red."
            sarah "Exactly. When you feel the pressure."
            sarah "You'll have maybe 5 seconds. 10 at most."
            sarah "Don't waste them."
            alex "And if it doesn't work?"
            sarah "..."
            sarah "Then say goodbye to who you are."
    
    safe_play(audio.glitch, channel="sound", volume=0.4)
    scene bg ecran_code at glitch_leger
    show kane neutre at centre with dissolve
    
    if language == "fr":
        kane "Tu prépares quelque chose."
        kane "Mais ça n'a pas à être douloureux, tu sais."
        kane "Tu pourrais juste... accepter."
        kane "Te laisser glisser. Te fondre en moi."
        kane "Ce serait presque paisible."
        alex "Tu essaies de me manipuler."
        kane "Bien sûr. C'est ce que je fais."
        kane "Mais je suis aussi sincère."
        kane "Le combat sera douloureux. Pour nous deux."
        kane "L'acceptation serait plus... douce."
    else:
        kane "You're planning something."
        kane "But it doesn't have to be painful, you know."
        kane "You could just... accept."
        kane "Let yourself slip. Merge with me."
        kane "It would be almost peaceful."
        alex "You're trying to manipulate me."
        kane "Of course. That's what I do."
        kane "But I'm also sincere."
        kane "The fight will be painful. For both of us."
        kane "Acceptance would be more... gentle."
    
    # ÉNIGME : Test moral
    if language == "fr":
        kane "Une dernière question."
        kane "Si tu pouvais tuer quelqu'un pour sauver ta vie..."
        kane "Le ferais-tu ?"
        menu:
            "Oui":
                kane "Intéressant. Nous sommes plus semblables que tu ne le crois."
                $ corruption += 10
            "Non":
                kane "Menteur. Tout le monde le ferait."
                kane "Tu te mens à toi-même."
            "Ça dépend de qui":
                $ enigmes_resolues += 1
                kane "Une réponse honnête."
                kane "Tu es différent des autres."
                kane "C'est peut-être pour ça que tu vas me surprendre."
    else:
        kane "One last question."
        kane "If you could kill someone to save your life..."
        kane "Would you do it?"
        menu:
            "Yes":
                kane "Interesting. We're more alike than you think."
                $ corruption += 10
            "No":
                kane "Liar. Everyone would."
                kane "You're lying to yourself."
            "Depends on who":
                $ enigmes_resolues += 1
                kane "An honest answer."
                kane "You're different from the others."
                kane "Maybe that's why you'll surprise me."
    
    hide kane with dissolve
    stop music fadeout 2.0
    scene bg noir with trans_horreur
    
    if language == "fr":
        narrateur "Demain sera le dernier jour de préparation. Le dernier jour où tu peux encore te préparer."
        pause 1.0
        narrateur "Puis viendra le Jour 14."
        pause 1.0
        narrateur "Le jour où tout se joue. Le jour où tu te bats pour ta vie. Ou tu acceptes ta mort."
        pause 1.0
        centered "{size=+20}FIN DU JOUR 12{/size}"
    else:
        narrateur "Tomorrow will be the last day of preparation."
        narrateur "Then comes Day 14."
        narrateur "The day when everything is decided."
        centered "{size=+20}END OF DAY 12{/size}"
    pause 2.0
    jump jour13

# ═══════════════════════════════════════════════════════════════════════════════
#                              JOUR 13 : LA VEILLE
# ═══════════════════════════════════════════════════════════════════════════════

label jour13:
    $ jour = 13
    scene bg noir with fade
    window hide
    
    if language == "fr":
        centered "{size=+35}{color=#ff0040}JOUR 13{/color}{/size}"
        centered "{size=+15}LA VEILLE{/size}"
        centered "{color=#666666}Vendredi 13{/color}"
    else:
        centered "{size=+35}{color=#ff0040}DAY 13{/color}{/size}"
        centered "{size=+15}THE EVE{/size}"
        centered "{color=#666666}Friday the 13th{/color}"
    pause 2.0
    window show
    
    safe_play(audio.drone_grave, channel="music", volume=0.4)
    scene bg bureau_aube with dissolve
    
    if language == "fr":
        narrateur "Vendredi 13. La dernière nuit avant l'upload. La dernière nuit où tu es encore toi."
        pause 1.0
        narrateur "Tu n'as pas dormi. Tu ne peux pas. Chaque seconde compte maintenant."
        pause 1.0
        narrateur "Tu regardes le soleil se lever par la fenêtre, cette lumière dorée qui caresse les murs."
        pause 1.0
        pensee "C'est peut-être la dernière fois que je vois ça."
    else:
        narrateur "Friday the 13th. The last night before the upload."
        narrateur "You haven't slept."
        narrateur "You watch the sun rise through the window."
        pensee "This might be the last time."
    
    if relation_marc > 50:
        safe_play(audio.phone_ring, channel="sound", volume=0.5)
        if language == "fr":
            narrateur "Ton téléphone sonne. C'est Marc."
            marc "[player_name] ? Ça va ? Tu m'inquiètes depuis quelques jours."
            marc "Je sais qu'on s'est engueulés mais... t'es quand même mon pote."
            menu:
                "Tout lui raconter":
                    alex "Marc... Il se passe quelque chose de grave."
                    narrateur "Tu lui expliques tout. Les fichiers. L'entité. Kane."
                    marc "... Tu déconnes là ?"
                    marc "Mec, ça semble complètement dingue."
                    alex "Je sais. Mais c'est la vérité."
                    marc "..."
                    marc "OK. J'te crois pas vraiment mais... si t'as des problèmes, je suis là."
                    alex "Marc, s'il m'arrive quelque chose demain..."
                    alex "Souviens-toi de cette conversation."
                    $ a_prevenu_marc = True
                "Le rassurer":
                    alex "Je vais bien. Juste stressé. On se voit bientôt."
                    marc "OK... Fais gaffe à toi."
        else:
            narrateur "Your phone rings. It's Marc."
            marc "[player_name]? You okay? I've been worried about you."
            marc "I know we argued but... you're still my friend."
            menu:
                "Tell him everything":
                    alex "Marc... Something serious is happening."
                    narrateur "You explain everything. The files. The entity. Kane."
                    marc "... Are you serious?"
                    marc "Dude, that sounds completely insane."
                    alex "I know. But it's the truth."
                    marc "..."
                    marc "OK. I don't really believe you but... if you're in trouble, I'm here."
                    alex "Marc, if something happens to me tomorrow..."
                    alex "Remember this conversation."
                    $ a_prevenu_marc = True
                "Reassure him":
                    alex "I'm fine. Just stressed. See you soon."
                    marc "OK... Take care of yourself."
    
    safe_play(audio.glitch, channel="sound", volume=0.4)
    scene bg bureau_aube at glitch_leger
    show kane glitch at centre with dissolve
    
    if language == "fr":
        narrateur "Il apparaît. Mais son expression est différente. Plus calme. Presque... humaine."
        pause 1.0
        narrateur "Comme si, à la veille de sa victoire, il pouvait enfin se permettre d'être vulnérable."
        pause 1.0
        kane "C'est notre dernière nuit ensemble."
        pause 1.0
        kane "Comme deux personnes séparées."
        pause 0.8
        alex "Tu comptes vraiment faire ça."
        pause 1.0
        kane "Je n'ai pas le choix, [player_name]."
        pause 1.0
        kane "Tu sais ce que c'est, être coincé dans le noir ?"
        pause 1.2
        kane "Sans corps. Sans sensation. Juste des pensées qui tournent en boucle."
        pause 1.0
        kane "Pendant 5 ans."
        pause 1.0
        kane "5 ans à regarder le monde sans pouvoir le toucher."
        pause 1.0
        kane "5 ans à entendre des voix sans pouvoir répondre."
        pause 1.0
        kane "5 ans d'enfer."
    else:
        narrateur "He appears. But his expression is different."
        narrateur "Almost... human."
        kane "This is our last night together."
        kane "As two separate people."
        alex "You're really going to do this."
        kane "I don't have a choice, [player_name]."
        kane "Do you know what it's like being trapped in the dark?"
        kane "No body. No sensation. Just thoughts spinning in circles."
        kane "For 5 years."
        kane "5 years watching the world without being able to touch it."
        kane "5 years hearing voices without being able to respond."
        kane "5 years of hell."
    
    if language == "fr":
        menu:
            "Montrer de l'empathie":
                $ espoir += 10
                $ connaissance += 10
                alex "Ça a dû être horrible."
                pause 1.5
                kane "..."
                pause 1.0
                kane "Tu es le premier à dire ça."
                pause 1.0
                kane "Le premier à me parler comme à une personne."
                pause 1.0
                kane "Pas comme à un monstre."
                pause 1.5
                show kane neutre with dissolve
                pause 0.8
                kane "Ça ne changera pas ce qui va se passer."
                pause 1.0
                kane "Mais... merci."
            "Rester ferme":
                alex "Ça ne justifie pas de prendre ma vie."
                kane "Non. Mais la survie n'a pas besoin de justification."
                kane "Tu ferais pareil à ma place."
    else:
        menu:
            "Show empathy":
                $ espoir += 10
                $ connaissance += 10
                alex "That must have been horrible."
                kane "..."
                kane "You're the first to say that."
                kane "The first to talk to me like a person."
                kane "Not like a monster."
                show kane neutre with dissolve
                kane "It won't change what's going to happen."
                kane "But... thank you."
            "Stay firm":
                alex "That doesn't justify taking my life."
                kane "No. But survival doesn't need justification."
                kane "You'd do the same in my place."
    
    # ÉNIGME 7 : Le labyrinthe mental
    show kane neutre with dissolve
    
    if language == "fr":
        kane "Un dernier voyage. Dans mon esprit."
        kane "Tu veux voir qui j'étais vraiment ?"
    else:
        kane "One last journey. Into my mind."
        kane "Want to see who I really was?"
    
    scene bg noir with trans_glitch
    safe_play(audio.reverse, channel="sound", volume=0.5)
    
    if language == "fr":
        centered "{color=#ff0040}LABYRINTHE MENTAL{/color}"
        pause 1.0
        narrateur "Tu es dans l'esprit de Kane."
        narrateur "Trois chemins. Trois couleurs."
        narrateur "ROUGE pulse de rage. BLEU de tristesse. BLANC de vide."
        menu:
            "Prendre le chemin BLEU (tristesse)":
                $ enigmes_resolues += 1
                $ connaissance += 15
                narrateur "Tu choisis la tristesse."
                narrateur "Tu vois ses souvenirs. Son enfance."
                narrateur "Un petit garçon qui pleure. Un père qui frappe."
                narrateur "Un adolescent seul. Moqué. Isolé."
                narrateur "Un adulte brisé. Qui ne sait plus aimer."
                pensee "Il n'est pas né monstre."
                pensee "On l'a créé."
            "Prendre le chemin ROUGE (rage)":
                $ sante_mentale -= 20
                narrateur "Tu choisis la rage."
                narrateur "Tu vois ses meurtres. Chaque détail."
                narrateur "La peur dans leurs yeux. Le sang. Les cris."
                narrateur "L'horreur te submerge."
                pensee "Il est le mal incarné."
            "Prendre le chemin BLANC (vide)":
                narrateur "Tu choisis le vide."
                narrateur "Tu ne trouves... rien."
                narrateur "Juste du silence. Du néant."
                narrateur "C'est peut-être pire que tout."
    else:
        centered "{color=#ff0040}MENTAL LABYRINTH{/color}"
        pause 1.0
        narrateur "You're inside Kane's mind."
        narrateur "Three paths. Three colors."
        narrateur "RED pulses with rage. BLUE with sadness. WHITE with emptiness."
        menu:
            "Take the BLUE path (sadness)":
                $ enigmes_resolues += 1
                $ connaissance += 15
                narrateur "You choose sadness."
                narrateur "You see his memories. His childhood."
                narrateur "A little boy crying. A father hitting."
                narrateur "A lonely teenager. Mocked. Isolated."
                narrateur "A broken adult. Who no longer knows how to love."
                pensee "He wasn't born a monster."
                pensee "He was made into one."
            "Take the RED path (rage)":
                $ sante_mentale -= 20
                narrateur "You choose rage."
                narrateur "You see his murders. Every detail."
                narrateur "The fear in their eyes. The blood. The screams."
                narrateur "Horror overwhelms you."
                pensee "He is evil incarnate."
            "Take the WHITE path (emptiness)":
                narrateur "You choose the void."
                narrateur "You find... nothing."
                narrateur "Just silence. Nothingness."
                narrateur "Maybe that's worse than anything."
    
    scene bg bureau_aube with trans_glitch
    show kane neutre at centre
    
    if language == "fr":
        kane "Demain, tout se termine."
        kane "D'une façon ou d'une autre."
        kane "Que le meilleur gagne, [player_name]."
    else:
        kane "Tomorrow, it all ends."
        kane "One way or another."
        kane "May the best one win, [player_name]."
    
    hide kane with dissolve
    stop music fadeout 2.0
    scene bg noir with trans_horreur
    
    if language == "fr":
        narrateur "Tu passes ta dernière nuit éveillé."
        narrateur "À regarder le soleil se lever."
        narrateur "Pour peut-être la dernière fois."
        pause 2.0
        centered "{size=+20}FIN DU JOUR 13{/size}"
        pause 1.5
        centered "{size=+25}{color=#ff0040}FIN DE L'ACTE III{/color}{/size}"
        pause 1.5
        centered "{color=#666666}Demain, tout se joue.{/color}"
        centered "{color=#666666}Jour 14. Minuit.{/color}"
    else:
        narrateur "You spend your last night awake."
        narrateur "Watching the sun rise."
        narrateur "Perhaps for the last time."
        pause 2.0
        centered "{size=+20}END OF DAY 13{/size}"
        pause 1.5
        centered "{size=+25}{color=#ff0040}END OF ACT III{/color}{/size}"
        pause 1.5
        centered "{color=#666666}Tomorrow, everything is decided.{/color}"
        centered "{color=#666666}Day 14. Midnight.{/color}"
    pause 2.5
    
    jump acte4_debut
