---
title: "Text.Contains | Microsoft Docs"
ms.date: 8/2/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Text.Contains

## Syntax

<pre>
Text.Contains(<b>text</b> as nullable text, <b>substring</b> as text, optional <b>comparer</b> as nullable function) as nullable logical 
</pre>
  
## About  
Detects whether the text `text` contains the text `substring`. Returns true if the text is found. <div> `comparer` is a `Comparer` which is used to control the comparison. Comparers can be used to provide case insensitive or culture and locale aware comparisons. </div> <div> The following built in comparers are available in the formula language: </div> <ul> <li><code>Comparer.Ordinal</code>: Used to perform an exact ordinal comparison</li> <li><code>Comparer.OrdinalIgnoreCase</code>: Used to perform an exact ordinal case-insensitive comparison</li> <li> <code>Comparer.FromCulture</code>: Used to perform a culture aware comparison</li> </ul>

## Example 1
Find if the text "Hello World" contains "Hello".

```powerquery-m
Text.Contains("Hello World", "Hello")
```

`true`

## Example 2
Find if the text "Hello World" contains "hello".

```powerquery-m
Text.Contains("Hello World", "hello")
```

`false`
