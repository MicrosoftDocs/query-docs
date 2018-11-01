---
title: "BinaryFormat.ByteOrder | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# BinaryFormat.ByteOrder

  
## About  
Returns a binary format with the specified byte order.  
  
## Syntax

<pre>   
BinaryFormat.ByteOrder(binaryFormat as function, byteOrder as number) as function  
</pre>  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|binaryFormat|The binary format that will be used to read the value.|  
|byteOrder|The most signficant byte appears first in Big Endian byte order.  The least significant byte appears first in Little Endian byte order.<br /><br />ByteOrder.LittleEndian = 0<br /><br />ByteOrder.BigEndian = 1|  
  
## Example  
  
```powerquery-m  
let  
binaryData = #binary({0x01, 0x00}),  
littleEndianFormat = BinaryFormat.ByteOrder(  
BinaryFormat.UnsignedInteger16, ByteOrder.LittleEndian)  
in  
littleEndianFormat(binaryData)   
equals 1  
```  
