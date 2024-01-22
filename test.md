## Notion to Obsidian

### Basic Blocks

#### Paragraph

This is a simple paragraph

This is a **bolded** paragraph

This is a _italized_ paragraph

This is a _**bolded and italized**_ paragraph

This is a [linked](http://www.google.com/) paragraph

This is a $\text{mathed}$ paragraph

This is a `coded` paragraph

#### Heading

##### This is a simple heading

##### This is a **bolded** heading

##### This is a _italized_ heading

##### This is a _**bolded and italized**_ heading

##### This is a ~~striked~~ heading

##### This is a [linked](http://www.google.com/) heading

##### This is a $\text{mathed}$ heading

##### This is a `coded` heading

#### Code

```json
{
  //...other keys excluded
  "type": "code",
  //...other keys excluded
  "code": {
   	"caption": [],
 		"rich_text": [{
      "type": "text",
      "text": {
        "content": "const a = 3"
      }
    }],
    "language": "javascript"
  }
}
```

#### Quote

> This is a simple quote

> This is a **bolded** quote

> This is a parent quote
>
> > With an inner quote
>
> And another paragraph

### Math

$$
\text{This is a math equation}
$$

$$
x_1, x_2 = \frac{-b \pm \sqrt{c^2 - 4ac}}{2}
$$

### Tables

| Col 1           | Col 2       |
| --------------- | ----------- |
| Col 1 **Row** 1 | Col 2 Row 1 |
| Col 1 _Row_ 3   | Col 2 Row 3 |

### Callout

> [!note]
> This is a simple Callout

> [!note]
> This is a **bolded** Callout

> [!note]
> This is a parent Callout…
>
> > [!note]
> > With an inner Callout!
>
> And a paragraph

### Toggles

* This is a simple toggle

* This is a **bolded** toggle

* This is a parent toggle

  * With an inner toggle

And another paragraph

* #### This is a heading toggle

  With an inner paragraph

* With a bullet point ahead

### Dividers

I am before a divider

***

I am after a divider

***

***

I am after two dividers

### Bulleted Lists

* This is a **bolded** item

* This is a simple item

* This is a parent item

  * With an inner item

  And another paragraph

### Numbered Lists

1. This is a simple item

2. This is a **bolded** item

3. This is a parent item

   1. With an inner item

   And another paragraph