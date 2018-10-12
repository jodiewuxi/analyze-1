
# coding: utf-8
import struct
#import pyDes
import binascii
from pathlib import Path
#from py4j.java_gateway import JavaGateway
#from py4j.java_gateway import GatewayParameters
#from py4j.java_collections import SetConverter, MapConverter, ListConverter
#import logging
import logging.handlers

logger = logging.getLogger('probe_cw')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler("probe_cw.debug")
fh.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

logger.addHandler(ch)
logger.addHandler(fh)

def get_decrypt(id):
    # For Python3, you'll need to use bytes, i.e.:
    #   data = b"Please encrypt my data"
    #   k = pyDes.des(b"DESCRYPT", pyDes.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
#    k = pyDes.des("carwings", pyDes.ECB, IV=None, pad=None, padmode=pyDes.PAD_PKCS5)
    #logger.debug(type(id))
    eid = k.decrypt(id)
    return eid
#logger.debug("Encrypted: %r" % binascii.hexlify(enc_tcuid))
#logger.debug("Decrypted: %r" % binascii.hexlify(k.decrypt(enc_tcuid)))
#get_bits = lambda bits, value:  get_bits(bits -1, value) +  (0x01&(value >> bits-1))  if bits > 0 else 0
get_bits = lambda value: get_bits(value>>1) +  (0x01&(value))  if  value.bit_length() > 0 else 0
def unpack_cwhead(cw_bin, cw_out):
    cw_head32 = '>H16sHcccHc32scI'
    cw_head64 = '>H16sHcccHc64scI'
    mapv = 32 if struct.unpack_from('>H', cw_bin, 0)[0] == 0x3D else 64
    if mapv == 32:
        #   header_size  send_file_no      label_x02
        head = struct.unpack_from(cw_head32, cw_bin, 0)
    else:
        head = struct.unpack_from(cw_head64, cw_bin, 0)
    logger.debug("head_size: {0}".format(head[0]))
    logger.debug("tcuid: {0}".format(get_decrypt(head[1])))
    logger.debug("fileno: {0}".format(head[2]))
    logger.debug("softvid: {0} softv: {1}".format(head[3], head[4]))
    logger.debug("confvid: {0} confv: {1}".format(head[5], head[6]))
    logger.debug("mapvid: {0} mapv: {1}".format(head[7], head[8]))
    logger.debug("flag: {0}".format(head[9]))
    logger.debug("record_num: {0}".format(head[10]))
    return (head[0], head[10])

def unpack_cwbody(cw_bin, cw_out, head_size, rec_num):
    cw_dict = {
        "0x02":[">1s", 1],
        "0x05":[">6s", 1],
        "0x06":[">9s", 1],
        "0x07":[">3s", 1],
        "0x08":[">3s", 1],
        "0x09":[">3s", 1],
        "0x0A":[">8s", 1],
        "0x0B":[">2s", 1],
        "0x0C":[">8s", 1],
        "0x0D":[">2s", 1],
        "0x0E":[">2s", 1],
        "0x0F":[">4s", 1],
        "0x10":[">1s", 1],
        "0x11":[">1s", 1],
        "0x12":[">1s", 1],
        "0x40":[">9s", 1],
        "0x41":[">9s", 1],
        "0x80":[">6s", 1],
        "0x81":[">6s", 1],
        "0x82":[">8s", 1],
        "0x83":[">8s", 1],
        "0x84":[">4s", 1],
        "0x85":[">4s", 1],
        "0x86":[">2s", 1],
        "0x87":[">2s", 1],
        "0x88":[">2s", 1],
        "0x89":[">2s", 1],
        "0x8A":[">2s", 1],
        "0x8B":[">2s", 1],
        "0x8C":[">2s", 1],
        "0x8D":[">2s", 1],
        "0x8E":[">1s", 1],
        "0x8F":[">1s", 1],
        "0x90":[">1s", 1],
        "0x91":[">1s", 1],
        "0x92":[">2s", 1],
        "0x93":[">2s", 1],
        "0x94":[">2s", 1],
        "0x96":[">2s", 1],
        "0x97":[">1s", 1],
        "0x98":[">4s", 1],
        "0x99":[">2s", 1],
        "0x9A":[">2s", 1],
        "0x9B":[">2s", 1],
        "0x9C":[">2s", 1],
        "0x9D":[">2s", 1],
        "0x9E":[">2s", 1],
        "0x9F":[">2s", 1],
        "0xA0":[">3s", 1],
        "0xA1":[">3s", 1],
        "0xA2":[">4s", 1],
        "0xA3":[">2s", 1],
        "0xA4":[">4s", 1],
        "0xA5":[">2s", 1],
        "0xA6":[">30s", 1],
        "0xA7":[">30s", 1],
        "0xA8":[">20s", 1],
        "0xA9":[">2s", 1],
        "0xAA":[">2s", 1],
        "0xAB":[">2s", 1],
        "0xAC":[">2s", 1],
        "0xAD":[">2s", 1],
        "0xAE":[">2s", 1],
        "0xAF":[">2s", 1],
        "0xB0":[">2s", 1],
        "0xB1":[">46s", 1],
        "0xB2":[">1s", 1],
        "0xB4":[">70s", 1],
        "0xB5":[">6s", 0],
        "0xB6":[">6s", 0],
        "0xB7":[">1s", 1],
        "0xC0":[">6s", 1],
        "0xC1":[">1s", 1],
        "0xC2":[">1s", 1],
        "0xC3":[">2s", 1],
        "0xCB":[">1s", 1],
        "0xCC":[">6s", 1],
        "0xCD":[">1s", 1],
        "0xCF":[">8s", 1],
        "0xD0":[">1s", 1],
        "0xD1":[">2s", 1],
        "0xD2":[">2s", 1],
        "0xE0":[">2s", 1],
        "0xE1":[">2s", 1],
        "0xE2":[">2s", 1],
        "0xE3":[">4s", 1],
        "0xE4":[">4s", 1],
        "0xE5":[">4s", 1],
        "0xE6":[">4s", 1],
        "0xE7":[">4s", 1],
        "0xE8":[">2s", 1],
        "0xEA":[">4s", 1],
        "0xEB":[">4s", 1],
        "0xEC":[">4s", 1],
        "0xED":[">4s", 1],
    }
    # JVMへ接続
    gateway = JavaGateway(gateway_parameters=GatewayParameters(port=25335))
    #Converterのインスタンスを取得
    label_convert = gateway.entry_point

    offset = head_size + 2
    for i in range(rec_num):
        idx = 0
        head_off = offset
        data_size = struct.unpack_from(">H", cw_bin, offset)[0]
        logger.debug("data_size:{0} record_num: {2}/{1}".format(data_size, rec_num, i+1))
        byte_src = struct.unpack_from(">{}s".format(data_size+2), cw_bin, offset)[0]
        logger.debug("idx:{} src:{}".format(idx, binascii.hexlify(byte_src)))
        offset += 2
        read_size = 9
        old_offset = offset
        gps_data = struct.unpack_from(">9s", cw_bin, offset)[0]
        logger.debug("GPS:{0}".format(gps_data))
        #Call Converter jar
        tsv_data = label_convert.bridgeCW("x05ToString", byte_src, idx)
        logger.debug("tsv GPS:{0}".format(tsv_data))
        offset += 9
        idx = int(tsv_data.split(";")[0])
        if  idx != read_size + 2:
            logger.warning("Offset unmatch:{}-{}".format(idx, read_size + 2))
            offset = head_off + data_size
            continue
        #idx = 0 # for cw
        while read_size < data_size:
            label = struct.unpack_from(">B", cw_bin, offset)[0]
            offset += 1
            label_inf = cw_dict["0x{:02X}".format(label)]
            if label_inf[1] == 1:#fix length
                label_data = struct.unpack_from(label_inf[0], cw_bin, offset)[0]
                offset += int(label_inf[0][1:-1])
            elif label_inf[1] == 0:#valuable
                label_data_num = struct.unpack_from(">B", cw_bin, offset)[0]
                logger.debug("label:{:02X} raw_loop:{}".format(label, cw_bin[offset]))
                offset += 1
                if (label == 0xB5 or label == 0xB6) and label_data_num == 0:
                    label_data = struct.unpack_from(">b", cw_bin, offset)
                    offset += 1
                else:
                    ssize = int(label_inf[0][1:-1])*label_data_num
                    logger.debug("label:{:02X} loop:{}".format(label, label_data_num))
                    label_data = struct.unpack_from(">{0}s".format(ssize), cw_bin, offset)[0]
                    offset += ssize
            read_size = offset - old_offset
            logger.debug("label:{:02X} value:{}".format(label, label_data))
            #Call Converter jar
            #logger.debug("idx:{} src:{}".format(idx, binascii.hexlify(byte_src)))
            tsv_data = label_convert.bridgeCW("x{:02X}ToString".format(label), byte_src, idx)
            logger.debug("0x{:02X} tsv :{}".format(label, tsv_data))
            idx = int(tsv_data.split(";")[0])
            if idx != read_size + 2:
                logger.warn("Offset unmatch:{}-{}".format(idx, read_size + 2))
                offset = head_off + data_size
                break
        if read_size != data_size:
            logger.warning("data_size over: {0} {1}".format(data_size, read_size))
        else:
            logger.debug("read Next recode from: {:02X}\n".format(offset))

def unpack(input_f, output_f):
    with open(input_f, 'rb') as in_f:
        with open(output_f, 'w') as ou_f:
            data = in_f.read()
            (head_size, rec_num) = unpack_cwhead(data, ou_f)
            unpack_cwbody(data, ou_f, head_size, rec_num)
#unpack("cw_data_v", "cw_txt", 32)
#unpack("Probe_1_ABCDEFGHIJK000001_55D62ECF31C04999538FFB9D4D0E93191FACE0009E5AAC57_01_01_01_2017020700005671701_EV.OK", "cw_txt", 32)
p = Path("D:\LocalData\FJT02454\Desktop\errzip")

# dir_A直下のファイルとディレクトリを取得
# Path.glob(pattern)はジェネレータを返す。結果を明示するためlist化しているが、普段は不要。
for f in list(p.glob("*/Probe_*")):
    logger.debug("read file: {}".format(f))
    try:
        unpack(f, "cw_txt")
    except Exception as e:
        logger.debug("Out:{}".format(f))
        logger.debug(e)
        continue
