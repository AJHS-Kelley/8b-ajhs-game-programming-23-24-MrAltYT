# DNA Replication Game, Johnson Traevon v0.2

# Import Entire Modules -- Get the whole tool box
import time, datetime

# Import Specific Methods -- Get the specific tool
from random import choice

# Store the DNA Bases
dnsBases = ["A", "T", "G", "C"]

# Game Functions
def gameIntro() -> None:
    pass

def genDNA() -> str:
    basesGenerated = 0
    basesRequested = int(input("How many bases do you want, Please enter a possitive number\n"))
    dnaSequence = ""

    while basesGenerated < basesRequested:
        dnaSequence += choice(dnsBases)
        basesGenerated += 1
    return dnaSequence
dna = genDNA()
print(dna)
