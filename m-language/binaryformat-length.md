---
title: "BinaryFormat.Length | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 138fe5d3-501a-47ed-8678-f3c817f82720
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# BinaryFormat.Length
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a binary format that limits the amount of data that can be read.  Both BinaryFormat.List and BinaryFormat.Binary can be used to read until end of the data.  BinaryFormat.Length can be used to limit the number of bytes that are read.  
  
```  
BinaryFormat.Length(binaryFormat as function, length as number) as function  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|binaryFormat|The binary format to limit.|  
|length|The number of bytes to read|  
  
## Example  
Limit the number of bytes read to 2 when reading a list of bytes.  
  
```  
let  
binaryData = #binary({1, 2, 3}),  
listFormat = BinaryFormat.Length(  
BinaryFormat.List(BinaryFormat.Byte), 2)  
in  
listFormat(binaryData)   
equals {1, 2}  
```  
