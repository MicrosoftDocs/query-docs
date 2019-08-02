---
title: "Text.EndsWith | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.EndsWith

## Syntax

<pre>
Text.EndsWith(<b>text</b> as nullable text, <b>substring</b> as text, optional <b>comparer</b> as nullable function) as nullable logical 
</pre>
  
## About  
Indicates whether the given text, `text`, ends with the specified value, `substring`. The indication is case-sensitive. <div> `comparer` is a `Comparer` which is used to control the comparison. Comparers can be used to provide case insensitive or culture and locale aware comparisons. </div> <div> The following built in comparers are available in the formula language: </div> <ul> <li><code>Comparer.Ordinal</code>: Used to perform an exact ordinal comparison</li> <li><code>Comparer.OrdinalIgnoreCase</code>: Used to perform an exact ordinal case-insensitive comparison</li> <li> <code>Comparer.FromCulture</code>: Used to perform a culture aware comparison</li> </ul>

## Example 1
Check if "Hello, World" ends with "world".

```powerquery-m
Text.EndsWith("Hello, World", "world")
```

`false`

## Example 2
Check if "Hello, World" ends with "World".

```powerquery-m
Text.EndsWith("Hello, World", "World")
```

`true`
