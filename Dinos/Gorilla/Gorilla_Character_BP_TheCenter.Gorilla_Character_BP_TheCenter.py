import sys,sce
class Gorilla_Character_BP_TheCenter(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Megapithecus'
       blueprintPath = '/Game/PrimalEarth/Dinos/Gorilla/Gorilla_Character_BP_TheCenter.Gorilla_Character_BP_TheCenter'
       variants = ['Boss', 'Gamma', 'TheCenter']
       fullStatsRaw = [[144000, 0, 0, 0.3, 0], [650, 0, 0, 0, 0], [350, 0.06, 0, 0.5, 0], [2000, 0, 0, 0, 0], [2600, 0, 0, 0, 0], None, None, [4000, 0.02, 0.02, 0, 0], [1, 0, 0, 0.3, 0.3], [1, 0, 0, 0, 0], None, None]
       altBaseStats = {'0': 180000}
       immobilizedBy = []
       noGender = True
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 1.5, 'affinityNeeded0': 8500, 'affinityIncreasePL': 150, 'foodConsumptionBase': 0.002066, 'foodConsumptionMult': 150}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
