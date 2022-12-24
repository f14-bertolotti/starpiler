
from src.transpilers.AddBeforeReturn import addBeforeReturn
from src.transpilers.MetaTranspiler  import MetaTranspiler
from src.transpilers.s.spp import deltas as sToSppDeltas
from src.transpilers.spp.s import deltas as sppToSDeltas
deltas = sToSppDeltas + sppToSDeltas
