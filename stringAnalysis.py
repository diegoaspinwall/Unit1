#Diego Aspinwall
#9-1-17
#stringAnalysis.py

sentence = input('Enter a sentence: ')
print('Your sentence has', sentence.count(' ')+1, 'words and', len(sentence), 'characters and', len(sentence)-sentence.count(' '), 'letters')
charsearch = input('Enter a character to search for: ')
print('Your sentence has', sentence.count(charsearch), 'of the character', charsearch)
wordsearch = input('Enter a word to search for: ')
print('Your sentence has', sentence.count(wordsearch), 'of the word', wordsearch)
