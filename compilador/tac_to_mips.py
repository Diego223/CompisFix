def tac_mips(listener, visitor):
    asm_code =[]
    asm_code.append('.data\n')
    for context in listener.symbol_table.context:
        for op1, op2 in context.items():
            if 'accessed' in op2 and op2['accessed'] == True:
                if op2['type'] == 'int':
                    if 'valor' in op2 and op2['valor'] != op1:
                        asm_code.append(f"{op1}: .word {op2['valor']}\n")
                    else:
                        asm_code.append(f"{op1}: .word 0\n")
              
                elif op2['type'] == 'bool':
                    asm_code.append(f"{op1}: .byte 0\n")
    asm_code.append('\n.text\n')
    asm_code.append('.globl main\n\n')
    for tac in visitor.aux_code:
        
        line_elements = [element for element in tac]
       
        if len(line_elements) == 2 and line_elements[0].endswith(':'):
            asm_code.append(f"{line_elements[0]}\n")
        else:
            
            if len(line_elements) == 3:  
                if (line_elements[0] == '  '):
                    asm_code.append(
                        f"{line_elements[0]} {line_elements[1]} {line_elements[2]}\n")
                else:
                    asm_code.append(
                        f"{line_elements[0]} {line_elements[1]}, {line_elements[2]}\n")
            elif len(line_elements) == 4: 
                if (line_elements[0] == '  '):
                    asm_code.append(
                        f"{line_elements[0]} {line_elements[1]} {line_elements[2]}, {line_elements[3]}\n")
                else:
                    asm_code.append(
                        f"{line_elements[0]} {line_elements[1]}, {line_elements[2]}, {line_elements[3]}\n")
            elif len(line_elements) == 5:  
                if (line_elements[0] == '  '):
                    asm_code.append(
                        f"{line_elements[0]} {line_elements[1]} {line_elements[2]}, {line_elements[3]}, {line_elements[4]}\n")
                else:
                    asm_code.append(
                        f"{line_elements[0]} {line_elements[1]}, {line_elements[2]}, {line_elements[3]}, {line_elements[4]}\n")
            else:
               
                formatted_line = ' '.join(line_elements)
                asm_code.append(f"{formatted_line}\n")
    return asm_code