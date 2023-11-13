import gradio as gr

"""
    底层网络请求，以便获取请求标头（例如用于高级身份验证）、记录客户端的 IP 地址、获取查询参数或出于其他原因。

    Request headers dictionary:
       Headers({'host': '127.0.0.1:7863', 'connection': 'keep-alive', 'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119",
       "Not?A_Brand";v="24"', 'accept': 'text/event-stream', 'cache-control': 'no-cache',
       'sec-ch-ua-mobile': '?0', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) 
       AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36', 'sec-ch-ua-platform': '"macOS"', 
       'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'cors', 'sec-fetch-dest': 'empty', 
       'referer': 'http://127.0.0.1:7863/', 'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9', 'cookie': '_ga=GA1.1.312011872.1699776775; 
        _gid=GA1.1.1034651796.1699776775; 
        access-token-FuKNMNNmfmmL_QCSqFcFlx2_9O04Elw2TDJtybfuCf8=Havjc6fRdfBFup-veGoiZQ;
         access-token-unsecure-FuKNMNNmfmmL_QCSqFcFlx2_9O04Elw2TDJtybfuCf8=Havjc6fRdfBFup-veGoiZQ;
          access-token-tJya1QEuKMXjKJ84cZw6P1STGBbjVbb5VJ71HtFTffk=TpDOc__dLDRUGqwemxoSkQ; 
          access-token-unsecure-tJya1QEuKMXjKJ84cZw6P1STGBbjVbb5VJ71HtFTffk=TpDOc__dLDRUGqwemxoSkQ;
           _ga_R1FN4KJKJH=GS1.1.1699789839.2.1.1699795564.0.0.0; _gat_gtag_UA_156449732_1=1'})
        
     IP address: 127.0.0.1
     Query parameters: {'fn_index': '0', 'session_hash': '8gy307r0yh8'}
"""
def echo(text, request: gr.Request):
    if request:
        print("Request headers dictionary:", request.headers)
        print("IP address:", request.client.host)
        print("Query parameters:", dict(request.query_params))
    return text

io = gr.Interface(echo, "textbox", "textbox")

if __name__ == '__main__':
    io.launch()