import sys,sce
class Thylacoleo_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Thylacoleo'
       blueprintPath = '/Game/PrimalEarth/Dinos/Thylacoleo/Thylacoleo_Character_BP.Thylacoleo_Character_BP'
       fullStatsRaw = [[700, 0.2, 0.189, 0.5, 0], [400, 0.1, 0.1, 0, 0], [700, 0.06, 0, 0.5, 0], [200, 0.1, 0.1, 0, 0], [1500, 0.1, 0.1, 0, 0.15], None, None, [400, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.4, 0.35], [1, 0, 0.01, 0.3, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Bear Trap', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 15037.594, 'incubationTime': 0, 'maturationTime': 175438.596, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Main Body', 'colors': ['Black', 'Dark Grey', 'DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1', 'Light Brown', 'Light Grey', 'Light Orange']}, None, None, None, {'name': 'Fur Highlights', 'colors': ['Dark Grey', 'DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Darker Grey', 'Dino Light Orange', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1', 'DragonFire', 'NearBlack']}, {'name': 'Stripes and Belly', 'colors': ['BigFoot4', 'Black', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey', 'WolfFur']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 3.125, 'affinityNeeded0': 2250, 'affinityIncreasePL': 60, 'torporDepletionPS0': 1.85, 'foodConsumptionBase': 0.001543, 'foodConsumptionMult': 288.0392}
       boneDamageAdjusters = {'Head': 1.5, 'Jaw': 1.5}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
