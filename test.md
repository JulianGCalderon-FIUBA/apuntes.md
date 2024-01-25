## Basic Blocks

### Paragraph

This is a simple paragraph

This is a **bolded** paragraph

This is a _italized_ paragraph

This is a _**bolded and italized**_ paragraph

This is a [linked](http://www.google.com/) paragraph

This is a $\text{mathed}$ paragraph

This is a `coded` paragraph

### Heading

#### This is a simple heading

#### This is a **bolded** heading

#### This is a _italized_ heading

#### This is a _**bolded and italized**_ heading

#### This is a ~~striked~~ heading

#### This is a [linked](http://www.google.com/) heading

#### This is a $\text{mathed}$ heading

#### This is a `coded` heading

### Code

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

### Quote

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

:::callout
This is a simple Callout
:::

:::callout
This is a **bolded** Callout
:::

::::callout
This is a parent Callout…

:::callout
With an inner Callout!
:::

And a paragraph
::::

## Lists

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

* This is a simple item

* This is a **bolded** item

* This is a parent item

  * With an inner item

  And another paragraph

### Numbered Lists

1. This is a simple item

2. This is a **bolded** item

3. This is a parent item

   1. With an inner item

   And another paragraph

### Todo Lists

* [ ] This is a simple item

* [x] This is a **bolded** item

* [ ] This is a parent item

  * [x] With an inner item

  And another paragraph

### Mixed Lists

* This is an unordered item

1. This is an ordered item

* [ ] This is a todo item

  * With an inner unordered item

1. This is an ordered item (again)

   * [x] With an inner todo item

## Containers

This is a synced block

> With an inner quote

And another paragraph

This is a synced block

> With an inner quote

And another paragraph

### Links

<https://www.youtube.com/>

A youtube bookmark

[CV Julian Gonzalez Calderon (en).pdf](https://prod-files-secure.s3.us-west-2.amazonaws.com/d4d5bb19-88f8-434c-a8f6-02428c700a6d/c2f47965-689d-4579-a5f0-3371e886ee15/CV_Julian_Gonzalez_Calderon_%28en%29.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256\&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD\&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240125%2Fus-west-2%2Fs3%2Faws4_request\&X-Amz-Date=20240125T032512Z\&X-Amz-Expires=3600\&X-Amz-Signature=10928861339e65bb3f1637ca1a071844e20940a34d4a266faef4118b467839cb\&X-Amz-SignedHeaders=host\&x-id=GetObject)

My resume

![https://prod-files-secure.s3.us-west-2.amazonaws.com/d4d5bb19-88f8-434c-a8f6-02428c700a6d/381d99c0-e3c0-45a0-98a9-56e1075c64bc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256\&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD\&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240125%2Fus-west-2%2Fs3%2Faws4\_request\&X-Amz-Date=20240125T032513Z\&X-Amz-Expires=3600\&X-Amz-Signature=8bd81bc70ea84475007be3bfa4a94e14abf077776a58e66017e82ebe59a05e93\&X-Amz-SignedHeaders=host\&x-id=GetObject](https://prod-files-secure.s3.us-west-2.amazonaws.com/d4d5bb19-88f8-434c-a8f6-02428c700a6d/381d99c0-e3c0-45a0-98a9-56e1075c64bc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256\&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD\&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240125%2Fus-west-2%2Fs3%2Faws4_request\&X-Amz-Date=20240125T032513Z\&X-Amz-Expires=3600\&X-Amz-Signature=8bd81bc70ea84475007be3bfa4a94e14abf077776a58e66017e82ebe59a05e93\&X-Amz-SignedHeaders=host\&x-id=GetObject)

Spirit **Galopando**

<https://prod-files-secure.s3.us-west-2.amazonaws.com/d4d5bb19-88f8-434c-a8f6-02428c700a6d/8613a46d-9d31-4e63-9011-b9a811b50d07/CV_Julian_Gonzalez_Calderon_%28en%29.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240125%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240125T032513Z&X-Amz-Expires=3600&X-Amz-Signature=73694cdd54a1159b3e087bd8476776587ebc7321c9a52b12c1f1576dd0c809b0&X-Amz-SignedHeaders=host&x-id=GetObject>

Embeded PDF

[A Child Page](https://www.notion.so/A-Child-Page-7696040109c94270ada547c3459a3882)

![https://www.youtube.com/watch?v=zt0Un7OVPjE\&list=LL\&index=168](https://www.youtube.com/watch?v=zt0Un7OVPjE\&list=LL\&index=168)

We are Number One!

<iframe src=https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d13138.566325268608!2d-58.38310044999999!3d-34.5879346!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bccaa199c2f643%3A0x49e543b8331abe7d!2sMuseo%20Nacional%20de%20Bellas%20Artes!5e0!3m2!1ses-419!2sar!4v1705965886253!5m2!1ses-419!2sar></iframe>

Museo Nacional de Bellas Artes

