import sys,sce
class SpiderL_Character_BP_Medium(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Broodmother Lysrix'
       blueprintPath = '/Game/PrimalEarth/Dinos/Spider-Large/SpiderL_Character_BP_Medium.SpiderL_Character_BP_Medium'
       variants = ['Beta', 'Boss']
       fullStatsRaw = [[648000, 0.15, 0.27, 0.5, 0], [150, 0.1, 0.1, 0, 0], [100000, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [1500, 0.1, 0.1, 0, 0], None, None, [4000, 0.02, 0.04, 0, 0], [1, 0.035, 0.1, 0.5, 0.4], [1, 0, 0.01, 0.151, 0], None, None]
       altBaseStats = {'0': 280000}
       immobilizedBy = []
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 2.5, 'affinityNeeded0': 1500, 'affinityIncreasePL': 75, 'foodConsumptionBase': 0.001929, 'foodConsumptionMult': 432.0028}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
