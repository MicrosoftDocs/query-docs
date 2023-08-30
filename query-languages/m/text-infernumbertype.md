---
description: "Learn more about: Text.InferNumberType"
title: "Text.InferNumberType"
---
# Text.InferNumberType

## Syntax

<pre>
Text.InferNumberType(<b>text</b> as text, optional <b>culture</b> as nullable text) as type
</pre>

## About

Infers the granular number type (Int64.Type, Double.Type, and so on) of `text`. An error is raised if `text` is not a number. An optional `culture` may also be provided (for example, "en-US").
