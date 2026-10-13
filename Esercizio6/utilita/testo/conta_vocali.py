def conta_vocali(testo):
    vocali = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}
    count = 0

    for i in testo:
        if i in vocali:
            count += 1
    
    return count
