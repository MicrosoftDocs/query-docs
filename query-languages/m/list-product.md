---
title: "List.Product | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# List.Product

  
## About  
Returns the product from a list of numbers.  
  
## Syntax

<pre>
List.Product(list as list) as number  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## <a name="__toc360789396"></a>Remarks  
  
-   If the list is empty, an Expression.Error is thrown.  
  
## Examples  
  
```powerquery-m 
List.Product({2, 3, 4}) equals 24  
```  
  
```powerquery-m
List.Product({}) equals error  
```  
