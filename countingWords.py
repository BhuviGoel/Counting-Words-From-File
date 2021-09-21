def countWordsFromFile():
      fileName = input("Give Path of File: ")
      fileOpen = open(fileName,'r')
      numberOfWords = 0
      for l in fileOpen:
            words = l.split()
            numberOfWords = numberOfWords + len(words)
            print(numberOfWords)

countWordsFromFile()


