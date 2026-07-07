class edit_file:
    global all_content
    def flw(cmd,add_line):
        if cmd == 'all':
                print('==========FLW==========')
                line_flw = 1
                for line_flw_all in all_content:
                    print(f'{line_flw:>{add_line}}.{line_flw_all}')
                    line_flw += 1
        elif ' to ' in cmd:
            print('==========FLW==========')
            try:
                line_flw_start, line_flw_end = cmd.split(' to ')
                line_flw_start = int(line_flw_start) - 1
                line_flw_end = int(line_flw_end)
                flw_content = all_content[line_flw_start:line_flw_end]
                for line_flw in flw_content:
                    print(f'{line_flw_start + 1:>{add_line}}.{line_flw}')
                    line_flw_start += 1
            except ValueError:
                print('Error:Not found data')
            print('=======================')
        else:
            print('==========FLW==========')
            try:
                line_flw = int(cmd) - 1
                print(f'Flw: {line_flw + 1}.{all_content[line_flw]}')
            except ValueError:
                print('Error:Not found data')
            except Exception:
                print(f'Error:Your text has only {len(all_content)}')
            print('=======================')
    def fix(cmd):
        global all_content
        print('==========FIX==========')
        try:
            line_fix = int(cmd) - 1
            text_fix = input(f'Fix:{line_fix + 1}.{all_content[line_fix]}\nTo:')
            all_content[line_fix] = text_fix
        except ValueError:
            print('Error:Not found data')
        except Exception:
            print(f'Error:Your text has only {len(all_content)} lines')
        print('=======================')
    def clr(cmd):
        global all_content
        if cmd == 'all':
            while True:
                confirm = input('Want to clear all?(y/n):').strip().lower()
                if confirm == 'y':
                    all_content = []
                    break
                else:
                    break
        else:
            if ' to ' in cmd:
                try:
                    line_clr_start, line_clr_end = cmd.split(' to ')
                    line_clr_start = int(line_clr_start) - 1
                    line_clr_end = int(line_clr_end)
                    del all_content[line_clr_start:line_clr_end]
                except ValueError:
                    print('Error:Not found data')
                except Exception:
                    print(f'Error:Your text has only {len(all_content)} lines')
            else:
                try:
                    line_clr = int(cmd) - 1
                    all_content.pop(line_clr)
                except ValueError:
                    print('Error:Please type number')
                except Exception:
                    print(f'Error:Your text has only {len(all_content)} lines')
    def add(cmd):
        global all_content
        try:
            line_add = int(cmd) - 1
            text_add = input(f'Add:{line_add + 1}.')
            all_content.insert(line_add,text_add)
        except ValueError:
            print('Error:Please type number')
    def lct(cmd,add_line):
        global all_content
        print('==========LCT==========')
        try:
            line_lc = int(cmd) - 1
            if line_lc > len(all_content):
                print(f'Error:Your text has {len(all_content)} lines')
            while True:
                text_lc = input(f'{line_lc + 1:>{add_line}}.')
                if text_lc.strip() == '!exit':
                    break
                all_content.insert(line_lc,text_lc)
                line_lc += 1
        except ValueError:
            print('Error:Not found data')
        print('=======================')
    def copy(cmd):
        global all_content,copy_var
        try:
            if ' to ' in cmd:
                try:
                    line_copy_start, line_copy_end = cmd.split(' to ')
                    line_copy_start = int(line_copy_start) - 1
                    line_copy_end = int(line_copy_end)
                    copy_var = all_content[line_copy_start:line_copy_end]
                except ValueError:
                    print('Error:Not found copy data')
            elif cmd == 'all':
                copy_var = all_content[:]
            else:
                copy_var = [all_content[int(cmd) - 1]]
        except ValueError:
            print('Error:Please type number')
    def paste(cmd):
        global all_content,copy_var
        if not copy_var:
            print('Error:Not found copied data')
            return
        if cmd == '':
            all_content.extend(copy_var)
        else:
            try:
                for var in reversed(copy_var):
                    all_content.insert(int(cmd) - 1,var)
            except ValueError:
                print('Error:Not found line need to copy')
    def find(cmd):
        global all_content
        print('==========FIND==========')
        line = 1
        all_line_find = []
        for line_find in all_content:
            if cmd in line_find:
                all_line_find.append(line)
            line += 1
        print(f'Found "{cmd}" in line {all_line_find}')
        print('========================')
    def repl(cmd):
        global all_content
        try:
            text,text_replace = cmd.split(' to ')
        except ValueError:
            print('Error:Not found replaced text')
        for line_replace in range(len(all_content)):
            all_content[line_replace] = all_content[line_replace].replace(text,text_replace)                    
    def info():
        global all_content
        char = 0
        word = 0
        byte = 0
        print('==========INFO==========')
        print(f'Line:{len(all_content)}')
        for line_2 in all_content:
            char += len(line_2)
        print(f'Characters:{char}')
        for line_2 in all_content:
            word += len(line_2.split())
        print(f'Words:{word}')
        for line_2 in all_content:
            byte += len(line_2) + 1
        print(f'Byte:{byte}')
        print('========================')
class file_io:
    global all_content,save_path,load_path
    def save(cmd):
        global all_content,save_path,load_path
        print('==========SAVE==========')
        save_path = cmd
        if save_path == '':
            save_path = load_path
        save_content = ''
        for content in all_content:
            save_content += f'{content}\n'
        try:
            with open(save_path,'w',encoding = 'utf-8') as f:
                f.write(save_content)
            print(f'Save:Saved {save_path}')
        except FileNotFoundError:
            print("Error:Not found file's path")
        print('========================')
    def load(cmd,add_line):
        global all_content,save_path,load_path
        print('==========LOAD==========')
        load_path = cmd
        try:
            with open(load_path,'r',encoding = 'utf-8-sig') as f:
                load_content = f.read().splitlines()
            all_content = load_content
            line = 1
            for content in all_content:
                print(f'{line:>{add_line}}.{content}')
                line += 1
        except FileNotFoundError:
            print(f'Error:Not found file {load_path}')
            print('========================')
class term_display:
    global all_content
    def clr(add_line):
        print('\n' * 200,flush = True)
        edit_file.flw('all',add_line)
    def prt_all():
        global all_content
        print(all_content)
class main:
    def edit(add_line,path_load):
        global all_content,load_path,copy_var
        all_content = []
        save_content = ''
        save_path = ''
        copy_var = ''
        if path_load:
            try:
                with open(path_load,'r',encoding = 'utf-8-sig') as f:
                    load_content = f.read().splitlines()
                    load_path = path_load
                all_content = load_content
                line = 1
                for content in all_content:
                    print(f'{line:>{add_line}}.{content}')
                    line += 1
            except FileNotFoundError:
                try:
                    file_io.save(path_load)
                    file_io.load(path_load,add_line)
                except FileNotFoundError:
                    print("Error:Not found file's path")
        while True:
            try:
                line = len(all_content) + 1
                line_input = input(f'{line:>{add_line}}.')
                if line_input.strip().startswith('!'):
                    cmd = line_input[1:]
                    if cmd == 'exit':
                        print('========================')
                        break
                    elif cmd == 'help':
                        print('''==========HLP==========
!help for more commands
!flw [line] to show line which you want
!fix [line] to edit line which you want
!clr [line] or [line to line] or all to clear line which you want or clear all
!add [line] to add text at line which you want
!lct [line] to place the cursor where you want
!replace or !repl [text to text] to replace text to new text
!find [text] to find text
!copy or !c [line] or [line to line] or all to copy data where you want
!paste or !p [line] to paste data where you want
!save [path] or nothing to save file (nothing that knows to save loaded file)
!load [path] to load file
?clr to clear screen
=======================''')
                    elif cmd == 'info':
                        edit_file.info()
                    elif cmd.startswith('flw'):
                        edit_file.flw(cmd[4:],add_line)
                    elif cmd.startswith('fix'):
                        edit_file.fix(cmd[4:])
                    elif cmd.startswith('clr'):
                        edit_file.clr(cmd[4:])
                    elif cmd.startswith('add'):
                        edit_file.add(cmd[4:])
                    elif cmd.startswith('lct'):
                        edit_file.lct(cmd[4:],add_line)
                    elif cmd.startswith('save'):
                        file_io.save(cmd[5:])
                    elif cmd.startswith('load'):
                        file_io.load(cmd[5:],add_line)
                    elif cmd.startswith('find'):
                        edit_file.find(cmd[5:])
                    elif cmd.startswith('replace') or cmd.startswith('repl'):
                        if cmd.startswith('replace'):
                            edit_file.repl(cmd[8:])
                        else:
                            edit_file.repl(cmd[5:])
                    elif cmd.startswith('copy') or cmd.startswith('c'):
                        if cmd.startswith('copy'):
                            edit_file.copy(cmd[5:])
                        else:
                            edit_file.copy(cmd[2:])
                    elif cmd.startswith('paste') or cmd.startswith('p'):
                        if cmd.startswith('paste'):
                            edit_file.paste(cmd[6:])
                        else:
                            edit_file.paste(cmd[1:])
                    else:
                        print('Error:Command not found')
                elif line_input.strip().startswith('?'):
                    cmd_1 = line_input[1:].strip()
                    if cmd_1 == 'clr':
                        term_display.clr(add_line)
                    elif cmd_1 == 'prt_all':
                        term_display.prt_all()
                    else:
                        print('Error:Command not found')
                else:
                    all_content.append(line_input)
            except KeyboardInterrupt:
                force_exit = input('\n\n\nWant to save file after exit?(y/n):').strip()
                if force_exit == 'y':
                    while True:
                        try:
                            path_exit = input('Path file:')
                            file_io.save(path_exit)
                            break
                        except BaseException:
                            print('Error:Path file not found')
                            print('========================')
                else:
                    break
    def read(path,add_line):
        print('==========READ==========')
        line = 1
        try:
            with open(path,'r',encoding = 'utf-8-sig') as f:
                all_content = f.read().splitlines()
            for line_read in all_content:
                print(f'{line:>{add_line}}.{line_read}')
                line += 1
        except FileNotFoundError:
            print(f'Error:Path "{path}" not found')
        print('========================')
    def info(path):
        try:
            with open(path,'r',encoding = 'utf-8-sig') as f:
                all_content = f.read().splitlines()
            print('==========INFO==========')
            char = 0
            word = 0
            byte = 0
            print(f'Line:{len(all_content)}')
            for line_2 in all_content:
                char += len(line_2)
            print(f'Characters:{char}')
            for line_2 in all_content:
                word += len(line_2.split())
            print(f'Words:{word}')
            for line_2 in all_content:
                byte += len(line_2) + 1
            print(f'Byte:{byte}')
            print('========================')
        except FileNotFoundError:
            print(f'Error:Path "{path}" not found')
    def copy(cmd):
        try:
            path,copy_path = cmd.split(' to ')
        except ValueError:
            print('Error:Not found path')
        try:
            with open(path,'r',encoding = 'utf-8-sig') as f:
                content = f.read()
        except FileNotFoundError:
            print('Error:Not found data')
        try:
            with open(copy_path,'w',encoding = 'utf-8') as f:
                f.write(content)
        except FileNotFoundError:
            print('Error:Not found path')
        print('Copy Completed')
    def set_var(var):
        global limit
        if var.startswith('limit'):
            try:
                limit = int(var.split(' ',maxsplit = 1)[1])
                print(f'Set limit = {limit}')
            except ValueError:
                limit = 4
                print('Error:Please type number')
        else:
            print(f'Error:Not found variable "{var}"')  
if __name__ == '__main__':
    limit = 4
    print('Term_editor version 0.1')
    print('"help" for some command' )
    while True:
        try:
            mode = input('>').strip()
            if mode == 'exit':
                exit()
            elif mode == '':
                continue
            elif mode == 'help':
                print('''set [variable] to edit variable
edit [path] to edit file or create file
read [path] to read and display file's content
info [path] to show file's infomation
copy [path to path need to copy] to copy file to file
exit to exit program
clr to clear terminal''')
            elif mode == 'clr':
                print('\n' * 200,flush = True)
            elif mode == 'ver':
                print('Term_editor version 0.1')
            elif mode.startswith('set'):
                main.set_var(mode[4:])
            elif mode.startswith('edit'):
                print('==========EDIT==========')
                path = mode[5:]
                main.edit(limit,path)
            elif mode.startswith('read'):
                main.read(mode[5:],limit)
            elif mode.startswith('info'):
                main.info(mode[5:])
            elif mode.startswith('copy'):
                main.copy(mode[5:])
            else:
                print(f'Error:Not found command "{mode}"')
        except KeyboardInterrupt:
            code = input('\n\n\nForce exit completed').lower()
            if code == ' that is a suck editor':
                for i in range(67):
                    with open(f'suck_{i}.suck','w') as hole:
                        hole.write('Idiot will type this.')
            exit()
