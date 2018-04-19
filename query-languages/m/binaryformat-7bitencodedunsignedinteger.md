---
title: "BinaryFormat.7BitEncodedUnsignedInteger | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# BinaryFormat.7BitEncodedUnsignedInteger

  
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
  
