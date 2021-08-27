import sys,sce
class Rhino_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Woolly Rhino'
       blueprintPath = '/Game/PrimalEarth/Dinos/WoollyRhino/Rhino_Character_BP.Rhino_Character_BP'
       fullStatsRaw = [[500, 0.2, 0.27, 0.5, 0], [120, 0.1, 0.1, 0, 0], [600, 0.06, 0, 0.5, 0], [100, 0.1, 0.1, 0, 0], [3000, 0.1, 0.1, 0, 0], None, None, [750, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 1.226, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Large Bear Trap']
       breeding = {'gestationTime': 14285.7143, 'incubationTime': 0, 'maturationTime': 166666.667, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Skins', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, {'name': 'Back', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, None, None, {'name': 'Underside', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, {'name': 'Horn', 'colors': ['BigFoot0', 'BigFoot4', 'BigFoot5', 'Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 1.25, 'affinityNeeded0': 3450, 'affinityIncreasePL': 125, 'torporDepletionPS0': 0.9, 'foodConsumptionBase': 0.003156, 'foodConsumptionMult': 150}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
