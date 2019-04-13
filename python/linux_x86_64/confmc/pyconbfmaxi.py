#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This file contains Python interface for CON-FMC AMBA AXI BFM.
"""
__author__     = "Ando Ki"
__copyright__  = "Copyright 2017-2019, Future Design Systems"
__credits__    = ["none", "some"]
__license__    = "FUTURE DESIGN SYSTEMS SOFTWARE END-USER LICENSE AGREEMENT FOR CON-FMC."
__version__    = "1"
__revision__   = "0"
__maintainer__ = "Ando Ki"
__email__      = "contact@future-ds.com"
__status__     = "Development"
__date__       = "2019.02.08"
__description__= "CON-FMC AMBA AXI BFM"

#-------------------------------------------------------------------------------
from confmc.pyconfmc import *

#===============================================================================
_con_bfm_type = 'axi'
_libbfm = os.path.abspath( os.path.join(CONFMC_BFM, "hwlib/trx_axi/lib", sys_mach, "libbfmaxi.so"))

if not os.path.isfile(_libbfm):
   print _libbfm+' not found'
   traceback.print_exc(file=sys.stdout)
   sys.exit(1)
else:
   if __debug__: print _libbfm+" found."

#-------------------------------------------------------------------------------
try:
    conbfm = ctypes.CDLL(_libbfm)
except:
    traceback.print_exc(file=sys.stdout)
    sys.exit(1)

#-------------------------------------------------------------------------------
# void BfmWrite( con_Handle_t handle
#              , unsigned int  addr
#              , unsigned int *data
#              , unsigned int  size
#              , unsigned int  length);
def BfmWrite(con_handle, addr, pdata, size, length):
    """
    Generate AMBA AXI write transaction.
    :param con_handle: CON-FMC handler
    :param addr: starting address to write
    :param pdata: pointer to the buffer holding 32-bit data, which is right-justified
    :param size: number of bytes of each pdata items, can be 1, 2, 4.
    :param length: number of burst length
    :return: void
    """
    _BfmWrite=wrap_function(conbfm, 'BfmWrite'
                                  ,  None
                                  ,[ ctypes.POINTER(con_Handle)
                                    ,ctypes.c_uint
                                    ,ctypes.POINTER(ctypes.c_uint)
                                    ,ctypes.c_uint
                                    ,ctypes.c_uint ])
    return _BfmWrite(con_handle, addr, pdata, size, length)

#-------------------------------------------------------------------------------
# void BfmRead ( con_Handle_t handle
#              , unsigned int  addr
#              , unsigned int *data
#              , unsigned int  size
#              , unsigned int  length);
def BfmRead(con_handle, addr, pdata, size, length):
    """
    Generate AMBA AXI read transaction.
    :param con_handle: CON-FMC handler
    :param addr: starting address to read
    :param pdata: pointer to the buffer holding 32-bit data, which is right-justified
    :param size: number of bytes of each pdata items, can be 1, 2, 4.
    :param length: number of burst length
    :return: void
    """
    _BfmRead=wrap_function(conbfm, 'BfmRead'
                                  ,  None
                                  ,[ ctypes.POINTER(con_Handle)
                                    ,ctypes.c_uint
                                    ,ctypes.POINTER(ctypes.c_uint)
                                    ,ctypes.c_uint
                                    ,ctypes.c_uint ])
    return _BfmRead(con_handle, addr, pdata, size, length)

#-------------------------------------------------------------------------------
# Only for AMBA AXI fixed address mode
if _con_bfm_type == 'axi':
   # void BfmWriteFix( con_Handle_t handle
   #                 , unsigned int  addr
   #                 , unsigned int *data
   #                 , unsigned int  size
   #                 , unsigned int  length);
   def BfmWriteFix(con_handle, addr, pdata, size, length):
       """
       Generate AMBA AXI write transaction with fixed-address.
       :param con_handle: CON-FMC handler
       :param addr: address to write
       :param pdata: pointer to the buffer holding 32-bit data, which is right-justified
       :param size: number of bytes of each pdata items, can be 1, 2, 4.
       :param length: number of burst length
       :return: void
       """
       if _con_bfm_type!='axi' and _con_bfm_type!='AXI' and _con_bfm_type!='AMBA AXI':
          print("fixed transaction is not supported")
          sys.exit(1)
       _BfmWriteFix=wrap_function(conbfm, 'BfmWriteFix'
                                     ,  None
                                     ,[ ctypes.POINTER(con_Handle)
                                       ,ctypes.c_uint
                                       ,ctypes.POINTER(ctypes.c_uint)
                                       ,ctypes.c_uint
                                       ,ctypes.c_uint ])
       return _BfmWriteFix(con_handle,addr, pdata, size, length)

#-------------------------------------------------------------------------------
# Only for AMBA AXI fixed address mode
if _con_bfm_type == 'axi':
   # void BfmReadFix ( con_Handle_t handle
   #                 , unsigned int  addr
   #                 , unsigned int *data
   #                 , unsigned int  size
   #                 , unsigned int  length);
   def BfmReadFix(con_handle, addr, pdata, size, length):
       """
       Generate AMBA AXI read transaction with fixed-address.
       :param con_handle: CON-FMC handler
       :param addr: address to read
       :param pdata: pointer to the buffer holding 32-bit data, which is right-justified
       :param size: number of bytes of each pdata items, can be 1, 2, 4.
       :param length: number of burst length
       :return: void
       """
       _BfmReadFix=wrap_function(conbfm, 'BfmReadFix'
                                     ,  None
                                     ,[ ctypes.POINTER(con_Handle)
                                       ,ctypes.c_uint
                                       ,ctypes.POINTER(ctypes.c_uint)
                                       ,ctypes.c_uint
                                       ,ctypes.c_uint ])
       return _BfmReadFix(con_handle, addr, pdata, size, length)

#-------------------------------------------------------------------------------
# int BfmGpout( con_Handle_t handle
#      , unsigned int value );
def BfmGpout(con_handle, value):
    """
    Drive value to the GPOUT port of AMBA AXI Transactor.
    :param con_handle: CON-FMC handler
    :param value: value to drive and lower 16-bit is valid
    :return: 0 on success, otherwize negative value.
    """
    _BfmGpout=wrap_function(conbfm, 'BfmGpout'
                                  ,  ctypes.c_int
                                  ,[ ctypes.POINTER(con_Handle)
                                    ,ctypes.c_uint ])
    return _BfmGpout(con_handle, value)

#-------------------------------------------------------------------------------
# int BfmGpin( con_Handle_t handle
#            , unsigned int value );
def BfmGpin(con_handle, pValue):
    """
    Read value from the GPIN port of AMBA AXI Transactor.
    :param con_handle: CON-FMC handler
    :param value: value has been read and lower 16-bit is valid
    :return: 0 on success, otherwize negative value.
    """
    _BfmGpin=wrap_function(conbfm, 'BfmGpin'
                                  ,  ctypes.c_int
                                  ,[ ctypes.POINTER(con_Handle)
                                    ,ctypes.POINTER(ctypes.c_uint)])
    return _BfmGpin(con_handle, pValue)

#-------------------------------------------------------------------------------
# It returns positive burst length on success.
if _con_bfm_type == 'axi':
   # int BfmSetAmbaAxi4( con_Handle_t handle );
   def BfmSetAmbaAxi4(con_handle):
       """
       Set AMBA AXI4 mode.
       :param con_handle: CON-FMC handler
       :return: the maximum number of burst length.
       """
       _BfmSetAmbaAxi4=wrap_function(conbfm, 'BfmSetAmbaAxi4'
                                     ,  ctypes.c_int
                                     ,[ ctypes.POINTER(con_Handle)])
       return _BfmSetAmbaAxi4(con_handle)

#===============================================================================
def MemTestAddRAW(con_handle, saddr, depth):
    """
    Memory test using addres in read-after-write fashion.
    :param con_hadle: CON-FMC handler
    :param saddr: starting address to test
    :param depth: number of bytes to test
    :return: void
    """
    Wdata = ctypes.c_uint32(0)
    Rdata = ctypes.c_uint32(0)
    error = 0
    for addr in range(saddr, depth, 4):
        Wdata = ctypes.c_uint32(addr)
        BfmWrite(con_handle, addr, ctypes.pointer(Wdata), 4, 1)
        BfmRead(con_handle, addr, ctypes.pointer(Rdata), 4, 1)
        if Wdata.value!=Rdata.value: error = error + 1
       #else: print("A=%d DW=%d DR=%d" %(addr, Wdata.value, Rdata.value))
    if error!=0:
        print get_function_name()+" "+str(error)+" mis-match out of "+str(depth)
    else:
        print get_function_name()+" "+str(depth)+" OK"

#-------------------------------------------------------------------------------
def MemTestAdd(con_handle, saddr, depth):
    """
    Memory test using addres in read-all-after-write-all fashion.
    :param con_hadle: CON-FMC handler
    :param saddr: starting address to test
    :param depth: number of bytes to test
    :return: void
    """
    error = 0
    addr  = saddr
    for addr in range(saddr, depth, 4):
        Wdata = ctypes.c_uint32(addr+1)
        BfmWrite(con_handle, addr, ctypes.pointer(Wdata), 4, 1)
    addr  = saddr
    for addr in range(saddr, depth, 4):
        Edata = ctypes.c_uint32(addr+1)
        Rdata = ctypes.c_uint32(0)
        BfmRead(con_handle, addr, ctypes.pointer(Rdata), 4, 1)
        if Rdata.value!=Edata.value: error = error + 1;
       #else: print("A=%d DW=%d DR=%d" %(addr, Edata.value, Rdata.value))
    if error!=0:
        print get_function_name()+" "+str(error)+" mis-match out of "+str(depth)
    else:
        print get_function_name()+" "+str(depth)+" OK"

#-------------------------------------------------------------------------------
def MemTestRAW(con_handle, saddr, depth, size):
    """
    Memory test using random number in read-after-write fashion.
    :param con_hadle: CON-FMC handler
    :param saddr: starting address to test
    :param depth: number of bytes to test
    :param size: number of bytes for each access and can be 1, 2, 4.
    :return: void
    """
    import random
    Wdata = ctypes.c_uint32(0)
    Rdata = ctypes.c_uint32(0)
    if   size==1: mask = 0x000000FF
    elif size==2: mask = 0x0000FFFF
    elif size==4: mask = 0xFFFFFFFF
    else: 
         mask = 0xFFFFFFFF
         size = 4
    random.seed(0x7)
    error = 0
    for addr in range(saddr, depth, size):
        Wdata = ctypes.c_uint32(mask & random.randint(0,0xFFFFFFFF))
        BfmWrite(con_handle, addr, ctypes.pointer(Wdata), size, 1)
        BfmRead(con_handle, addr, ctypes.pointer(Rdata), size, 1)
        if Wdata.value!=(Rdata.value&mask): error = error + 1
       #else: print("A=%d DW=%d DR=%d" %(addr, Wdata.value, (Rdata.value&mask)))
    if error!=0:
        print get_function_name()+" size "+str(size)+" "+str(error)+" mis-match out of "+str(depth)
    else:
        print get_function_name()+" size"+str(size)+" "+str(depth)+" OK"

#-------------------------------------------------------------------------------
def MemTest(con_handle, saddr, depth, size):
    """
    Memory test using random number in read-all-after-write-all fashion.
    :param con_hadle: CON-FMC handler
    :param saddr: starting address to test
    :param depth: number of bytes to test
    :param size: number of bytes for each access and can be 1, 2, 4.
    :return: void
    """
    import random
    Wdata = ctypes.c_uint32(0)
    Rdata = ctypes.c_uint32(0)
    if   size==1: mask = 0x000000FF
    elif size==2: mask = 0x0000FFFF
    elif size==4: mask = 0xFFFFFFFF
    else: 
         mask = 0xFFFFFFFF
         size = 4
    random.seed(0x11)
    for addr in range(saddr, depth, size):
        Wdata = ctypes.c_uint32(mask & random.randint(0,0xFFFFFFFF))
        BfmWrite(con_handle, addr, ctypes.pointer(Wdata), size, 1)
    random.seed(0x11)
    error = 0
    for addr in range(saddr, depth, size):
        Wdata = ctypes.c_uint32(mask & random.randint(0,0xFFFFFFFF))
        BfmRead(con_handle, addr, ctypes.pointer(Rdata), size, 1)
        if Wdata.value!=(Rdata.value&mask): error = error + 1
       #else: print("A=%d DW=%d DR=%d" %(addr, Wdata.value, (Rdata.value&mask)))
    if error!=0:
        print get_function_name()+" size "+str(size)+" "+str(error)+" mis-match out of "+str(depth)
    else:
        print get_function_name()+" size"+str(size)+" "+str(depth)+" OK"

#-------------------------------------------------------------------------------
def MemTestBurstRAW(con_handle, saddr, depth, leng):
    """
    Memory test using burst and random number in read-after-write fashion.
    :param con_hadle: CON-FMC handler
    :param saddr: starting address to test
    :param depth: number of bytes to test
    :param length: burst length and can be 1-256 for AMBA AXI4
    :return: void
    """
    import random
    Wdata = [ctypes.c_uint32(i) for i in range(leng)]
    Rdata = [ctypes.c_uint32(0)]*leng
    random.seed(0x3)
    error = 0
    for addr in range(saddr, depth, 4*leng):
        for idx in range(0, leng, 1):
            Wdata[idx] = ctypes.c_uint32(random.randint(0,0xFFFFFFFF))
       #print Wdata
        wints = (ctypes.c_uint32 * len(Wdata))(*Wdata)
       #pwints = ctypes.cast(wints, ctypes.POINTER(ctypes.c_uint32))
        BfmWrite(con_handle, addr, wints, 4, leng)
        rints = (ctypes.c_uint32 * len(Rdata))(*Rdata)
       #prints = ctypes.cast(rints, ctypes.POINTER(ctypes.c_uint32))
        BfmRead(con_handle, addr, rints, 4, leng)
        for idx in range(0, leng, 1):
            if Wdata[idx].value!=rints[idx]:
                  error = error + 1
                 #print("A=%d DW=%s DR=%s" %(addr, hex(Wdata[idx].value), hex(rints[idx])))
           #else: print("A=%d DW=%s DR=%s" %(addr, hex(Wdata[idx].value), hex(rints[idx])))
    if error!=0:
        print get_function_name()+" burst "+str(leng)+" "+str(error)+" mis-match out of "+str(depth)
    else:
        print get_function_name()+" burst " +str(leng)+" "+str(depth)+" OK"

#-------------------------------------------------------------------------------
def MemTestBurst(con_handle, saddr, depth, leng):
    """
    Memory test using burst and random number in read-all-after-write-all fashion.
    :param con_hadle: CON-FMC handler
    :param saddr: starting address to test
    :param depth: number of bytes to test
    :param length: burst length and can be 1-256 for AMBA AXI4
    :return: void
    """
    import random
    Wdata = [ctypes.c_uint32(i) for i in range(leng)]
    random.seed(0x3)
    for addr in range(saddr, depth, 4*leng):
        for idx in range(0, leng, 1):
            Wdata[idx] = ctypes.c_uint32(random.randint(0,0xFFFFFFFF))
        wints = (ctypes.c_uint32 * len(Wdata))(*Wdata)
        BfmWrite(con_handle, addr, wints, 4, leng)
    error = 0
    random.seed(0x3)
    Rdata = [ctypes.c_uint32(0)]*leng
    for addr in range(saddr, depth, 4*leng):
        rints = (ctypes.c_uint32 * len(Rdata))(*Rdata)
        BfmRead(con_handle, addr, rints, 4, leng)
        for idx in range(0, leng, 1):
            if Wdata[idx].value!=rints[idx]:
                  error = error + 1
                 #print("A=%d DW=%s DR=%s" %(addr, hex(Wdata[idx].value), hex(rints[idx])))
           #else: print("A=%d DW=%s DR=%s" %(addr, hex(Wdata[idx].value), hex(rints[idx])))
    if error!=0:
        print get_function_name()+" burst "+str(leng)+" "+str(error)+" mis-match out of "+str(depth)
    else:
        print get_function_name()+" burst "+str(leng)+" "+str(depth)+" OK"

#-------------------------------------------------------------------------------
# Testing code for standalone
#-------------------------------------------------------------------------------
def main(argv):
    import getopt
    #----------------------------------------
    cid = 0
    try:
        opts, args = getopt.getopt(argv, "hc:",['help','cid='])
    except getopt.GetoptError:
        print 'pyconbfm.py -c 0'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
             print 'pyconbfm.py -c 0'
             sys.exit()
        elif opt in ("-c", "--cid"):
             cid = int(arg)
        else:
             print 'Unknown options: '+str(opt)
             sys.exit(1)
  
    #----------------------------------------
    ret = conGetVersionApi()
    print('API version: '+hex(ret).upper())
    ret = conGetVersionLibusb()
    print('Libusb version: '+hex(ret).upper())
  
    #----------------------------------------
    hdl = conInit(cid)
    if not hdl:
       error = conGetErrorConapi()
       print error
       print conErrorMsgConapi(error)+' for CID: '+str(cid)
       sys.exit(1)
    con = hdl.contents; #con = con_Handle.from_address(hdl)
    print(con.__repr__())
    print(con.__str__())
    print(con)
    print(con.cid)
    print(con.mode)
    print(con.usb)
  
    #----------------------------------------
    cid_r = conGetCid(hdl)
    if cid_r<0:
       error = conGetErrorConapi()
       print 'error code: '+str(error)
       print conErrorMsgConapi(error)
       sys.exit(1)
    elif cid!=cid_r:
       print 'cid mis-match'
       sys.exit(1)
    print('CID: '+str(cid))

    #----------------------------------------
    UsbInfo=_usb()
    pUsbInfo = ctypes.byref(UsbInfo)
    conGetUsbInfo( hdl, pUsbInfo )
    print("USB Infomation")
    print "      %s" % UsbInfo.__str__()
  
    #----------------------------------------
    Fx3Info=con_Fx3Info()
    pFx3Info = ctypes.byref(Fx3Info); # pFx3Info = ctypes.pointer(Fx3Info)
    conGetFx3Info ( hdl, pFx3Info )
    print('FX3 Version')
    print "      %s" % Fx3Info.__str__()
  
    #----------------------------------------
    BoardInfo=con_BoardInfo()
    pBoardInfo = ctypes.byref(BoardInfo); # pBoardInfo = ctypes.pointer(BoardInfo)
    length = ctypes.sizeof(con_BoardInfo)
    crc_check = ctypes.c_uint(0)
    ret = conGetBoardInfo( hdl, pBoardInfo, length, crc_check )
    if ret:
       print("Board Infomation")
       print "      %s" % BoardInfo.__str__()
    else:
       print("Board Information not found; check if programmed")
  
    #----------------------------------------
    MasterInfo=con_MasterInfo()
    pMasterInfo = ctypes.byref(MasterInfo); # pMasterInfo = ctypes.pointer(MasterInfo)
    ret = conGetMasterInfo( hdl, pMasterInfo )
    if ret:
       print("Master Infomation")
       print "      %s" % MasterInfo.__str__()
    else:
       print 'CON-FMC master not found; FPGA may not be configured yet.'
       error = conGetErrorConapi()
       print error
       print conErrorMsgConapi(error)+' for CID: '+str(cid)
       print('ret:'+str(ret))
       if  ret <= -6 and ret >= -18:
             print 'conGetErrorLibusb'
             print conGetErrorLibusb()
       sys.exit(1)
  
    #----------------------------------------
   #duration = ctypes.c_uint(10)
   #conReset ( hdl, duration )

    #----------------------------------------
    if _con_bfm_type == 'axi':
       ret = BfmSetAmbaAxi4(hdl)
       print "AMBA AXI burst length: "+str(ret)
    MemTestAddRAW(hdl, 0, 0x100)
    MemTestAdd(hdl, 0, 0x100)
    MemTestRAW(hdl, 0, 0x100, 4)
    MemTest(hdl, 0, 0x100, 4)
    MemTestBurstRAW(hdl, 0, 4*8*2, 8)
    MemTestBurst(hdl, 0, 4*8*2, 16)
  
    #----------------------------------------
    ret = conRelease ( hdl )
    print(ret)

#-------------------------------------------------------------------------------
if __name__ == '__main__':
    ret=lsconfmc(card_ids=[], flag_usb=1, flag_fx3=1, flag_master=1); print(ret)
    ret=lsconfmc(card_ids=[0], flag_usb=1, flag_fx3=1, flag_master=1); print(ret)
    ret=lsconfmc(card_ids=[1], flag_usb=0, flag_fx3=0, flag_master=0); print(ret)
    ret=lsconfmc(card_ids=[2, 1], flag_usb=0, flag_fx3=0, flag_master=0); print(ret)
    main(sys.argv[1:])

#===============================================================================
# Revision history:
#
# 2019.01.28: Started by Ando Ki (adki@future-ds.com)
#             - Not finished yet
#===============================================================================
