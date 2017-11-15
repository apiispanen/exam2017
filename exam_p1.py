trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si', '5':'wu', 
         '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi', '100': 'bai'}



def speak_Chinese(number):
    if number != int(number) or not 0<=int(number)<=999:
        print('无效号码。 请输入0到999之间的整数.')
    else: 
        intnumber = number
        number = str(number)
        if 0<=intnumber<=10:
            return trans[number]
        if 11<=intnumber<=19:
            return '{} {}'.format(trans['10'],trans[number[1]])
        if 20<=intnumber<=99:
            if number[1] == '0':
                return '{} {}'.format(trans[number[0]],trans['10'])    
            else:
                return '{} {} {}'.format(trans[number[0]],trans['10'],trans[number[1]])
        if 100<=intnumber<=999:
            if number[1]=='0' and number[2]!='0':
                return '{} {} {} {}'.format(trans[number[0]],trans['100'],trans['0'],trans[number[2]])
            if number[2]=='0' and number[1]!='0':
                return '{} {} {} {}'.format(trans[number[0]],trans['100'],trans[number[1]],trans['10'])
            if number[1]=='0' and number[2]=='0':
                return '{} {} '.format(trans[number[0]],trans['100'])
            else:
                return '{} {} {} {} {}'.format(trans[number[0]],trans['100'],trans[number[1]],trans['10'], trans[number[2]])
# For testing
def main():
    print(speak_Chinese(36))
    print('In Chinese: 36 = san shi liu')
    print(speak_Chinese(20))
    print('In Chinese: 20 = er shi')
    print(speak_Chinese(16))
    print('In Chinese: 16 = shi liu')
    print(speak_Chinese(200))
    print('In Chinese: 200 = er bai')
    print(speak_Chinese(109))
    print('In Chinese: 109 = yi bai ling jiu')
    print(speak_Chinese(999))
    print('In Chinese: 999 = jiu bai jiu shi jiu')

if __name__ == '__main__':
    main()
