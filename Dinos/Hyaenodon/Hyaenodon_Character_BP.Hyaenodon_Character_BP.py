import sys,sce
class Hyaenodon_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Hyaenodon'
       blueprintPath = '/Game/PrimalEarth/Dinos/Hyaenodon/Hyaenodon_Character_BP.Hyaenodon_Character_BP'
       fullStatsRaw = [[175, 0.2, 0.27, 0.66, 0], [260, 0.1, 0.1, 0, 0], [450, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1200, 0.1, 0.1, 0, 0.15], None, None, [170, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.4, 0.35], [1, 0, 0.01, 0.3, 0], None, None]
       immobilizedBy = ['Bola', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 14285.7143, 'incubationTime': 0, 'maturationTime': 166666.667, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body Main', 'colors': ['BigFoot0', 'BigFoot5', 'Black', 'Dark Grey', 'DarkWolfFur', 'Dino Dark Brown', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Medium Brown', 'DragonBase0', 'Light Grey', 'WolfFur']}, None, None, None, {'name': 'Body Highlights and spots', 'colors': ['BigFoot0', 'BigFoot5', 'Black', 'Dark Grey', 'DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Medium Brown', 'DragonBase0', 'Light Grey', 'WolfFur']}, {'name': 'Underbelly', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey', 'WolfFur']}]
       taming = {'nonViolent': True, 'violent': False, 'tamingIneffectiveness': 1.875, 'affinityNeeded0': 6000, 'affinityIncreasePL': 80, 'wakeAffinityMult': 1.6, 'wakeFoodDeplMult': 2, 'foodConsumptionBase': 0.001543, 'foodConsumptionMult': 288.0392}
       boneDamageAdjusters = {'Cnt_Head_JNT_SKL': 3, 'Cnt_Neck_002_JNT_SKL': 3, 'Cnt_Neck_000_JNT_SKL': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
