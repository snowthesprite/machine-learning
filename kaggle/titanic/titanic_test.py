from parse_line import *

print('Does parse_line work?')

line_1 = "1,0,3,'Braund, Mr. Owen Harris',male,22,1,0,A/5 21171,7.25,,S"

assert parse_line(line_1) == ['1', '0', '3', "'Braund, Mr. Owen Harris'", 'male', '22', '1', '0', 'A/5 21171', '7.25', '', 'S']

line_2 = '102,0,3,"Petroff, Mr. Pastcho (""Pentcho"")",male,,0,0,349215,7.8958,,S'

assert parse_line(line_2) == ['102', '0', '3', '"Petroff, Mr. Pastcho (""Pentcho"")"', 'male', '', '0', '0', '349215', '7.8958', '', 'S']

line_3 = '187,1,3,"O\'Brien, Mrs. Thomas (Johanna ""Hannah"" Godfrey)",female,,1,0,370365,15.5,,Q'

assert parse_line(line_3) == ['187', '1', '3', '"O\'Brien, Mrs. Thomas (Johanna ""Hannah"" Godfrey)"', 'female', '', '1', '0', '370365', '15.5', '', 'Q']

print('Yes it does!')