f_names = ['random_gen_log_BONUS.txt', 'random_gen_log_random_search.txt', 'website_puzzle_log_BONUS.txt', 'website_puzzle_log_random_search.txt', 'website_puzzle_log.txt']

for f_name in f_names:
    with open(f_name, 'r') as f:
        out = ''

        text = f.read()
        text1 = text[text.find('Run'):].split('\n')
        
        prev_run = -1
        i = 0
        while i < len(text1):
            line = text1[i]

            if line:
                if line[0] == 'R':
                    # it's a run
                    _, this_run = line.split()

                    if this_run != prev_run:
                        # We found a new one!
                        out += '\n' + line + '\n'
                        prev_run = this_run
                        i += 1
                    else:
                        i += 1

                else:
                    out += line + '\n'
                    i += 1
                
            else:
                i += 1
        
        result = text[:text.find('Run')-1] + out


    with open(f_name, 'w') as f:
        f.write(result)