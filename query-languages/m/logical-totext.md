---
title: "Logical.ToText | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Logical.ToText

  
## About  
Returns a text value from a logical value.  
  
## Syntax

<pre>
Logical.ToText(logical as nullable logical) as nullable text  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|logical|The logical value to evaluate.|  
  
## Example  
  
```powerquery-m
Logical.ToText(true) equals "true"  
```  
