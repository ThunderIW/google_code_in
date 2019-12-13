import time
import winsound
global character_information
character_information = {}
winsound.PlaySound('Eon - Lucid (Synthwave).wav',winsound.SND_LOOP + winsound.SND_ASYNC)


def main_game():
    print(
        'welcome to the world of new Canada->{}. in this world Canada has become a massive superpower with high tech military equipment'.format(
            character_information['Player name']))
    if character_information['Class'] == 'Medic':
        print('You are a Medic who works for the medical company in new Canada where you')
    if character_information['Class'] == 'Hacker':
        print('You are a hacker')
    if character_information['Class'] == 'Ranger':
        print('You are a Ranger')
    if character_information['Class'] == 'Gunslinger':
        print('You are a Gunslinger')


def character_confirm():
    print('Your character information are as follow')
    for key, value in character_information.items():
        print('********************')
        print(key, '->', value)
        print('********************')

    confirm = input('is everything correct->')
    if confirm.upper() == 'YES':
        main_game()

    if confirm.upper() == 'NO':
        print('ALright lets us fix that')
        print('Here is your character information->{}'.format(character_information.keys()))
        ItemToRemove = input(str('What would like to remove->'))
        if str(ItemToRemove) in character_information:
            del character_information[str(ItemToRemove)]
        print('The updated list->{}'.format(character_information))

        fix = input(
            'If you want to change your Class role type C\nIf you want to change your name type N\nI you want to change your skills type S\n-->')

        if fix.upper() == 'C':
            character_making()
        if fix.upper() == 'N':
            character_name()
        if fix.upper() == 'S':
            skills()


def intro():
    ReadyToPlay = input('welcome user to my computer scince IA, woud you like to play-->')
    if ReadyToPlay.upper() == 'YES':
        print('welcome player')
        character_making()
    if ReadyToPlay.upper() == 'NO':
        print('Thank you for dropping by hope you come back')


def skills():
    traits = {}
    Traits = ['strength', 'Perception', 'Endurance', 'Intelligence', 'Agility']
    n = 0
    num_of_points = 15
    num_strength = 0
    num_Perception = 0
    num_Endurance = 0
    num_Intelligence = 0
    num_Agility = 0
    print('You have a total of->{}'.format(num_of_points))
    while num_of_points != 0:
        skill_selection = input(
            'Cuurent trait selected->{} and you have->{} skill points remaining ,type D  to add points to the skill->'.format(
                Traits[n], num_of_points))

        if skill_selection.upper() == 'D':

            if Traits[n].upper() == "STRENGTH":
                num_strength += 1
                print('Point added to strength->{}'.format(num_strength))
                num_of_points -= 1
                traits['Strength'] = num_strength

            if Traits[n].upper() == 'PERCEPTION':
                num_Perception += 1
                print('Point added to Perception->{}'.format(num_Perception))
                num_of_points -= 1
                traits['Perception'] = num_Perception

            if Traits[n].upper() == 'ENDURANCE':
                num_Endurance += 1
                print('Point added to Endurance->{}'.format(num_Endurance))
                num_of_points -= 1
                traits['Endurance'] = num_Endurance

            if Traits[n].upper() == 'INTELLIGENCE':
                num_Intelligence += 1
                print('Point added to Intelligence->{}'.format(num_Intelligence))
                num_of_points -= 1
                traits['Intelligence'] = num_Intelligence

            if Traits[n].upper() == 'AGILITY':
                num_Agility += 1
                print('Point added to Agility->{}'.format(num_Agility))
                num_of_points -= 1
                traits['Agility'] = num_Agility

        n += 1
        if n == len(Traits):
            n = 0

    print('Your skills are as followed->{}'.format(traits))
    time.sleep(1)
    character_information['Skills'] = traits
    character_confirm()


def character_name():
    final_name = str()
    letters_uppercase = ['A', "B", 'C', "D", "E", "F", 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'Q', 'R', 'S', 'T',
                         'U', 'V', 'W', 'X', 'Y', 'Z']
    letter_lowecase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'q', 'r']
    final_name = []
    n = 0
    while True:
        choice = input(
            'Current letter-->{},press E when your happy with your chosen letter\nType D if your happy with your character name->'.format(
                letters_uppercase[n]))
        if choice.upper() == 'E':
            final_name.append(letters_uppercase[n])
            name = ''.join(final_name)
            print('current name->{}'.format(name))
        if choice.upper() == 'D':
            break
        n += 1
        if n == len(letters_uppercase):
            n = 0
    time.sleep(1)
    character_information['Player name'] = name
    skills()
    # character_confirm()


def character_making():
    character_class = ['Gunslinger', "Hacker", 'Medic', 'Ranger', 'Cybernetics Investigator',
                       'Extra-dimensional Investigator', 'Neutron Cyborg Assassin']
    n = 0
    while True:
        character_slection = input(
            'Your character role is:{} if your happy with your choice type D\nLike to hear more information type Info-->'.format(
                character_class[n]))

        if character_slection.upper() == "D":
            character_role = character_class[n]
            break

        if character_slection.upper() == 'WEEB':
            print('New class unlocked->Weeb master')
            character_class.append('Weeb Master')
        if character_slection.upper() == 'TIME IS EVERYTHING':
            print('New Class unlocked->Time Doctor')
            character_class.append('Time Doctor')

        if character_slection.upper() == 'INFO':
            if character_class[n] == 'Gunslinger':
                time.sleep(1)
                print('TEST infor for Gunslinger')
            if character_class[n] == 'Hacker':
                print('Test info for Hacker')
                time.sleep(1)
            if character_class[n] == 'Medic':
                print('Test info for Medic')
                time.sleep(1)
            if character_class[n] == 'Ranger':
                print('Test info for Ranger')
                time.sleep(1)
            if character_class[n] == 'Weeb Master':
                print('Test info for Weeb master')
            if character_class[n] == "Cybernetics Investigator":
                print('TEST info for Cybernetics Investigator')
            if character_class[n] == 'Extra-dimensional Investigator':
                print('TEST info for Extra-dimensional Investigator')
            if character_class[n] == 'Neutron Cyborg Assassin':
                print('TEST INFO FOR Neutron Cyborg Assassin')
            if character_class[n] == 'Time Doctor':
                print('TEST INFO FOR Time Doctor')
        n += 1
        if n == len(character_class):
            n = 0

    print('Outside')
    print('Your character_class is:{}'.format(character_role))
    time.sleep(1)
    character_information['Class'] = character_role
    character_name()


intro()