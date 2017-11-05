head='# Deep Architecture Genealogy\n' \
     'There are so many new models and archtectures. ' \
     'If you find something inetresting and worth to pay attention, please let us know.\n' \
     '## Mindmap Coggle Link\n' \
     'https://coggle.it/diagram/Wf5mYoJbsgABUF9P\n' \
     '## Text Version\n'

tail = '\n## Mind Map (IMG)\n' \
       '![https://coggle.it/diagram/Wf5mYoJbsgABUF9P](Neural_Net_Arch_Genealogy.png)'

with open('Neural Net Arch Genealogy.txt') as fin, open('README.md', 'w') as fout:
    fout.write(head)
    for line in fin:
        tab_count = line.count('\t')
        if not tab_count:
            continue

        spaces = ['  ' for i in range(tab_count-1)]
        fout.write(''.join(spaces) + '* ' + line.replace('\t', ''))

    fout.write(tail)