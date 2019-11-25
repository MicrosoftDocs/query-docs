---
title: "Cube.AddMeasureColumn | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Cube.AddMeasureColumn

## Syntax

<pre>
Cube.AddMeasureColumn(**cube** as table, **column** as text, **measureSelector** as any) as table
</pre>

## About
Adds a column with the name `column` to the `cube` that contains the results of the measure `measureSelector` applied in the row context of each row. Measure application is affected by changes to dimension granularity and slicing. Measure values will be adjusted after certain cube operations are performed.