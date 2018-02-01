---
title: "Cube.AddMeasureColumn | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 1660b9e9-3864-45c1-b887-94af4a72ee25
caps.latest.revision: 2
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Cube.AddMeasureColumn
<code>Cube.AddMeasureColumn(**cube** as table, **column** as text, **measureSelector** as any) as table</code>

## About
Adds a column with the name <code>column</code> to the <code>cube</code> that contains the results of the measure <code>measureSelector</code> applied in the row context of each row. Measure application is affected by changes to dimension granularity and slicing. Measure values will be adjusted after certain cube operations are performed.