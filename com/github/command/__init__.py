"""Naval Fate.

Usage:
  naval_fate.py ship new <name>...
  naval_fate.py ship <name> move <x> <y> [--speed=<kn>]
  naval_fate.py ship shoot <x> <y>
  naval_fate.py mine (set|remove) <x> <y> [--moored | --drifting]
  naval_fate.py (-h | --help)
  naval_fate.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.

"""

from docopt import  docopt
import  requests
import  base64

url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2017-11-28&leftTicketDTO.from_station=GZQ&leftTicketDTO.to_station=HYQ&purpose_codes=ADULT';
rsp = requests.get(url,verify=False);
print(rsp.json())

print(base64.decodestring(rsp.json()))