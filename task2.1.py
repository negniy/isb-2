from math import sqrt
from scipy.special import erfc


def main():
    bits = '01111000011111001010111110011000101010001001000110101110110100001110111100000001000100111101000011001100110111110110011010010011'
    ones = bits.count('1')
    zeros = bits.count('0')
    sum = ones+(-1)*zeros
    S = sum/sqrt(128)
    P = erfc(S / sqrt(2))
    print(P)
    if (P < 0.01):
        print("Failed  test")
    else:
        print( "Passed  test")

if __name__ == "__main__":
    main()


#0.8596837951986662
#тест пройден