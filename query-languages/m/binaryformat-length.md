---
title: "BinaryFormat.Length | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
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
