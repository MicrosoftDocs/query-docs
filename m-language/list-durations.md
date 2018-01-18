---
title: "List.Durations | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 20888ac1-9947-440c-8ddf-4b501b537881
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# List.Durations
<code>List.Durations(**start** as duration, **count** as number, **step** as duration) as list</code>

## About
Returns a list of <code>count</code> <code>duration</code> values, starting at <code>start</code> and incremented by the given <code>duration</code> <code>step</code>.

## Example
Create a list of 5 values starting 1 hour and incrementing by an hour.

```
List.Durations(#duration(0, 1, 0, 0), 5, #duration(0, 1, 0, 0))
```
<table> <tr><td>01:00:00</td></tr> <tr><td>02:00:00</td></tr> <tr><td>03:00:00</td></tr> <tr><td>04:00:00</td></tr> <tr><td>05:00:00</td></tr> </table>
