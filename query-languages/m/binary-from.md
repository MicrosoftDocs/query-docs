---
description: "Learn more about: Binary.From"
title: "Binary.From"
ms.date: 4/13/2022
---
# Binary.From

## Syntax  

<pre>
Binary.From(<b>value</b> as any, optional <b>encoding</b> as nullable number) as nullable binary
</pre>

## About

Returns a `binary` value from the given `value`. If the given `value` is `null`, **Binary.From** returns `null`. If the given `value` is `binary`, `value` is returned. Values of the following types can be converted to a `binary` value:

* `text`: A `binary` value from the text representation. Refer to [Binary.FromText](/powerquery-m/binary-fromtext) for details.

If `value` is of any other type, an error is returned.

## Example 1

Get the `binary` value of `"1011"`.

**Usage**

```powerquery-m
Binary.From("1011")
```

**Output**

`Binary.FromText("1011", BinaryEncoding.Base64)`
