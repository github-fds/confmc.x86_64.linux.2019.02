#ifndef TRX_AHB_API_H
#define TRX_AHB_API_H
//------------------------------------------------------------------------------
// Copyright (c) 2018-2019 Future Design Systems
//
// http://www.future-ds.com
//------------------------------------------------------------------------------
// trx_ahb_api.h
//------------------------------------------------------------------------------
// VERSION = 2019.02.07.
//------------------------------------------------------------------------------
// Note that "data" carries justified data.
#include "conapi.h"

#if (defined(_WIN32)||defined(_WIN64))
   #ifdef BUILDING_DLL
      #define CONFMC_API __declspec(dllexport)
   #else
      #define CONFMC_API __declspec(dllimport)
   #endif
#else
   #define CONFMC_API
#endif

#ifdef __cplusplus
extern "C" {
#endif

CONFMC_API void BfmWrite( con_Handle_t  handle
                    , unsigned int  addr
                    , unsigned int *data
                    , unsigned int  size
                    , unsigned int  length);
CONFMC_API void BfmRead ( con_Handle_t  handle
                    , unsigned int  addr
                    , unsigned int *data
                    , unsigned int  size
                    , unsigned int  length);
CONFMC_API int BfmGpout( con_Handle_t  handle
                   , unsigned int Value );
CONFMC_API int BfmGpin ( con_Handle_t  handle
                   , unsigned int *pValue );

#ifdef __cplusplus
}
#endif
//------------------------------------------------------------------------------
// Revision History
//
// 2018.02.07: Each API has new argument, con_Handle_t handle
// 2018.04.27: Start by Ando Ki (adki@future-ds.com)
//------------------------------------------------------------------------------
#endif
