numbers = [4,6,2,11,1,11,5]
def FindSecond (arr):
    arr=set(arr)
    arr.remove(max(arr))
    print(max(arr))
FindSecond(numbers)

numbers = [15, 7, 28, 10, 21]
def FindSecond (arr):
    arr=set(arr)
    arr.remove(max(arr))
    print(max(arr))
FindSecond(numbers)

import re
text = """
Вчера Анна и Артем гуляли в парке. Анна заметила слово level на
старом плакате. Рядом кто-то написал radar, а чуть дальше было
нарисовано слово kayak. На скамейке сидел человек с книгой civic,
а возле фонтана дети мелом написали refer. Остальные слова в тексте
палиндромами не являются."""
def FindPal(text):
    text=text.lower()
    text=re.findall(r"\w+", text)
    answer = [w for w in text if len(w)>1 and w==w[::-1]]
    return answer
print(FindPal(text))



