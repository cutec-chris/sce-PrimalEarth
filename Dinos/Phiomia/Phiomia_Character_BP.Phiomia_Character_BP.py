import sys,sce
class Phiomia_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Phiomia'
       blueprintPath = '/Game/PrimalEarth/Dinos/Phiomia/Phiomia_Character_BP.Phiomia_Character_BP'
       fullStatsRaw = [[300, 0.2, 0.27, 0.5, 0], [300, 0.1, 0.1, 0, 0], [240, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [3000, 0.1, 0.1, 0, 0.15], None, None, [200, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 1, 0.4], [1, 0, 0.01, 0.35, 0], None, None]
       immobilizedBy = ['Bola', 'Bear Trap', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 35714.2857, 'incubationTime': 0, 'maturationTime': 175438.596, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Yellow', 'Dino Medium Brown', 'Light Grey']}, None, None, None, {'name': 'Spots 1', 'colors': ['Black', 'Dark Grey', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Spots 2', 'colors': ['Black', 'Dark Grey', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.2, 'affinityNeeded0': 3000, 'affinityIncreasePL': 150, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.003156, 'foodConsumptionMult': 1584.284}
       boneDamageAdjusters = {'c_head': 3, 'c_jaw': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
