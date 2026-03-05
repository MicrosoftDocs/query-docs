---
description: "Learn more about: Duration.From"
title: "Duration.From"
ms.subservice: m-source
ms.topic: reference
---
# Duration.From

## Syntax

<pre>
Duration.From(<b>value</b> as any) as nullable duration
</pre>
  
## About

Returns the duration value from the given value.

* `value`: The value from which the duration is derived. If the given `value` is `null`, this function returns `null`. If the given `value` is a `duration`, `value` is returned. Values of the following types can be converted to a `duration` value:
  * `text`: A `duration` value from textual elapsed time forms (d.h:m:s). Refer to [Duration.FromText](duration-fromtext.md) for details.
  * `number`: A `duration` equivalent to the number of whole and fractional days expressed by `value`.

If `value` is of any other type, an error is returned.

## Example 1

Convert `2.525` into a `duration` value.

**Usage**

```powerquery-m
Duration.From(2.525)
```

**Output**

`#duration(2, 12, 36, 0)`

## Example 2

Convert the text value `"2.05:55:20.34567"` into a `duration` value.

**Usage**

```powerquery-m
Duration.From("2.05:55:20.34567")
```

**Output**

`#duration(2, 5, 55, 20.3456700)`
