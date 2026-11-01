import subprocess, requests, urllib3, time, requests.utils
urllib3.disable_warnings()
tok=open(r"C:\Users\12891\Documents\deepseek-harness\default-workspace\work\luoyan\gh_token.txt").read().strip()
cwd=r"C:\Users\12891\Documents\deepseek-harness\default-workspace\work\luoyan\site"
subprocess.run(["git","add","-A"],cwd=cwd)
r=subprocess.run(["git","-c","user.name=donk","-c","user.email=donk@local","commit","-m","add nojekyll"],cwd=cwd,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("commit",r.returncode,(r.stdout or "")[-100:])
url="https://x-access-token:%s@github.com/donk666-bit/tiku-2027.git" % tok
for i in range(3):
    r=subprocess.run(["git","push",url,"main"],cwd=cwd,capture_output=True,text=True,encoding="utf-8",errors="replace",timeout=300)
    print("push",r.returncode,(r.stderr or "")[-120:])
    if r.returncode==0: break
    time.sleep(10)
S=requests.Session(); S.trust_env=False
h={"Authorization":"token "+tok,"Accept":"application/vnd.github+json"}
base="https://donk666-bit.github.io/tiku-2027/"
for i in range(18):
    b=S.get("https://api.github.com/repos/donk666-bit/tiku-2027/pages/builds/latest",headers=h,timeout=30,verify=False).json()
    idx=S.get(base+"index.html?x=%d"%int(time.time()),timeout=30,verify=False).text
    hd=S.get(base+requests.utils.quote("华电-水利水电类-考纲版-刷题.html")+"?x=%d"%int(time.time()),timeout=30,verify=False).status_code
    print(i,b.get("status"),"华电",hd,"首页含华电","华电" in idx)
    if hd==404 and "华电" not in idx: break
    time.sleep(20)
