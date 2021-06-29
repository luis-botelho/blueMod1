from random import choice
tryTimes = 0
trysToEnd = 6
words = ["banana","Chuveiro","macumba","batuque","menina","suave","tomate","teclado","mosquito"]
wrongLetters = []
rightLetters = []
word = choice(words).lower()
displayWord = list('_' * len(word))
print('Bem-vindo(a) ao jogo da forca!')
print(f'Você pode errar {trysToEnd} vezes.')
while tryTimes < trysToEnd and '_' in displayWord:
    print('Palavra:', ' '.join(displayWord))
    print(f'Status: {tryTimes} de {trysToEnd} erros')
    print(f'Letras erradas: {",".join(wrongLetters)}')
    letter = str(input('Digite uma letra: ').lower())
    while letter in wrongLetters or letter in rightLetters:
        letter = input(f'Letra >>>{letter}<<< já foi utilizada, por favor, informe outra: ')
    if letter not in word:
        wrongLetters.append(letter)
        tryTimes += 1
    else:
        rightLetters.append(letter)
        cont = 0
        while cont < len(word):
            if word[cont] == letter:
                displayWord[cont]
            cont +=1
if '_' not in displayWord:
    print(f'Parabéns! você ganhou o jogo, a palavra certa era {word}')
if tryTimes == trysToEnd:
    print(f'Você perdeu, a palavra era {word}')