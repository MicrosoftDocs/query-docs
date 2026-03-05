---
description: "Learn more about: Cube.ReplaceDimensions"
title: "Cube.ReplaceDimensions"
ms.subservice: m-source
ms.topic: reference
---
# Cube.ReplaceDimensions

## Syntax

<pre>
Cube.ReplaceDimensions(<b>cube</b> as table, <b>dimensions</b> as table) as table
</pre>

## About

Replaces the set of dimensions returned by `Cube.Dimensions`. For example, this function can be used to add an ID column to a dimension attribute, so that the data source can group on the ID rather than the displayed value.
