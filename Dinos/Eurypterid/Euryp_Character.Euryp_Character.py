import sys,sce
class Euryp_Character(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Eurypterid'
       blueprintPath = '/Game/PrimalEarth/Dinos/Eurypterid/Euryp_Character.Euryp_Character'
       fullStatsRaw = [[160, 0.2, 0.27, 0.5, 0], [100, 0.1, 0.1, 0, 0], [50, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [450, 0.1, 0.1, 0, 0], None, None, [150, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = []
       noGender = True
       colors = [{'name': 'Unknown', 'colors': ['DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Unknown', 'colors': ['DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1']}, {'name': 'Unknown', 'colors': ['DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1']}, {'name': 'Unknown', 'colors': ['DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1']}, {'name': 'Unknown', 'colors': ['DarkWolfFur', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Medium Brown', 'DragonBase0', 'DragonBase1']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 1.333333, 'affinityNeeded0': 450, 'affinityIncreasePL': 22.5, 'foodConsumptionBase': 0.001736, 'foodConsumptionMult': 864.0553}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
