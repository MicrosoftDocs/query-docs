---
title: "List.Zip | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 639194fb-1f02-4f5b-acea-1bf5695304e5
caps.latest.revision: 2
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.Zip
<code>List.Zip(<b>lists</b> as list) as list</code>

## About
Takes a list of lists, <code>lists</code>, and returns a list of lists combining items at the same position.

## Example 1
Zips the two simple lists {1, 2} and {3, 4}.

<code>List.Zip({{1, 2}, {3, 4}})</code>

<table> <tr><td>[List]</td></tr> <tr><td>[List]</td></tr> </table>

## Example 2
Zips the two simple lists of different lengths {1, 2} and {3}.

<code>List.Zip({{1, 2}, {3}})</code>

<table> <tr><td>[List]</td></tr> <tr><td>[List]</td></tr> </table> 
