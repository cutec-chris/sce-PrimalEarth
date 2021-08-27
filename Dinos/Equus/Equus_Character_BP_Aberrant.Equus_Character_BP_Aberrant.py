import sys,sce
class Equus_Character_BP_Aberrant(sce.Aberration):
   def __init__(self):
       super().__init__(self)
       name = 'Aberrant Equus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Equus/Equus_Character_BP_Aberrant.Equus_Character_BP_Aberrant'
       variants = ['Aberrant']
       fullStatsRaw = [[240, 0.2, 0.27, 0.5, 0], [560, 0.1, 0.1, 0, 0], [420, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1500, 0.1, 0.1, 0, 0], None, None, [350, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.0175, 0.2, 0], None, None]
       immobilizedBy = ['Bola', 'Bear Trap', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 28571.4286, 'incubationTime': 0, 'maturationTime': 166666.667, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'BodyMain', 'colors': ['Black', 'Dark Grey', 'DarkWolfFur', 'Dino Dark Brown', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Medium Brown', 'DragonBase0', 'Light Brown', 'Light Grey', 'NearBlack', 'NearWhite']}, None, None, None, {'name': 'Stripes', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey', 'NearWhite']}, {'name': 'Underbelly and Highlights', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey', 'NearWhite']}]
       taming = {'nonViolent': True, 'violent': False, 'tamingIneffectiveness': 0.4, 'affinityNeeded0': 3600, 'affinityIncreasePL': 180, 'wakeAffinityMult': 1.6, 'wakeFoodDeplMult': 2, 'foodConsumptionBase': 0.001929, 'foodConsumptionMult': 432.0028}
       boneDamageAdjusters = {'c_jaw': 2, 'c_head': 2}
       TamedBaseHealthMultiplier = 0.96
       displayedStats = 927
