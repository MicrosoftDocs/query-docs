---
title: "LOWER Function (DAX) | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "analysis-services"
  - "daxlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
f1_keywords: 
  - "sql13.as.daxref.LOWER.f1"
helpviewer_keywords: 
  - "LOWER function"
ms.assetid: 29eb9d54-2fc4-4402-97d3-5cd95cebd3d2
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# LOWER Function (DAX)
Converts all letters in a text string to lowercase.  
  
## Syntax  
  
```  
LOWER(<text>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**text**|The text you want to convert to lowercase, or a reference to a column that contains text.|  
  
## Property Value/Return Value  
Text in lowercase.  
  
## Remarks  
Characters that are not letters are not changed. For example, the formula `=LOWER("123ABC")` returns **123abc**.  
  
## Example  
The following formula gets each row in the column, [ProductCode], and converts the value to all lowercase. Numbers in the column are not affected.  
  
```  
=LOWER('New Products'[ProductCode])  
```  
  
## See Also  
[Text Functions &#40;DAX&#41;](text-functions-dax.md)  
  
