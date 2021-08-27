import sys,sce
class Piranha_Character_BP_BreakNet(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Piranha'
       blueprintPath = '/Game/PrimalEarth/Dinos/Piranha/Piranha_Character_BP_BreakNet.Piranha_Character_BP_BreakNet'
       variants = ['BreakNet']
       fullStatsRaw = [[150, 0.2, 0.27, 0.5, 0], [120, 0.1, 0.1, 0, 0], [250, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1200, 0.1, 0.1, 0, 0.15], None, None, [15, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 1, 0.4], [1, 0, 0.01, 0.284, 0], None, None]
       immobilizedBy = []
       noGender = True
       colors = [{'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Purple', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Purple', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Purple', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Green']}, None, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Purple', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Green']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 8.333333, 'affinityNeeded0': 450, 'affinityIncreasePL': 22.5, 'foodConsumptionBase': 0.001543, 'foodConsumptionMult': 216.0294}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
