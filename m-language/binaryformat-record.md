---
title: "BinaryFormat.Record | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 29ed9420-802f-4e7c-9951-5a1a95f13dfa
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# BinaryFormat.Record
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a binary format that reads a record.  Each field in the record can have a different binary format.  
  
```  
BinaryFormat.Record(record as record) as function  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The format of the record|  
  
## Remarks  
  
-   If a field contains a value that is not a binary format value, then no data is read for that field, and the field value is echoed to the result.  
  
## Example  
  
```  
// Read a record containing one 16-bit integer and one 32-bit integer.  
let  
binaryData = #binary({  
0x00, 0x01,   
0x00, 0x00, 0x00, 0x02}),  
recordFormat = BinaryFormat.Record([  
A = BinaryFormat.UnsignedInteger16,  
B = BinaryFormat.UnsignedInteger32  
])  
in  
recordFormat(binaryData)   
equals [A = 1, B = 2]  
```  
