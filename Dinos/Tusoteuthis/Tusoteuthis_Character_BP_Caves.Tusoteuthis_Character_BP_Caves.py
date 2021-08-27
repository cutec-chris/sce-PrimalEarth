import sys,sce
class Tusoteuthis_Character_BP_Caves(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Tusoteuthis'
       blueprintPath = '/Game/PrimalEarth/Dinos/Tusoteuthis/Tusoteuthis_Character_BP_Caves.Tusoteuthis_Character_BP_Caves'
       variants = ['Cave']
       fullStatsRaw = [[2700, 0.2, 0.2025, 0.5, 0], [300, 0.1, 0.1, 0, 0], [1800, 0.06, 0, 0.5, 0], [215, 0.1, 0.1, 0, 0], [3200, 0.1, 0.1, 0, 0.15], None, None, [800, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 1, 0], None, None]
       immobilizedBy = []
       colors = [{'name': 'Body Highlights', 'colors': ['Black', 'Dino Dark Blue', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Orange', 'Dino Light Red', 'Dino Light Yellow']}, {'name': 'Tentacle Highlights', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, None, None, {'name': 'Tentacle Main', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Body Main', 'colors': ['Black', 'Dino Albino', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 0.75, 'affinityNeeded0': 12000, 'affinityIncreasePL': 150, 'foodConsumptionBase': 0.005, 'foodConsumptionMult': 180.0011}
       boneDamageAdjusters = {'upper_beak': 3, 'lower_beak': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
