---
title: "BinaryFormat.Record | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
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
manager: "kfile"
---
# BinaryFormat.Record

  
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
