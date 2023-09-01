---
description: "Learn more about: Text.Select"
title: "Text.Select"
---
# Text.Select

## Syntax

<pre>
Text.Select(<b>text</b> as nullable text, <b>selectChars</b> as any) as nullable text
</pre>

## About

Returns a copy of the text value `text` with all the characters not in `selectChars` removed.

## Example 1

Select all characters in the range of 'a' to 'z' from the text value.

**Usage**

```powerquery-m
Text.Select("a,b;c", {"a".."z"})
```

**Output**

`"abc"`
