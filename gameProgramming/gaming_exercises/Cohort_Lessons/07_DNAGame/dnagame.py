# DNA Replication Game, Johnson Traevon v0.4

# Import Entire Modules -- Get the whole tool box
import time, datetime

# Import Specific Methods -- Get the specific tool
from random import choice

# Store the DNA Bases
dnaBases = ["A", "T", "G", "C"]

# Game Functions
def gameIntro() -> None:
    pass

def genDNA() -> str:
    basesGenerated = 0
    basesRequested = int(input("How many bases do you want, Please enter a possitive number\n"))
    dnaSequence = ""

    while basesGenerated < basesRequested:
        dnaSequence += choice(dnaBases)
        basesGenerated += 1
    return dnaSequence

def doTranscription(dnaSequence: str) -> tuple:
    print(f"The DNA Sequence is {dnaSequence}.\n")
    print("You will now generate the RNA sequence that would match\n")
    print("Please remember, in the RNA sequence U pairs with A from the DNA sequence")
    rnaStart = time.time() # time.time() returns the number of seconds since 00:00:00 UTC Jan, 01, 1970
    rnaSequence = input("Please enter the matching RNA sequence.  Leave no spaces! Then press enter.\n").upper()
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    return (rnaSequence, rnaTime)

    # Tuples are ORDERED -- you can reference itmes with the index
    # Tuples are UNCHANGEABLE -- you cannot add, modify, or delete after creating
    # Tuples can have duplicate values
def verifySequence(dnaSequence: str, rnaSequence: str) -> bool:
    isMatch = False
    if len(dnaSequence) != len(rnaSequence):
        print("Since the Sequence are not equal, they do not match.\n")
        return isMatch
    for dnaBase, rnaBase in zip(dnaSequence, rnaSequence):
        if dnaBase == "A" and rnaBase == "U":
            isMatch = True
        elif dnaBase == "C" and rnaBase == "G":
            isMatch = True
        elif dnaBase == "G" and rnaBase == "C":
            isMatch =  True
        elif dnaBase == "T" and rnaBase == "A":
            isMatch = True
        else:
            print("They do not match because no base is True.\n")
    return isMatch

def calcScore(rnaSequence: str, rnaTime: float) -> int:
    score = 0
    if rnaTime < 3.0:
        score += 1000000
    elif rnaTime < 15.0:
        score += 5000
    else:
        score += 25000
        print("You tried your best <3\n")

    scoreMulti = 0.0
    if len(rnaSequence) >= 10:
        scoreMulti = 3.0
    elif len(rnaSequence) >= 5:
        scoreMulti = 2.0
    else: 
        scoreMulti = 0.01
    score *= scoreMulti
    return score

dna = genDNA()
rna = doTranscription(dna)
print(verifySequence(dna, rna[0]))

print(calcScore(rna[0], rna[1]))


