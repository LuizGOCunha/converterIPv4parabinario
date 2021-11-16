def binaryfinder(octet, binary, n):
    if octet >= n:
        octet -= n
        binary += "1"
    else:
        binary += "0"
    return octet, binary


def octetconverter(octet, binary):
    octet, binary = binaryfinder(octet, binary, 128)
    octet, binary = binaryfinder(octet, binary, 64)
    octet, binary = binaryfinder(octet, binary, 32)
    octet, binary = binaryfinder(octet, binary, 16)
    octet, binary = binaryfinder(octet, binary, 8)
    octet, binary = binaryfinder(octet, binary, 4)
    octet, binary = binaryfinder(octet, binary, 2)
    octet, binary = binaryfinder(octet, binary, 1)
    return binary


print('Insira seu ip, com os pontos.')
while True:
    try:
        ip = input('>')
        ip = ip.split(".")
        if len(ip) != 4:
            print("Formato Ipv4 apenas!")
        elif int(ip[0]) > 255 or int(ip[1]) > 255 or int(ip[2]) > 255 or int(ip[3]) > 255:
            print('octeto deve ser menor que 255!')
        elif int(ip[0]) < 0 or int(ip[1]) < 0 or int(ip[2]) < 0 or int(ip[3]) < 0:
            print('octeto deve ser maior que 0!')
        else:
            binary = ""
            binary += octetconverter(int(ip[0]), binary)
            binary += octetconverter(int(ip[1]), binary)
            binary += octetconverter(int(ip[2]), binary)
            binary += octetconverter(int(ip[3]), binary)
            print(binary)
            break
    except ValueError:
        print('Apenas números!')
    except IndexError:
        print('Coloque os pontos!')

