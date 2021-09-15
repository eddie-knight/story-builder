from .canine import Canine, CanineSapient
from .celestial import Celestial
from .common import Common
from .fowl import Fowl, FowlSapient
from .high_common import HighCommon
from .low_common import LowCommon
from .non_communicative import NonCommunicative

"""

These imports are present to simplify imports outside
of this module. Without these, it would be necessary
to type something like:
    from .communication.canine import Canine

But with these imports it becomes slightly shorter:
    from .communication import Canine

Also, IDEs such as VSCode will help developers find
all of the classes imported here, presenting an
autofill prompt when developers type `from .communication`

Additionally, these imports allow us to "obscure" any
classes that are not intended for use outside of this
module, as they will not show up when a developer looks
at the autofill options for the communications module.

And, as a final note, these imports allow us to visualize
the work we have done. Looking at this list, we may
turn a critical eye to our progress, and find some
optimizations that we might otherwise miss.

"""