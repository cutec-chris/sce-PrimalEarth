import sys,sce
class Baryonyx_Character_BP_Aberrant(sce.Aberration):
   def __init__(self):
       super().__init__(self)
       name = 'Aberrant Baryonyx'
       blueprintPath = '/Game/PrimalEarth/Dinos/Baryonyx/Baryonyx_Character_BP_Aberrant.Baryonyx_Character_BP_Aberrant'
       variants = ['Aberrant']
       fullStatsRaw = [[440, 0.2, 0.27, 0.5, 0], [325, 0.1, 0.1, 0, 0], [400, 0.06, 0, 0.5, 0], [225, 0.1, 0.1, 0, 0], [2250, 0.1, 0.1, 0, 0], None, None, [325, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0.2, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Bear Trap', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 7199.42405, 'eggTempMin': 29, 'eggTempMax': 35, 'maturationTime': 166666.667, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Top Fins', 'colors': ['BigFoot0', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Darker Grey', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green']}, None, None, {'name': 'Top Stripes', 'colors': ['BigFoot5', 'Dark Grey', 'DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Grey', 'Dino Dark Yellow', 'Dino Light Brown', 'Dino Medium Brown']}, {'name': 'Underbelly', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Dino Light Brown', 'Dino Light Yellow', 'Dino Medium Brown', 'Light Grey', 'WolfFur']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 2.5, 'affinityNeeded0': 2500, 'affinityIncreasePL': 100, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.001543, 'foodConsumptionMult': 648.0881}
       TamedBaseHealthMultiplier = 0.96
       displayedStats = 919
