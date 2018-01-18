---
title: "BinaryFormat.ByteOrder | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
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
manager: "erikre"
---
# BinaryFormat.ByteOrder
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
