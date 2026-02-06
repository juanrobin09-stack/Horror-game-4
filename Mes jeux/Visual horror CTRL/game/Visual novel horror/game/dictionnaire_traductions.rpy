# ═══════════════════════════════════════════════════════════════════════════════
#                    DICTIONNAIRE DE TRADUCTIONS FR/EN
#                         CTRL+ALT+DELETE
# ═══════════════════════════════════════════════════════════════════════════════
#
#   COMMENT UTILISER :
#   Au lieu d'écrire : narrateur "Le texte en français"
#   Tu écris :         narrateur "[TR_jour1_intro]"
#
#   Ou utilise la fonction t() :
#   narrateur t("Texte FR", "Text EN")
#
# ═══════════════════════════════════════════════════════════════════════════════

init python:
    # Dictionnaire de traductions
    translations = {
        # ═══════════════════════════════════════════════════════════════════════
        #                         INTERFACE / UI
        # ═══════════════════════════════════════════════════════════════════════
        "menu_new_game": {"fr": "► NOUVELLE PARTIE", "en": "► NEW GAME"},
        "menu_continue": {"fr": "► CONTINUER", "en": "► CONTINUE"},
        "menu_options": {"fr": "► OPTIONS", "en": "► OPTIONS"},
        "menu_quit": {"fr": "► QUITTER", "en": "► QUIT"},
        "menu_warning": {"fr": "Ce jeu contient des thèmes matures et de l'horreur psychologique.", 
                         "en": "This game contains mature themes and psychological horror."},
        "menu_subtitle": {"fr": "Tu n'aurais jamais dû ouvrir ce fichier.",
                          "en": "You should never have opened that file."},
        
        # ═══════════════════════════════════════════════════════════════════════
        #                         ACTES / TITRES
        # ═══════════════════════════════════════════════════════════════════════
        "acte1_titre": {"fr": "L'INTRUSION", "en": "THE INTRUSION"},
        "acte1_quote": {"fr": "La curiosité est un poison lent.", "en": "Curiosity is a slow poison."},
        "acte2_titre": {"fr": "L'EMPRISE", "en": "THE GRIP"},
        "acte2_quote": {"fr": "Elle contrôle tout. Sauf ta volonté. Pour l'instant.", 
                        "en": "She controls everything. Except your will. For now."},
        "acte3_titre": {"fr": "LA BATAILLE", "en": "THE BATTLE"},
        "acte3_quote": {"fr": "Tu connais ton ennemi. Maintenant, bats-toi.", 
                        "en": "You know your enemy. Now fight."},
        "acte4_titre": {"fr": "LE JUGEMENT", "en": "THE JUDGMENT"},
        "acte4_quote": {"fr": "Une seule fin est possible.", "en": "Only one ending is possible."},
        
        "jour": {"fr": "JOUR", "en": "DAY"},
        "fin_jour": {"fr": "FIN DU JOUR", "en": "END OF DAY"},
        "fin_acte": {"fr": "FIN DE L'ACTE", "en": "END OF ACT"},
        
        # ═══════════════════════════════════════════════════════════════════════
        #                         JOURS - TITRES
        # ═══════════════════════════════════════════════════════════════════════
        "jour1_titre": {"fr": "LE FICHIER", "en": "THE FILE"},
        "jour2_titre": {"fr": "LES YEUX", "en": "THE EYES"},
        "jour3_titre": {"fr": "L'ISOLEMENT", "en": "THE ISOLATION"},
        "jour4_titre": {"fr": "LE PIÈGE", "en": "THE TRAP"},
        "jour5_titre": {"fr": "LA MAISON", "en": "THE HOUSE"},
        "jour6_titre": {"fr": "LES RÈGLES", "en": "THE RULES"},
        "jour7_titre": {"fr": "LA FAIM", "en": "THE HUNGER"},
        "jour8_titre": {"fr": "LE PASSÉ", "en": "THE PAST"},
        "jour9_titre": {"fr": "LE CONTACT", "en": "THE CONTACT"},
        "jour10_titre": {"fr": "L'ALLIANCE", "en": "THE ALLIANCE"},
        "jour10_titre_solo": {"fr": "LA TRAQUE", "en": "THE HUNT"},
        "jour11_titre": {"fr": "LA VÉRITÉ", "en": "THE TRUTH"},
        "jour12_titre": {"fr": "LA PRÉPARATION", "en": "THE PREPARATION"},
        "jour13_titre": {"fr": "LA VEILLE", "en": "THE EVE"},
        "jour14_titre": {"fr": "MINUIT", "en": "MIDNIGHT"},
        
        # ═══════════════════════════════════════════════════════════════════════
        #                         FINS
        # ═══════════════════════════════════════════════════════════════════════
        "fin1_titre": {"fr": "LIBÉRATION TOTALE", "en": "TOTAL LIBERATION"},
        "fin1_desc": {"fr": "Tu as détruit Kane et sauvé les autres.", 
                      "en": "You destroyed Kane and saved the others."},
        "fin2_titre": {"fr": "SACRIFICE", "en": "SACRIFICE"},
        "fin2_desc": {"fr": "Tu as donné ta vie pour sauver les autres.", 
                      "en": "You gave your life to save the others."},
        "fin3_titre": {"fr": "RÉDEMPTION", "en": "REDEMPTION"},
        "fin3_desc": {"fr": "Kane a trouvé la paix. Et toi, la liberté.", 
                      "en": "Kane found peace. And you, freedom."},
        "fin4_titre": {"fr": "VICTOIRE PARTIELLE", "en": "PARTIAL VICTORY"},
        "fin4_desc": {"fr": "Tu as gagné cette bataille. Pas la guerre.", 
                      "en": "You won this battle. Not the war."},
        "fin5_titre": {"fr": "SURVIE", "en": "SURVIVAL"},
        "fin5_desc": {"fr": "Tu survis. Mais Kane aussi.", 
                      "en": "You survive. But so does Kane."},
        "fin6_titre": {"fr": "FUITE", "en": "ESCAPE"},
        "fin6_desc": {"fr": "Tu as fui. Kane cherche une autre victime.", 
                      "en": "You fled. Kane is looking for another victim."},
        "fin7_titre": {"fr": "OUBLI", "en": "OBLIVION"},
        "fin7_desc": {"fr": "Tu as oublié. Mais Kane se souvient.", 
                      "en": "You forgot. But Kane remembers."},
        "fin8_titre": {"fr": "POSSESSION", "en": "POSSESSION"},
        "fin8_desc": {"fr": "Kane vit. Tu n'existes plus.", 
                      "en": "Kane lives. You no longer exist."},
        "fin9_titre": {"fr": "FUSION", "en": "FUSION"},
        "fin9_desc": {"fr": "Vous êtes devenus un. Pour l'éternité.", 
                      "en": "You became one. For eternity."},
        "fin10_titre": {"fr": "FOLIE", "en": "MADNESS"},
        "fin10_desc": {"fr": "La réalité t'a échappé. Ou peut-être pas.", 
                       "en": "Reality escaped you. Or maybe not."},
        "fin11_titre": {"fr": "ÉCHEC TRAGIQUE", "en": "TRAGIC FAILURE"},
        "fin11_desc": {"fr": "Tu as échoué. Kane continue.", 
                       "en": "You failed. Kane continues."},
        "fin12_titre": {"fr": "ÉTERNEL", "en": "ETERNAL"},
        "fin12_desc": {"fr": "Tu es devenu ce que tu combattais.", 
                       "en": "You became what you were fighting."},
        "game_over": {"fr": "GAME OVER", "en": "GAME OVER"},
        "sante_zero": {"fr": "Santé mentale à zéro.", "en": "Mental health at zero."},
    }
    
    def TR(key):
        """Récupère une traduction depuis le dictionnaire"""
        lang = store.language if hasattr(store, 'language') else "fr"
        if key in translations:
            return translations[key].get(lang, translations[key].get("fr", key))
        return key

# ═══════════════════════════════════════════════════════════════════════════════
#                    VARIABLES DE TRADUCTION DYNAMIQUES
# ═══════════════════════════════════════════════════════════════════════════════

# Ces variables sont utilisables directement dans le texte avec [TR_xxx]
define TR_acte1 = "ACTE I"
define TR_acte2 = "ACTE II"
define TR_acte3 = "ACTE III"
define TR_acte4 = "ACTE FINAL"
