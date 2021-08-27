import sys,sce
class SpiderL_Character_BP_Hard(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Broodmother Lysrix'
       blueprintPath = '/Game/PrimalEarth/Dinos/Spider-Large/SpiderL_Character_BP_Hard.SpiderL_Character_BP_Hard'
       variants = ['Alpha', 'Boss']
       fullStatsRaw = [[972000.062, 0.25, 0.27, 0.5, 0], [150, 0.1, 0.1, 0, 0], [100000, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1500, 0.1, 0.1, 0, 0], None, None, [4000, 0.02, 0.04, 0, 0], [1, 0.075, 0.1, 0.5, 0.4], [1, 0, 0.01, 0.151, 0], None, None]
       altBaseStats = {'0': 470000}
       immobilizedBy = []
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 2.5, 'affinityNeeded0': 1500, 'affinityIncreasePL': 75, 'foodConsumptionBase': 0.001929, 'foodConsumptionMult': 432.0028}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
