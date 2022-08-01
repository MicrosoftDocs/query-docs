---
description: "Learn more about: Replacer.ReplaceValue"
title: "Replacer.ReplaceValue"
ms.date: 3/14/2022
---
# Replacer.ReplaceValue

## Syntax

<pre>
Replacer.ReplaceValue(<b>value</b> as any, <b>old</b> as any, <b>new</b> as any) as any
</pre>
  
## About

Replaces the `old` value in the original `value` with the `new` value. This replacer function can be used in `List.ReplaceValue` and `Table.ReplaceValue`.

## Example 1

Replace the value 11 with the value 10.

**Usage**

```powerquery-m
Replacer.ReplaceValue(11, 11, 10)
```

**Output**

`10`
