import sys,sce
class FlyingAnt_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Titanomyrma Soldier'
       blueprintPath = '/Game/PrimalEarth/Dinos/Ant/FlyingAnt_Character_BP.FlyingAnt_Character_BP'
       isFlyer = True
       fullStatsRaw = [[50, 0.2, 0.27, 0.5, 0], [100, 0.1, 0.1, 0, 0], [75, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [900, 0.1, 0.1, 0, 0], None, None, [50, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = []
       noGender = True
       colors = [{'name': 'Unknown', 'colors': ['DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1']}, None, {'name': 'Unknown', 'colors': ['DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1']}, {'name': 'Unknown', 'colors': ['DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1']}, {'name': 'Unknown', 'colors': ['DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1']}, {'name': 'Unknown', 'colors': ['DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 0.666666, 'affinityNeeded0': 900, 'affinityIncreasePL': 45, 'foodConsumptionBase': 0.001736, 'foodConsumptionMult': 864.0553}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
