---
title: "Text.RemoveRange | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 3f2ec914-70f9-4d94-92ee-cd08986e1402
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Text.RemoveRange

  
## About  
Removes count characters at a zero-based offset from a text value.  
  
```  
Text.RemoveRange(text as nullable text, offset as number, count as number) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to parse.|  
|offset|The index to start at.|  
|count|The number of characters to remove.|  
  
## <a name="__toc360788862"></a>Remarks  
  
-   If count is not specified, the default value of 1 is used.  
  
-   If offset is less than zero or more than the length of a text value, or if count if less than zero then an Expression.Error is thrown.  
  
## Examples  
  
```  
Text.RemoveRange("abcdef", 2) equals "abdef"  
```  
  
```  
Text.RemoveRange("abcdef", 2, 2) equals "abef"  
```  
