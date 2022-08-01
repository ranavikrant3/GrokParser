from pygrok import Grok
text = 'my name is vikrant and age is 26'
pattern = 'my name is %{WORD:name} and age is %{NUMBER:age}'
grok = Grok(pattern)
print(grok.match(text))