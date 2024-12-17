---
description: "Learn more about: Text.Lower"
title: "Text.Lower"
ms.subservice: m-source
---
# Text.Lower

## Syntax

<pre>
Text.Lower(<b>text</b> as nullable text, optional <b>culture</b> as nullable text) as nullable text
</pre>
  
## About

Returns the result of converting all characters in `text` to lowercase. An optional `culture` may also be provided (for example, "en-US").

## Example 1

Get the lowercase version of "AbCd".

**Usage**

```powerquery-m
Text.Lower("AbCd")
```

**Output**

`"abcd"`

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
