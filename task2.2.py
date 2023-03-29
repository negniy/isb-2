from math import sqrt
from scipy.special import erfc


def main():
    bits = '01111000011111001010111110011000101010001001000110101110110100001110111100000001000100111101000011001100110111110110011010010011'
    f1 = bits.count('1') /128
    num = 0
    for i in range (1,128):
        if bits[i] != bits[i-1]:
            num+=1
    P = erfc( abs(num-2*128*f1*(1-f1))/(2*sqrt(2*128)*f1*(1-f1)) )
    print(P) 
    if (P < 0.01):
        print("Failed  test")
    else:
        print( "Passed  test")

if __name__ == "__main__":
    main()

#0.5977098069466218 тест пройден