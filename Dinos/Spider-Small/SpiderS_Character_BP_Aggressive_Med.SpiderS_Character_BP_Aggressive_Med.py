import sys,sce
class SpiderS_Character_BP_Aggressive_Med(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Araneo'
       blueprintPath = '/Game/PrimalEarth/Dinos/Spider-Small/SpiderS_Character_BP_Aggressive_Med.SpiderS_Character_BP_Aggressive_Med'
       variants = ['Beta', 'Boss']
       fullStatsRaw = [[300, 0.2, 0.135, 0.5, 0], [100, 0.1, 0.1, 0, 0], [80, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [900, 0.1, 0.1, 0, 0], None, None, [100, 0.02, 0.08, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0.67, 0], None, None]
       altBaseStats = {'0': 150}
       immobilizedBy = []
       breeding = {'gestationTime': 0, 'incubationTime': 5142.44575, 'eggTempMin': 4, 'eggTempMax': 12, 'maturationTime': 90090.0901, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, None, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}]
       taming = {'nonViolent': True, 'violent': False, 'tamingIneffectiveness': 4.166667, 'affinityNeeded0': 4000, 'affinityIncreasePL': 120, 'wakeAffinityMult': 1, 'wakeFoodDeplMult': 2, 'foodConsumptionBase': 0.001736, 'foodConsumptionMult': 864.0553}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
