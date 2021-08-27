import sys,sce
class Kairuku_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Kairuku'
       blueprintPath = '/Game/PrimalEarth/Dinos/Kairuku/Kairuku_Character_BP.Kairuku_Character_BP'
       fullStatsRaw = [[95, 0.2, 0.27, 0.5, 0], [200, 0.1, 0.1, 0, 0], [300, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [900, 0.1, 0.1, 0, 0.15], None, None, [70, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 1, 0.4], [1, 0, 0.01, 2, 0], None, None]
       immobilizedBy = ['Bola', 'Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 5454.10913, 'eggTempMin': 22, 'eggTempMax': 30, 'maturationTime': 101010.101, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Back and Markings', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey']}, {'name': 'Beak', 'colors': ['Black', 'Dino Albino', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown']}, {'name': 'Feet', 'colors': ['Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, None, {'name': 'Osteoderms', 'colors': ['Black', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow']}, None]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 4.166667, 'affinityNeeded0': 1200, 'affinityIncreasePL': 45, 'torporDepletionPS0': 1, 'foodConsumptionBase': 0.001389, 'foodConsumptionMult': 1079.914}
       boneDamageAdjusters = {'c_neck4': 3, 'c_head': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
