---
description: "Learn more about: GeometryPoint.From"
title: "GeometryPoint.From"
ms.subservice: m-source
---
# GeometryPoint.From

## Syntax

<pre>
GeometryPoint.From(<b>x</b> as number, <b>y</b> as number, optional <b>z</b> as nullable number, optional <b>m</b> as nullable number, optional <b>srid</b> as nullable number) as record
</pre>

## About

Creates a record representing a geometric point from its constituent parts, such as X coordinate, Y coordinate, and if present, Z coordinate and measure (M). An optional spatial reference identifier (SRID) can be given if different from the default value (0).
