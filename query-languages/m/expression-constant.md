---
description: "Learn more about: Expression.Constant"
title: "Expression.Constant | Microsoft Docs"
ms.date: 3/11/2022
ms.service: powerquery
ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

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

**Usage**

```powerquery-m
Expression.Constant(123)
```

**Output**

`"123"`

## Example 2

Get the M source code representation of a date value.

**Usage**

```powerquery-m
Expression.Constant(#date(2035, 01, 02))
```

**Output**

`"#date(2035, 1, 2)"`

## Example 3

Get the M source code representation of a text value.

**Usage**

```powerquery-m
Expression.Constant("abc")
```

**Output**

`"""abc"""`
