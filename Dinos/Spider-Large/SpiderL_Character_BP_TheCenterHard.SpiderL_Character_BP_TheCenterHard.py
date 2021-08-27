import sys,sce
class SpiderL_Character_BP_TheCenterHard(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Broodmother Lysrix'
       blueprintPath = '/Game/PrimalEarth/Dinos/Spider-Large/SpiderL_Character_BP_TheCenterHard.SpiderL_Character_BP_TheCenterHard'
       variants = ['Alpha', 'Boss', 'TheCenter']
       fullStatsRaw = [[486000, 0.2, 0.27, 0.5, 0], [150, 0.1, 0.1, 0, 0], [100000, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1500, 0.1, 0.1, 0, 0], None, None, [4000, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.5, 0.4], [1, 0, 0.01, 0.151, 0], None, None]
       altBaseStats = {'0': 324000}
       immobilizedBy = []
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 2.5, 'affinityNeeded0': 1500, 'affinityIncreasePL': 75, 'foodConsumptionBase': 0.001929, 'foodConsumptionMult': 432.0028}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
