import sys,sce
class Bee_Queen_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Giant Queen Bee'
       blueprintPath = '/Game/PrimalEarth/Dinos/Bee/Bee_Queen_Character_BP.Bee_Queen_Character_BP'
       isFlyer = True
       fullStatsRaw = [[80, 0, 0, 0.5, 0], [200, 0, 0, 0, 0], [400, 0.06, 0, 0.5, 0], [150, 0, 0, 0, 0], [800, 0, 0, 0, 0], None, None, [150, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = []
       noGender = True
       colors = [{'name': 'Unknown', 'colors': ['DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1']}, None, {'name': 'Unknown', 'colors': ['DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1']}, {'name': 'Unknown', 'colors': ['DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1']}, {'name': 'Unknown', 'colors': ['DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1']}, {'name': 'Unknown', 'colors': ['DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1']}]
       taming = {'nonViolent': True, 'violent': False, 'tamingIneffectiveness': 1.333333, 'affinityNeeded0': 2000, 'affinityIncreasePL': 22.5, 'wakeAffinityMult': 1.6, 'wakeFoodDeplMult': 2.5, 'foodConsumptionBase': 0.001929, 'foodConsumptionMult': 420}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
