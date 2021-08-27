import sys,sce
class BionicPara_Character_BP_Malfunctioned(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Malfunctioned Tek Parasaur'
       blueprintPath = '/Game/PrimalEarth/Dinos/Para/BionicPara_Character_BP_Malfunctioned.BionicPara_Character_BP_Malfunctioned'
       fullStatsRaw = [[200, 0.2, 0.27, 0.5, 0], [450, 0.1, 0.1, 0, 0], [150, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1500, 0.1, 0.1, 0, 0], None, None, [480, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0.67, 0], None, None]
       immobilizedBy = ['Bola', 'Bear Trap', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 5142.44575, 'eggTempMin': 24, 'eggTempMax': 28, 'maturationTime': 95238.0952, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Head Main', 'colors': ['Black', 'Dark Grey', 'Dino Darker Grey', 'Light Grey']}, {'name': 'Spine', 'colors': ['Black', 'Dark Grey', 'Dino Darker Grey', 'Light Grey']}, {'name': 'Body Main', 'colors': ['Black', 'Dark Grey', 'Dino Darker Grey', 'Light Grey']}, {'name': 'Body Highlights', 'colors': ['Black', 'Dark Grey', 'Dino Darker Grey', 'Light Grey']}, {'name': 'Internals', 'colors': ['Red']}, {'name': 'Emissives', 'colors': ['Red']}]
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 0.4, 'affinityNeeded0': 1500, 'affinityIncreasePL': 75, 'foodConsumptionBase': 0.001929, 'foodConsumptionMult': 864.0056}
       boneDamageAdjusters = {'c_jaw': 2, 'c_head': 2}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
