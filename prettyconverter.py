from subprocess import call
import subprocess
import os
import sys
import time
import re
import math
import datetime
from modules.ext_list import EXT_VID, EXT_PIC, formatfix
os.system("")

_placeholder = "--_temp"

############### забираем параметры из батника
progressinfo = re.compile('time=(.*?)\s.*speed=(.*?x)', re.M)
_output = os.getenv("_output")
_params = os.getenv("_params")
_delorig = str(os.getenv("delorig"))
_scriptpath = os.path.dirname(os.path.abspath(__file__))
try:
    _formats = [el.replace(" ", "") for el in os.getenv("_formats").split(",")]
except:
    _formats = []

def clearpath(path=""):
    r = path
    r.strip()
    r = r.replace('"','')
    return os.path.normpath(r)

if os.getenv("_folder"):
    _folder= clearpath(os.getenv("_folder"))
else:
    _folder= ""

##############################

def cutdescr(string):
    tsize = os.get_terminal_size().columns-25
    offs = int(tsize/2)
    return f'{string[0:offs]}...{string[offs*-1:]}' if len(string)>tsize else string    

def clearlaststr(descr=None,lines=1):
    for i in range(lines):
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')
    if descr:
        print(cutdescr(descr))

def progress(current, range, descr=""):
    clearlaststr()
    print(f'[{math.floor(float(current)/float(range)*100)}%] {cutdescr(descr)}')

def getext(name,formats=[]):
    try:
        return [ext for ext in formats if name.lower().endswith(f'.{ext}')][0]
    except:
        return None
    
def getrem(name):
    return name if f'{_placeholder}.' in name else None
    
def parse_folder(folder, template):
    queue = []
    for root, dirs, files in os.walk(os.path.normpath(folder)):
        for file in files:
            if getext(file, template) != None:
                queue.append(os.path.join(root, file))
    return queue

def createqueue(str, template):
    queue = [i.strip() for i in str.split(";")]
    ret_queue = []
    for item in queue:
        if os.path.isfile(item):
            if getext(item, template) != None:
                ret_queue.append(item)
        elif os.path.isdir(item):
            ret_queue+=parse_folder(item, template=_formats)
    return ret_queue

def delfiles(_list):
    _except = []
    for file in _list:
        try:
            os.remove(file)
        except:
            _except.append(file)
    return _except

def get_sec(time_str):
    """Get seconds from time."""
    if type(time_str) is str:
        h, m, s = time_str.split(':')
        return int(h) * 3600 + int(m) * 60 + round(float(s),2)
    elif type(time_str) is float or type(time_str) is int:
        h=int(time_str/3600)
        m=int((time_str%3600)//60)
        s=math.ceil((time_str%3600)%60*100)/100
        return f'{str(h).zfill(2)}:{str(m).zfill(2)}:{str(int(s)).zfill(2)}.{int(s%1*100)}'

def getduration(file):
    duration = subprocess.check_output([f'{_scriptpath}/libs/ffprobe.exe', '-i', file, '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=%s' % ("p=0")]).decode("utf-8")
    return math.ceil(float(duration)*100)/100

def setOutputName(name, outputformat):
    if not os.path.isfile(f'{name}{_placeholder}.{outputformat}'):
        return f'{name}{_placeholder}.{outputformat}'
    else:
        for i in range(30):
            if not os.path.isfile(f'{name}_{str(i)}{_placeholder}.{outputformat}'):
                return f'{name}_{str(i)}{_placeholder}.{outputformat}'

def convertvideo(_input, _params, _output):
    clearname, ext = os.path.splitext(os.path.normpath(_input))
    cmd = f'{_scriptpath}/libs/ffmpeg.exe -y -hide_banner -i "{_input}" {_params} "{setOutputName(clearname, _output)}"'
    _duration = getduration(_input)
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)
        for line in process.stdout:
            if "error" in line.lower():
                print(f"ошибка в файле {_input} : {line}\n\n\n")
                return f"{clearname}{_placeholder}.{_output}"
            elif progressinfo.search(line):
                _time, _speed = progressinfo.search(line).groups()
                progress(get_sec(_time), _duration, descr=f'completed time: [{_time}/{get_sec(_duration)}] speed: [{_speed}]')
                # print(line)
        return None
    except OSError:
        pass

def convertpic(_input, _params, _output="jpeg"):
    clearname, ext = os.path.splitext(os.path.normpath(_input))
    cmd = f'"{_scriptpath}/libs/nconvert.exe" -out {formatfix(_output)} -o "{setOutputName(clearname, _output)}" {_params} "{_input}"'
    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)
        for line in process.stdout:
            if "error" in line.lower():
                print(line+"\n\n\n")
                return f"{clearname}{_placeholder}.{_output}"
        return None
    except OSError:
        pass

def createResult(completed=[], failed=[]):
    print(f"""
Completed: {len(completed)}
Failed: {len(failed)}""")
    if len(failed)>0:
        print("Список необработанных файлов записан в файл")
        homeDir = os.path.expanduser('~')
        with open(os.path.join(homeDir,'Desktop',f'failed_files_{datetime.datetime.now().strftime("%H-%M-%S")}.txt'), 'w') as outfile:
            for item in failed:
                outfile.write(f"{item}\n")
    print("\n\n")


def run():
    equeue = createqueue(_folder, template=_formats)
    todel = []
    completed = []
    failed = []

    type_file = ""

    if _output in EXT_VID:
        type_file = "видео"
        for num, file in enumerate(equeue):
            print(f'[{num+1}/{len(equeue)}] {os.path.basename((file))}\n')
            current = convertvideo(file, _params=_params, _output=_output)
            if current != None:
                todel.append(current)
                failed.append(file)
            else:
                completed.append(file)
            clearlaststr(lines=2)

    elif _output in EXT_PIC:
        type_file = "картинки"
        for num, file in enumerate(equeue):
            progress(num, len(equeue), descr=f'[{num}/{len(equeue)}] {os.path.basename(file)}')
            current = convertpic(file, _params=_params, _output=_output)
            if current != None:
                todel.append(current)
                failed.append(file)
            else:
                completed.append(file)
        
    if len(todel)>0 or len(failed)>0 or len(completed)>0:
        clearlaststr(descr=f'[100%] Все {type_file} переконвертированы!')

        if len(todel)>0:
            time.sleep(2)
            delfiles(todel)

        if _delorig == "True":
            print("Удаляю оригинальные файлы")
            time.sleep(1)
            _except = delfiles(equeue)
            print("Переименовываю временные файлы")
            time.sleep(1)
            torename = []
            torename = [os.path.normpath(f'{os.path.splitext(i)[0]}{_placeholder}.{_output}') for i in completed]
            for file in torename:
                if file.replace(_placeholder,'') in _except:
                    failed.append(file)
                else:
                    os.rename(file, file.replace(f"{_placeholder}.","."))
            clearlaststr(descr=f'{type_file} готовы!')
        
        createResult(completed, failed)


if __name__ == "__main__":
    run()
