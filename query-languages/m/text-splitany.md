---
description: "Learn more about: Text.SplitAny"
title: "Text.SplitAny"
ms.subservice: m-source
ms.topic: reference
---
# Text.SplitAny

## Syntax

<pre>
Text.SplitAny(<b>text</b> as text, <b>separators</b> as text) as list
</pre>
  
## About

Returns a list of text values resulting from the splitting of a text value based on any character specified in the delimiter.

* `text`: The text value to split.
* `separator`: The delimiter characters used to split the text.

## Example 1

Create a list from the given text using the specified delimiter characters.

**Usage**

```powerquery-m
Text.SplitAny("Name|Customer ID|Purchase|Month-Day-Year", "|-")
```

**Output**

```powerquery-m
{
    "Name",
    "Customer ID",
    "Purchase",
    "Month",
    "Day",
    "Year"
}
```
