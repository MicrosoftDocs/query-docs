---
description: "Learn more about: Lines.ToText"
title: "Lines.ToText"
ms.subservice: m-source
ms.topic: reference
---

# Lines.ToText

## Syntax

<pre>
Lines.ToText(<b>lines</b> as list, optional <b>lineSeparator</b> as nullable text) as text
</pre>

## About

Converts a list of text values into a single text value. The specified line separator is appended to each line. If not specified, then the carriage return and line feed characters are used as the line separator.

## Example

Convert three text values into a three-line text value.

**Usage**

```powerquery-m
Lines.ToText({"ID,Name", "1,Bob Smith", "2,Jan Lee"})
```

**Output**

`"ID,Name#(cr)#(lf)1,Bob Smith#(cr)#(lf)2,Jan Lee#(cr)#(lf)"`
