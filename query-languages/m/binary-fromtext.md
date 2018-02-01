---
title: "Binary.FromText | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: f736728a-5899-4d17-8009-90bbb330d04c
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Binary.FromText

  
## About  
Decodes data from a text form into binary.  
  
```  
Binary.FromText (text as text, encoding as number) as Binary  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to decode.|  
|encoding|The encoding option to apply.|  
  
**Binary encoding**  
  
-   BinaryEncoding.Base64 = 0;  
  
-   BinaryEncoding.Hex = 1;  
  
