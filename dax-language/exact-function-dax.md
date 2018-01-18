---
title: "EXACT Function (DAX) | Microsoft Docs"
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
  - "sql13.as.daxref.EXACT.f1"
helpviewer_keywords: 
  - "EXACT function"
ms.assetid: 586196ed-24bf-4f37-a096-be5b0824d9b8
caps.latest.revision: 4
author: "Minewiskan"
ms.author: "owend"
manager: "mblythe"
---
# EXACT Function (DAX)
Compares two text strings and returns TRUE if they are exactly the same, FALSE otherwise. EXACT is case-sensitive but ignores formatting differences. You can use EXACT to test text being entered into a document.  
  
## Syntax  
  
```  
EXACT(<text1>,<text2>)  
```  
  
#### Parameters  
  
|Term|Definition|  
|--------|--------------|  
|**text1**|The first text string or column that contains text.|  
|**text2**|The second text string or column that contains text.|  
  
## Property Value/Return Value  
True or false. (Boolean)  
  
## Example  
The following formula checks the value of Column1 for the current row against the value of Column2 for the current row, and returns TRUE if they are the same, and returns FALSE if they are different.  
  
```  
=EXACT([Column1],[Column2])  
```  
  
## See Also  
[Text Functions &#40;DAX&#41;](../DAX/text-functions-dax.md)  
  
