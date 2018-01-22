---
title: "Text.ToList | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: be2ad426-18a6-4b86-ac20-a18cc04796f8
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Text.ToList

  
## About  
Returns a list of characters from a text value.  
  
```  
Text.ToList(text as text) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|Text|The text to parse through.|  
  
## Example  
  
```  
Text.ToList("abc") equals {"a","b","c"}  
```  
