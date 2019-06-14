from slackbot.bot import respond_to
import csv
import urllib.parse


@respond_to('tel (.*)')
def tel_func(message, params):
    args = [row for row in csv.reader([params], delimiter=' ')][0]
    if len(args) < 3:
        message.reply('usage: tel 宛先 問い合わせ会社名 お客様名 [コメント]')
        return

    note = ""

    if len(args) == 4:
        note = args.pop(-1)

    to_whom = args.pop(0)
    corp = args.pop(0)
    from_whom = args.pop(0)

    subject = "{0}の{1}様よりお電話がありました".format(corp, from_whom)
    search_url = "https://www.google.co.jp/search?q=" + \
        urllib.parse.quote(corp)

    body = """{0}さん

{1}の{2}様よりお電話がありました。

### 伝言
{3}

### 会社情報検索
{4}
""".format(to_whom, corp, from_whom, note, search_url)
    url = "https://mail.google.com/mail/?view=cm&to=staff@ferix.jp&su={0}&body={1}".format(
        urllib.parse.quote(subject), urllib.parse.quote(body))
    res = """
ﾎﾚ(ﾟДﾟ)ノ⌒

```
{}
```
""".format(url)

    message.reply(res)
