import sys,sce
class Argent_Character_BP(sce.Dinos):
   def __init__(self):
       super().__init__(self)
       name = 'Argentavis'
       blueprintPath = '/Game/PrimalEarth/Dinos/Argentavis/Argent_Character_BP.Argent_Character_BP'
       isFlyer = True
       fullStatsRaw = [[365, 0.2, 0.30375, 0.5, 0], [400, 0.05, 0.075, 0, 0], [600, 0.06, 0, 0.5, 0], [150, 0.1, 0.1, 0, 0], [2000, 0.1, 0.1, 0, 0], None, None, [400, 0.02, 0.055, 0, 0], [1, 0.05, 0.15, 0.5, 0.4], [1, 0, 0.01, 0, 0], None, None]
       statImprintMult = [0.2, 0, 0.2, 0, 0.2, 0.2, 0, 0.2, 0.2, 0, 0, 0]
       immobilizedBy = ['Chain Bola', 'Bear Trap', 'Large Bear Trap', 'Plant Species Y']
       breeding = {'gestationTime': 0, 'incubationTime': 10587.3883, 'eggTempMin': 12, 'eggTempMax': 13.5, 'maturationTime': 196078.431, 'matingCooldownMin': 64800, 'matingCooldownMax': 172800}
       colors = [{'name': 'Main Body', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'White']}, None, {'name': 'Wing Tips', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'White']}, {'name': 'Legs', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'White']}, {'name': 'Head Feathers', 'colors': ['Black', 'Dark Grey', 'Dino Dark Brown', 'Dino Dark Orange', 'Dino Dark Red', 'Dino Dark Yellow', 'Dino Darker Grey', 'Dino Medium Brown', 'White']}, {'name': 'Underside', 'colors': ['Black', 'Dino Light Brown', 'Dino Light Orange', 'Dino Light Yellow', 'Dino Medium Brown', 'Light Grey', 'White']}]
       taming = {'nonViolent': False, 'violent': True, 'tamingIneffectiveness': 1.875, 'affinityNeeded0': 2000, 'affinityIncreasePL': 100, 'torporDepletionPS0': 0.3, 'foodConsumptionBase': 0.001852, 'foodConsumptionMult': 199.984}
       boneDamageAdjusters = {'c_neck4': 3}
       TamedBaseHealthMultiplier = 1
       displayedStats = 927
