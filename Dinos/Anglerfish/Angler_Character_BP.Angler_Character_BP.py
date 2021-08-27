import sys,sce
class Angler_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Anglerfish'
       blueprintPath = '/Game/PrimalEarth/Dinos/Anglerfish/Angler_Character_BP.Angler_Character_BP'
       fullStatsRaw = [[450, 0.2, 0.27, 0.3, 0], [240, 0.1, 0.1, 0, 0], [900, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1500, 0.1, 0.1, 0, 0.15], None, None, [350, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 1, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = []
       breeding = {'gestationTime': 0, 'incubationTime': 17998.5601, 'eggTempMin': -75, 'eggTempMax': 75, 'maturationTime': 133333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body', 'colors': ['Black', 'Blue', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Green', 'Green', 'Orange', 'Purple', 'Red', 'Yellow']}, None, None, None, {'name': 'Spots', 'colors': ['Black', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Green']}, {'name': 'Tail fin and Accents', 'colors': ['Black', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Light Blue', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Green']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 2.5, 'affinityNeeded0': 1800, 'affinityIncreasePL': 90, 'torporDepletionPS0': 2.8, 'foodConsumptionBase': 0.001852, 'foodConsumptionMult': 149.988}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
