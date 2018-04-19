---
title: "Cube.AddAndExpandDimensionColumn | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Cube.AddAndExpandDimensionColumn
<code>Cube.AddAndExpandDimensionColumn(**cube** as table, **dimensionSelector** as any, **attributeNames** as list, optional **newColumnNames** as any) as table</code>

## About
Merges the specified dimension table, <code>dimensionSelector</code>, into the cube’s, <code>cube</code>, filter context and changes the dimensional granularity by expanding the specified set, <code>attributeNames</code>, of dimension attributes. The dimension attributes are added to the tabular view with columns named <code>newColumnNames</code>, or <code>attributeNames</code> if not specified.
