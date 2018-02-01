---
title: "Text.EndsWith | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 62e30b7e-552a-4d8d-8b5e-b0fc50a74fcc
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Text.EndsWith

  
## About  
Returns a logical value indicating whether a text value substring was found at the end of a string.  
  
```  
Text.EndsWith(string as nullable text, substring as text, optional comparer as nullable function) as nullable logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|string|The text value to parse.|  
|substring|The string to search for.|  
|optional comparer|An optional comparer can be provided to influence the result.|  
  
## <a name="__toc360788886"></a>Remarks  
  
-   Only comparer functions created through the library (Comparer.FromCulture) are supported.  
  
