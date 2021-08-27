import sys,sce
class Ptero_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Pteranodon'
       blueprintPath = '/Game/PrimalEarth/Dinos/Ptero/Ptero_Character_BP.Ptero_Character_BP'
       isFlyer = True
       fullStatsRaw = [[210, 0.2, 0.15, 0.5, 0], [150, 0.05, 0.04, 0, 0], [120, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1200, 0.1, 0.1, 0, 0.15], None, None, [120, 0.02, 0.03, 0, 0], [1, 0.05, 0.075, 0.65, 0.4], [1, 0, 0.02, 0.35, 0], None, None]
       statImprintMult = [0.2, 0, 0.2, 0, 0.2, 0.2, 0, 0.2, 0.2, 0, 0, 0]
       immobilizedBy = ['Bola', 'Chain Bola', 'Bear Trap', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 5999.52004, 'eggTempMin': 29, 'eggTempMax': 32, 'maturationTime': 133333.333, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Patterning', 'colors': ['Black', 'Dark Grey', 'Dino Albino', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Wing Base', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Face, Crest, and Hands', 'colors': ['Black', 'Dark Grey', 'Dino Dark Blue', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Purple', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}, {'name': 'Inner Crest', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Wing Membrane', 'colors': ['Black', 'Dino Light Blue', 'Dino Light Brown', 'Dino Light Green', 'Dino Light Orange', 'Dino Light Purple', 'Dino Light Red', 'Dino Light Yellow', 'Dino Medium Brown', 'Dino Medium Green', 'Light Grey']}, {'name': 'Body', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Green', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'Dino Medium Green']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 3.125, 'affinityNeeded0': 1200, 'affinityIncreasePL': 60, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.001543, 'foodConsumptionMult': 216.0294}
       boneDamageAdjusters = {'c_head': 3}
       TamedBaseHealthMultiplier = 0.9
       displayedStats = 927
