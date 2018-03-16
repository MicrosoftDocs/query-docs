---
title: "BinaryFormat.Length | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
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
manager: "kfile"
---
# BinaryFormat.Length

  
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
