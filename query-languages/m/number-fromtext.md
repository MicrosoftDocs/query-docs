---
title: "Number.FromText | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.FromText

  
## About  
Returns a number value from a text value.  
  
## Syntax

<pre>
Number.FromText(text as nullable text, optional culture as nullable text) as nullable number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|Text value to convert to a number. If **text** does not represent a valid number, **Expression.Error** is thrown.|  
|optional culture|A text value corresponding to the culture values supported on your version of Windows, such as "en-US". If the culture is not specified, the current user culture is used. For a list of culture names, see [National Language Support (NLS) API Reference](https://msdn.microsoft.com/en-us/goglobal/bb896001.aspx).|  
  
## Examples  
  
```powerquery-m 
Number.FromText("1") equals 1  
```  
  
```powerquery-m
Number.FromText("a") equals error  
```  
