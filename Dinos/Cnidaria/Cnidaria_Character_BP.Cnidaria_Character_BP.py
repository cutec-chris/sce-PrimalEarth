import sys,sce
class Cnidaria_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Cnidaria'
       blueprintPath = '/Game/PrimalEarth/Dinos/Cnidaria/Cnidaria_Character_BP.Cnidaria_Character_BP'
       fullStatsRaw = [[180, 0.2, 0.27, 0.5, 0], [120, 0.1, 0.1, 0, 0], [250, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1200, 0.1, 0.1, 0, 0.15], None, None, [25, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 1, 0.4], [1, 0, 0.01, 0.284, 0], None, None]
       immobilizedBy = []
       noGender = True
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 8.333333, 'affinityNeeded0': 450, 'affinityIncreasePL': 22.5, 'foodConsumptionBase': 0.001543, 'foodConsumptionMult': 216.0294}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
