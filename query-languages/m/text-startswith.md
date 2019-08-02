---
title: "Text.StartsWith | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.StartsWith

## Syntax

<pre>
Text.StartsWith(<b>text</b> as nullable text, <b>substring</b> as text, optional <b>comparer</b> as nullable function) as nullable logical 
</pre>
  
## About  
Returns true if text value `text` starts with text value `substring`. <ul> <li><code>text</code>: <i></i> A <code>text</code> value which is to be searched</li> <li><code>substring</code>: <i></i> A <code>text</code> value which is the substring to be searched for in <code>substring</code></li> <li><code>comparer</code>: <i>[Optional]</i> A <code>Comparer</code> used for controlling the comparison. For example, <code>Comparer.OrdinalIgnoreCase</code> may be used to perform case insensitive searches</li> </ul> <div> `comparer` is a `Comparer` which is used to control the comparison. Comparers can be used to provide case insensitive or culture and locale aware comparisons. </div> <div> The following built in comparers are available in the formula language: </div> <ul> <li><code>Comparer.Ordinal</code>: Used to perform an exact ordinal comparison</li> <li><code>Comparer.OrdinalIgnoreCase</code>: Used to perform an exact ordinal case-insensitive comparison</li> <li> <code>Comparer.FromCulture</code>: Used to perform a culture aware comparison</li> </ul>

## Example 1
Check if the text "Hello, World" starts with the text "hello".

```powerquery-m
Text.StartsWith("Hello, World", "hello")
```

`false`

## Example 2
Check if the text "Hello, World" starts with the text "Hello".

```powerquery-m
Text.StartsWith("Hello, World", "Hello")
```

`true`
