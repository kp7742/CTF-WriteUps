def decrypt(file_path):
    im = Image.open(file_path).convert('RGB')
    pixels = list(im.getdata())
    for i in range(100):
        pixels.append((125,0,0))
    data =[]
    for pixel in pixels:
        data.append(pixel[2])
    line = ''
    for p in data:
        t = "{0:b}".format(p)
        if len(t) < 8:
            t = '0'*(8-len(t)) + t
        line += t
    original = []
    for ch in line:
        if ch == '0':
            original.append((255,255,255))
        else:
            original.append((0,0,0))
    res = b''
    for o in original:
        res += bytes([o[0]]) + bytes([o[1]]) + bytes([o[2]])
    print(len(res), 40000)
    im2 = Image.frombytes('RGB', (200, 200), res)
    pixels = list(im2.getdata())
    print(pixels)
    im2.save("target.png", "PNG")