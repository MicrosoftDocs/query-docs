---
title: "Single.From | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Single.From

  
## About  
Returns a Single number value from the given value.  
  
## Syntax

<pre>
Single.From(value as any, optional culture as nullable text)  as nullable number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to convert.|  
|optional culture|A text value corresponding to the culture values supported on your version of Windows, such as "en-US". If the culture is not specified, the current user culture is used. For a list of culture names, see [National Language Support (NLS) API Reference](https://msdn.microsoft.com/en-us/goglobal/bb896001.aspx).|  
  
## Remarks  
If the given value is null, Single.From returns null. If the given value is number within the range of Single, value is returned, otherwise an error is returned. If the given value is of any other type, see Number.FromText for converting it to number value, then the previous statement about converting number value to Single number value applies.  
  
## Examples  
  
```powerquery-m
Single.From("1.5") equals 1.5  
```  
