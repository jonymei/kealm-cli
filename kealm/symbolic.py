# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import sys
import os
import re

hasExtensions = lambda path, extension: os.path.splitext(path)[-1][1:] in extension

def getfile(extension):
    files = os.listdir()
    exts = [f for f in files if hasExtensions(f, extension)]
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
            index = input('Please select a {} file: '.format(extension))
            if not str.isdigit(index):
                continue
            index = int(index)
            if 0 < index < dlen + 1:
                extf = exts[index - 1]
                break
    return extf

def symbolic():
    #获取crash log文件
    try:
        beta = sys.argv[1]
    except IndexError as e:
        beta = getfile(['beta', 'crash'])
    if not beta:
        print('beta file not found.')
        return
    print('symbolic beta file {}'.format(beta))
    with open(beta, 'r') as f:
        log = f.read()
        print('log length: {}'.format(len(log)))
        uuids = re.findall(r'"slice_uuid":"([0-9a-z]{8}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{12})"', log)
        print('founded uuids: {}'.format(uuids))
        try:
            uuid = uuids[0].upper()
            findcmd = 'mdfind "com_apple_xcode_dsym_uuids == {}"'.format(uuid)
            print(findcmd)
            dsym = os.popen(findcmd, 'r').readlines()[0].rstrip()
        except Exception as e:
            print(e)
            dsym = getfile(['dSYM'])
    if not dsym:
        print('dSYM file not found.')
        return
    print('set dSYM file to {}'.format(dsym))
    #shell
    os.environ['DEVELOPER_DIR'] = '/Applications/XCode.app/Contents/Developer'
    logf = beta.replace('beta', 'log')
    os.system('touch {}'.format(logf))
    symbolicatecrash = '/Applications/Xcode.app/Contents/SharedFrameworks/DVTFoundation.framework/Versions/A/Resources/symbolicatecrash'
    cmd = '{} -d "{}" -o "{}" "{}" > /dev/null'.format(symbolicatecrash, dsym, logf, beta)
    print(cmd)
    os.system(cmd)
    os.system('open {}'.format(logf))


def main():
    symbolic()

if __name__ == '__main__':
    main()





