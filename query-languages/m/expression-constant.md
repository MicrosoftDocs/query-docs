---
title: "Expression.Constant | Microsoft Docs"
ms.date: 8/21/2019
ms.service: powerquery
ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Expression.Constant


## Syntax

<pre>
Expression.Constant(<b>value</b> as any) as text  
</pre>
  
## About  
Returns the M source code representation of a constant value.

## Example 1
Get the M source code representation of a number value.

```powerquery-m
Expression.Constant(123)
```

`"123"`

## Example 2
Get the M source code representation of a date value.

```powerquery-m
Expression.Constant(#date(2035, 01, 02))
```

`"#date(2035, 1, 2)"`

## Example 3
Get the M source code representation of a text value.

```powerquery-m
Expression.Constant("abc")
```

`"""abc"""`