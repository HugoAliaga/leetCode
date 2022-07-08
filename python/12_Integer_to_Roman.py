class Solution(object):
    def intToRoman(self, num):
        res = ''
        mil = num // 1000
        rem = num - mil*1000

        novec = rem // 900
        rem = rem - novec*900

        quin = rem // 500 
        rem = rem - quin*500

        cuat = rem // 400
        rem = rem - cuat*400

        cien = rem // 100
        rem = rem - cien*100

        nov = rem // 90
        rem = rem - nov*90

        cincu = rem // 50
        rem = rem - cincu*50

        cuar = rem // 40
        rem = rem - cuar*40

        diez = rem // 10
        rem = rem - diez*10

        nueve = rem // 9
        rem = rem - nueve*9

        cinco = rem // 5
        rem = rem - cinco*5

        cuatr = rem // 4
        uno = rem - cuatr*4

        res += mil*'M' + novec*'CM' + quin*'D' + cuat*'CD' + cien*'C' + nov*'XC' + cincu*'L' + cuar*'XL' + diez*'X' + nueve*'IX' + cinco*'V' + cuatr*'IV' + uno*'I'
        return res

tests = []
solutions = []

tests.append(500)
solutions.append('D')

tests.append(423)
solutions.append('CDXXIII')

tests.append(67)
solutions.append('LXVII')

tests.append(1)
solutions.append('I')

tests.append(1564)
solutions.append('MDLXIV')

tests.append(1964)
solutions.append('MCMLXIV')

tests.append(41)
solutions.append('XLI')



for i in range(len(tests)):
    result = Solution().intToRoman(tests[i])
    print('Test ' + str(i),'Result',result,solutions[i])