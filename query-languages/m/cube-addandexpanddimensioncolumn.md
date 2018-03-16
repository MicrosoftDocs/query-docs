---
title: "Cube.AddAndExpandDimensionColumn | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 28c1f8f5-8c04-4d55-89b7-e399c6d720c7
caps.latest.revision: 2
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Cube.AddAndExpandDimensionColumn
<code>Cube.AddAndExpandDimensionColumn(**cube** as table, **dimensionSelector** as any, **attributeNames** as list, optional **newColumnNames** as any) as table</code>

## About
Merges the specified dimension table, <code>dimensionSelector</code>, into the cube’s, <code>cube</code>, filter context and changes the dimensional granularity by expanding the specified set, <code>attributeNames</code>, of dimension attributes. The dimension attributes are added to the tabular view with columns named <code>newColumnNames</code>, or <code>attributeNames</code> if not specified.
