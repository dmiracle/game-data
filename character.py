import uuid
import random

dice = [0, 4, 6, 8, 10, 12]
attributes = {
    'Agility' : 4,
    'Smart' : 4,
    'Spirit': 4,
    'Strength': 4,
    'Vigor': 4
}
skills = {
    'Athletics' : 4,
    'Common Knowledge' : 4,
    'Notice' : 4,
    'Persuasion' : 4,
    'Stealth' : 4,
    'Academics' : 0,
    'Battle' : 0,
    'Boating' : 0,
    'Driving' : 0,
    'Electronics' : 0,
    'Faith' : 0,
    'Fighting' : 0,
    'Focus' : 0,
    'Gambling' : 0,
    'Hacking' : 0,
    'Healing' : 0,
    'Intimidation' : 0,
    'Language' : 0,
    'Occult' : 0,
    'Performance' : 0,
    'Piloting' : 0,
    'Psionics' : 0,
    'Repair' : 0,
    'Research' : 0,
    'Riding' : 0,
    'Science' : 0,
    'Shooting' : 0,
    'Spellcasting' : 0,
    'Survival' : 0,
    'Taunt' : 0,
    'Thievery' : 0,
    'Weird Science' : 0
}
skill_attr = {
    'Academics': 'Smarts',
    'Athletics': 'Agility',
    'Battle': 'Smarts',
    'Boating': 'Agility',
    'Common Knowledge': 'Smarts',
    'Driving': 'Agility',
    'Electronics': 'Smarts',
    'Faith': 'Spirit',
    'Fighting': 'Agility',
    'Focus': 'Spirit',
    'Gambling': 'Smarts',
    'Hacking': 'Smarts',
    'Healing': 'Smarts',
    'Intimidation': 'Spirit',
    'Language': 'Smarts',
    'Notice': 'Smarts',
    'Occult': 'Smarts',
    'Performance': 'Spirit',
    'Persuasion': 'Spirit',
    'Piloting': 'Agility',
    'Psionics': 'Smarts',
    'Repair': 'Smarts',
    'Research': 'Smarts',
    'Riding': 'Agility',
    'Science': 'Smarts',
    'Shooting': 'Agility',
    'Spellcasting': 'Smarts',
    'Stealth': 'Agility',
    'Survival': 'Smarts',
    'Taunt': 'Smarts',
    'Thievery': 'Agility',
    'Weird Science': 'Smarts'
}
hindrances = {
    'All Thumbs': 'm',
    'Anemic': 'm',
    'Arrogant': 'M',
    'Bad Eyes': 'M/m',
    'Bad Luck': 'M',
    'Big Mouth': 'm',
    'Blind': 'M',
    'Bloodthirsty': 'M',
    'Can’t Swim': 'm',
    'Cautious': 'm',
    'Clueless': 'M',
    'Clumsy': 'M',
    'Code of Honor': 'M',
    'Curious': 'M',
    'Death Wish': 'm',
    'Delusional': 'M/m',
    'Doubting Thomas': 'm',
    'Driven': 'M/m',
    'Elderly': 'M',
    'Enemy': 'M/m',
    'Greedy': 'M/m',
    'Habit': 'M/m',
    'Hard of Hearing': 'M/m',
    'Heroic': 'M',
    'Hesitant': 'm',
    'Illiterate': 'm',
    'Impulsive': 'M',
    'Jealous': 'M/m',
    'Loyal': 'm',
    'Mean': 'm',
    'Mild Mannered': 'm',
    'Mute': 'M',
    'Obese': 'm',
    'Obligation': 'M/m',
    'One Arm': 'M',
    'One Eye': 'M',
    'Outsider': 'M/m',
    'Overconfident': 'M',
    'Pacifist': 'M/m',
    'Phobia': 'M/m',
    'Poverty': 'm',
    'Quirk': 'm',
    'Ruthless': 'M/m',
    'Secret': 'M/m',
    'Shamed': 'M/m',
    'Slow': 'M/m',
    'Small': 'm',
    'Stubborn': 'm',
    'Suspicious': 'M/m',
    'Thin Skinned': 'M/m',
    'Tongue-Tied': 'M',
    'Ugly': 'M/m',
    'Vengeful': 'M/m',
    'Vow': 'M/m',
    'Wanted': 'M/m',
    'Yellow': 'M',
    'Young': 'M/m',
    'Alien Form': 'M',
    'Allergy': 'M/m',
    'Dependency': 'M',
    'Dependent': 'M',
    'Distinctive Appearance': 'm',
    'Gimmick': 'M',
    'Monologuer': 'M',
    'Mania': 'M/m',
    'Out Of My League': 'm',
    'Power Negation': 'M',
    'Terminally Ill': 'M',
    'Weakness': 'M/m',
    'Bad Filters': 'M',
    'Bad Rep': 'm',
    'Giri': 'M/m',
    'Magnet': 'M/m',
    'Nano-Infection': 'M/m',
    'Unplugged': 'M',
    'Watched': 'm'
}
edges = {
    'Alertness': 'Novice',
    'Ambidextrous': 'Novice',
    'Arcane Background': 'Novice',
    'Arcane Resistance': 'Novice',
    'Improved Arcane Resistance': 'Novice',
    'Aristocrat': 'Novice',
    'Attractive': 'Novice',
    'Very Attractive': 'Novice',
    'Berserk': 'Novice',
    'Brave': 'Novice',
    'Brawny': 'Novice',
    'Brute': 'Novice',
    'Charismatic': 'Novice',
    'Elan': 'Novice',
    'Fame': 'Novice',
    'Famous': 'Seasoned',
    'Fast Healer': 'Novice',
    'Fleet-Footed': 'Novice',
    'Linguist': 'Novice',
    'Luck': 'Novice',
    'Great Luck': 'Novice',
    'Quick': 'Novice',
    'Rich': 'Novice',
    'Filthy Rich': 'Novice',
    'Block': 'Novice',
    'Improved Block': 'Veteran',
    'Brawler': 'Seasoned',
    'Bruiser': 'Seasoned',
    'Calculating': 'Novice',
    'Combat Reflexes': 'Seasoned',
    'Counterattack': 'Seasoned',
    'Improved Counterattack': 'Veteran',
    'Dead Shot': 'Novice',
    'Dodge': 'Seasoned',
    'Improved Dodge': 'Veteran',
    'Double Tap': 'Seasoned',
    'Extraction': 'Novice',
    'Improved Extraction': 'Seasoned',
    'Feint': 'Novice',
    'First Strike': 'Novice',
    'Improved First Strike': 'Heroic',
    'Free Runner': 'Novice',
    'Frenzy': 'Seasoned',
    'Improved Frenzy': 'Veteran',
    'Giant Killer': 'Veteran',
    'Hard to Kill': 'Novice',
    'Harder to Kill': 'Veteran',
    'Improvisational Fighter': 'Seasoned',
    'Iron Jaw': 'Novice',
    'Killer Instinct': 'Seasoned',
    'Level Headed': 'Seasoned',
    'Improved Level Headed': 'Seasoned',
    'Marksman': 'Seasoned',
    'Martial Artist': 'Novice',
    'Martial Warrior': 'Seasoned',
    'Mighty Blow': 'Novice',
    'Nerves of Steel': 'Novice',
    'Improved Nerves of Steel': 'Novice',
    'No Mercy': 'Seasoned',
    'Rapid Fire': 'Seasoned',
    'Improved Rapid Fire': 'Veteran',
    'Rock and Roll!': 'Seasoned',
    'Steady Hands': 'Novice',
    'Sweep': 'Novice',
    'Improved Sweep': 'Veteran',
    'Trademark Weapon': 'Novice',
    'Improved Trademark Weapon': 'Seasoned',
    'Two-Fisted': 'Novice',
    'Two-Gun Kid': 'Novice',
    'Command': 'Novice',
    'Command Presence': 'Seasoned',
    'Fervor': 'Veteran',
    'Hold the Line': 'Seasoned',
    'Inspire': 'Seasoned',
    'Natural Leader': 'Veteran',
    'Tactician': 'Seasoned',
    'Master Tactician': 'Veteran',
    'Artificer': 'Seasoned',
    'Channeling': 'Seasoned',
    'Concentration': 'Seasoned',
    'Extra Effort': 'Seasoned',
    'Gadgeteer': 'Seasoned',
    'Holy/Unholy Warrior': 'Seasoned',
    'Mentalist': 'Seasoned',
    'New Powers': 'Novice',
    'Power Points': 'Novice',
    'Power Surge': 'Novice',
    'Rapid Recharge': 'Seasoned',
    'Improved Rapid Recharge': 'Veteran',
    'Soul Drain': 'Seasoned',
    'Wizard': 'Seasoned',
    'Ace': 'Novice',
    'Acrobat': 'Novice',
    'Assassin': 'Novice',
    'Investigator': 'Novice',
    'Jack-Of-All-Trades': 'Novice',
    'McGyver': 'Novice',
    'Mr. Fix It': 'Novice',
    'Scholar': 'Novice',
    'Soldier': 'Novice',
    'Thief': 'Novice',
    'Woodsman': 'Novice',
    'Bolster': 'Novice',
    'Common Bond': 'Novice',
    'Connections': 'Novice',
    'Humiliate': 'Novice',
    'Menacing': 'Novice',
    'Provoke': 'Novice',
    'Rabble-Rouser': 'Seasoned',
    'Reliable': 'Novice',
    'Retort': 'Novice',
    'Streetwise': 'Novice',
    'Strong Willed': 'Novice',
    'Iron Will': 'Novice',
    'Work the room': 'Novice',
    'Work the Crowd': 'Seasoned',
    'Beast Bond': 'Novice',
    'Champion': 'Novice',
    'Chi': 'Veteran',
    'Danger Sense': 'Novice',
    'Healer': 'Novice',
    'Liquid Courage': 'Novice',
    'Scavenger': 'Novice',
    'Followers': 'Legendary',
    'Professional': 'Legendary',
    'Expert': 'Legendary',
    'Master': 'Legendary',
    'Sidekick': 'Legendary',
    'Tough As Nails': 'Legendary',
    'Weapon Master': 'Legendary',
    'Master of Arms': 'Legendary',
    'Back from the Dead': 'Novice',
    'Augmented Warrior': 'Novice',
    'Gun Fu': 'Novice',
    'Enlightened Gun Fu': 'Seasoned',
    'Master Gun Fu': 'Veteran',
    'Pack Fighting': 'Novice',
    'Batch Edit': 'Novice',
    'Cage Breaker': 'Heroic',
    'Cutter': 'Seasoned',
    'Cleaner': 'Novice',
    'Cybermonk': 'Novice',
    'Hacker': 'Novice',
    'Survivalist': 'Novice',
    'Alternate Identity': 'Novice',
    'Reputation': 'Novice',
    'Street Samurai': 'Novice',
    'Augmented Master': 'Veteran',
    'Cyber Tolerance': 'Novice',
    'Improved Cyber Tolerance': 'Veteran',
    'Miracle Worker': 'Seasoned'
}

class Character:
    def __init__(self, name):
        self.name = name
        self.uid = uuid.uuid4()
        self.attributes = attributes
        self.attribute_incs = 0
        self.skills = skills
        self.skill_incs = 0
        self.hindrances = {}
        self.hind_pts = 0
        self.edges = []
        self.advancement = 0
        self.derived = self.get_derived()
        self.money = 20000
        self.inventory = {}
    
    def get_derived(self):
        return {
            'pace' : 6,
            'parry' :  2 + self.skills['Fighting']/2,
            'toughness' : 2 + self.attributes['Vigor']/2
        }

    def get_rank(self):
        ranks = ['Novice', 'Seasoned', 'Veteran', 'Heroic', 'Legendary']
        return ranks[min(self.advancement//4, len(ranks) - 1)]

    def add_advancement(self, lvls=1):
        self.advancement += lvls

    def add_attribute(self, attr):
        self.attribute_incs += 1
        lvl = dice.index(self.attributes[attr])
        if lvl >= len(dice) - 1:
            print("at max")
            # throw exception
        else:
            self.attributes[attr] = dice[lvl + 1]
    
    def add_skill(self, sk):
        try:
            lvl = dice.index(self.skills[sk])
            attr = skill_attr[sk]
            attr_lvl = dice.index(self.attributes[attr])
            if lvl >= len(dice) - 1:
                raise ValueError('Exceeded max value for skill')
            elif lvl <= attr_lvl:
                self.skill_incs += 1
            else:
                self.skill_incs += 2
            self.skills[sk] = dice[lvl + 1]
        except Exception as e:
            return e


    def add_hindrance(self, hindrance, lvl='m'):
        try:
            if lvl not in ['M','m']:
                raise ValueError('Only M or m allowed for hindrance level')
            val = hindrances[hindrance]
            if val == 'M':
                self.hind_pts += 2
            elif val == 'm':
                self.hind_pts += 1
            else:
                if lvl == 'M':
                    self.hind_pts += 2
                elif lvl == 'm':
                    self.hind_pts += 1
                else:
                    raise ValueError('You should not have come here')
        except KeyError as e:
            return "Hindrance not found"
        except Exception as e:
            return e

    def add_edge(self):
        return 0

    def add_item(self, item, cost, *args):
        try:
            if cost > self.money:
                raise ValueError('Not enough money')
            else:
                self.money -= cost
            val = [cost] + list(args)
            print(val)
            self.inventory.update({item: val})
        except Exception as e:
            return e

    def get_all_hindrances(self):
        return hindrances

    def get_random_hindrances(self):
        my_hindrances = {}
        hpts = 0
        hind_starter_combos = [
            [],
            ['m'],
            ['m', 'm'],
            ['m', 'm', 'm'],
            ['m', 'm', 'm', 'm'],
            ['M'],
            ['M', 'm'],     
            ['M', 'm', 'm'],
            ['M', 'M']       
        ]
        h_choice = random.choice(hind_starter_combos)
        for rank in h_choice:
            hind_list_tmp = [k for k,v in hindrances.items() if v.find(rank) != -1]
            hindrance = random.choice(hind_list_tmp)
            my_hindrances.update({ hindrance: rank })
            hpts += (1 if rank == 'm' else 2)
        return my_hindrances, hpts

    def get_random_edges(self):
        if self.hind_pts//2 >= 2:
            print('Herp')
            # rans one or 2 edges
        elif self.hind_pts//2 >= 1:
            print('Derp')
        return 0

    def generate_random_character(self):
        self.hindrances, self.hind_pts = self.get_random_hindrances()
        