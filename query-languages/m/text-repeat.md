---
title: "Text.Repeat | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 333b3a8a-1c6d-4e51-9ea7-9c6de7e38504
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Text.Repeat

  
## About  
Returns a text value composed of the input text value repeated a number of times.  
  
```  
Text.Repeat(string as text, repeatCount as number) as text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|string|The text to repeat.|  
|repeatCount|The number of times to repeat the text.|  
  
## Example  
  
```  
Text.Repeat("a",5) equals "aaaaa"  
```  
