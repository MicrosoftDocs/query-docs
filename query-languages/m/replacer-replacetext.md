---
description: "Learn more about: Replacer.ReplaceText"
title: "Replacer.ReplaceText"
ms.date: 3/14/2022
---
# Replacer.ReplaceText

## Syntax

<pre>
Replacer.ReplaceText(<b>text</b> as nullable text, <b>old</b> as text, <b>new</b> as text) as nullable text
</pre>
  
## About

Replaces the `old` text in the original `text` with the `new` text. This replacer function can be used in `List.ReplaceValue` and `Table.ReplaceValue`.

## Example 1

Replace the text "hE" with "He" in the string "hEllo world".

**Usage**

```powerquery-m
Replacer.ReplaceText("hEllo world", "hE", "He")
```

**Output**

`"Hello world"`
