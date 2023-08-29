---
description: "Learn more about: Cube.AddAndExpandDimensionColumn"
title: "Cube.AddAndExpandDimensionColumn"
---
# Cube.AddAndExpandDimensionColumn

## Syntax

<pre>Cube.AddAndExpandDimensionColumn(**cube** as table, **dimensionSelector** as any, **attributeNames** as list, optional **newColumnNames** as any) as table
</pre>

## About

Merges the specified dimension table, `dimensionSelector`, into the cube's, `cube`, filter context and changes the dimensional granularity by expanding the specified set, `attributeNames`, of dimension attributes. The dimension attributes are added to the tabular view with columns named `newColumnNames`, or `attributeNames` if not specified.
