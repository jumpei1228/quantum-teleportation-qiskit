# 量子テレポーテーションをQiskitで実装する｜状態を"転送"するしくみ

[![run](https://github.com/jumpei1228/quantum-teleportation-qiskit/actions/workflows/run.yml/badge.svg)](https://github.com/jumpei1228/quantum-teleportation-qiskit/actions/workflows/run.yml)

量子情報の基本プロトコル「量子テレポーテーション」をQiskitで実装。もつれと古典通信を組み合わせて、量子ビットの状態を別の量子ビットへ移す流れを、コードと測定結果で確かめます。

> 📖 このコードの詳しい解説（理論・図解つき）は元記事をどうぞ:
> **[量子テレポーテーションをQiskitで実装する｜状態を"転送"するしくみ](https://quantum.yurufuwa.work/learn/teleportation-qiskit)** — ゆるふわ量子コンピュータ

## セットアップ

```bash
pip install -r requirements.txt
```

## 実行方法

```bash
python teleportation-qiskit.py
```

## これは何？

[ゆるふわ量子コンピュータ](https://quantum.yurufuwa.work) はやさしい技術解説サイト「ゆるふわ」シリーズの一つです。このリポジトリは記事内で解説しているコードをそのまま動かせる形にまとめた、記事の副教材（コンパニオンリポジトリ）です。

## License

MIT
