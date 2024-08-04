
import sys
import re
import libpwl

class PWLUtil:
    def __init__(self):
        self.m_pwl_filename         = ''
        self.m_find                 = ''
        self.m_pwl_output_filename  = ''
        self.m_pwls                 = []
    def PrintUsage(self):
        print(f'# pwl_util.py usage:')
        print(f'% python3 pwl_util.py pwl_file find_str output_file')
    def ReadArgs(self, args):
        print(f'# read args start')
        if 4 != len(args):
            self.PrintUsage()
            exit()
        self.m_pwl_filename     = args[1]
        self.m_find             = args[2]
        self.m_pwl_output_filename  = args[3]
        #self.m_recompile    = re.compile(r'{self.m_find}')
        print(f'# read args end')
    def PrintInputs(self):
        print(f'# print inputs start')
        print(f'    input pwl file  : {self.m_pwl_filename}')
        print(f'    find_str        : {self.m_find}')
        print(f'    output pwl file : {self.m_pwl_output_filename}')
        print(f'    find re compile : {self.m_recompile}')
        print(f'# print inputs end')
    def ReadPWL(self):
        print(f'# read pwl file({self.m_pwl_filename}) start')
        f_pwl       = open(self.m_pwl_filename, 'rt')
        lines       = ''
        while True:
            line = f_pwl.readline()
            if not line:
                break
            if '+' == line[0]:
                lines.append(line[1:])
            else:
                lines   = lines.replace('+', ' ')
                lines   = lines.replace('(', ' ')
                lines   = lines.replace(')', ' ')
                tokens  = lines.split()
                if 0 == len(tokens):
                    continue
                # srcname nodename1 nodename2 pwl t1 v1 t2 v2 ...
                pwl     = libpwl.PWL()
                pwl.SetName(tokens[0])
                pwl.SetPosNodename(tokens[1])
                pwl.SetNegNodename(tokens[2])
                for pos in range(3, len(tokens), 2):
            f_pwl.close()
        print(f'# read pwl file({self.m_pwl_filename}) end')
    def PrintXs(self):
        print(f'# print xs start')
        for x in self.m_xs:
            print(f'{x}')
        print(f'# print xs end')
    def PrintYsDic(self):
        print(f'# print ys dic start')
        for key in self.m_ys_dic:
            ys  = self.m_ys_dic[key]
            print(f'i{key} {key} 0 pwl')
            for pos in range(0, len(ys)):
                print(f'+ {self.m_xs[pos]} {ys[pos]}')
        print(f'# print ys dic end')
    def Run(self, args):
        print(f'# pwl_util.py start')
        self.ReadArgs(args)
        self.PrintInputs()
        self.ReadPWL()
        print(f'# pwl_util.py end')
    def Atof2(self):

def main(args):
    my_pwl_util  = PWLSum()
    my_pwl_util.Run(args)

if __name__ == '__main__':
    main(sys.argv):1
    :1