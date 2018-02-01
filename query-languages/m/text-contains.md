---
title: "Text.Contains | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 88e751e2-b418-45c8-bee3-c84f944ef22a
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Text.Contains

  
## About  
Returns true if a text value **substring** was found within a text value **string**; otherwise, false.  
  
```  
Text.Contains(string as nullable text, substring as text, optional comparer as nullable function) as nullable logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|string|The text to parse.|  
|substring|The text to search for.|  
|optional comparer|The optional culture aware comparer function can be provided.|  
  
## Examples  
  
```  
Text.Contains("abc", "a") equals true  
```  
  
```  
Text.Contains("abc", "d") equals false  
```  
