import sys,sce
class DodoRex_Character_BP(sce.Event Creatures):
   def __init__(self):
       super().__init__(self)
       name = 'DodoRex'
       blueprintPath = '/Game/PrimalEarth/Dinos/DodoRex/DodoRex_Character_BP.DodoRex_Character_BP'
       fullStatsRaw = [[666666, 0.2, 0.27, 0, 0], [1666, 0.1, 0.1, 0, 0], [1550, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [3000, 0.1, 0.1, 0, 0], None, None, [500, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = ['Large Bear Trap']
       noGender = True
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 1.25, 'affinityNeeded0': 3450, 'affinityIncreasePL': 150, 'foodConsumptionBase': 0.002314, 'foodConsumptionMult': 180.0634}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
