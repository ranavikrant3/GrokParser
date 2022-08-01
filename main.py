from pygrok import Grok
text = 'my name is vikrant and age is 26, my name is abc'
pattern = 'my name is %{WORD:name} and age is %{NUMBER:age}, my name is %{WORD:secondname}'
grok = Grok(pattern)
print(grok.match(text))