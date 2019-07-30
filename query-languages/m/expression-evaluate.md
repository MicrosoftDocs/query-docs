---
title: "Expression.Evaluate | Microsoft Docs"
ms.date: 7/30/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Expression.Evaluate

## Syntax

<pre>
Expression.Evaluate(<b>document</b> as text, optional <b>environment</b> as nullable record) as any 
</pre>
  
## About  
Evaluates a Text expression and returns the evaluated value.  
  
  
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
