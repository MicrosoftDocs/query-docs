---
title: "List.First | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.First

  
## About  
Returns the first value of the list or the specified default if empty. Returns the first item in the list, or the optional default value, if the list is empty. If the list is empty and a default value is not specified, the function returns.  
  
## Syntax

<pre>
List.First(list as list, optional defaultValue as any) as any  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|optional defaultValue|Default value if list is empty.|  
  
## Examples  
  
```powerquery-m
List.First({1, 2, 3}) equals 1  
```  
  
```powerquery-m
List.First({}) equals null  
```  
