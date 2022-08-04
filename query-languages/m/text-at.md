---
description: "Learn more about: Text.At"
title: "Text.At"
ms.date: 3/14/2022
---
# Text.At

## Syntax

<pre>
Text.At(<b>text</b> as nullable text, <b>index</b> as number) as nullable text
</pre>
  
## About

Returns the character in the text value, `text` at position `index`. The first character in the text is at position 0.

## Example 1

Find the character at position 4 in string "Hello, World".

**Usage**

```powerquery-m
Text.At("Hello, World", 4)
```

**Output**

`"o"`
