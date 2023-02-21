
from src.transpilers.AddBeforeReturn import addBeforeReturn
from src.transpilers.MetaTranspiler  import MetaTranspiler

from src.transpilers.s.spp      import deltas as s2spp_deltas
from src.transpilers.spp.s      import deltas as spp2s_deltas
from src.transpilers.ssharp.spp import deltas as ssharp2spp_deltas

from src.transpilers.s.spp      import transpile as s2spp_transpile
from src.transpilers.spp.s      import transpile as spp2s_transpile
from src.transpilers.ssharp.spp import transpile as ssharp2spp_transpile

deltas = s2spp_deltas + spp2s_deltas + ssharp2spp_deltas
