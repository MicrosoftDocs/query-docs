---
title: "Cube.Dimensions | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 3ce1f029-fb6e-4a80-aac6-79b73d74de37
caps.latest.revision: 2
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Cube.Dimensions
<code>Cube.Dimensions(**cube** as table) as table</code>

## About
Returns a table containing the set of available dimensions within the <code>cube</code>. Each dimension is a table containing a set of dimension attributes and each dimension attribute is represented as a column in the dimension table. Dimensions can be expanded in the cube using Cube.AddAndExpandDimensionColumn. 


