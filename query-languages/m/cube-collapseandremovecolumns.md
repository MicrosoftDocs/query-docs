---
title: "Cube.CollapseAndRemoveColumns | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Cube.CollapseAndRemoveColumns
<code>Cube.CollapseAndRemoveColumns(**cube** as table, **columnNames** as list) as table</code>

## About
Changes the dimensional granularity of the filter context for the <code>cube</code> by collapsing the attributes mapped to the specified columns <code>columnNames</code>. The columns are also removed from the tabular view of the cube.