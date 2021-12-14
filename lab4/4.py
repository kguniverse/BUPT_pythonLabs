
import aiohttp
import asyncio
import json
import statsmodels.api as sm
import numpy as np


async def process(X:np.ndarray, Y:np.ndarray):
    lowess = sm.nonparametric.lowess
    n = np.size(X, 0);
    y_hat = lowess(Y, X, frac=10./n)[:, 1]
    
    return y_hat.tolist()
    
    
async def main(params):
    async with aiohttp.ClientSession('http://127.0.0.1:1337') as session:
        async with session.get('/data', params = params) as response:
            form = params.get('form', 'json')
            if form == 'json':
                json_str = await response.json()
                # j_data = json.loads(json_str)
                x = []
                y = []
                for data in json_str:
                   x.append(data.get('Year')) 
                   y.append(data.get('Temperature'))
                str = json.dumps(json_str, indent=4, sort_keys=True)
                
                z = await process(np.array(x), np.array(y))
                for a, b, c in zip(x, y, z):
                    print(a, b, round(c, 2))

            else:
                print(await response.text())


def test():
    key = input('input keyword (Temparature/[Year]):')
    if key == '':
        key = 'Year'
    reverse = input('want reverse sort \? (y/[N]):')
    if reverse == 'y':
        reverse = 'True'
    form = input('form \? (csv/xml/[json]):')
    if form == '':
        form = 'json'
    params = {'key': key, 'reverse': reverse, 'form': form}
    return params
loop = asyncio.get_event_loop()
loop.run_until_complete(main(test()))