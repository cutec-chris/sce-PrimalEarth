import sys,sce
class Mosa_Character_BP_Cave(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Mosasaur'
       blueprintPath = '/Game/PrimalEarth/Dinos/Mosasaurus/Mosa_Character_BP_Cave.Mosa_Character_BP_Cave'
       variants = ['Cave']
       fullStatsRaw = [[3600, 0.12, 0.21, 0.3, 0], [400, 0.1, 0.1, 0, 0], [3000, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [8000, 0.1, 0.1, 0, 0.15], None, None, [1300, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.65, 0.4], [1, 0, 0.005, 0, 0], None, None]
       immobilizedBy = []
       colors = [{'name': 'Unknown', 'colors': ['Black', 'Dino Dark Blue', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Orange', 'Dino Light Red', 'Dino Light Yellow']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Unknown', 'colors': ['Black', 'Dino Albino', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.06, 'affinityNeeded0': 11000, 'affinityIncreasePL': 600, 'torporDepletionPS0': 12.8, 'foodConsumptionBase': 0.005, 'foodConsumptionMult': 180.0011}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
