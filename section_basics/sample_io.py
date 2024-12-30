import sys
import struct
import argparse

parser = argparse.ArgumentParser(description='Read a PLY file')# パーサーの作成　ここのプログラムの説明も持って来れる。
parser.add_argument('filename', type=str, help='PLY file to read')

# 引数の宣言　ここで、デフォルト値の指定や、型の指定、
# ヘルプメッセージの指定や、必須引数の指定もできる。
# 選択肢を追加することもできる。

args = parser.parse_args() #型の解析
#引数は、parse_args()メソッドを呼び出すことで解析され、
#パースされた結果がargsに格納される。

with open(args.filename, 'rb') as f:
    # read header
    while True:
        line = f.readline()
        print (line)
        if b'end_header' in line:
            break
        if b'vertex ' in line:
            vnum = int(line.split(b' ')[-1]) # num of vertices
        if b'face ' in line:
            fnum = int(line.split(b' ')[-1]) # num of faces

    # read vertices
    for i in range(vnum):
        for j in range(3):
            print (struct.unpack('f', f.read(4))[0], end=' ')
        print ("")

    # read faces
    for i in range(fnum):
        n = struct.unpack('B', f.read(1))[0]
        for j in range(n):
            print (struct.unpack('i', f.read(4))[0], end=' ')
        print ("")
