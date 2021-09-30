from cgi import print_form
import speedtest
test = speedtest.Speedtest()
 
print("Loading server list ...")
test.get_best_server()
print("Choising best server ...")
best = test.get_best_server()
print(f"Found -->  {best['host']} located in {best['country']}")
print("Performing downlead test ...")
downlead = test.download()
print("Performing upload test ...")
upload = test.upload()
ping = test.results.ping
print(f"Downlead speed is : {downlead / 1024 /1024:.2f} Mb/s")
print(f"Upload speed is : {upload / 1024 /1024:.2f} Mb/s")
print(f"ping : {ping:.2f} Ms")