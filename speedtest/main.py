from speedtest_cli import Speedtest

st=Speedtest()

st.get_best_server()
print(f"Ping Seviyeniz: {st.results.ping} Ms")
print(f"İndirme Hızınız: {round(st.download()/1000/1000,1)} Mbit/s")
print(f"Yükleme Hızınız: {round(st.upload()/1000/1000,1)} Mbit/s")
