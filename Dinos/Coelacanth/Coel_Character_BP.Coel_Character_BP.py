import sys,sce
class Coel_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Coelacanth'
       blueprintPath = '/Game/PrimalEarth/Dinos/Coelacanth/Coel_Character_BP.Coel_Character_BP'
       fullStatsRaw = [[30, 0.2, 0.27, 0.5, 0], [100, 0.1, 0.1, 0, 0], [15, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [100, 0.1, 0.1, 0, 0], None, None, [8, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = []
       noGender = True
       colors = [{'name': 'Unknown', 'colors': ['Black', 'Blue', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Green', 'Green', 'Orange', 'Purple', 'Red', 'Yellow']}, None, None, None, {'name': 'Unknown', 'colors': ['Black', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Green']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 2000, 'affinityNeeded0': 10000, 'affinityIncreasePL': 5, 'foodConsumptionBase': 0.01, 'foodConsumptionMult': 0.05}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
