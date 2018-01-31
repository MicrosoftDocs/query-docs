---
title: "BinaryFormat.ByteOrder | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: a3cecc21-5dfc-4855-85fb-ed7d41ab46c4
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# BinaryFormat.ByteOrder

  
## About  
Returns a binary format with the specified byte order.  
  
```  
BinaryFormat.ByteOrder(binaryFormat as function, byteOrder as number) as function  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|binaryFormat|The binary format that will be used to read the value.|  
|byteOrder|The most signficant byte appears first in Big Endian byte order.  The least significant byte appears first in Little Endian byte order.<br /><br />ByteOrder.LittleEndian = 0<br /><br />ByteOrder.BigEndian = 1|  
  
## Example  
  
```  
let  
binaryData = #binary({0x01, 0x00}),  
littleEndianFormat = BinaryFormat.ByteOrder(  
BinaryFormat.UnsignedInteger16, ByteOrder.LittleEndian)  
in  
littleEndianFormat(binaryData)   
equals 1  
```  
