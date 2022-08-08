---
description: "Learn more about: Text.Trim"
title: "Text.Trim"
ms.date: 3/14/2022
---
# Text.Trim

## Syntax

<pre>
Text.Trim(<b>text</b> as nullable text, optional <b>trim</b> as any) as nullable text
</pre>
  
## About

Returns the result of removing all leading and trailing whitespace from text value `text`.

## Example 1

Remove leading and trailing whitespace from " a b c d ".

**Usage**

```powerquery-m
Text.Trim("     a b c d    ")
```

**Output**

`"a b c d"`
