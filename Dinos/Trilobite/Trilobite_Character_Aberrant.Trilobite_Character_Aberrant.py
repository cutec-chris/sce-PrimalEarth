import sys,sce
class Trilobite_Character_Aberrant(sce.Aberration):
   def __init__(self):
       super().__init__(self)
       name = 'Aberrant Trilobite'
       blueprintPath = '/Game/PrimalEarth/Dinos/Trilobite/Trilobite_Character_Aberrant.Trilobite_Character_Aberrant'
       variants = ['Aberrant']
       fullStatsRaw = [[160, 0.2, 0.27, 0.5, 0], [100, 0.1, 0.1, 0, 0], [50, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [450, 0.1, 0.1, 0, 0], None, None, [150, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = []
       noGender = True
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 1.333333, 'affinityNeeded0': 450, 'affinityIncreasePL': 22.5, 'foodConsumptionBase': 0.001736, 'foodConsumptionMult': 864.0553}
       TamedBaseHealthMultiplier = 0.96
       displayedStats = 919
