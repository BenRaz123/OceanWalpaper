![Example image](./example/image.png)

# Ocean Walpaper

## What is This?

Ocean walpaper is a nifty little python script that generates a nice walpaper or animation when run by `manim`.

## How-To

In order to run the file, you first need to ![install manim](https://docs.manim.community/en/stable/installation.html). To run the file simply write

```shell
$ manim -pq{x} scene.py -- [--animate|-a]
```
where `x` is either `l`, `m`, `h`, `k`. The values of `x` are shown in the table below:

| Flag |     Meaning    |
|------|----------------|
|  l   |  low quality   |
|  m   | medium quality |
|  h   |  high quality  |
|  k   |   4K quality   |

Additionaly, `-a` or `--animate` can be used to toggle animation.



