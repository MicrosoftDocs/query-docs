---
description: "Learn more about: GeographyPoint.From"
title: "GeographyPoint.From"
ms.subservice: m-source
---
# GeographyPoint.From

## Syntax

<pre>
GeographyPoint.From(
    <b>longitude</b> as number,
    <b>latitude</b> as number,
    optional <b>z</b> as nullable number,
    optional <b>m</b> as nullable number,
    optional <b>srid</b> as nullable number
) as record
</pre>

## About

Creates a record representing a geographic point from its constituent parts, such as longitude, latitude, and if present, elevation (Z) and measure (M). An optional spatial reference identifier (SRID) can be given if different from the default value (4326).
