---
title: "Text.BeforeDelimiter | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Text.BeforeDelimiter
<code>Text.BeforeDelimiter(**text** as nullable text, **delimiter** as text, optional **index** as any) as any</code>

## About
Returns the portion of <code>text</code> before the specified <code>delimiter</code>. An optional numeric <code>index</code> indicates which occurrence of the <code>delimiter</code> should be considered. An optional list <code>index</code> indicates which occurrence of the <code>delimiter</code> should be considered, as well as whether indexing should be done from the start or end of the input.

## Example 1
Get the portion of "111-222-333" before the (first) hyphen.

<code>Text.BeforeDelimiter("111-222-333", "-")</code>

<code>"111"</code>

## Example 2
Get the portion of "111-222-333" before the second hyphen.

<code>Text.BeforeDelimiter("111-222-333", "-", 1)</code>

<code>"111-222"</code>

## Example 3
Get the portion of "111-222-333" before the second hyphen from the end.

<code>Text.BeforeDelimiter("111-222-333", "-", {1, RelativePosition.FromEnd})</code>

<code>"111"</code>


  
