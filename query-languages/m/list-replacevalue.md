---
title: "List.ReplaceValue | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.ReplaceValue

  
## About  
Searches a list of values for the value and replaces each occurrence with the replacement value.  
## Syntax

<pre>
List.ReplaceValue(list as list,  oldValue as any, newValue as any,  replacer as function) as list  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to modify.|  
|oldValue|The value to replace.|  
|newValue|The new value to replace with.|  
|replacer|A function provided as replacer determines the kind of values that are being replaced. Built-in functions be be used such as  Replacer.ReplaceText and Replacer.ReplaceValue.|  
  
## <a name="__goback"></a>Example  
  
```powerquery-m
List.ReplaceValue({"a", "B", "a", "a"}, "a", "A", Replacer.ReplaceText) equals {"A", "B", "A", "A"}  
```  
