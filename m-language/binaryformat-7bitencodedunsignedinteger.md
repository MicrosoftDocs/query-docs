---
title: "BinaryFormat.7BitEncodedUnsignedInteger | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: a255f71a-7d86-4b07-97eb-d8e8534f1688
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# BinaryFormat.7BitEncodedUnsignedInteger
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
A binary format that reads a 64-bit unsigned integer that was encoded using a 7-bit variable-length encoding.  
  
```  
BinaryFormat.7BitEncodedUnsignedInteger(binary as binary) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|binary|A 64-bit unsigned integer that was encoded using a 7-bit variable-length encoding.|  
  
### Controlling byte order  
The default byte order for binary formats is ByteOrder.BigEndian.  To change this use the  BinaryFormat.ByteOrder function.  
  
