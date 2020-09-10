import emoji
from time import sleep
for c in range(10,-1,-1):
    print(c)
    sleep(1)
print(emoji.emojize('\033[31m:boom:Fogos de Artíficios:boom:\033[m',use_aliases=True))
