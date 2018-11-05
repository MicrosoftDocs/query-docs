---
title: "Value.FromText | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Value.FromText

  
## About  
Decodes a value from a textual representation, value, and interprets it as a value with an appropriate type. Value.FromText takes a text value and returns a number, a logical value, a null value, a DateTime value, a Duration value, or a text value. The empty text value is interpreted as a null value.  
  
## Syntax

<pre> 
Value.FromText(value as text, optional culture as nullable text)  
</pre>  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|The value to transform.|  
|optional culture|A text value corresponding to the culture values supported on your version of Windows, such as "en-US". If the culture is not specified, the current user culture is used. For a list of culture names, see [National Language Support (NLS) API Reference](https://msdn.microsoft.com/en-us/goglobal/bb896001.aspx).|  
  
## Examples  
  
```powerquery-m
Value.FromText("1") equals 1  
```  
  
```powerquery-m
Value.FromText("2012/5/16") equals #date(2012,5,16)  
```  
  
```powerquery-m
Value.FromText("null") equals null  
```  
  
```powerquery-m 
Value.FromText("somevalue") equals "somevalue"  
```  
