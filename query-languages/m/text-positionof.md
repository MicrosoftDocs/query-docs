---
title: "Text.PositionOf | Microsoft Docs"
ms.date: 5/22/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.PositionOf
<code>Text.PositionOf(<b>text</b> as text, <b>substring</b> as text, optional <b>occurrence</b> as nullable number, optional <b>comparer</b> as nullable function) as any</code>

## About
Returns the position of the specified occurrence of the text value <code>substring</code> found in <code>text</code>. An optional parameter <code>occurrence</code> may be used to specify which occurrence position to return (first occurrence by default). Returns -1 if <code>substring</code> was not found. <div> <code>comparer</code> is a <code>Comparer</code> which is used to control the comparison. Comparers can be used to provide case insensitive or culture and locale aware comparisons. </div> <div> The following built in comparers are available in the formula language: </div> <ul> <li><code>Comparer.Ordinal</code>: Used to perform an exact ordinal comparison</li> <li><code>Comparer.OrdinalIgnoreCase</code>: Used to perform an exact ordinal case-insensitive comparison</li> <li> <code>Comparer.FromCulture</code>: Used to perform a culture aware comparison</li> </ul>

## Example 1
Get the position of the first occurrence of "World" in the text "Hello, World! Hello, World!".

<code>Text.PositionOf("Hello, World! Hello, World!", "World")</code>

<code>7</code>

## Example 2
Get the position of last occurrence of "World" in "Hello, World! Hello, World!".

<code>Text.PositionOf("Hello, World! Hello, World!", "World", Occurrence.Last)</code>

<code>21</code>