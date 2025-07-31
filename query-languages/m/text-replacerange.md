---
description: "Learn more about: Text.ReplaceRange"
title: "Text.ReplaceRange"
ms.subservice: m-source
---
# Text.ReplaceRange

## Syntax

<pre>
Text.ReplaceRange(
    <b>text</b> as nullable text,
    <b>offset</b> as number,
    <b>count</b> as number,
    <b>newText</b> as text
) as nullable text
</pre>
  
## About

Returns the result of removing a number of characters, `count`, from text value `text` beginning at position `offset` and then inserting the text value `newText` at the same position in `text`.

## Example 1

Replace a single character at position 2 in text value "ABGF" with new text value "CDE".

**Usage**

```powerquery-m
Text.ReplaceRange("ABGF", 2, 1, "CDE")
```

**Output**

`"ABCDEF"`
