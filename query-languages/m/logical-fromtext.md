---
title: "Logical.FromText | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Logical.FromText

  
## About  
Returns a logical value of true or false from a text value.  
  
## Syntax

<pre> 
Logical.FromText(text as nullable text) as nullable logical  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to evaluate.|  
  
## Examples  
  
```powerquery-m
Logical.FromText("true") equals true  
```  
  
```powerquery-m
Logical.FromText("a") equals error  
```  
