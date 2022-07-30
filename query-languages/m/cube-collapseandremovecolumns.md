---
description: "Learn more about: Cube.CollapseAndRemoveColumns"
title: "Cube.CollapseAndRemoveColumns"
ms.date: 4/16/2018
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Cube.CollapseAndRemoveColumns

## Syntax

<pre>
Cube.CollapseAndRemoveColumns(**cube** as table, **columnNames** as list) as table
</pre>

## About
Changes the dimensional granularity of the filter context for the `cube` by collapsing the attributes mapped to the specified columns `columnNames`. The columns are also removed from the tabular view of the cube.
