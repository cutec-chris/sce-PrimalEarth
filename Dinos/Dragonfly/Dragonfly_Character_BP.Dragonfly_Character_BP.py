import sys,sce
class Dragonfly_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Meganeura'
       blueprintPath = '/Game/PrimalEarth/Dinos/Dragonfly/Dragonfly_Character_BP.Dragonfly_Character_BP'
       isFlyer = True
       fullStatsRaw = [[45, 0.2, 0.27, 0.5, 0], [100, 0.1, 0.1, 0, 0], [100, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [450, 0.1, 0.1, 0, 0], None, None, [50, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = []
       noGender = True
       colors = [{'name': 'Unknown', 'colors': ['Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Green']}, None, {'name': 'Unknown', 'colors': ['Black', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Blue', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Medium Green']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 8.333333, 'affinityNeeded0': 450, 'affinityIncreasePL': 22.5, 'foodConsumptionBase': 0.001736, 'foodConsumptionMult': 864.0553}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
