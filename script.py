#!/usr/bin/env python3

import collections
import sys

args = sys.argv[1:] # удаляем нулевой элемент, являющийся названием скрипта

# если аргументов не предоставленно - читаем инпут
if len(args) == 0:
    args = sys.stdin.readline().split()

occurances = collections.Counter(args) # получаем dict-like ключи - слова, значения - кол-во повторений
sorted_occurances = sorted(sorted(occurances.items(), key=lambda kv: kv[0]),  key=lambda kv: kv[1], reverse=True)

for (word, count) in sorted_occurances:
    print(word + ' ' + str(count))
