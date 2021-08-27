import sys,sce
class BionicQuetz_Character_BP_Malfunctioned(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Malfunctioned Tek Quetzal'
       blueprintPath = '/Game/PrimalEarth/Dinos/Quetzalcoatlus/BionicQuetz_Character_BP_Malfunctioned.BionicQuetz_Character_BP_Malfunctioned'
       isFlyer = True
       fullStatsRaw = [[1200, 0.2, 0.108, 0.5, 0], [800, 0.05, 0.05, 0, 0], [1850, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1200, 0.1, 0.1, 0, 0.15], None, None, [800, 0.02, 0.05, 0, 0], [1, 0.04, 0.1, 0.4, 0.4], [1, 0, 0.01, 0.365, 0], None, None]
       statImprintMult = [0.2, 0, 0.2, 0, 0.2, 0.2, 0, 0.2, 0.2, 0, 0, 0]
       immobilizedBy = ['Chain Bola', 'Bear Trap', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 59995.2004, 'eggTempMin': 5, 'eggTempMax': 6, 'maturationTime': 476190.476, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Head Main', 'colors': ['Black', 'Dark Grey', 'Dino Darker Grey', 'Light Grey']}, {'name': 'Spine', 'colors': ['Black', 'Dark Grey', 'Dino Darker Grey', 'Light Grey']}, {'name': 'Body Main', 'colors': ['Black', 'Dark Grey', 'Dino Darker Grey', 'Light Grey']}, {'name': 'Body Highlights', 'colors': ['Black', 'Dark Grey', 'Dino Darker Grey', 'Light Grey']}, {'name': 'Internals', 'colors': ['Red']}, {'name': 'Emissives', 'colors': ['Red']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 0.9375, 'affinityNeeded0': 6850, 'affinityIncreasePL': 300, 'foodConsumptionBase': 0.0035, 'foodConsumptionMult': 140}
       boneDamageAdjusters = {'c_head': 3}
       TamedBaseHealthMultiplier = 0.85
       displayedStats = 927
