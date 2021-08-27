import sys,sce
class BionicQuetz_Character_BP(sce.Tek Creatures):
   def __init__(self):
       super().__init__(self)
       name = 'Tek Quetzal'
       blueprintPath = '/Game/PrimalEarth/Dinos/Quetzalcoatlus/BionicQuetz_Character_BP.BionicQuetz_Character_BP'
       isFlyer = True
       fullStatsRaw = [[1200, 0.2, 0.108, 0.5, 0], [800, 0.05, 0.05, 0, 0], [1850, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1200, 0.1, 0.1, 0, 0.15], None, None, [800, 0.02, 0.05, 0, 0], [1, 0.04, 0.1, 0.4, 0.4], [1, 0, 0.01, 0.365, 0], None, None]
       statImprintMult = [0.2, 0, 0.2, 0, 0.2, 0.2, 0, 0.2, 0.2, 0, 0, 0]
       immobilizedBy = ['Chain Bola', 'Bear Trap', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 59995.2004, 'eggTempMin': 5, 'eggTempMax': 6, 'maturationTime': 476190.476, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Wing Highlights', 'colors': ['Black', 'Cyan', 'Dark Grey', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Purple', 'Dino Deep Blue', 'Dino Light Blue', 'Dino Light Purple', 'Dino Light Yellow', 'Dino Medium Blue', 'Light Grey', 'Magenta', 'NearWhite', 'WyvernBlue0', 'WyvernPurple0', 'WyvernPurple1']}, {'name': 'Body Main', 'colors': ['Black', 'Cyan', 'Dark Grey', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Purple', 'Dino Deep Blue', 'Dino Light Blue', 'Dino Light Purple', 'Dino Light Yellow', 'Dino Medium Blue', 'Light Grey', 'Magenta', 'NearWhite', 'WyvernBlue0', 'WyvernPurple0', 'WyvernPurple1']}, {'name': 'Head and Wings', 'colors': ['Black', 'Cyan', 'Dark Grey', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Purple', 'Dino Deep Blue', 'Dino Light Blue', 'Dino Light Purple', 'Dino Light Yellow', 'Dino Medium Blue', 'Light Grey', 'Magenta', 'NearWhite', 'WyvernBlue0', 'WyvernPurple0', 'WyvernPurple1']}, {'name': 'Joints', 'colors': ['Black', 'Cyan', 'Dark Grey', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Purple', 'Dino Deep Blue', 'Dino Light Blue', 'Dino Light Purple', 'Dino Light Yellow', 'Dino Medium Blue', 'Light Grey', 'Magenta', 'NearWhite', 'WyvernBlue0', 'WyvernPurple0', 'WyvernPurple1']}, {'name': 'UnderBelly', 'colors': ['Black', 'Cyan', 'Dark Grey', 'Dino Albino', 'Dino Dark Blue', 'Dino Dark Purple', 'Dino Deep Blue', 'Dino Light Blue', 'Dino Light Purple', 'Dino Light Yellow', 'Dino Medium Blue', 'Light Grey', 'Magenta', 'NearWhite', 'WyvernBlue0', 'WyvernPurple0', 'WyvernPurple1']}, {'name': 'Emissive', 'colors': ['Dino Albino', 'Dino Light Blue', 'Dino Light Purple', 'Dino Medium Blue', 'Light Green', 'Light Orange', 'Light Red', 'Light Yellow']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 0.9375, 'affinityNeeded0': 6850, 'affinityIncreasePL': 300, 'torporDepletionPS0': 3.4, 'foodConsumptionBase': 0.0035, 'foodConsumptionMult': 140}
       boneDamageAdjusters = {'c_head': 3}
       TamedBaseHealthMultiplier = 0.85
       displayedStats = 927
