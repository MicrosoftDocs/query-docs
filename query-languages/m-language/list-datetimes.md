---
title: "List.DateTimes | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: da1803d7-fd0f-48d9-ae14-80bc282de909
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.DateTimes
<code>List.Times(**start** as time, **count** as number, **step** as duration) as list</code>

## About
Returns a list of <code>time</code> values of size <code>count</code>, starting at <code>start</code>. The given increment, <code>step</code>, is a <code>duration</code> value that is added to every value.

  
## Example  
  Create a list of 4 values starting from noon (#time(12, 0, 0)) incrementing by one hour (#duration(0, 1, 0, 0)).
```  
List.DateTimes(#time(10, 0, 0), #duration(0, 1, 0, 0), 5) List.Times(#time(12, 0, 0), 4, #duration(0, 1, 0, 0))   
```  
<table> <tr><td>12:00:00</td></tr> <tr><td>13:00:00</td></tr> <tr><td>14:00:00</td></tr> <tr><td>15:00:00</td></tr> </table>