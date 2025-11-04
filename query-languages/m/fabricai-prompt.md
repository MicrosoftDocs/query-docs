---
description: "Learn more about: FabricAI.Prompt"
title: "FabricAI.Prompt"
ms.subservice: m-source
---
# FabricAI.Prompt

## Syntax

<pre>
FabricAI.Prompt(<b>input</b> as text, optional <b>options</b> as record) as text
</pre>

## About

Returns the result of passing the specified `input` to an AI model. An `options` record can be provided in order to specify the context of the request.

## Example 1

Use an AI model to categorize a product review.

**Usage**

```powerquery-m
FabricAI.Prompt(
    "Categorize the review as positive, negative, or neutral, and extract a single key word in parentheses.",
    [Context = [Review = "This is a great product. It only broke four times before we had to return it!"]]
)
```

**Output**

`"Negative (broke)"`
