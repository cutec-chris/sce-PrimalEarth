import sys,sce
class Ant_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Titanomyrma Drone'
       blueprintPath = '/Game/PrimalEarth/Dinos/Ant/Ant_Character_BP.Ant_Character_BP'
       fullStatsRaw = [[35, 0.2, 0.27, 0.5, 0], [100, 0.1, 0.1, 0, 0], [50, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [450, 0.1, 0.1, 0, 0], None, None, [150, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = []
       noGender = True
       colors = [{'name': 'Unknown', 'colors': ['DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1']}, None, {'name': 'Unknown', 'colors': ['DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1']}, {'name': 'Unknown', 'colors': ['DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1']}, {'name': 'Unknown', 'colors': ['DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1']}, {'name': 'Unknown', 'colors': ['DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 1.333333, 'affinityNeeded0': 450, 'affinityIncreasePL': 22.5, 'foodConsumptionBase': 0.001736, 'foodConsumptionMult': 864.0553}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
