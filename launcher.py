from tkinter import *
import info
import names
root = Tk()



ProgenitorChapterLab=Label(root, text = 'Progenitor Chapter')
ProgenitorChapterTXT=Entry(root, width = 30)

ReasonofFoundingLab=Label(root, text = 'Reason of Founding')
ReasonofFoundingTXT=Entry(root, width = 30)

PurityLab=Label(root, text = 'Purity')
PurityTXT=Entry(root, width = 30)

DemeanourLab=Label(root, text = 'Demeanour')
DemeanourTXT=Entry(root, width = 30)

FlawLab=Label(root, text = 'Flaw')
FlawTXT=Entry(root, width = 30)

CharacteristicModifiersLab=Label(root, text = 'Characteristic Modifiers')
CharacteristicModifiersTXT=Entry(root, width = 30)



ChapterOrganisationLab=Label(root, text = 'Chapter Organisation')
ChapterOrganisationTXT=Entry(root, width = 30)

CombatDoctrineLab=Label(root, text = 'Combat Doctrine')
CombatDoctrineTXT=Entry(root, width = 30)

SpecialEquipmentLab=Label(root, text = 'Special Equipment')
SpecialEquipmentTXT=Entry(root, width = 30)

SpecialityRestrictionsLab=Label(root, text = 'Speciality Restrictions')
SpecialityRestrictionsTXT=Entry(root, width = 30)

beliefsLab=Label(root, text = 'Beliefs')
beliefsTXT=Entry(root, width = 30)

currentStatusLab=Label(root, text = 'Current Status')
currentStatusTXT=Entry(root, width = 30)


DateofOriginLab=Label(root, text = 'Date of Origin')
DateofOriginTXT=Text (root, height = 5, width = 30, wrap = WORD)

DeficiencyLab=Label(root, text = 'Deficiency')
DeficiencyTXT=Text (root, height = 5, width = 30, wrap = WORD)

FigureofLegendLab=Label(root, text = 'Figure of Legend')
FigureofLegendTXT=Text (root, height = 5, width = 30, wrap = WORD)

DeedofLegendLab=Label(root, text = 'Deed of Legend')
DeedofLegendTXT=Text (root, height = 4, width = 30, wrap = WORD)

HomeWorldLab=Label(root, text = 'Home World')
HomeWorldTXT=Text (root, height = 6, width = 30, wrap = WORD)

SoloAbilitiesLab=Label(root, text = 'Solo Abilities')
SoloAbilitiesTXT=Text (root, height = 15, width = 30, wrap = WORD)

SquadAbilitiesLab=Label(root, text = 'Squad Abilities')
SquadAbilitiesTXT=Text (root, height = 6, width = 30, wrap = WORD)

chapterFriendsLab=Label(root, text = 'Chapter Friends')
chapterFriendsTXT=Text (root, height = 5, width = 30, wrap = WORD)

chapterEnemiesLab=Label(root, text = 'Chapter Enemies')
chapterEnemiesTXT=Text (root, height = 5, width = 30, wrap = WORD)

generateBTN=Button(root, text ='Create Chapter', command = lambda: generate_chapter())



chapterNameLab=Label(root, text = 'Possible names:')
chapterName1=Entry(root, width = 35)
chapterName2=Entry(root, width = 35)
chapterName3=Entry(root, width = 35)
chapterName4=Entry(root, width = 35)
chapterName5=Entry(root, width = 35)
chapterName6=Entry(root, width = 35)

generateNameBTN=Button(root, text ='Generate Names', command = lambda: create_names())

def create_names():
    name1 = names.create_name(info.Chapter.progenitor)
    name2 = names.create_name(info.Chapter.progenitor)
    name3 = names.create_name(info.Chapter.progenitor)
    name4 = names.create_name(info.Chapter.progenitor)
    name5 = names.create_name(info.Chapter.progenitor)
    name6 = names.create_name(info.Chapter.progenitor)
    chapterName1.delete(0, END)
    chapterName2.delete(0, END)
    chapterName3.delete(0, END)
    chapterName4.delete(0, END)
    chapterName5.delete(0, END)
    chapterName6.delete(0, END)
    chapterName1.insert(0,name1)
    chapterName2.insert(0,name2)
    chapterName3.insert(0,name3)
    chapterName4.insert(0,name4)
    chapterName5.insert(0,name5)
    chapterName6.insert(0,name6)
    
    


def generate_chapter():
    ReasonofFoundingTXT.delete(0, END)
    DateofOriginTXT.delete('1.0', END)
    ProgenitorChapterTXT.delete(0, END)
    PurityTXT.delete(0, END)
    DemeanourTXT.delete(0, END)
    DeficiencyTXT.delete('1.0', END)
    FlawTXT.delete(0, END)
    CharacteristicModifiersTXT.delete(0, END)
    FigureofLegendTXT.delete('1.0', END)
    DeedofLegendTXT.delete('1.0', END)
    HomeWorldTXT.delete('1.0', END)
    ChapterOrganisationTXT.delete(0, END)
    CombatDoctrineTXT.delete(0, END)
    SoloAbilitiesTXT.delete('1.0', END)
    SquadAbilitiesTXT.delete('1.0', END)
    SpecialityRestrictionsTXT.delete(0, END)
    SpecialEquipmentTXT.delete(0, END)
    beliefsTXT.delete(0, END)
    currentStatusTXT.delete(0, END)
    chapterFriendsTXT.delete('1.0', END)
    chapterEnemiesTXT.delete('1.0', END)

    reasonFounding = info.origin()
    ReasonofFoundingTXT.insert(0, reasonFounding)

    dateOrigin = info.date_of_origin()
    DateofOriginTXT.insert(1.0, dateOrigin)

    progenitorChapter = info.progenitor()
    ProgenitorChapterTXT.insert(0, progenitorChapter)

    purity = info.purity()
    PurityTXT.insert(0,purity[0])

    demeanour = info.demeanour()
    DemeanourTXT.insert(0, demeanour)

    deficiency = info.deficiency()
    DeficiencyTXT.insert(1.0, deficiency)

    flaw = info.flaw()
    FlawTXT.insert(0, flaw)

    characteristics = info.characteristic_modifier()
    CharacteristicModifiersTXT.insert(0, characteristics)

    legend = info.figure_of_legend()
    FigureofLegendTXT.insert(1.0, legend)

    deed = info.deed_of_legend()
    DeedofLegendTXT.insert(1.0, deed)

    home_world = info.home_world()
    HomeWorldTXT.insert(1.0, home_world)

    organisation = info.chapter_organisation()
    ChapterOrganisationTXT.insert(0, organisation)

    combatDoctrine = info.combat_doctrine()
    CombatDoctrineTXT.insert(0, combatDoctrine)

    soloAbilities = info.solo_abilities()
    SoloAbilitiesTXT.insert(1.0, soloAbilities)

    squadAbilities = info.squad_mode_abilities()
    SquadAbilitiesTXT.insert(1.0, squadAbilities)

    if organisation == "Unique Organisation":
        restrictions = info.speciality_restrictions()
    else:
        restrictions = "None"
    SpecialityRestrictionsTXT.insert(0, str(restrictions)) ##

    if organisation == "Unique Organisation" or organisation == "Divergent Chapter":
        equipment = info.special_equipment()
    else:
        equipment = "Standard"
    SpecialEquipmentTXT.insert(0, equipment)

    beliefs = info.chapter_beliefs()
    beliefsTXT.insert(0, beliefs)

    status = info.current_status()
    currentStatusTXT.insert(0, status)

    friends = info.chapter_friends()
    chapterFriendsTXT.insert(1.0, friends)

    enemies = info.chapter_enemies()
    chapterEnemiesTXT.insert(1.0, enemies)    
    


ReasonofFoundingLab.grid(row=0,column=0)
ReasonofFoundingTXT.grid(row=1,column=0)

DateofOriginLab.grid(row=2,column=0)
DateofOriginTXT.grid(row=3,column=0)

ProgenitorChapterLab.grid(row=4,column=0)
ProgenitorChapterTXT.grid(row=5,column=0)

PurityLab.grid(row=6,column=0)
PurityTXT.grid(row=7,column=0)

DemeanourLab.grid(row=8,column=0)
DemeanourTXT.grid(row=9,column=0)

DeficiencyLab.grid(row=10,column=0)
DeficiencyTXT.grid(row=11,column=0)

FlawLab.grid(row=12,column=0)
FlawTXT.grid(row=13,column=0)

generateBTN.grid(row=14,column=0)
##
CharacteristicModifiersLab.grid(row=0,column=1)
CharacteristicModifiersTXT.grid(row=1,column=1)

FigureofLegendLab.grid(row=2,column=1)
FigureofLegendTXT.grid(row=3,column=1)

DeedofLegendLab.grid(row=4,column=1)
DeedofLegendTXT.grid(row=5,column=1)

HomeWorldLab.grid(row=6,column=1)
HomeWorldTXT.grid(row=7,column=1)


ChapterOrganisationLab.grid(row=8,column=1)
ChapterOrganisationTXT.grid(row=9,column=1)

CombatDoctrineLab.grid(row=10,column=1)
CombatDoctrineTXT.grid(row=11,column=1)

SoloAbilitiesLab.grid(row=12,column=1)
SoloAbilitiesTXT.grid(row=13,column=1)
##

SquadAbilitiesLab.grid(row=0,column=2)
SquadAbilitiesTXT.grid(row=1,column=2)

SpecialityRestrictionsLab.grid(row=2,column=2)
SpecialityRestrictionsTXT.grid(row=3,column=2)

SpecialEquipmentLab.grid(row=4,column=2)
SpecialEquipmentTXT.grid(row=5,column=2)

beliefsLab.grid(row=6,column=2)
beliefsTXT.grid(row=7,column=2)


currentStatusLab.grid(row=8,column=2)
currentStatusTXT.grid(row=9,column=2)

chapterFriendsLab.grid(row=10,column=2)
chapterFriendsTXT.grid(row=11,column=2)

chapterEnemiesLab.grid(row=12,column=2)
chapterEnemiesTXT.grid(row=13,column=2)


chapterNameLab.grid(row=0,column=3)
chapterName1.grid(row=1,column=3)
chapterName2.grid(row=2,column=3)
chapterName3.grid(row=3,column=3)
chapterName4.grid(row=4,column=3)
chapterName5.grid(row=5,column=3)
chapterName6.grid(row=6,column=3)
generateNameBTN.grid(row=7,column=3)




root.mainloop()



