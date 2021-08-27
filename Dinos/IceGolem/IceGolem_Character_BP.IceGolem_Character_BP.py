import sys,sce
class IceGolem_Character_BP(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Ice Golem'
       blueprintPath = '/Game/PrimalEarth/Dinos/IceGolem/IceGolem_Character_BP.IceGolem_Character_BP'
       fullStatsRaw = [[25000, 0.0125, 0.135, -22000, 0], [300, 0.1, 0.1, 0, 0], [5000, 0.02, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [6000, 0.1, 0.1, 0, 0], None, None, [660, 0.02, 0.04, 0, 0], [1, 0.05, 0.1, 0.125, 0.4], [1, 0, 0.01, 0, 0], None, None]
       immobilizedBy = []
       noGender = True
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 2.5, 'affinityNeeded0': 6500, 'affinityIncreasePL': 325, 'torporDepletionPS0': 0.325, 'foodConsumptionBase': 0.002543, 'foodConsumptionMult': 180.0634}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
