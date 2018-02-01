---
title: "BinaryFormat.Binary | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 467026d3-21bd-4322-b6b9-9d91b6eed0f6
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
  
