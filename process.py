import sys
import re

if len(sys.argv) != 2:
    print('Usage: python process.py [filename]')
    sys.exit()

try:
    f = open(sys.argv[1], 'r')
    content = f.read()
    f.close()
except:
    print('Error: File not found')
    sys.exit()

instructions = re.findall(r'[01]{8}', content)

REG = [0] * 4
MEM = [ (i if i < 16 else 16 - i) for i in range(32)]
disp = 0
pc = 0

if __name__ == '__main__':
    while True:
        instr = instructions[pc]
        print(f'assign memory[{pc}] = 8\'b{instr};')
        print(f'// PC({pc}) INSTR({instr})')
        opcode = instr[0:2]
        rs = int(instr[2:4], 2)
        rt = int(instr[4:6], 2)
        rd = int(instr[6:8], 2)

        print(f'// OPCODE({opcode}) RS({rs}) RT({rt}) RD/IMM({rd})')

        if opcode == '00':
            print(f'// [ADD] REG[{REG[rs]}]({hex(REG[rs])}) + REG[{REG[rt]}]({hex(REG[rt])}) to REG[{rd}]')
            res = REG[rs] + REG[rt]
            REG[rd] = res
            disp = res
        elif opcode == '01':
            print(f'// [SAVE] MEM[{REG[rs]} + {rd}]({MEM[REG[rs] + rd]}) to REG[{rt}]')
            res = MEM[REG[rs] + rd]
            REG[rt] = res
            disp = res
        elif opcode == '10':
            print(f'// [LOAD] REG[{rt}]({hex(REG[rt])}) to MEM[{REG[rs]} + {rd}]')
            res = REG[rt]
            MEM[REG[rs] + rd] = res
        elif opcode == '11':
            imm = rd
            if imm > 1:
                imm -= 4
            print(f'// [JMP] IMM({rd})')
            if imm == -1:
                print('[!] End Of Instructions: Infinite loop')
                break
        
        print('// ', end= '')
        for i, r in enumerate(REG):
            print(f'REG[{i}]({hex(r)})', end=' ')
        print(f'DISP({hex(disp)})', end=' ')

        print('\n')
        pc += 1
