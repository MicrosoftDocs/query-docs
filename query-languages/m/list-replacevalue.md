---
title: "List.ReplaceValue | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 7687d1a5-2e87-4c06-b85b-5fae183d5e4b
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.ReplaceValue

  
## About  
Searches a list of values for the value and replaces each occurrence with the replacement value.  
  
```  
List.ReplaceValue(list as list,  oldValue as any, newValue as any,  replacer as function) as list  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
|oldValue|The value to replace.|  
|newValue|The new value to replace with.|  
|replacer|A function provided as replacer determines the kind of values that are being replaced. Built-in functions be be used such as  Replacer.ReplaceText and Replacer.ReplaceValue.|  
  
## <a name="__goback"></a>Example  
  
```  
List.ReplaceValue({"a", "B", "a", "a"}, "a", "A", Replacer.ReplaceText) equals {"A", "B", "A", "A"}  
```  
