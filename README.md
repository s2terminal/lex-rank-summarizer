# LexRank Summarizer

```
$ docker build -t s2terminal/lex-rank-summarizer:latest .
$ docker run --rm s2terminal/lex-rank-summarizer 'メロスは激怒した。必ず、かの邪智暴虐の王を除かなければならぬ と決意した。メロスには政治がわからぬ。メロスは、村の牧人である。笛を吹き、羊と遊んで暮して来た。けれども邪悪に対しては、人一倍に敏感であっ た。きょう未明メロスは村を出発し、野を越え山越え、十里はなれた此のシラクスの市にやって来た。メロスには父も、母も無い。女房も無い。十六の、 内気な妹と二人暮しだ。この妹は、村の或る律気な一牧人を、近々、花婿として迎える事になっていた。結婚式も間近かなのである。メロスは、それゆえ 、花嫁の衣裳やら祝宴の御馳走やらを買いに、はるばる市にやって来たのだ。先ず、その品々を買い集め、それから都の大路をぶらぶら歩いた。'
メロスは激怒した。
メロスは、村の牧人である。
きょう未明メロスは村を出発し、野を越え山越え、十里はなれた此のシラクスの市にやって来た。
```

## dev

```
$ docker-compose up
```

and use [VS Code Remote Container](https://code.visualstudio.com/docs/remote/containers)

### Testing

```
$ docker-compose run --rm app poetry run pytest
```

## References
- [Python: LexRankで日本語の記事を要約する \- け日記](https://ohke.hateblo.jp/entry/2018/11/17/230000)
- [図書カード：走れメロス](https://www.aozora.gr.jp/cards/000035/card1567.html)
