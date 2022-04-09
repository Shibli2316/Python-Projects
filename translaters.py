from audioop import add
# from gettext import translation
# from translate import Translator

# translator= Translator(from_lang="english", to_lang="arabic")
# translation = translator.translate("Brother")
# print(translation)



from textblob import TextBlob

adding_blob = TextBlob('Easy way to print in python')
new_word= adding_blob.translate(to='ge')
print(new_word)