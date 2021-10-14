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

""" FOREST:   You find sprites that are being beseiged by packs of 
angry wolves that have been driven from their home.  The sprites in turn are just trying to get to the Caves in 
order to save a sprite maiden that has been taken hostage in the 
dungeon hidden below.  If you help the sprites they will give you a 
HUNTING KNIFE to fight with.  Every pack of wolves you defeat they will
craft you armor from their hides.  If you defeat all the packs 
(5: Breast plate, Pants, Boots, Helmet, Gloves) you will have a full
set of ARMOR and the boost it gives as well as be given a MACE.

Caves: You will fight lesser skeletons that will earn you HEALTH POTIONS
and in the LargeCavern you will fight a boss level skeleton that will 
earn you a LONG BONE SWORD. As well as the story and why the hostage 
was kidnapped (She was hired to be a guide to the dungeon, but was used 
as bait and left for dead when the Adventurer found what he was looking for.)

Coast:  You will fight hidden bandits that will earn you special RINGS. 
at the end you will find and fight the Lead Bandit and his pet bird. You will 
also learn why he stole the artifact, and that he gave it to 'some-hooded guy
with a raspy voice'. You just missed him.  He went into the plains) but since
it would be bad for business to rat out customers, the Bandit will have to 
kill you anyway. He earns you a NECKLACE OF SWIFT MOVEMENT.

Plains: Here you will fight 3 large, undead beasts.
    Bear: earns you a BELT OF STRENGTH.
    Cougar: earns you BOOTS OF STEALTH.
    Python: earns you ANTIDOTE x 4 and POWDER OF STONE x 4

Temple: Here you will fight off Slime monsters. (applying POWDER OF STONE to your
weapons makes them solid enough to take damage from weapons.
They will earn you HEALTH or POWDER or ANTIDOTE (antidote to their slime).
in the Sanctum you will fight a powerful Large Slime.  He will earn you
a RING OF SPELL REJECTION.   After the slime, a Lych is revealed, holding the Artifact.
if you beat him, you win the artifact and the loot you have retained to this point. All of
which can be sold or used in the REAL GAME (?), and the Arifact definitly is worth the time
spent in our little world. What do you think?"""