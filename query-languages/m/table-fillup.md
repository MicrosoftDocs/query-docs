---
title: "Table.FillUp | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 6cd6d109-f72d-4103-aadf-09b9a1b01f9d
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.FillUp
<code>Table.FillUp(<b>table</b> as table, <b>columns</b> as list) as table</code>

## About
Returns a table from the <code>table</code> specified where the value of the next cell is propagated to the null-valued cells above in the <code>columns</code> specified.

## Example 1
Return a table with the null values in column [Column2] filled with the value below them from the table.

<code>Table.FillUp(Table.FromRecords({[Column1 = 1, Column2 = 2], [Column1 = 3, Column2 = null], [Column1 = 5, Column2 = 3]}), {"Column2"})</code>

<table> <tr> <th>Column1</th> <th>Column2</th> </tr> <tr> <td>1</td> <td>2</td> </tr> <tr> <td>3</td> <td>3</td> </tr> <tr> <td>5</td> <td>3</td> </tr> </table>
