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
`Cube.AddAndExpandDimensionColumn(**cube** as table, **dimensionSelector** as any, **attributeNames** as list, optional **newColumnNames** as any) as table`

## About
Merges the specified dimension table, `dimensionSelector`, into the cube’s, `cube`, filter context and changes the dimensional granularity by expanding the specified set, `attributeNames`, of dimension attributes. The dimension attributes are added to the tabular view with columns named `newColumnNames`, or `attributeNames` if not specified.
