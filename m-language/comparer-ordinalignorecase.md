---
title: "Comparer.OrdinalIgnoreCase | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 1cc5fbe3-6560-4c35-8125-fc822c956453
caps.latest.revision: 3
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Comparer.OrdinalIgnoreCase
<code>Comparer.OrdinalIgnoreCase(**x** as any, **y** as any) as number</code>

## About
Returns a case-insensitive comparer function which uses Ordinal rules to compare the provided values <code>x</code> and <code>y</code>.

## Example 
Using case-insensitive Ordinal rules, compare "Abc" with "abc". Note "Abc" is less than "abc" using <code>Comparer.Ordinal</code>. 

<code>Comparer.OrdinalIgnoreCase("Abc", "abc")</code>

<code>0</code>