
#from src.transpilers.AddSppEndMethod    import addSppEndMethod
from src.transpilers.AddBeforeReturn    import addBeforeReturn
#from src.transpilers.SppTypes           import sppTypes
#from src.transpilers.SppClassesToS      import sppClassesToS
#from src.transpilers.SppNewToS          import sppNewToS
#from src.transpilers.SppStructAccessToS import sppStructAccessToS
#from src.transpilers.SppToSImport       import sppToSImport
#from src.transpilers.SppToSIdentities   import sppToSIdentities
#from src.transpilers.SppToSGlobalAssignement import sppToSGlobalAssignement

#from src.transpilers.IsSLangCondition import isSLang
#from src.transpilers.IsSppLangCondition import isSppLang
#from src.transpilers.ToString import toString
#from src.transpilers.AddBeforeReturn import addBeforeReturn
#from src.transpilers.SStructToSppClass import sStructToSppClass
#from src.transpilers.SppClassesToSStruct import sppClassesToSStruct
#from src.transpilers.SppToSImports import sppToSImports
#from src.transpilers.RemoveSppImports import removeSppImports
#from src.transpilers.SToSppImports import sToSppImports
#from src.transpilers.SToSppIdentities import sToSppIdentities

#deltas = [SppClassesToSStruct, sppToSImports, sToSppImports, sppToSIdentities, sToSppIdentities, sStructToSppClass]
#deltas = [sppToSImports, sppClassesToSStruct, sppToSIdentities]
from src.transpilers.MetaTranspiler import MetaTranspiler
