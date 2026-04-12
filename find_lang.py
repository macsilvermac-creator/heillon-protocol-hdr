lines = open('C:\\HEILLON_PROTOCOL_HDR\\index.html', encoding='utf-8', errors='replace').readlines()
kws = ['currentLang', 'activeLang', 'toggleLang', 'setLanguage', 'initLang', 'lang =']
for i, l in enumerate(lines):
    for kw in kws:
        if kw in l and '<script' not in l and '</script' not in l:
            print('%d [%s]: %s' % (i+1, kw, l.strip()[:100]))
            break
