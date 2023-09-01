from subprocess import call
import subprocess
import os
import sys
import time
import re
import math
import datetime
os.system("")

allext = ['3dostr', '3g2', '3gp', '4xm', 'a64', 'aa', 'aac', 'aax', 'ac3', 'ace', 'acm', 'act', 'adf', 'adp', 'ads', 'adts', 'adx', 'aea', 'afc', 'aiff', 'aix', 'alaw', 'alias_pix', 'alp', 'amr', 'amrnb', 'amrwb', 'amv', 'anm', 'apac', 'apc', 'ape', 'apm', 'apng', 'aptx', 'aptx_hd', 'aqtitle', 'argo_asf', 'argo_brp', 'argo_cvg', 'asf', 'asf_o', 'asf_stream', 'ass', 'ast', 'au', 'av1', 'avi', 'avif', 'avisynth', 'avm2', 'avr', 'avs', 'avs2', 'avs3', 'bethsoftvid', 'bfi', 'bfstm', 'bin', 'bink', 'binka', 'bit', 'bitpacked', 'bmp_pipe', 'bmv', 'boa', 'bonk', 'brender_pix', 'brstm', 'c93', 'caca', 'caf', 'cavsvideo', 'cdg', 'cdxl', 'chromaprint', 'cine', 'codec2', 'codec2raw', 'concat', 'crc', 'cri_pipe', 'dash', 'data', 'daud', 'dcstr', 'dds_pipe', 'derf', 'dfa', 'dfpwm', 'dhav', 'dirac', 'dnxhd', 'dpx_pipe', 'dsf', 'dshow', 'dsicin', 'dss', 'dts', 'dtshd', 'dv', 'dvbsub', 'dvbtxt', 'dvd', 'dxa', 'ea', 'ea_cdata', 'eac3', 'epaf', 'exr_pipe', 'f32be', 'f32le', 'f4v', 'f64be', 'f64le', 'ffmetadata', 'fifo', 'fifo_test', 'film_cpk', 'filmstrip', 'fits', 'flac', 'flic', 'flv', 'framecrc', 'framehash', 'framemd5', 'frm', 'fsb', 'fwse', 'g722', 'g723_1', 'g726', 'g726le', 'g729', 'gdigrab', 'gdv', 'gem_pipe', 'genh', 'gif', 'gif_pipe', 'gsm', 'gxf', 'h261', 'h263', 'h264', 'hash', 'hca', 'hcom', 'hdr_pipe', 'hds', 'hevc', 'hls', 'hnm', 'ico', 'idcin', 'idf', 'iff', 'ifv', 'ilbc', 'image2', 'image2pipe', 'imf', 'ingenient', 'ipmovie', 'ipod', 'ipu', 'ircam', 'ismv', 'iss', 'iv8', 'ivf', 'ivr', 'j2k_pipe', 'jacosub', 'jpeg_pipe', 'jpegls_pipe', 'jpegxl_pipe', 'jv', 'kux', 'kvag', 'laf', 'latm', 'lavfi', 'libcdio', 'libmodplug', 'libopenmpt', 'live_flv', 'lmlm4', 'loas', 'lrc', 'luodat', 'lvf', 'lxf', 'm4v', 'matroska', 'matroska', 'webm', 'mca', 'mcc', 'md5', 'mgsts', 'microdvd', 'mjpeg', 'mjpeg_2000', 'mlv', 'mm', 'mmf', 'mods', 'moflex', 'mov', 'mov', 'mp4', 'm4a', '3gp', '3g2', 'mp3', 'mp4', 'mpc', 'mpc8', 'mpeg', 'mpeg1video', 'mpeg2video', 'mpegts', 'mpegtsraw', 'mpegvideo', 'mpjpeg', 'mpl2', 'mpsub', 'msf', 'msnwctcp', 'msp', 'mtaf', 'mtv', 'mulaw', 'musx', 'mv', 'mvi', 'mxf', 'mxf_d10', 'mxf_opatom', 'mxg', 'nc', 'nistsphere', 'nsp', 'nsv', 'null', 'nut', 'nuv', 'obu', 'oga', 'ogg', 'ogv', 'oma', 'opus', 'paf', 'pam_pipe', 'pbm_pipe', 'pcx_pipe', 'pfm_pipe', 'pgm_pipe', 'pgmyuv_pipe', 'pgx_pipe', 'phm_pipe', 'photocd_pipe', 'pictor_pipe', 'pjs', 'pmp', 'png_pipe', 'pp_bnk', 'ppm_pipe', 'psd_pipe', 'psp', 'psxstr', 'pva', 'pvf', 'qcp', 'qdraw_pipe', 'qoi_pipe', 'r3d', 'rawvideo', 'realtext', 'redspark', 'rl2', 'rm', 'roq', 'rpl', 'rsd', 'rso', 'rtp', 'rtp_mpegts', 'rtsp', 's16be', 's16le', 's24be', 's24le', 's32be', 's32le', 's337m', 's8', 'sami', 'sap', 'sbc', 'sbg', 'scc', 'scd', 'sdl', 'sdl2', 'sdp', 'sdr2', 'sds', 'sdx', 'segment', 'ser', 'sga', 'sgi_pipe', 'shn', 'siff', 'simbiosis_imx', 'sln', 'smjpeg', 'smk', 'sol', 'sox', 'spdif', 'spx', 'srt', 'stl', 'subviewer', 'subviewer1', 'sunrast_pipe', 'sup', 'svag', 'svcd', 'svg_pipe', 'svs', 'swf', 'tak', 'tedcaptions', 'tee', 'thp', 'tiertexseq', 'tiff_pipe', 'tmv', 'truehd', 'tta', 'ttml', 'tty', 'txd', 'ty', 'u16be', 'u16le', 'u24be', 'u24le', 'u32be', 'u32le', 'u8', 'v210x', 'vag', 'vbn_pipe', 'vc1', 'vc1test', 'vcd', 'vfwcap', 'vidc', 'vividas', 'vivo', 'vmd', 'vob', 'vobsub', 'voc', 'vpk', 'vplayer', 'vqf', 'w64', 'wady', 'wav', 'wc3movie', 'webm', 'webm_chunk', 'webp_pipe', 'webvtt', 'wsaud', 'wsd', 'wsvqa', 'wtv', 'wv', 'wve', 'xa', 'xbin', 'xbm_pipe', 'xmd', 'xmv', 'xpm_pipe', 'xvag', 'xwd_pipe', 'xwma', 'yop', 'yuv4mpegpipe',]
allpic = ['2bp', '2d', '3fr', '411', 'a64', 'abmp', 'abr', 'abs', 'acc', 'ace', 'aces', 'acorn', 'adex', 'adt', 'afdesig', 'afphoto', 'afpub', 'afx', 'ai', 'aim', 'aip', 'aipd', 'alias', 'ami', 'ani', 'anv', 'aphp', 'apx', 'arcib', 'arf', 'arn', 'art', 'artdir', 'arw', 'atk', 'att', 'aurora', 'avs', 'avw', 'az7', 'b16', 'b3d', 'bdr', 'bfli', 'bfx', 'bga', 'bias', 'bif', 'biorad', 'bip', 'bld', 'blend', 'blp', 'bmc', 'bmg', 'bmp', 'bmp565', 'bms', 'bmx', 'bob', 'bpr', 'brk', 'bsg', 'btn', 'bum', 'byusir', 'c4', 'cadc', 'cals', 'cam', 'can', 'car', 'cart', 'cat', 'cbmf', 'cdr', 'cdu', 'ce', 'ce1', 'cel', 'cft', 'cgm', 'che', 'cin', 'cip', 'ciph', 'cipt', 'cish', 'cism', 'cloe', 'clp', 'cmt', 'cmu', 'cmx', 'cncd', 'cnct', 'cp8', 'cpa', 'cpat', 'cpc', 'cpt', 'cr2', 'craw', 'crd', 'crg', 'crw', 'csv', 'ct', 'cur', 'cut', 'cvp', 'cwg', 'd3d', 'dali', 'dbw', 'dcmp', 'dcpy', 'dcr', 'dcx', 'dd', 'dds', 'degas', 'dib', 'dicom', 'dkb', 'dng', 'dol', 'doodle', 'dpx', 'drz', 'dsi', 'dta', 'dwg', 'dwg', 'ecc', 'efx', 'eidi', 'eif', 'emf', 'emz', 'epa', 'epi', 'eps', 'epsp', 'erf', 'esm', 'esmp', 'eyes', 'f96', 'face', 'fax', 'fbm', 'fcx', 'fff', 'fff', 'ffpg', 'fgs', 'fi', 'fit', 'fits', 'fli', 'fmag', 'fmap', 'fmf', 'fp2', 'fpg', 'fpr', 'fpt', 'fre', 'frm', 'frm2', 'fsh', 'fsy', 'ftf', 'fx3', 'fxs', 'g16', 'g3n', 'gaf', 'gbr', 'gcd', 'gem', 'geo', 'gfaray', 'gg', 'gicon', 'gig', 'gih', 'gm', 'gmf', 'god', 'gpat', 'gpb', 'grob', 'gun', 'hdri', 'hdru', 'hed', 'heic', 'hf', 'hir', 'hpgl', 'hpi', 'hr', 'hru', 'hrz', 'hsi', 'hta', 'iam', 'icb', 'icd', 'icl', 'icn', 'icns', 'ico', 'icon', 'iff', 'ifx', 'iim', 'iimg', 'ilab', 'im5', 'img', 'imgt', 'imi', 'imt', 'indd', 'info', 'ingr', 'insp', 'ioca', 'ipg', 'ipl', 'ipl2', 'ipn', 'ipseq', 'ipt', 'iris', 'ish', 'iss', 'j6i', 'jbf', 'jbr', 'jif', 'jig', 'jig2', 'jj', 'jls', 'jp2', 'jpeg', 'jpegxl', 'jps', 'jtf', 'jxr', 'k25', 'k25b', 'kdc', 'kdc2', 'kfx', 'kntr', 'koa', 'kps', 'kqp', 'kro', 'kskn', 'lbm', 'lcel', 'lda', 'lff', 'lif', 'lsm', 'lss', 'lvp', 'lwi', 'm8', 'mac', 'mag', 'map', 'mbig', 'mcl', 'mdl', 'mef', 'mfrm', 'mgr', 'mh', 'miff', 'mil', 'mjpg', 'mkcf', 'mklg', 'mng', 'mon', 'mos', 'mph', 'mpo', 'mrc', 'mrf', 'mrw', 'msp', 'msx2', 'mtv', 'mtx', 'ncr', 'ncy', 'ncy', 'nef', 'neo', 'ngg', 'nifti', 'nist', 'nitf', 'nlm', 'nol', 'npm', 'nrw', 'nsr', 'oaz', 'ocp', 'of', 'ofx', 'ohir', 'oil', 'ols', 'orf', 'os2', 'otap', 'otb', 'p64', 'p7', 'pabx', 'palm', 'pam', 'pan', 'patps', 'pbm', 'pbt', 'pcd', 'pcl', 'pcp', 'pcx', 'pd', 'pdd', 'pdf', 'pds', 'pdx', 'pef', 'peg', 'pegs', 'pfi', 'pfm', 'pfs', 'pgc', 'pgf', 'pgm', 'pi', 'pic', 'pict', 'pig', 'pixi', 'pixp', 'pld', 'pm', 'pm', 'pmg', 'pmp', 'pmsk', 'png', 'pnm', 'pp4', 'pp5', 'ppm', 'ppp', 'pps', 'ppt', 'prc', 'prf', 'prisms', 'prx', 'ps', 'psa', 'psb', 'psd', 'pseg', 'psf', 'psion3', 'psion5', 'psp', 'pspb', 'pspf', 'pspm', 'pspp', 'pspt', 'ptg', 'pwp', 'pxa', 'pxr', 'pzl', 'pzp', 'q0', 'qcad', 'qdv', 'qoi', 'qrt', 'qtif', 'rad', 'raf', 'ras', 'raw', 'raw1', 'raw2', 'raw3', 'raw4', 'raw5', 'raw6', 'raw7', 'raw8', 'raw9', 'rawa', 'rawb', 'rawdvr', 'rawe', 'ray', 'rdc', 'rfa', 'rfax', 'ript', 'rix', 'rla', 'rlc2', 'rle', 'rp', 'rpm', 'rsb', 'rsrc', 'rw2', 'rwl', 'sar', 'sci', 'sct', 'sdg', 'sdt', 'sfax', 'sfw', 'sgi', 'sif', 'sir', 'sj1', 'skf', 'skn', 'skp', 'smp', 'soft', 'spc', 'spot', 'sps', 'spu', 'srf', 'srf2', 'srw', 'ssi', 'ssp', 'sst', 'st4', 'stad', 'star', 'stm', 'stw', 'stx', 'svg', 'syj', 'synu', 'taac', 'tdi', 'tdim', 'teal', 'tg4', 'tga', 'thmb', 'ti', 'tiff', 'til', 'tile', 'tim', 'tim2', 'tiny', 'tjp', 'tnl', 'trup', 'tsk', 'ttf', 'tub', 'txc', 'uni', 'upe4', 'upi', 'upst', 'uyvy', 'uyvyi', 'v', 'vda', 'vfx', 'vi', 'vicar', 'vid', 'vif', 'viff', 'vista', 'vit', 'vivid', 'vob', 'vort', 'vpb', 'wad', 'wal', 'wbc', 'wbmp', 'webp', 'wfx', 'winm', 'wmf', 'wmz', 'wpg', 'wrl', 'wzl', 'x3f', 'xar', 'xbm', 'xcf', 'xif', 'xim', 'xim2', 'xnf', 'xp0', 'xpm', 'xwd', 'xyz', 'yuv411', 'yuv422', 'yuv444', 'zbr', 'zmf', 'zxhob', 'zxscr', 'zxsna', 'zzrough', 'jpg',]

_placeholder = "--_temp"

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
def clearfilename(name):
    return os.path.normpath(name).split(_folder)[1][1:] if _folder!=name else os.path.basename(name)
def formatfix(ext):
    exts = {
        "jpg": "jpeg",
    }
    return exts[ext] if ext in exts else ext
def getext(name,formats=[]):
    try:
        return [ext for ext in formats if name.lower().endswith(f'.{ext}')][0]
    except:
        return None
    
def getrem(name):
    return name if f'{_placeholder}.' in name else None
    
def createqueue(folder, template):
    queue = []
    for root, dirs, files in os.walk(os.path.normpath(folder)):
        for file in files:
            # print(file)
            if getext(file, template) != None:
                queue.append(os.path.join(root, file))
    return queue

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
    if _output in allext:
        typeconv = 'folder'
        equeue = []
        if os.path.isdir(_folder):
            equeue = createqueue(_folder, template=_formats)
        elif os.path.isfile(_folder):
            typeconv = 'file'
            equeue = [_folder]
        todel = []
        completed = []
        failed = []
        for num, file in enumerate(equeue):
            print(f'[{num+1}/{len(equeue)}] {clearfilename(file)}\n')
            current = convertvideo(file, _params=_params, _output=_output)
            if current != None:
                todel.append(current)
                failed.append(file)
            else:
                completed.append(file)
            clearlaststr(lines=2)

        if len(todel)>0 or len(failed)>0 or len(completed)>0:
            if len(todel)>0:
                time.sleep(2)
                delfiles(todel)

            if _delorig == "True":
                print("Удаляю оригинальные файлы")
                time.sleep(1)
                _except = delfiles(completed)
                print("Переименовываю новые")
                time.sleep(1)
                torename = []
                if typeconv == 'folder':
                    torename = createqueue(_folder, template=[_output])
                elif typeconv == 'file':
                    torename = [os.path.normpath(f'{os.path.splitext(_folder)[0]}{_placeholder}.{_output}')]
                for file in torename:
                    if f"{_placeholder}.{_output}" in file:
                        if file.replace(_placeholder,'') in _except:
                            failed.append(file)
                        else:
                            os.rename(file, file.replace(f"{_placeholder}.","."))

            
            createResult(completed, failed)

    elif _output in allpic:
        equeuepic = createqueue(_folder, template=_formats)
        todel = []
        completed = []
        failed = []
        for num, file in enumerate(equeuepic):
            progress(num, len(equeuepic), descr=f'[{num}/{len(equeuepic)}] {clearfilename(file)}')
            current = convertpic(file, _params=_params, _output=_output)
            if current != None:
                todel.append(current)
                failed.append(file)
            else:
                completed.append(file)
        
        if len(todel)>0 or len(failed)>0 or len(completed)>0:
            clearlaststr(descr=f'[100%] Все картинки переконвертированы!')

            if len(todel)>0:
                time.sleep(2)
                delfiles(todel)

            if _delorig == "True":
                print("Удаляю оригинальные файлы")
                time.sleep(1)
                _except = delfiles(equeuepic)
                print("Переименовываю временные файлы")
                time.sleep(1)
                torename = createqueue(_folder, template=[_output])
                for file in torename:
                    if file.replace(_placeholder,'') in _except:
                        failed.append(file)
                    else:
                        os.rename(file, file.replace(f"{_placeholder}.","."))
                clearlaststr(descr=f'Картинки готовы!')
            
            createResult(completed, failed)

if __name__ == "__main__":
    run()
    