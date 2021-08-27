import sys,sce
class Dragon_Character_BP_Boss_Medium(sce.BaseCreature):
   def __init__(self):
       super().__init__(self)
       name = 'Dragon'
       blueprintPath = '/Game/PrimalEarth/Dinos/Dragon/Dragon_Character_BP_Boss_Medium.Dragon_Character_BP_Boss_Medium'
       variants = ['Beta', 'Boss']
       isFlyer = True
       fullStatsRaw = [[864000.062, 0.2, 0.2, 0.3, 0], [10000, 0.1, 0.1, 0, 0], [350, 0.06, 0, 0.5, 0], [2000, 0.1, 0.1, 0, 0], [2600, 0.1, 0.1, 0, 0], None, None, [4000, 0.02, 0.02, 0, 0], [1, 0.05, 0.04, 0.3, 0.3], [1, 0, 0, 0, 0], None, None]
       altBaseStats = {'0': 195000}
       immobilizedBy = []
       noGender = True
       taming = {'nonViolent': False, 'violent': False, 'tamingIneffectiveness': 1.5, 'affinityNeeded0': 8500, 'affinityIncreasePL': 150, 'foodConsumptionBase': 0.002066, 'foodConsumptionMult': 150}
       TamedBaseHealthMultiplier = 1
       displayedStats = 919
