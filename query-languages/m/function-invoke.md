---
title: "Function.Invoke | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Function.Invoke

## Syntax

<pre>
Function.Invoke(<b>function</b> as function, <b>args</b> as list) as any 
</pre>
  
## About  
Invokes the given function using the specified list of arguments and returns the result.

## Example 1
Invokes Record.FieldNames with one argument [A=1,B=2]

```powerquery-m
Function.Invoke(Record.FieldNames, {[A = 1, B = 2]}
```

<table> <tr><td>A</td></tr> <tr><td>B</td></tr> </table>
