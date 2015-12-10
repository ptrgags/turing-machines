#Beginnings of a Brainf**k compiler
def bf(code, input)
  output = ''
  
  #Initial state
  memory = Hash.new 0
  program_ptr = 0
  memory_ptr = 0
  input_ptr = 0
  
  until program_ptr == code.length
    instruction = code[program_ptr]
    case instruction
    when '>'
      memory_ptr += 1
    when '<'
      memory_ptr -= 1
    when '+'
      memory[memory_ptr] += 1
      memory[memory_ptr] %= 256
    when '-'
      memory[memory_ptr] -= 1
      memory[memory_ptr] %= 256
    when '.'
      output += memory[memory_ptr].chr
    when ','
      in_chr = input[input_ptr] || 0
      input_ptr += 1
      memory[memory_ptr] = in_chr.ord
    when '['
      if memory[memory_ptr] == 0
        profile = 1
        until profile == 0
          program_ptr += 1
          if code[program_ptr] == '['
            profile += 1
          elsif code[program_ptr] == ']'
            profile -= 1
          end
        end
      end
    when ']'
      if memory[memory_ptr] != 0
        profile = 1
        until profile == 0
          program_ptr -= 1
          if code[program_ptr] == ']'
            profile += 1
          elsif code[program_ptr] == '['
            profile -= 1
          end
        end
      end
    end
    program_ptr += 1
  end
  output
end

#Hello world
puts bf "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.", ""