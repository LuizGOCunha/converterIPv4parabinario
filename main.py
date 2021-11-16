def binaryfinder(octet, binary, n):
    if octet >= n:
        octet -= n
        binary += "1"
    else:
        binary += "0"
    return octet, binary


elevation2 = [128, 64, 32, 16, 8, 4, 2, 1]


def octetconverter(octet, binary):
    for n in elevation2:
        octet, binary = binaryfinder(octet, binary, n)
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
            for oct in ip:
                binary += octetconverter(int(oct), binary)
            print(binary)
            break
    except ValueError:
        print('Apenas números!')
    except IndexError:
        print('Coloque os pontos!')

