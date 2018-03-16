---
title: "Table.FillDown | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: bb548e07-8c08-47ec-9305-51605b3f82b8
caps.latest.revision: 8
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.FillDown
  <code>Table.FillDown(<b>table</b> as table, <b>columns</b> as list) as table</code>

## About
Returns a table from the <code>table</code> specified where the value of a previous cell is propagated to the null-valued cells below in the <code>columns</code> specified.

## Example 1
Return a table with the null values in column [Place] filled with the value above them from the table.

<code>Table.FillDown(Table.FromRecords({[Place=1, Name="Bob"], [Place=null, Name="John"], [Place=2, Name="Brad"], [Place=3, Name="Mark"], [Place=null, Name="Tom"], [Place=null, Name="Adam"]}), {"Place"})</code>

<table> <tr> <th>Place</th> <th>Name</th> </tr> <tr> <td>1</td> <td>Bob</td> </tr> <tr> <td>1</td> <td>John</td> </tr> <tr> <td>2</td> <td>Brad</td> </tr> <tr> <td>3</td> <td>Mark</td> </tr> <tr> <td>3</td> <td>Tom</td> </tr> <tr> <td>3</td> <td>Adam</td> </tr> </table>

  
