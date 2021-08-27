import sys,sce
class BionicTrike_Character_BP_Malfunctioned(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Malfunctioned Tek Triceratops'
       blueprintPath = '/Game/PrimalEarth/Dinos/Trike/BionicTrike_Character_BP_Malfunctioned.BionicTrike_Character_BP_Malfunctioned'
       fullStatsRaw = [[375, 0.2, 0.27, 0.5, 0], [150, 0.1, 0.1, 0, 0], [250, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [3000, 0.1, 0.1, 0, 0], None, None, [365, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.015, 1.2, 0], None, None]
       immobilizedBy = ['Chain Bola', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 8999.28006, 'eggTempMin': 22, 'eggTempMax': 28, 'maturationTime': 166666.667, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Head Main', 'colors': ['Black', 'Dark Grey', 'Dino Darker Grey', 'Light Grey']}, {'name': 'Spine', 'colors': ['Black', 'Dark Grey', 'Dino Darker Grey', 'Light Grey']}, {'name': 'Body Main', 'colors': ['Black', 'Dark Grey', 'Dino Darker Grey', 'Light Grey']}, {'name': 'Body Highlights', 'colors': ['Black', 'Dark Grey', 'Dino Darker Grey', 'Light Grey']}, {'name': 'Internals', 'colors': ['Red']}, {'name': 'Emissives', 'colors': ['Red']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 0.2, 'affinityNeeded0': 3000, 'affinityIncreasePL': 150, 'foodConsumptionBase': 0.003156, 'foodConsumptionMult': 352.0631}
       boneDamageAdjusters = {'c_head': 0.15, 'c_jaw': 0.15}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
