
from src.transpilers.AddBeforeReturn import addBeforeReturn
from src.transpilers.MetaTranspiler  import MetaTranspiler
from src.transpilers.s.spp      import deltas as sToSppDeltas
from src.transpilers.spp.s      import deltas as sppToSDeltas
from src.transpilers.ssharp.spp import deltas as ssharpToSppDeltas
deltas = sToSppDeltas + sppToSDeltas + ssharpToSppDeltas
