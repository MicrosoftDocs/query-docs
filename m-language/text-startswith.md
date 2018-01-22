---
title: "Text.StartsWith | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 474a1a8b-1abf-41c3-8a79-be96134f097e
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Text.StartsWith

  
## About  
Returns a logical value indicating whether a text value substring was found at the beginning of a string.  
  
**Note**: Only comparer functions created through the library (Comparer.FromCulture) are supported.  
  
```  
Text.StartsWith(string as nullable text, substring as text, optional comparer as nullable function) as nullable logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|string|The text value to parse.|  
|substring|The string to search for.|  
|optional comparer|An optional comparer can be provided to influence the result.|  
  
