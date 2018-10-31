---
title: "List.NonNullCount | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.NonNullCount

  
## About  
Returns the number of items in a list excluding null values  
  
## Syntax

<pre>
List.NonNullCount(list as list) as number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## <a name="__goback"></a>Example  
  
```powerquery-m
List.NonNullCount({1, null}) equals 1  
```  
