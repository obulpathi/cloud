import textwrap

import mlapi as api

text = textwrap.dedent(u'''\
    Keep away from people who try to belittle your ambitions. Small people
    always do that, but the really great make you feel that you, too, can
    become great.
    - Mark Twain''')

result = api.syntax(text)
print(result)
