# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import sys
import os

hasExtension = lambda path, extension: os.path.splitext(path)[-1] == '.' + extension

def getfile(extension):
    files = os.listdir()
    exts = [f for f in files if hasExtension(f, extension)]
    dlen = len(exts)
    if dlen == 0:
        return
    elif dlen == 1:
        extf = exts[0]
    else:
        while True:    
            for i in range(0, dlen):
                item = '{}. {}'.format(i + 1, exts[i])
                print(item)
            index = int(input('Please select a file: '))
            if 0 < index < dlen + 1:
                extf = exts[index - 1]
                break
    return extf

def symbolic():
    #TODO: 根据uuid查找
    dsym = getfile('dSYM')
    if not dsym:
        print('dSYM file not found.')
        return
    print('set dSYM file to {}'.format(dsym))
    try:
        beta = sys.argv[1]
    except IndexError as e:
        beta = getfile('beta')
    if not beta:
        print('beta file not found.')
        return
    print('symbolic beta file {}'.format(beta))
    #shell
    os.environ['DEVELOPER_DIR'] = '/Applications/XCode.app/Contents/Developer'
    logf = beta.replace('beta', 'log')
    symbolicatecrash = '/Applications/Xcode.app/Contents/SharedFrameworks/DVTFoundation.framework/Versions/A/Resources/symbolicatecrash'
    cmd = '{} -d {} -o {} {}'.format(symbolicatecrash, dsym, logf, beta)
    print('excuting cmd {}'.format(cmd))
    os.system(cmd)
    os.system('open {}'.format(logf))


def main():
    symbolic()

if __name__ == '__main__':
    main()





