
from src.transpilers.ToString import toString
from src.transpilers.RemoveSppClasses import removeSppClasses
from src.transpilers.SppToSImports import sppToSImports
from src.transpilers.SppToSIdentities import sppToSIdentities
from src.transpilers.IsSLangCondition import isSLang

deltas = [removeSppClasses, sppToSImports, sppToSIdentities]
from src.transpilers.MetaTranspiler import MetaTranspiler
