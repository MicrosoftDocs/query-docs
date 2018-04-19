---
title: "BinaryFormat.Binary | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# BinaryFormat.Binary

  
## About  
Returns a binary format that reads a binary value.  
  
```  
BinaryFormat.Binary(optional length as nullable number) as function  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|optional length|Length of bytes.|  
  
## Remarks  
  
-   If a length is specified, the binary value will contain that many bytes.  
  
-   If length is not specified, the binary value will contain the remaining bytes.  
  
