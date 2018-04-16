---
title: "Cube.AddMeasureColumn | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Cube.AddMeasureColumn
<code>Cube.AddMeasureColumn(**cube** as table, **column** as text, **measureSelector** as any) as table</code>

## About
Adds a column with the name <code>column</code> to the <code>cube</code> that contains the results of the measure <code>measureSelector</code> applied in the row context of each row. Measure application is affected by changes to dimension granularity and slicing. Measure values will be adjusted after certain cube operations are performed.