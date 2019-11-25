---
title: "Expression.Identifier | Microsoft Docs"
ms.date: 8/21/2019
ms.service: powerquery
ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Expression.Identifier

## Syntax

<pre>
Expression.Identifier(<b>name</b> as text) as text
</pre>
  
## About  
Returns the M source code representation of an identifier `name`.

## Example 1
Get the M source code representation of an identifier.

```powerquery-m
Expression.Identifier("MyIdentifier")
```

`"MyIdentifier"`

## Example 2
Get the M source code representation of an identifier that contains a space.

```powerquery-m
Expression.Identifier("My Identifier")
```

`"#""My Identifier"""`