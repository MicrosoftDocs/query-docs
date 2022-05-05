---
description: "Learn more about: Logical.From"
title: "Logical.From | Microsoft Docs"
ms.date: 4/13/2022
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Logical.From

## Syntax

<pre>
Logical.From(<b>value</b> as any) as nullable logical
</pre>

## About

Returns a `logical` value from the given `value`. If the given `value` is `null`, **Logical.From** returns `null`. If the given `value` is `logical`, `value` is returned. 

Values of the following types can be converted to a `logical` value:

* `text`: A `logical` value from the text value, either `"true"` or `"false"`. Refer to [Logical.FromText](/powerquery-m/logical-fromtext) for details.
* `number`: `false` if `value` equals `0`, `true` otherwise.

If `value` is of any other type, an error is returned.

## Example 1

Convert `2` to a `logical` value.

**Usage**

```powerquery-m
Logical.From(2)
```

**Output**

`true`
