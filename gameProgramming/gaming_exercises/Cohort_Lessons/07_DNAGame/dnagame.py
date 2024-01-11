# DNA Replication Game, Johnson Traevon v0.3

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

def genRNA(dnaSequence: str) -> tuple:
    print(f"The DNA Sequence is {dnaSequence}.\n")
    print("You will now generate the RNA sequence that would match\n")
    print("Please remember, in the RNA sequence U pairs with A from the DNA sequence")
    rnaStart = time.time() # time.time() returns the number of seconds since 00:00:00 UTC Jan, 01, 1970
    rnaSequence = input("Please enter the matching RNA sequence.  Leave no spaces! Then press enter.\n")
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    return (rnaSequence, rnaTime)


    # Tuples are ORDERED -- you can reference itmes with the index
    # Tuples are UNCHANGEABLE -- you cannot add, modify, or delete after creating
    # Tuples can have duplicate values
dna = genDNA()
rna = genRNA(dna)
print(rna)
