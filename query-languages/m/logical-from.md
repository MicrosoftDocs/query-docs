---
title: "Logical.From | Microsoft Docs"
ms.date: 8/30/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Logical.From

<code>Logical.From(<b>value</b> as any) as nullable logical</code>

## About

Returns a <code>logical</code> value from the given <code>value</code>. If the given <code>value</code> is <code>null</code>, <code>Logical.From</code> returns <code>null</code>. If the given <code>value</code> is <code>logical</code>, <code>value</code> is returned. 

Values of the following types can be converted to a <code>logical</code> value: <ul> <li><code>text</code>: A <code>logical</code> value from the text value, either <code>"true"</code> or <code>"false"</code>. See <code>Logical.FromText</code> for details.</li> <li><code>number</code>: <code>false</code> if <code>value</code> equals <code>0</code>, <code>true</code> otherwise.</li> </ul> If <code>value</code> is of any other type, an error is returned.

## Example 1
Convert <code>2</code> to a <code>logical</code> value.

<code>Logical.From(2)</code>

<code>true</code>
