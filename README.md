# python_selenium
Selenium WebDriver for Chrome を使用してChromeのheadlessモードを操作するサンプル

## 動作確認環境
- CentOS7
- python3.6 venv使用 (epel repo)

## setup
### 1. chromedriverを準備する
[ChromeDriver - WebDriver for Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)からchromedriverのzipをダウンロードして `vendor/driver/chromedriver` に実行ファイルを設置する。

### 2. 日本語フォントをインストールする？
(必須かどうかわからないけど) [窓の杜 - IPAフォント](https://forest.watch.impress.co.jp/library/software/ipafont/)とかからIPA日本語フォントをダウンロードして `~/.fonts/` ディレクトリを作成してそこに入れると日本語フォントが使用できるようになる。

## メモ
venvを作成すると自動的にpipが使えるようになる。親のpythonでpipをインストールする必要はない。
