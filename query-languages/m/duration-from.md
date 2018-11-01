---
title: "Duration.From | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Duration.From

  
## About  
Returns a duration value from a value.  
  
## Syntax

<pre>
Duration.From(value as any) as nullable duration  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to convert.|  
  
Values of the following types can be converted to a duration value:  
  
|**Type to Convert**|**Description**|  
|-----------------------|-------------------|  
|text|Returns a duration value from a text value in a elapsed time format of d.h:m:s. For more details, see Duration.FromText.|  
|number|A duration equivalent to the number of whole and fractional days expressed by value.|  
|Any other type|An error is returned|  
  
## <a name="__toc360789120"></a>Remarks  
  
-   If a value is null, Duration.From returns null.  
  
-   If a value is duration, the same value is returned.  
  
## Example  
  
```powerquery-m
Duration.From(2.525) equals #duration(2,12,36,0)  
```  
