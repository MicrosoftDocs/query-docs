---
title: "Text.End | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 31a55b0a-2255-4871-8374-69cba62b4934
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Text.End

  
## About  
Returns the number of characters from the end of a text value.  
  
```  
Text.End(string as nullable text, numChars as number) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|string|The string value to parse.|  
|numChars|The number of characters to return.|  
  
## Example  
  
```  
Text.End("abcd", 2) equals "cd"  
```  
