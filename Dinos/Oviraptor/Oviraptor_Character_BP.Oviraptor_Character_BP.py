import sys,sce
class Oviraptor_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Oviraptor'
       blueprintPath = '/Game/PrimalEarth/Dinos/Oviraptor/Oviraptor_Character_BP.Oviraptor_Character_BP'
       fullStatsRaw = [[140, 0.2, 0.27, 0.5, 0], [120, 0.1, 0.1, 0, 0], [125, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [900, 0.1, 0.1, 0, 0.15], None, None, [100, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 1, 0.4], [1, 0, 0.01, 1, 0.15], None, None]
       immobilizedBy = ['Bola', 'Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 4090.58184, 'eggTempMin': 26, 'eggTempMax': 30, 'maturationTime': 75757.5758, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Crest and Beak', 'colors': ['Black', 'Dark Grey', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Feathers', 'colors': ['Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, None, {'name': 'Patterning', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Belly', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 16.66667, 'affinityNeeded0': 960, 'affinityIncreasePL': 42, 'torporDepletionPS0': 0.208, 'foodConsumptionBase': 0.001302, 'foodConsumptionMult': 768.0491}
       boneDamageAdjusters = {'c_head': 3, 'c_jaw': 3, 'c_neck3': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
