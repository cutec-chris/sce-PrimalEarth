import sys,sce
class Quetz_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Quetzal'
       blueprintPath = '/Game/PrimalEarth/Dinos/Quetzalcoatlus/Quetz_Character_BP.Quetz_Character_BP'
       isFlyer = True
       fullStatsRaw = [[1200, 0.2, 0.108, 0.5, 0], [800, 0.05, 0.05, 0, 0], [1850, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1200, 0.1, 0.1, 0, 0.15], None, None, [800, 0.02, 0.05, 0, 0], [1, 0.04, 0.1, 0.4, 0.4], [1, 0, 0.01, 0.365, 0], None, None]
       statImprintMult = [0.2, 0, 0.2, 0, 0.2, 0.2, 0, 0.2, 0.2, 0, 0, 0]
       immobilizedBy = ['Chain Bola', 'Bear Trap', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 59995.2004, 'eggTempMin': 5, 'eggTempMax': 6, 'maturationTime': 476190.476, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Wing Membrane', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Crest', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Skins', 'colors': ['Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Freckles', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Beak', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Orange', 'Dino Medium Brown', 'Light Grey']}, {'name': 'Body Feathers', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.9375, 'affinityNeeded0': 6850, 'affinityIncreasePL': 300, 'torporDepletionPS0': 3.4, 'foodConsumptionBase': 0.0035, 'foodConsumptionMult': 140}
       boneDamageAdjusters = {'c_head': 3}
       TamedBaseHealthMultiplier = 0.85
       displayedStats = 927
