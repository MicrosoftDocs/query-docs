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
  
## Syntax

<pre>
Expression.Constant(value as any) as text  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Text literal value.|  
  
## Examples  

```powerquery-m
Expression.Constant(1)  equals  "1"  
```

```powerquery-m 
Expression.Constant(1 + 1)  equals  "2"  
```

```powerquery-m 
Expression.Constant(true)  equals  "true"  
```

```powerquery-m 
Expression.Constant("abc")  equals  """abc"""  
```

```powerquery-m 
Expression.Constant("#(tab)")  equals  """#(#)(tab)"""  
```

```powerquery-m
Expression.Constant(#date(2011, 1, 1))  equals  "#date(2011, 1, 1)"  
```

```powerquery-m 
Expression.Constant((x) =&gt; x)  equals  Error: Functions not supported  
```

```powerquery-m
Expression.Constant({1, 2, 3})  equals  Error: Lists not supported  
```

```powerquery-m
Expression.Constant([a = 1 + 1])  equals  Error: Records not supported  
```
