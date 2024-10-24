---
description: "Learn more about: Text.Proper"
title: "Text.Proper"
---
# Text.Proper

## Syntax

<pre>
Text.Proper(<b>text</b> as nullable text, optional <b>culture</b> as nullable text) as nullable text
</pre>
  
## About

Returns the result of capitalizing only the first letter of each word in text value `text`. All other letters are returned in lowercase. An optional `culture` may also be provided (for example, "en-US").

## Example 1

Use `Text.Proper` on a simple sentence.

**Usage**

```powerquery-m
Text.Proper("the QUICK BrOWn fOx jUmPs oVER tHe LAzy DoG")
```

**Output**

`"The Quick Brown Fox Jumps Over The Lazy Dog"`

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
