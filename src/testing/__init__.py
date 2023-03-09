from src.testing.slang import TestBasics as SlangTestBasics
from src.testing.slang import TestToSpp  as SlangTestToSpp

from src.testing.spplang import TestBasics as SpplangTestBasics
from src.testing.spplang import TestSyntax as SpplangTestSyntax

from src.testing.ssharplang.TestSyntax import TestSyntax as SsharpTestSyntax
from src.testing.ssharplang.TestBasics import TestBasics as SsharpTestBasics

from src.testing.transpilers import TestSppTypes
from src.testing.transpilers import TestSppToSClasses
from src.testing.transpilers import TestSppToSNew
from src.testing.transpilers import TestSppToSClassAccesses
from src.testing.transpilers import TestSToSppStruct


from src.testing.transpilers import SsharpToSppAStar
from src.testing.transpilers import SsharpToSppToSAStar
from src.testing.transpilers import SToSppBFS
from src.testing.transpilers import SToSppAStar
from src.testing.transpilers import SppToSBFS
from src.testing.transpilers import SppToSAStar

from src.testing.ssharplang import tests as ssharp_tests
from src.testing.spplang    import tests as spp_tests
from src.testing.slang      import tests as s_tests
