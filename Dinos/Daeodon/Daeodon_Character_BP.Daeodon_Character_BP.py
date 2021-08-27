import sys,sce
class Daeodon_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Daeodon'
       blueprintPath = '/Game/PrimalEarth/Dinos/Daeodon/Daeodon_Character_BP.Daeodon_Character_BP'
       fullStatsRaw = [[900, 0.2, 0.27, 0.5, 0], [250, 0.1, 0.1, 0, 0], [800, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [2500, 0.1, 0.1, 0, 0.15], None, None, [400, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.4, 0.35], [1, 0, 0.01, 0.3, 0], None, None]
       immobilizedBy = ['Bola', 'Bear Trap', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 28571.4286, 'incubationTime': 0, 'maturationTime': 175438.596, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Underbelly', 'colors': ['BigFoot0', 'BigFoot5', 'Black', 'Dino Albino', 'Dino Light Brown', 'Dino Medium Brown', 'WolfFur']}, None, {'name': 'Top Highlights', 'colors': ['BigFoot0', 'BigFoot5', 'Black', 'DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Medium Brown', 'DragonBase0', 'NearBlack']}, None, None, {'name': 'Body Main', 'colors': ['BigFoot0', 'Black', 'Dark Grey', 'DarkWolfFur', 'Dino Albino', 'Dino Dark Brown', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Yellow', 'Dino Medium Brown', 'DragonBase0', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.0625, 'affinityNeeded0': 4500, 'affinityIncreasePL': 245, 'torporDepletionPS0': 1.8, 'foodConsumptionBase': 0.01, 'foodConsumptionMult': 288.0392}
       boneDamageAdjusters = {'c_head': 3, 'c_jaw': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
