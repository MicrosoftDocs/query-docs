---
title: "Expression.Constant | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Expression.Constant

  
## About  
Returns a constant text literal from a value.  
  
```  
Expression.Constant(value as any) as text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Text literal value.|  
  
## Examples  
Expression.Constant(1)  equals  "1"  
  
Expression.Constant(1 + 1)  equals  "2"  
  
Expression.Constant(true)  equals  "true"  
  
Expression.Constant("abc")  equals  """abc"""  
  
Expression.Constant("#(tab)")  equals  """#(#)(tab)"""  
  
Expression.Constant(#date(2011, 1, 1))  equals  "#date(2011, 1, 1)"  
  
Expression.Constant((x) =&gt; x)  equals  Error: Functions not supported  
  
Expression.Constant({1, 2, 3})  equals  Error: Lists not supported  
  
Expression.Constant([a = 1 + 1])  equals  Error: Records not supported  
  
