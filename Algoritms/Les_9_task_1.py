import hashlib


def task(s: str):
    len_subs = 1
    result_set = set()
    for z in range(1, len(s)):
        for j in range(0, len(s) - len_subs + 1):
            subs = s[j:j + len_subs]
            pass
            len_sub = len(subs)
            h_subs = hashlib.sha1(subs.encode('utf-8')).hexdigest()

            for i in range(len(s) - len_sub + 1):
                if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():

                    if s[i:i + len_sub] == subs:
                        result_set.add(subs)
        len_subs += 1
    print(f'Кол-во уникальных подстрок: {len(result_set)}')
    print(result_set)


str = input("Введите текст: ")
task(str.replace(" ", ""))
