def f(text):
    wyraz = ""
    for i in range(0,len(text)):
        if i != len(text)-1:
            wyraz += text[i]
            wyraz += "-"
        else:
            wyraz += text[i]

    return wyraz
