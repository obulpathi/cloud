import analyze
import textwrap

text = textwrap.dedent(u'''\
    Keep away from people who try to belittle your ambitions. Small people
    always do that, but the really great make you feel that you, too, can
    become great.
    - Mark Twain''')

result = analyze.analyze_syntax(text)
print(result)
