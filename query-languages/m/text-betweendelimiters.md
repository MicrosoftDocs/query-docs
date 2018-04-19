---
title: "Text.BetweenDelimiters | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.BetweenDelimiters
<code>Text.BetweenDelimiters(**text** as nullable text, **startDelimiter** as text, **endDelimiter** as text, optional **startIndex** as any, optional **endIndex** as any) as any</code>

## About
Returns the portion of <code>text</code> between the specified <code>startDelimiter</code> and <code>endDelimiter</code>. An optional numeric <code>startIndex</code> indicates which occurrence of the <code>startDelimiter</code> should be considered. An optional list <code>startIndex</code> indicates which occurrence of the <code>startDelimiter</code> should be considered, as well as whether indexing should be done from the start or end of the input. The <code>endIndex</code> is similar, except that indexing is done relative to the <code>startIndex</code>.

## Example 1
Get the portion of "111 (222) 333 (444)" between the (first) open parenthesis and the (first) closed parenthesis that follows it.

<code>Text.BetweenDelimiters("111 (222) 333 (444)", "(", ")")</code>

<code>"222"</code>

## Example 2
Get the portion of "111 (222) 333 (444)" between the second open parenthesis and the first closed parenthesis that follows it.

<code>Text.BetweenDelimiters("111 (222) 333 (444)", "(", ")", 1, 0)</code>

<code>"444"</code>

## Example 3
Get the portion of "111 (222) 333 (444)" between the second open parenthesis from the end and the second closed parenthesis that follows it.

<code>Text.BetweenDelimiters("111 (222) 333 (444)", "(", ")", {1, RelativePosition.FromEnd}, {1, RelativePosition.FromStart})</code>

<code>"222) 333 (444"</code>

  
