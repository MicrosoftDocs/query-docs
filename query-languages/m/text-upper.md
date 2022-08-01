---
description: "Learn more about: Text.Upper"
title: "Text.Upper"
ms.date: 3/14/2022
---
# Text.Upper

## Syntax

<pre>
Text.Upper(<b>text</b> as nullable text, optional <b>culture</b> as nullable text) as nullable text
</pre>  
  
## About

Returns the result of converting all characters in `text` to uppercase. An optional `culture` may also be provided (for example, "en-US").

## Example 1

Get the uppercase version of "aBcD".

**Usage**

```powerquery-m
Text.Upper("aBcD")
```

**Output**

`"ABCD"`
