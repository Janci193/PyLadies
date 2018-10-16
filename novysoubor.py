#kousek piskvorek
def vyhodnot(hraci_plocha):
    if 'xxx' in hraci_plocha:
        return "x"
    elif 'ooo' in hraci_plocha:
        return "o"
    elif '-' not in hraci_plocha:
        return "!"
    else:
        return "-"