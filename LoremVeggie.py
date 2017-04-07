#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sublime
import sublime_plugin
import random
import re

class LoremVeggieCommand(sublime_plugin.TextCommand):

    def run(self, edit, qty=10):

        selections = self.view.sel()
        for selection in selections:

            # always start with Lorem ipsum for first outpur lorem
            para = "Veggies es bonus vobis, proinde vos postulo essum magis "

            # words from the original Lorum ipsum text
            #words = "dolor sit amet consectetur adipisicing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur Excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit anim id est laborum".split()
            # deutsches Gemuese:
            words = ['Blattgemüse', 'Salatpflanze', 'Acker-Hellerkraut', 'Acker-Rettich', 'Acker-Senf', 'Ackerlauch', 'Adlerfarn', 'Ähriger Erdbeerspinat', 'Allium tricoccum', 'Alpen-Ampfer', 'Alpen-Milchlattich', 'Amarant', 'Aufrechtes Glaskraut', 'Aufsteigender Fuchsschwanz', 'Bachbunge', 'Bärlauch', 'Baumspinat', 'Borretsch', 'Brandschopf', 'Brauner Senf', 'Breitblättriger Senf', 'Breitwegerich', 'Catjangbohne', 'Chayote', 'Chicorée', 'Chinakohl', 'Corchorus', 'Cyclanthera pedata', 'Dreifarbiger Fuchsschwanz', 'Echte Brunnenkresse', 'Echter Eibisch', 'Echter Erdbeerspinat', 'Echter Sellerie', 'Eisbergsalat', 'Endivie', 'Fleischkraut', 'Futterrübe', 'Garten-Senfrauke', 'Gartenkresse', 'Gartenmelde', 'Gartensalat', 'Gemeine Wegwarte', 'Gemeiner Bocksdorn', 'Gemüse-Gänsedistel', 'Gemüsekohl', 'Geschwänzte Brennnessel', 'Gewöhnliche Vogelmiere', 'Gewöhnlicher Feldsalat', 'Gewöhnliches Tellerkraut', 'Giersch', 'Goabohne', 'Große Brennnessel', 'Große Kapuzinerkresse', 'Grünähriger Amarant', 'Grünkohl', 'Guter Heinrich', 'Haferwurzel', 'Herbstrübe', 'Hiroshimana', 'Indische Lotosblume', 'Indischer Spinat', 'Jambú', 'Japanischer Staudenknöterich', 'Klatschmohn', 'Kleine Braunelle', 'Kleine Brennnessel', 'Knoblauch-Schnittlauch', 'Knoblauchsrauke', 'Komatsuna', 'Kopfkohl', 'Kopfsalat', 'Kriechender Sellerie', 'Kronenwucherblume', 'Langkapselige Jute', 'Gewöhnlicher Löwenzahn', 'Mairübe', 'Mangold', 'Maniok', 'Markstammkohl', 'Meerfenchel', 'Meerrettichbaum', 'Neuseeländer Spinat', 'Palmkohl', 'Perilla', 'Portulak', 'Puntarelle', 'Quinoa', 'Radicchio', 'Rattenschwanzrettich', 'Röhricht-Brennnessel', 'Römersalat', 'Rosenkohl', 'Rotkohl', 'Rübstiel', 'Rucola', 'Schlangen-Knöterich', 'Schlangen-Lauch', 'Schnittkohl', 'Schnittlauch', 'Schnittsalat', 'Schnittzichorie', 'Schwarzer Senf', 'Senfe', 'Silber-Brandschopf', 'Sommerlinde', 'Spieß-Melde', 'Spinat', 'Stängelkohl', 'Strand-Wegerich', 'Süßdolde', 'Süßkartoffel', 'Taro', 'Tatsoi', 'Toona sinensis', 'Wasserspinat', 'Weg-Malve', 'Weinrebenblätter', 'Weißer Gänsefuß', 'Weißer Senf', 'Weißer Fuchsschwanz', 'Wiesen-Bocksbart', 'Wiesen-Labkraut', 'Wiesen-Sauerampfer', 'Wilde Malve', 'Winterkresse', 'Winterzwiebel', 'Wirsing', 'Zuckerrübe', 'Fruchtgemüse', 'Ackerbohne', 'Adzukibohne', 'Ähriger Erdbeerspinat', 'Andine Knollenbohne', 'Äthiopische Eierfrucht', 'Aubergine', 'Augenbohne', 'Avocado', 'Bohne', 'Catjangbohne', 'Chayote', 'Cucurbita argyrosperma', 'Cyclanthera pedata', 'Echter Kapernstrauch', 'Erbse', 'Erdbohne', 'Feigenblatt-Kürbis', 'Feuerbohne', 'Flaschenkürbis', 'Gartenbohne', 'Gartenkürbis', 'Gem Squash', 'Gemeiner Bocksdorn', 'Goabohne', 'Guarbohne', 'Gurke', 'Helmbohne', 'Hokkaidokürbis', 'Jackbohne', 'Kefe', 'Kichererbse', 'Knollenbohne', 'Kochbanane', 'Limabohne', 'Linsen-Wicke', 'Mango', 'Mattenbohne', 'Meerrettichbaum', 'Melone', 'Moschus-Kürbis', 'Nara', 'Okra', 'Olivenbaum', 'Parkia speciosa', 'Patisson', 'Macrotyloma uniflorum', 'Quinoa', 'Rattenschwanzrettich', 'Reisbohne', 'Riesen-Kürbis', 'Schwertbohne', 'Sicana odorifera', 'Spaghettikürbis', 'Spargelbohne', 'Teparybohne', 'Thai-Aubergine', 'Tomate', 'Tomatillo', 'Urdbohne', 'Wachskürbis', 'Zucchini', 'Gemüsekohl', 'Bayerische Rübe', 'Blattkohl', 'Blauer Speck', 'Blumenkohl', 'Breitblättriger Senf', 'Brokkoli', 'Chinakohl', 'Federkohl', 'Grünkohl', 'Hiroshimana', 'Kai-lan', 'Kohl', 'Kohlrabi', 'Kopfkohl', 'Markstammkohl', 'Pak Choi', 'Palmkohl', 'Pfatterer Rübe', 'Romanesco', 'Rosenkohl', 'Rotkohl', 'Spitzkohl', 'Stängelkohl', 'Steckrübe', 'Tsa Tsai', 'Weißkohl', 'Wirsing', 'Zierkohl', 'Wurzelgemüse', 'Andine Knollenbohne', 'Arakacha', 'Bayerische Rübe', 'Chayote', 'Echter Sellerie', 'Garten-Rettich', 'Garten-Schwarzwurzel', 'Goabohne', 'Große Klette', 'Haferwurzel', 'Herbstrübe', 'Indische Lotosblume', 'Karotte', 'Kartoffel', 'Knollen-Ziest', 'Knollenbohne', 'Knolliger Kälberkropf', 'Küttiger Rüebli', 'Mairübe', 'Maniok', 'Meerrettich', 'Meerrettichbaum', 'Olluco', 'Pastinak', 'Pfatterer Rübe', 'Radieschen', 'Rote Bete', 'Schlangen-Knöterich', 'Schwarzer Winter-Rettich', 'Speiserübe', 'Steckrübe', 'Süßkartoffel', 'Taro', 'Teltower Rübchen', 'Topinambur', 'Wiesen-Bocksbart', 'Winterrettich', 'Wurzelpetersilie', 'Yacón', 'Yambohne', 'Zuckerwurzel', 'Artischocke', 'Bambus', 'Cardy', 'Dioscorea bulbifera', 'Europäischer Queller', 'Fenchel', 'Fenton’s Special', 'Gelbrote Taglilie', 'Gemeine Nachtkerze', 'Gemeiner Rhabarber', 'Gemüsespargel', 'Glaskin’s Perpetual', 'Holsteiner Blut', 'Indische Lotosblume', 'Kasseler Strünkchen', 'Knollige Kapuzinerkresse', 'Knolliger Sauerklee', 'Linse', 'Moso-Bambus', 'Mungbohne', 'Opuntia ficus-indica', 'Prince Albert (Rhabarber)', 'Raue Stechwinde', 'Timperley Early', 'Turibaum', 'Victoria (Rhabarber)', 'Weg-Malve']
            # get preceding numbers (possibly with decimal separation) if available
            lastchars = self.view.substr(sublime.Region(selection.begin()-20, selection.end()))
            last = re.search("(|(\d+)(\.\d+)?)$", lastchars).group(0)

            m = str(last).split(".")

            if re.search("\d", last) and (
                (len(m) > 1 and (int(m[0]) * int(m[1])) < 1000)
                or (len(m) == 1 and int(m[0]) < 1000)
            ):
                selection = sublime.Region(selection.begin() - len(str(last)), selection.end())
            else:
                # if they wasked for too much lorem, just give 'em one - for their own safety!
                last = 1
            # could give error instead - but who wants to think that much about lorem?
            # else:
            #     print("[ERROR] too much lorem ipsum - try a smaller number")

            m = str(last).split(".")
            paras = int(m[0])

            if len(m) > 1:
                qty = int(m[1])

            for i in list(range(0, paras)):
                from random import choice
                para += choice(words).capitalize() + " "
                for x in list(range(random.randint(int(qty - qty/3)-2, int(qty + qty/3)-2))):
                    para += choice(words) + " "
                para += choice(words) + "."
                if i != paras and paras > 1:
                    para += "\n\n"

            # erase region
            self.view.erase(edit, selection)

            last = self.view.substr(sublime.Region(selection.begin()-1, selection.end()))
            if last == ".":
                para = " " + para

            # insert para before current cursor position
            self.view.insert(edit, selection.begin(), para)

            self.view.end_edit(edit)

