import sys,sce
class DungBeetle_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Dung Beetle'
       blueprintPath = '/Game/PrimalEarth/Dinos/DungBeetle/DungBeetle_Character_BP.DungBeetle_Character_BP'
       fullStatsRaw = [[200, 0.2, 0.135, 0.5, 0], [100, 0.1, 0.1, 0, 0], [200, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [900, 0.1, 0.1, 0, 0], None, None, [5, 0.02, 0.08, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = ['Bola', 'Bear Trap', 'Plant Species Y']
       noGender = True
       colors = [{'name': 'Shell', 'colors': ['Black', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Medium Green']}, {'name': 'Legs', 'colors': ['Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, None, {'name': 'Palps and Leg Patterning', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Shell Patterning', 'colors': ['Black', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Medium Green']}, {'name': 'Underside', 'colors': ['Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}]
       taming = {'nonViolent': True, 'violent': False, 'tamingIneffectiveness': 4.166667, 'affinityNeeded0': 900, 'affinityIncreasePL': 50, 'wakeAffinityMult': 1, 'wakeFoodDeplMult': 2, 'foodConsumptionBase': 0.001488, 'foodConsumptionMult': 336.0215}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
