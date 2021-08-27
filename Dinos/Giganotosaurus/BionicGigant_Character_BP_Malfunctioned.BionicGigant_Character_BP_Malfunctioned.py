import sys,sce
class BionicGigant_Character_BP_Malfunctioned(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Malfunctioned Tek Giganotosaurus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Giganotosaurus/BionicGigant_Character_BP_Malfunctioned.BionicGigant_Character_BP_Malfunctioned'
       fullStatsRaw = [[80000, 0.0005, 0.002, -63000, 0], [400, 0.0005, 0.01, 0, 0], [10000, 0.06, 0, 0, 0], [150, 0.0025, 0.025, 0, 0], [4000, 0.0025, 0.025, 0, 0], None, None, [700, 0.01, 0.01, 0, 0], [1, 0.05, 0.05, -0.8, 0], [1, 0, 0.0031, 0, 0], None, None]
       immobilizedBy = ['Large Bear Trap']
       breeding = {'gestationTime': 0, 'incubationTime': 8999.28006, 'eggTempMin': 24, 'eggTempMax': 28, 'maturationTime': 878348.704, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Head Main', 'colors': ['Black', 'Dark Grey', 'Dino Darker Grey', 'Light Grey']}, {'name': 'Spine', 'colors': ['Black', 'Dark Grey', 'Dino Darker Grey', 'Light Grey']}, {'name': 'Body Main', 'colors': ['Black', 'Dark Grey', 'Dino Darker Grey', 'Light Grey']}, {'name': 'Body Highlights', 'colors': ['Black', 'Dark Grey', 'Dino Darker Grey', 'Light Grey']}, {'name': 'Internals', 'colors': ['Red']}, {'name': 'Emissives', 'colors': ['Red']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 1.25, 'affinityNeeded0': 5000, 'affinityIncreasePL': 160, 'foodConsumptionBase': 0.002314, 'foodConsumptionMult': 160.0563}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
