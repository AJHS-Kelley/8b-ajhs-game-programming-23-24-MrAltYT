# DNA Replication Game, Johnson Traevon v0.8
# Program crashes as soon as I enter a number of bases to generate. 

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


def doTranscription(dnaSequence: str,) -> tuple:
    print(f"The DNA Sequence is {dnaSequence}.\n")
    print("You will now generate the RNA sequence that would match\n")
    print("Please remember, in the RNA sequence U pairs with A from the DNA sequence")
    rnaStart = time.time() # time.time() returns the number of seconds since 00:00:00 UTC Jan, 01, 1970
    rnaStop = time.time()
    rnaTime = rnaStop - rnaStart
    rnaSequence = input("Please enter the matching RNA sequence.  Leave no spaces! Then press enter.\n").upper().split()
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

def calcScore(rnaSequence: str, rnaTime: float) -> float:
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

def saveScore(dnaSequence: str, rnaSequence: str, rnaTime: int, score: float) -> None:
    playerName = input("What is your first name?\n")
    lastName = input("What is your last name?\n")
    fullName = playerName + "  " + lastName

    fileName = "dnaReplicationScore" + fullName + ".txt"
    saveData = open(fileName, "a")
    # File Modes
    # "x" mode -- Create file, if file exists, exit with error
    # "w" mode -- create file, if file exists, overwrite it
    # "a" mode -- create file, if file exists, append to it
    saveData.write(f"DNA Sequence: {dnaSequence}\nRNA Sequence: {rnaSequence}\n")
    saveData.write(f"Transcription Time: {rnaTime}\n")
    saveData.write(f"Score: {score}\n")
    saveData.write(f"{fullName}\n")
    saveData.write(f"{datetime.datetime.now()}\n")
    saveData.close()
dna = genDNA()
rna = doTranscription(dna)
if verifySequence(dna, rna[0]):
    score = (calcScore(rna[0], rna[1]))
    saveScore(dna, rna[0], rna[1], score)

print(calcScore(rna[0], rna[1]))


