import sys,sce
class Dilo_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Dilophosaur'
       blueprintPath = '/Game/PrimalEarth/Dinos/Dilo/Dilo_Character_BP.Dilo_Character_BP'
       fullStatsRaw = [[130, 0.2, 0.27, 0.5, 0], [100, 0.1, 0.1, 0, 0], [75, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [450, 0.1, 0.1, 0, 0.15], None, None, [45, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 1, 0.4], [1, 0, 0.01, 2, 0], None, None]
       immobilizedBy = ['Bola', 'Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 4090.58184, 'eggTempMin': 28, 'eggTempMax': 32, 'maturationTime': 75757.5758, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Body', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Back and Face', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Spike Tips', 'colors': ['Black', 'Dino Albino', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Spine and Spike Base', 'colors': ['Black', 'Dino Albino', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Frill, Crest and Belly', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Legs and Arms', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 8.333333, 'affinityNeeded0': 450, 'affinityIncreasePL': 22.5, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.000868, 'foodConsumptionMult': 1728.111}
       boneDamageAdjusters = {'c_head': 3, 'c_jaw': 3, 'c_neck3': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
