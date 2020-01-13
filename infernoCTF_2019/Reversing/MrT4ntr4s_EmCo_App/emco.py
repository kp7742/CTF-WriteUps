def encrypt(file_path):
    im = Image.open(file_path).convert('RGB')
    width, height = im.size
    pixels = list(im.getdata())
    pixels = [ pixels[i * width:(i + 1) * width] for i in range(height) ]
    binary_pixels = []
    for item in pixels:
        for pixel in item:
            if pixel == (255, 255, 255):
                binary_pixels.append('0')
            else:
                binary_pixels.append('1')
    
    line = ''.join(binary_pixels)
    n = 8
    enc = [ int(line[i:i + n], 2) for i in range(0, len(line), n) ]
    data = ''
    enc_len = len(enc)
    s = int(sqrt(enc_len))
    for i in range(enc_len):
        data += chr(125) + chr(0) + chr(enc[i])
    im2 = Image.frombytes('RGB', (s, s), data.encode())
    im2.save('encrypted.png', 'PNG')