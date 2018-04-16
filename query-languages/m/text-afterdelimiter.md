---
title: "Text.AfterDelimiter | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.AfterDelimiter
<code>Text.AfterDelimiter(**text** as nullable text, **delimiter** as text, optional **index** as any) as any</code>

## About
Returns the portion of <code>text</code> after the specified <code>delimiter</code>. An optional numeric <code>index</code> indicates which occurrence of the <code>delimiter</code> should be considered. An optional list <code>index</code> indicates which occurrence of the <code>delimiter</code> should be considered, as well as whether indexing should be done from the start or end of the input.

## Example 1
Get the portion of "111-222-333" after the (first) hyphen.

<code>Text.AfterDelimiter("111-222-333", "-")</code>

<code>"222-333"</code>

## Example 2
Get the portion of "111-222-333" after the second hyphen.

<code>Text.AfterDelimiter("111-222-333", "-", 1)</code>

<code>"333"</code>

## Example 3
Get the portion of "111-222-333" after the second hyphen from the end.

<code>Text.AfterDelimiter("111-222-333", "-", {1, RelativePosition.FromEnd})</code>

<code>"222-333"</code>


  
