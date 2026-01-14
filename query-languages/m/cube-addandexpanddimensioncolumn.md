---
description: "Learn more about: Cube.AddAndExpandDimensionColumn"
title: "Cube.AddAndExpandDimensionColumn"
ms.subservice: m-source
ms.topic: reference
---
# Cube.AddAndExpandDimensionColumn

## Syntax

<pre>
Cube.AddAndExpandDimensionColumn(
    <b>cube</b> as table,
    <b>dimensionSelector</b> as any,
    <b>attributeNames</b> as list,
    optional <b>newColumnNames</b> as any
) as table
</pre>

## About

Merges the specified dimension table, `dimensionSelector`, into the cube's, `cube`, filter context and changes the dimensional granularity by expanding the specified set, `attributeNames`, of dimension attributes. The dimension attributes are added to the tabular view with columns named `newColumnNames`, or `attributeNames` if not specified.
