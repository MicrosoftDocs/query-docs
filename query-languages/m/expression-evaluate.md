---
title: "Expression.Evaluate | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Expression.Evaluate
  
## About  
Evaluates a Text expression and returns the evaluated value.  
  
## Syntax

<pre>
Expression.Evaluate(expression as text, optional environment as [...]) as any  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|expression|The expression to evaluate.|  
|optional environment|The expression environment.|  
  
## Examples  

```powerquery-m
Expression.Evaluate("1 + 1")
``` 
equals 2  
  
```powerquery-m
Expression.Evaluate("1 +") 
```
equals Error  
  
```powerquery-m
Expression.Evaluate(  
"section Section1; shared X = 1;"  
)
```  
equals  Error, only expressions are supported  
