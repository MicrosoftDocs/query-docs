---
description: "Learn more about: Text.TrimEnd"
title: "Text.TrimEnd"
ms.date: 4/22/2022
---
# Text.TrimEnd

## Syntax

<pre>
Text.TrimEnd(<b>text</b> as nullable text, optional <b>trim</b> as any) as nullable text
</pre>
  
## About

Returns the result of removing all trailing whitespace from text value `text`.

## Example 1

Remove trailing whitespace from " a b c d ".

**Usage**

```powerquery-m
Text.TrimEnd("     a b c d    ")
```

**Output**

<pre>
"     a b c d"
</pre>
