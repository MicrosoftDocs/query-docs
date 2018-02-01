---
title: "BinaryFormat.7BitEncodedUnsignedInteger | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
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
manager: "kfile"
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
  
